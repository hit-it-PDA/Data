import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# 증권사 데이터
securities_data = [
    ("신한투자증권", "000-00-000000"),
    ("미래에셋대우", "000–0000–0000-0"),
    ("키움증권", "0000-0000"),
    ("하나증권", "00000000-000"),
    ("한국투자증권", "00000000-00"),
    ("KB증권", "000000-000000")
]

# 잔액 범위
balance_ranges = [
    (0, 999),
    (1_000, 9_999),
    (10_000, 99_999),
    (100_000, 999_999),
    (1_000_000, 9_999_999),
    (10_000_000, 99_999_999),
]

# 랜덤한 잔액 생성 함수
def generate_balance():
    range_choice = random.choice(balance_ranges)
    return random.randint(range_choice[0], range_choice[1])

# 랜덤한 날짜 생성 함수
def generate_random_date(start_date, end_date):
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())
    random_timestamp = random.randint(start_timestamp, end_timestamp)
    return datetime.fromtimestamp(random_timestamp).strftime('%Y-%m-%d')

# 유저 ID 생성
user_ids = list(range(1, 301))

# 은행 계좌 데이터 로드
bank_accounts_df = pd.read_excel('../bank_accounts/db/bank_accounts.xlsx')

# 증권 계좌 데이터 저장용 리스트
securities_accounts = []

# 계좌번호 랜덤 생성 함수
def generate_account_no(format_string):
    return ''.join(str(random.randint(0, 9)) if char == '0' else char for char in format_string)

# 증권 계좌 생성
for user_id in user_ids:
    user_bank_accounts = bank_accounts_df[bank_accounts_df['user_id'] == user_id]
    has_dc_or_db = any(user_bank_accounts['account_type'].isin(['DC', 'DB']))
    
    number_of_accounts = random.randint(0, 5)  # 유저가 가질 계좌 수 랜덤 결정
    
    for _ in range(number_of_accounts):
        if has_dc_or_db:
            possible_account_types = ['종합', 'IRP']
        else:
            possible_account_types = ['종합', 'DC', 'DB', 'IRP']
        
        account_type = random.choice(possible_account_types)
        
        # 증권사와 계좌번호 선택
        security_name, account_no_format = random.choice(securities_data)
        
        # 계좌번호 생성
        account_no = generate_account_no(account_no_format)
        
        # 잔액 생성
        balance = generate_balance()
        
        # 생성일자 생성
        created_at = generate_random_date(datetime(2010, 1, 1), datetime(2024, 6, 12))
        
        # 증권 계좌 추가
        securities_accounts.append({
            'account_no': account_no,
            'security_name': security_name,
            'account_type': account_type,
            'balance': balance,
            'created_at': created_at,
            'user_id': user_id
        })

# DataFrame으로 변환 후 CSV로 저장
securities_accounts_df = pd.DataFrame(securities_accounts)
securities_accounts_df.to_excel('./db/security_accounts.xlsx', index=False)
securities_accounts_df.to_csv('./db/security_accounts.csv', index=False)

print("증권 계좌 데이터 생성 완료!")
