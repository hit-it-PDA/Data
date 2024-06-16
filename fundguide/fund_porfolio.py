from utils.db import connect_db
from utils.converter import to_str, decode_html
from utils.date import get_date_sdt
import requests
import pandas as pd
from tqdm import tqdm
import sqlalchemy
from sqlalchemy import text

db_connection, conn = connect_db()


def get_fund_portfolio(fund_code):
    url = f"https://www.fundguide.net/Api/Fund/GetFundPortfolio?fund_cd={fund_code}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["Data"]
        fund_asset = []
        fund_stock_item = []
        fund_bond_item = []

        if len(data[0]) > 0:  # 자산 구성
            fund_asset = get_fund_asset(fund_code, data[0][0])
        if len(data[2]) > 0:  # 주식
            fund_stock_item = get_fund_stock_item(fund_code, data[2])
        if len(data[6]) > 0:  # 채권
            fund_bond_item = get_fund_bond_item(fund_code, data[6])

        return fund_asset, fund_stock_item, fund_bond_item


def get_fund_asset(fund_code, data):
    stock = data["STOCK_RT"]
    stock_foreign = data["STOCK_FRG_RT"]
    bond = data["BOND_RT"]
    bond_foreign = data["BOND_FRG_RT"]
    investment = data["INVEST_RT"]
    etc = data["ETC_RT"]

    return [fund_code, stock, stock_foreign, bond, bond_foreign, investment, etc]


def get_fund_stock_item(fund_code, data):
    stock_items = []
    for d in data:
        stock_name = d["ITEM_NM"]
        size = to_str(d["STK_SIZE_GB"])
        style = to_str(d["STK_VAL_GB"])
        rate = d["ASSET_C_RT"]

        stock_items.append([fund_code, stock_name, size, style, rate])
    return stock_items


def get_fund_bond_item(fund_code, data):
    bond_items = []
    for d in data:
        bond_name = decode_html(d["ITEM_NM"])
        expire_date = d["EXP_DT"]
        duration = d["ADJ_DUR"]
        credit = d["CREDIT_NM"]
        rate = d["ASSET_C_RT"]

        bond_items.append([fund_code, bond_name, expire_date, duration, credit, rate])
    return bond_items


def get_fund_code_from_db():
    # fund_products 에는 존재하지만 fund_assets에는 존재하지 않는 펀드 코드들
    sql = """ 
        SELECT fp.fund_code
        FROM fund_products fp
        LEFT JOIN fund_assets fa ON fp.fund_code = fa.fund_code
        WHERE fa.fund_code IS NULL
        ORDER BY fund_code
        """
    df = pd.read_sql(sql, con=db_connection)
    return df['fund_code'].tolist()


def upload_fund_asset_db(fund_asset_list):
    print(">> 자산 구성 DB 업로드..")
    df = pd.DataFrame(fund_asset_list,
                      columns=['fund_code', 'stock', 'stock_foreign', 'bond', 'bond_foreign', 'investment', 'etc'])

    # TODO: 펀드 자산 구성이 바뀌는지 확인해보고 있으면 update 없으면 insert로 변경하기
    # 데이터베이스에 데이터 삽입
    for index, row in df.iterrows():
        insert_query = text("""
            INSERT IGNORE INTO fund_assets (fund_code, stock, stock_foreign, bond, bond_foreign, investment, etc)
            VALUES (:fund_code, :stock, :stock_foreign, :bond, :bond_foreign, :investment, :etc);
            """)
        conn.execute(insert_query, {'fund_code': row['fund_code'], 'stock': row['stock'],
                                    'stock_foreign': row['stock_foreign'], 'bond': row['bond'],
                                    'bond_foreign': row['bond_foreign'], 'investment': row['investment'],
                                    'etc': row['etc']})
        conn.commit()

    print(">> 자산 구성 DB 업로드 완료")


def upload_fund_stocks_db(fund_stock_item_list):
    print(">> 펀드 보유 주식 DB 업로드..")
    df = pd.DataFrame(fund_stock_item_list, columns=['fund_code', 'stock_name', 'size', 'style', 'rate'])
    dtypesql = {
        'fund_code': sqlalchemy.types.VARCHAR(255),
        'stock_name': sqlalchemy.types.VARCHAR(255),
        'size': sqlalchemy.types.VARCHAR(255),
        'style': sqlalchemy.types.VARCHAR(255),
        'rate': sqlalchemy.types.Float,
    }
    df.to_sql(name='fund_stocks', con=db_connection, if_exists='append', index=False, dtype=dtypesql)
    print(">> 펀드 보유 주식 DB 업로드 완료")


def upload_fund_bonds_db(fund_bond_item_list):
    print(">> 펀드 보유 채권 DB 업로드 ...")
    df = pd.DataFrame(fund_bond_item_list,
                      columns=['fund_code', 'bond_name', 'expire_date', 'duration', 'credit', 'rate'])
    dtypesql = {
        'fund_code': sqlalchemy.types.VARCHAR(255),
        'bond_name': sqlalchemy.types.VARCHAR(255),
        'expire_date': sqlalchemy.types.Date,
        'duration': sqlalchemy.types.Float,
        'credit': sqlalchemy.types.VARCHAR(255),
        'rate': sqlalchemy.types.Float,
    }
    df.to_sql(name='fund_bonds', con=db_connection, if_exists='append', index=False, dtype=dtypesql)
    print(">> 펀드 보유 채권 DB 업로드 완료")


if __name__ == "__main__":
    fund_code_list = get_fund_code_from_db()
    UNIT = 2000 # 양이 많아서 끊어서 크롤링
    fund_asset_list = []
    fund_stock_item_list = []
    fund_bond_item_list = []

    fail_code_list = []

    for fund_code in tqdm(fund_code_list[:UNIT]):
        try:
            fund_asset, fund_stock_item, fund_bond_item = get_fund_portfolio(fund_code)
            fund_asset_list.append(fund_asset)
            fund_stock_item_list.extend(fund_stock_item)
            fund_bond_item_list.extend(fund_bond_item)
        except Exception as e:
            print(f"크롤링 실패 : {fund_code}")
            print(e)
            fail_code_list.append(fund_code)

    try:
        upload_fund_asset_db(fund_asset_list)
        upload_fund_bonds_db(fund_bond_item_list)
        upload_fund_stocks_db(fund_stock_item_list)
    except Exception as e:
        print(f"DB 업로드 실패 : {fund_code}")
        print(e)
        fail_code_list.append(fund_code)

    if fail_code_list:
        # DataFrame 생성
        df = pd.DataFrame(fail_code_list, columns=['fund_code'])
        # 파일로 저장
        df.to_csv(f'fail_code_list_{get_date_sdt()}.csv', index=False)
