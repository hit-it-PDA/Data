import pandas as pd
import random

# security_accounts 데이터를 읽어옴
security_accounts_df = pd.read_excel('../security_accounts/db/security_accounts.xlsx')

# stocks_products 데이터를 읽어옴
stocks_products_df = pd.read_excel('../../public_data_api/stock/stocks_products_details/db/stocks_products_details.xlsx')

# security_stocks 데이터 저장용 집합
security_stocks_set = set()

# security_accounts에서 account_no 리스트 추출
account_nos = security_accounts_df['account_no'].tolist()

# stocks_products에서 stock_code 리스트 추출
stock_codes = stocks_products_df['stock_code'].tolist()

# 데이터 생성
while len(security_stocks_set) < 3000:
    account_no = random.choice(account_nos)
    stock_code = random.choice(stock_codes)
    # stock_code를 6자리 문자열로 변환
    formatted_stock_code = f"{int(stock_code):06d}"
    security_stocks_set.add((account_no, formatted_stock_code))

# 리스트로 변환 후 DataFrame 생성
security_stocks = list(security_stocks_set)
security_stocks_df = pd.DataFrame(security_stocks, columns=['account_no', 'stock_code'])

# 엑셀 파일로 저장
security_stocks_df.to_excel('./db/security_stocks.xlsx', index=False)
# CSV로 저장
security_stocks_df.to_csv('./db/security_stocks.csv', index=False)

print("security_stocks 데이터 생성 완료!")