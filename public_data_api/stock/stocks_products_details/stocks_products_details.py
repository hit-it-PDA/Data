import requests
import xml.etree.ElementTree as ET
import pandas as pd
from dotenv import load_dotenv
import os 

# load .env
load_dotenv()

# 공공데이터포털에서 발급받은 API 키
api_key = os.environ.get('api_key')

# 요청할 API URL
url = f'https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey={api_key}&resultType=xml'

params = {
    "numOfRows": 100,
    "pageNo": 1,
    "beginBasDt": "20240101",
    "beginMrktTotAmt": 1000000000000
}

# API 요청 보내기
response = requests.get(url, params=params)

# 응답 상태 코드 확인
if response.status_code == 200:
    # 응답 데이터 파싱 (XML 형식)
    root = ET.fromstring(response.content)
    
    # totalCount와 numOfRows 요소 찾기
    total_count_element = root.find('.//totalCount')
    num_of_rows_element = root.find('.//numOfRows')

    if total_count_element is not None and num_of_rows_element is not None:
        total_count = int(total_count_element.text)
        rows = int(num_of_rows_element.text)

        print(total_count)
        print(rows)

        all_items = []

        for page in range(1, (total_count // rows) + 2):  # 페이지 계산 수정
            params['pageNo'] = page
            response = requests.get(url, params=params)

            if response.status_code == 200:
                root = ET.fromstring(response.content)
                items = root.findall('.//item')
                for item in items:
                    basDt_element = item.find('basDt')
                    srtnCd_element = item.find('srtnCd')
                    clpr_element = item.find('clpr')
                    mrktTotAmt_element = item.find('mrktTotAmt')
                    trqu_element = item.find('trqu')

                    
                    if basDt_element is not None and srtnCd_element is not None and clpr_element is not None and trqu_element is not None:
                        basDt = basDt_element.text
                        srtnCd = srtnCd_element.text
                        clpr = clpr_element.text
                        mrktTotAmt = mrktTotAmt_element.text
                        trqu = trqu_element.text

                        all_items.append((basDt, srtnCd, clpr, mrktTotAmt, trqu))
            else:
                print(f'페이지 {page} 요청 실패: {response.status_code}')
                break

        # DataFrame 생성
        df = pd.DataFrame(all_items, columns=['date', 'code', 'price', 'amount', 'volume', 'per'])

        # 엑셀 파일로 저장
        df.to_excel('./db/stocks_products_details.xlsx', index=False)
        print('엑셀 파일 저장 완료: 종목코드_종목명_종목상세.xlsx')

    else:
        print('totalCount 또는 numOfRows 요소를 찾을 수 없습니다.')

else:
    print(f'API 요청 실패: {response.status_code}')
