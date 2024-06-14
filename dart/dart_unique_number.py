import requests
import zipfile
import io
import os
import pandas as pd
import xml.etree.ElementTree as ET
from dotenv import load_dotenv

# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019018

# .env 파일에서 환경 변수 로드
load_dotenv()

# DART에서 발급받은 인증키
dart_api_key = os.environ.get('dart_api_key')

# 요청할 API URL
url = f'https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key={dart_api_key}'

# API 요청 보내기
response = requests.get(url)

# 응답 상태 코드 확인
if response.status_code == 200:
    # 응답 데이터가 ZIP 파일이므로 이를 처리
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        # ZIP 파일 내의 XML 파일을 읽어오기
        for filename in z.namelist():
            with z.open(filename) as xml_file:
                xml_content = xml_file.read()
                root = ET.fromstring(xml_content)
                
                # XML 데이터 파싱하여 DataFrame으로 변환
                data = []
                for corp in root.findall('list'):
                    corp_code = corp.find('corp_code').text
                    corp_name = corp.find('corp_name').text
                    stock_code = corp.find('stock_code').text
                    modify_date = corp.find('modify_date').text
                    
                    # stock_code가 존재하는 경우에만 리스트에 추가
                    if len(stock_code) > 1:
                        data.append([corp_code, corp_name, stock_code, modify_date])
                
                # DataFrame으로 변환
                df = pd.DataFrame(data, columns=['corp_code', 'corp_name', 'code', 'modify_date'])
                
                # 엑셀 파일로 저장
                df.to_excel('국내주식_고유번호.xlsx', index=False, engine='openpyxl')
                print('엑셀 파일로 저장되었습니다: 국내주식_고유번호.xlsx')
else:
    print(f'API 요청 실패: {response.status_code}')