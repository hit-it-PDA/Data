#### PER = 현재 주가 ÷ EPS
## 종목코드 -> 2023.12월 EPS
from urllib import parse
import pandas as pd

def get_fnguide(code):
    get_param = {
        'pGB': 1,
        'gicode': 'A%s' % (code),
        'cID': '',
        'MenuYn': 'M',
        'ReportGB': '',
        'NewMenuID': 101,
        'stkGb': 701,
    }
    get_param = parse.urlencode(get_param)
    url = "http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?%s" % (get_param)
    tables = pd.read_html(url, header=0)
    return tables


# 엑셀 파일을 읽어온다
df = pd.read_excel('./db/종목코드_종목명_종목상세.xlsx')

# 필요한 열만 추출하여 딕셔너리 배열로 변환
data = df[['date', 'code', 'price', 'amount', 'volume']].to_dict(orient='records')

# 새로운 열을 추가
df['per'] = None
df['eps'] = None

# 각 종목에 대해 FnGuide 데이터를 가져오고 PER을 계산
for idx, item in enumerate(data):
    # if idx >= 1000:  # 1000번만 실행
    #     break

    # if idx < 1000:  # 1000번 이전은 건너뜀
    #     continue
    # if idx >= 3000:  # 3000번 이후는 중단
    #     break

    # if idx < 3000:  # 3000번 이전은 건너뜀
    #     continue
    # if idx >= 8000:  # 8000번 이후는 중단
    #     break

    # if idx < 8000:  # 3000번 이전은 건너뜀
    #     continue
    # if idx >= 12000:  # 8000번 이후는 중단
    #     break

    # if idx < 12000:  # 3000번 이전은 건너뜀
    #     continue
    # if idx >= 20000:  # 8000번 이후는 중단
    #     break

    if idx < 20000:  # 3000번 이전은 건너뜀
        continue
    if idx >= 28752:  # 8000번 이후는 중단
        break

    date = item['date']
    code = str(item['code']).zfill(6)
    price = item['price']
    amount = item['amount']
    volume = item['volume']
    
    try:
        tables = get_fnguide(code)
        
        # Table 11의 19행 5열의 값을 가져오기
        table_11 = tables[11]  # 리스트는 0부터 시작하므로 11번째 테이블은 인덱스 10
        eps = table_11.iloc[19, 5]  # 19행 5열의 값 (0부터 시작하므로 18행 4열)
        
        # EPS가 숫자인지 확인 (NaN 등의 값을 처리)
        if pd.isna(eps):
            print(f"Code {code}: EPS 값이 유효하지 않습니다.")
            continue
        
        eps = float(eps)  # EPS 값을 실수로 변환
        
        # PER 계산
        per = price / eps
        print(f"Date: {date}, Code: {code}, PER: {per}, EPS: {eps}")

        # 원래 데이터프레임에 값을 업데이트
        df.loc[(df['code'] == int(code)) & (df['date'] == date), 'code'] = code
        df.loc[(df['code'] == code) & (df['date'] == date), 'per'] = per
        df.loc[(df['code'] == code) & (df['date'] == date), 'eps'] = eps
        
    
    except Exception as e:
        print(f"Code {code}: 데이터를 처리하는 중 오류 발생 - {e}")
        # 오류가 발생할 경우 NaN 값을 넣는다 (date와 code가 일치하는 경우에만)
        df.loc[(df['code'] == int(code)) & (df['date'] == date), 'code'] = code
        df.loc[(df['code'] == code) & (df['date'] == date), 'per'] = None
        df.loc[(df['code'] == code) & (df['date'] == date), 'eps'] = None

# 수정된 데이터프레임을 엑셀 파일에 저장
df.to_excel('./db/종목코드_종목명_종목상세_업데이트.xlsx', index=False)

# 참조 - API
# https://joycecoder.tistory.com/entry/API-%EC%9E%AC%EB%AC%B4%EC%A0%9C%ED%91%9C-%EB%B0%8F-ROE-%EC%A1%B0%ED%9A%8C-API

# 참조 - 코드
# https://velog.io/@goyoon5526/pandas-dataframe%EC%97%90%EC%84%9C-%EC%A1%B0%EA%B1%B4%EC%9D%84-%EC%97%AC%EB%9F%AC-%EA%B0%9C-%EA%B1%B0%EB%8A%94-%EB%B0%A9%EB%B2%95
# https://cheris8.github.io/python/PY-Compare-String/
# https://codechacha.com/ko/python-convert-integer-to-string/


## 전체 데이터
# from urllib import parse
# import pandas as pd

# def get_fnguide(code):
#     get_param = {
#         'pGB': 1,
#         'gicode': 'A%s' % (code),
#         'cID': '',
#         'MenuYn': 'M',
#         'ReportGB': '',
#         'NewMenuID': 101,
#         'stkGb': 701,
#     }
#     get_param = parse.urlencode(get_param)
#     url = "http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?%s" % (get_param)
#     tables = pd.read_html(url, header=0)
#     return tables

# # '005930' (삼성전자)의 데이터를 가져와서 tables로 저장
# tables = get_fnguide('000150')

# # 가져온 tables를 출력
# for idx, table in enumerate(tables):
#     print(f"Table {idx}:")
#     print(table)
#     print("\n")