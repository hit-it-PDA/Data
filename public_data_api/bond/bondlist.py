import requests
import pandas as pd
import sqlalchemy
from dotenv import load_dotenv
import os

import utils.db
from tqdm import tqdm


# load .env
load_dotenv()

# 공공데이터포털에서 발급받은 API 키
api_key = os.environ.get('api_key')

# 요청할 API URL
url = f'https://apis.data.go.kr/1160100/service/GetBondSecuritiesInfoService/getBondPriceInfo?serviceKey={api_key}'
num_of_rows = 100

# 기준일자 설정 (begin ~ end 하루전 )
begin_base_date = "20240612"  # get_date_ymd() # 기준일자가 검색값보다 크거나 같은 데이터를 검색
end_base_date = "20240613"  # get_date_ymd() # 기준일자가 검색값보다 작은 데이터를 검색


def request_api(page=1):
    params = {
        "numOfRows": num_of_rows,
        "pageNo": page,
        "beginBasDt": begin_base_date,
        "endBasDt": end_base_date,
        "resultType": "json"
    }

    # API 요청 보내기
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['response']
    else:
        print(f'API 요청 실패: {response.status_code}')
        return None


def get_total_count():
    data = request_api(1)['body']
    total_count = int(data['totalCount'])
    return total_count


def fetch_bond_price_list(last_page):
    all_items = []

    for page in tqdm(range(1, last_page + 1)):  # 페이지 계산 수정
        data = request_api(page)['body']
        if data is None:
            print(f'페이지 실패: {page}')
            return

        items = data['items']['item']

        if (len(items) == 0):
            print(f'상품 정보가 나오지 않습니다..')
            print(data['header'])
            return

        for item in items:
            basDt = item['basDt']  # 기준일자
            isinCd = item['isinCd']  # 종목코드
            clprPrc = item['clprPrc']  # 정규시장의 매매시간종료시까지 형성되는 최종가격
            clprVs = item['clprVs']  # 종가의 전일 대비 등락
            clprBnfRt = item['clprBnfRt']  # 종가로 체결된 경우의 수익률
            mkpPrc = item['mkpPrc']  # 정규시장의 매매시간개시후 형성되는 최초가격
            mkpBnfRt = item['mkpBnfRt']  # 시가로 체결된 경우의 수익률
            hiprPrc = item['hiprPrc']  # 하루 중 가격의 최고치
            hiprBnfRt = item['hiprBnfRt']  # 고가로 체결된 경우의 수익률
            loprPrc = item['loprPrc']  # 하루 중 가격의 최저치
            loprBnfRt = item['loprBnfRt']  # 저가로 체결된 경우의 수익률
            all_items.append((basDt, isinCd, clprPrc, clprVs, clprBnfRt,
                              mkpPrc, mkpBnfRt, hiprPrc, hiprBnfRt, loprPrc, loprBnfRt))

    # DataFrame 생성
    df = pd.DataFrame(all_items, columns=['기준일자', '종목코드', '종가', '전일대비등락',
                                          '종가_수익률', '최초가', '시가_수익률',
                                          '최고가', '최고가_수익률', '최저가', '최저가_수익률'])

    # 파일로 저장
    df.to_csv(f'채권시세_{begin_base_date}~{end_base_date}.csv', index=False)
    df.to_excel(f'채권시세_{begin_base_date}~{end_base_date}.xlsx', index=False)

    print(f'채권 데이터 수집 완료 : 채권시세_{begin_base_date}~{end_base_date}')


def fetch_bond_product_list(last_page):
    all_items = []

    for page in tqdm(range(1, last_page + 1)):  # 페이지 계산 수정
        data = request_api(page)['body']
        if data is None:
            print(f'페이지 실패: {page}')
            return

        items = data['items']['item']

        if (len(items) == 0):
            print(f'상품 정보가 나오지 않습니다..')
            print(data['header'])
            return

        for item in items:
            isinCd = item['isinCd']  # 종목코드
            itmsNm = item['itmsNm']  # 코드 이름
            mrktCtg = item['mrktCtg']  # 시장 구분
            all_items.append((isinCd, itmsNm, mrktCtg))

            ########################################################
            # 제외한 데이터
            # xpYrCnt = item['xpYrCnt'] # 년단위 만기기간(KTS만 허용)
            # itmsCtg = item['itmsCtg'] # 지표/경과(KTS만 허용)
            # srtnCd = item['srtnCd'] # 종목 코드보다 짧으면서 유일성이 보장되는 코드(9자리)
            # trqu : 체결수량의 누적 합계
            # trPrc : 거래건 별 체결가격 * 체결수량의 누적 합계
            ########################################################

    # DataFrame 생성
    df = pd.DataFrame(all_items, columns=['code', 'name', 'market'])

    # 파일로 저장
    # df.to_json(f'채권상품_{begin_base_date}~{end_base_date}.json', index=False)
    df.to_csv(f'채권상품_{begin_base_date}~{end_base_date}.csv', index=False)
    # df.to_excel(f'채권상품_{begin_base_date}~{end_base_date}.xlsx', index=False)
    print(f'채권 데이터 수집 완료 : 채권상품_{begin_base_date}~{end_base_date}')

    # db에 업로드
    # db_connection = utils.db.connect_db()
    #
    # dtypesql = {
    #     'id': sqlalchemy.types.Integer,
    #     'code': sqlalchemy.types.VARCHAR(255),
    #     'name': sqlalchemy.types.VARCHAR(255),
    #     'market': sqlalchemy.types.VARCHAR(255),
    # }
    # df.to_sql(name='bond_products', con=db_connection, if_exists='append', index=True, dtype=dtypesql)
    #
    # print(f'채권 상품 DB 업로드 완료(bond_products)')


if __name__ == "__main__":
    print(f"{begin_base_date} ~ {end_base_date} 채권 데이터 수집을 시작합니다.")
    total_count = get_total_count()
    print(f"{total_count}개 데이터 수집")

    last_page = (total_count // num_of_rows) + 1
    fetch_bond_product_list(last_page)
    fetch_bond_price_list(last_page)
