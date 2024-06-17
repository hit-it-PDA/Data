import pandas as pd
import random

# security_accounts 데이터를 읽어옴
security_accounts_df = pd.read_excel('../security_accounts/db/security_accounts.xlsx')

# fund_products 데이터를 읽어옴
fund_products_df = pd.read_csv('./db/fundlist.csv')
delete_products_df = pd.read_csv('./db/deleted_funds.csv')

# deleted_funds에 있는 fund_code를 리스트로 추출
deleted_fund_codes = delete_products_df['fund_code'].tolist()

# fund_products_df에서 deleted_fund_codes를 제외한 데이터를 필터링
valid_fund_products_df = fund_products_df[~fund_products_df['fund_code'].isin(deleted_fund_codes)]

# security_funds 데이터 저장용 집합
security_funds_set = set()

# security_accounts에서 account_no 리스트 추출
account_nos = security_accounts_df['account_no'].tolist()

# valid_fund_products_df에서 stock_code 리스트 추출
fund_codes = valid_fund_products_df['fund_code'].tolist()

# 데이터 생성
while len(security_funds_set) < 3000:
    account_no = random.choice(account_nos)
    fund_code = random.choice(fund_codes)
    security_funds_set.add((account_no, fund_code))

# 리스트로 변환 후 DataFrame 생성
security_funds = list(security_funds_set)
security_funds_df = pd.DataFrame(security_funds, columns=['account_no', 'fund_code'])

# 엑셀 파일로 저장
security_funds_df.to_excel('./db/security_funds.xlsx', index=False)
# CSV로 저장
security_funds_df.to_csv('./db/security_funds.csv', index=False)

print("security_funds 데이터 생성 완료!")
