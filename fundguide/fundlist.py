from utils.db import connect_db
from utils.converter import to_int
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
            code = data["FUND_CD"]
            name = data["FUND_NM"]
            std_price = data["STD_PRC"].replace(",", "") # 기준가
            set_date = data["SET_DT"] # 설정일
            type = data["PEER_CD_NM"] # 펀드
            type_detail = data["PEER_CD_L_NM"]
            set_amount = data["SET_AMT"]
            risk_grade = data["RISK_GRADE"]
            risk_grade_txt = data["RISK_GRADE_TXT"]
            company_name = data["CO_NM"]

            return [code, name, std_price, set_date, type, type_detail, set_amount, risk_grade, risk_grade_txt, company_name]


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
        funds = [data["FUND_CD"] for data in data_list]
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
    fund_codes = []
    print("펀드 코드 수집 시작 >> ")
    for page in tqdm(range(1, total_pages + 1)):
        code_list, _ = get_fund_code_list(sel_peer, page, row_cnt)
        fund_codes.extend(code_list)

    print(f"수집한 코드 개수: {len(fund_codes)} / {total_count}")
    fund_codes = list(set(fund_codes)) # 중복이 있다면 제거
    print(f"중복 제거 후: {len(fund_codes)}개")
    print("펀드 상세 정보 수집 시작 >> ")
    all_items = []
    for fund_code in tqdm(fund_codes):
        fund_info = get_fund_info(fund_code)
        if fund_info:
            all_items.append(fund_info)

    df = pd.DataFrame(all_items, columns=['code', 'name', 'std_price', 'set_date', 'type', 'type_detail', 'set_amount', 'risk_grade', 'risk_grade_txt', 'company_name'])

    # csv로 저장
    df.to_csv(f'펀드리스트_{name}.csv', index=False)

    db_connection = connect_db()
    dtypesql = {
        'code': sqlalchemy.types.VARCHAR(255),
        'name': sqlalchemy.types.VARCHAR(255),
        'std_price': sqlalchemy.types.Float,
        'set_date': sqlalchemy.types.Date,
        'type': sqlalchemy.types.VARCHAR(255),
        'type_detail': sqlalchemy.types.VARCHAR(255),
        'set_amount': sqlalchemy.types.Integer,
        'risk_grade': sqlalchemy.types.Integer,
        'risk_grade_txt': sqlalchemy.types.VARCHAR(255),
        'company_name': sqlalchemy.types.VARCHAR(255)
    }

    df.to_sql(name='fund_products', con=db_connection, if_exists='append', index=False, dtype=dtypesql)
if __name__ == "__main__":

    sel_peers = {
        # "국내주식형": "HS001|HSA01|HSAG1|HSAM1|HSAD1|HSAS1|HSAT1|HSP01|HSPP1|HSPX1|HSPS1|HSPO1",
        # "국내혼합형": "HM001|HMA01|HMS01|HMB01|HMBM1|HMBA1|HMBH1",
        # "국내채권형": "HB001|HBG01|HBC01|HBB01|HBBO1|HBBS1|HBH01",
        # "해외주식형": "FS001|FSC01|FSCJ1|FSCC1|FSCI1|FSCV1|FSCB1|FSCR1|FSCO1|FSS01|FSSE1|FSSM1|FSSH1|FSSF1|FSSI1|FSSP1|FSSC1|FSSN1|FSSO1|FSR01|FSRG1|FSRD1|FSRM1|FSRU1|FSRE1|FSRN1|FSRS1|FSRP1|FSRX1|FSRA1|FSRI1|FSRO1|FSO01",
        "해회혼합형": "FM001|FMA01|FMAD1|FMS01|FMB01|FMO01",
        "해외채권형": "FB001|FBG01|FBGB1|FBGH1|FBR01|FBRM1|FBRP1|FBRN1|FBRS1|FBRU1|FBO01"
    }

    for key, value in sel_peers.items():
        print(f"[{key}] 데이터 수집")
        upload_funds(key, value)