# from utils.db import connect_db
# from utils.converter import to_int, to_float

import os
print(os.getcwd())
import requests
import pandas as pd
from tqdm import tqdm
import sqlalchemy



def get_fund_info(fund_code):
    url = f"https://www.fundguide.net/Api/Fund/GetFundInfo?fund_cd={fund_code}"
    response = requests.get(url)
    if response.status_code == 200:
        data_list = response.json()['Data'][0]
        for data in data_list:
            type = data["PEER_CD_NM"]  # 펀드 타입
            type_detail = data["PEER_CD_L_NM"]  # 펀드 타입 디테일
            set_amount = to_int(data["SET_AMT"])  # 설정액
            company_name = data["CO_NM"]  # 운용사
            return [type, type_detail, set_amount, company_name]
    else:
        print("연결 실패")


def get_fund_code_list(sel_peer, page=1, row_cnt=10):
    url = f'https://www.fundguide.net/Api/Fund/GetFundList'
    params = {
        "selPeer": sel_peer,
        "selPeerDepth": "1|2|3|3|3|3|3|2|3|3|3|3",
        "listCondFr": "0.00|0.00",
        "listCondNm": "수탁고|총보수율",
        "listCondTo": "120,375.66|73.58",
        "listCondOption": "1|1",
        "listCondGroup": "C|B",
        "listCondSeq": "2|1",
        "sort_col": "RT_1Y",
        "ord_gb": "DESC",
        "page_no": page,
        "row_cnt": row_cnt,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data_list = response.json()['Data'][0]
        total = to_int(data_list[0]["ROW_CNT"])
        funds = []
        for data in data_list:
            try:
                fund_code = data["FUND_CD"]
                fund_name = data["FUND_NM"]  # 펀드 이름
                hashtag = data["HASHTAG"]  # 해시 태그
                std_price = to_float(data["STD_PRC"])  # 기준가
                set_date = data["SET_DT"]  # 설정일
                risk_grade = data["RISK_GRADE"]  # 위험등급
                risk_grade_txt = data["RISK_GRADE_TXT"]  # 위험등급 텍스트
                drv_nav = to_float(data["DRV_NAV"])  # 운용 규모

                # 비중
                bond = data["BOND_RT"]  # 국내 채권
                bond_foreign = data["BOND_FRG_RT"]  # 해외 채권
                stock = data["STOCK_RT"]  # 국내 주식
                stock_foreign = data["STOCK_FRG_RT"]  # 해외 주식
                investment = data["INVEST_RT"]  # 수익 증권
                etc = data["ETC_RT"]

                # 수익률
                return_1m = to_float(data["RT_1M"])
                return_3m = to_float(data["RT_3M"])
                return_6m = to_float(data["RT_6M"])
                return_1y = to_float(data["RT_1Y"])
                return_3y = to_float(data["RT_3Y"])
                return_5y = to_float(data["RT_5Y"])
                return_idx = to_float(data["RT_IDX"])
                return_ytd = to_float(data["RT_YTD"])
                fund_type, fund_type_detail, set_amount, company_name = get_fund_info(fund_code)

                funds.append([fund_code, fund_name, hashtag, std_price, set_date,
                              fund_type, fund_type_detail, set_amount, company_name,
                              risk_grade, risk_grade_txt, drv_nav,
                              bond, bond_foreign, stock, stock_foreign, investment, etc,
                              return_1m, return_3m, return_6m, return_1y, return_3y, return_5y, return_idx, return_ytd])
            except Exception as e:
                print(data["FUND_CD"])
                print(e)
        return funds, total
    else:
        print("연결 실패")
        return [], 0


def calculate_total_pages(total_count, row_cnt):
    if row_cnt == 0:
        return 0
    return (total_count + row_cnt - 1) // row_cnt


def upload_funds(name, sel_peer):
    page = 1
    row_cnt = 50
    _, total_count = get_fund_code_list(sel_peer, page, row_cnt)
    total_pages = calculate_total_pages(total_count, row_cnt)

    start_page = 1
    end_page = total_pages
    all_items = []
    print("펀드 코드 수집 시작 >> ")
    for page in tqdm(range(start_page, end_page)):
        funds, _ = get_fund_code_list(sel_peer, page, row_cnt)
        all_items.extend(funds)

    print(f"수집한 코드 개수: {len(all_items)} / {total_count}")

    tuple_arr = [tuple(i) for i in all_items]  # 'I'를 'i'로 수정
    unique_arr = [list(j) for j in set(tuple_arr)]
    print(f"중복 제거 후: {len(unique_arr)}개")

    df = pd.DataFrame(unique_arr, columns=['fund_code', 'fund_name', 'hashtag', 'std_price', 'set_date',
                                          'fund_type', 'fund_type_detail', 'set_amount', 'company_name',
                                          'risk_grade', 'risk_grade_txt', 'drv_nav',
                                          'bond', 'bond_foreign', 'stock', 'stock_foreign', 'investment', 'etc',
                                          'return_1m', 'return_3m', 'return_6m', 'return_1y', 'return_3y', 'return_5y',
                                          'return_idx', 'return_ytd'])

    # csv로 저장
    df.to_csv(f'펀드리스트_{name}.csv', index=False)

    db_connection, conn = connect_db()
    dtypesql = {
        'fund_code': sqlalchemy.types.VARCHAR(255),
        'fund_name': sqlalchemy.types.VARCHAR(255),
        'hashtag': sqlalchemy.types.VARCHAR(255),
        'std_price': sqlalchemy.types.Float,
        'set_date': sqlalchemy.types.Date,

        'fund_type': sqlalchemy.types.VARCHAR(255),
        'fund_type_detail': sqlalchemy.types.VARCHAR(255),
        'set_amount': sqlalchemy.types.Integer,
        'company_name': sqlalchemy.types.VARCHAR(255),

        'risk_grade': sqlalchemy.types.Integer,
        'risk_grade_txt': sqlalchemy.types.VARCHAR(255),
        'drv_nav': sqlalchemy.types.Float,

        'bond': sqlalchemy.types.Float,
        'bond_foreign': sqlalchemy.types.Float,
        'stock': sqlalchemy.types.Float,
        'investment': sqlalchemy.types.Float,
        'etc': sqlalchemy.types.Float,

        'return_1m': sqlalchemy.types.Float,
        'return_3m': sqlalchemy.types.Float,
        'return_6m': sqlalchemy.types.Float,
        'return_1y': sqlalchemy.types.Float,
        'return_3y': sqlalchemy.types.Float,
        'return_5y': sqlalchemy.types.Float,
        'return_idx': sqlalchemy.types.Float,
        'return_ytd': sqlalchemy.types.Float,
    }

    df.to_sql(name='fund_products_3', con=db_connection, if_exists='append', index=False, dtype=dtypesql)


if __name__ == "__main__":

    sel_peers = {
        # "국내주식형": "HS001|HSA01|HSAG1|HSAM1|HSAD1|HSAS1|HSAT1|HSP01|HSPP1|HSPX1|HSPS1|HSPO1",
        # "국내혼합형": "HM001|HMA01|HMS01|HMB01|HMBM1|HMBA1|HMBH1",
        # "국내채권형": "HB001|HBG01|HBC01|HBB01|HBBO1|HBBS1|HBH01",
        # "해외주식형": "FS001|FSC01|FSCJ1|FSCC1|FSCI1|FSCV1|FSCB1|FSCR1|FSCO1|FSS01|FSSE1|FSSM1|FSSH1|FSSF1|FSSI1|FSSP1|FSSC1|FSSN1|FSSO1|FSR01|FSRG1|FSRD1|FSRM1|FSRU1|FSRE1|FSRN1|FSRS1|FSRP1|FSRX1|FSRA1|FSRI1|FSRO1|FSO01",
        "해회혼합형": "FM001|FMA01|FMAD1|FMS01|FMB01|FMO01",
        # "해외채권형": "FB001|FBG01|FBGB1|FBGH1|FBR01|FBRM1|FBRP1|FBRN1|FBRS1|FBRU1|FBO01"
    }

    for key, value in sel_peers.items():
        print(f"[{key}] 데이터 수집")
        upload_funds(key, value)
