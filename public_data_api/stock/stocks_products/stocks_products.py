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
url = f'https://apis.data.go.kr/1160100/service/GetKrxListedInfoService/getItemInfo?serviceKey={api_key}&resultType=xml'

params = {
    "numOfRows": 10,
    "pageNo": 1,
    "basDt": "20240101"
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
                    srtnCd_element = item.find('srtnCd')
                    itmsNm_element = item.find('itmsNm')
                    mrktCtg_element = item.find('mrktCtg')
                    
                    if srtnCd_element is not None and itmsNm_element is not None and mrktCtg_element is not None:
                        srtnCd = srtnCd_element.text
                        itmsNm = itmsNm_element.text
                        mrktCtg = mrktCtg_element.text

                        # 'A'로 시작하는 문자열 제거
                        # if srtnCd.startswith('A'):
                        #     srtnCd = srtnCd[1:]

                        all_items.append((srtnCd, itmsNm, mrktCtg, 'Korea'))
            else:
                print(f'페이지 {page} 요청 실패: {response.status_code}')
                break

        # DataFrame 생성
        df = pd.DataFrame(all_items, columns=['code', 'name', 'market_type', 'region'])

        # 엑셀 파일로 저장
        df.to_excel('./db/stocks_products_text.xlsx', index=False)
        print('엑셀 파일 저장 완료: stocks_products_text.xlsx')

    else:
        print('totalCount 또는 numOfRows 요소를 찾을 수 없습니다.')

else:
    print(f'API 요청 실패: {response.status_code}')
