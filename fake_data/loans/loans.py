import pandas as pd
import random

# 은행 계좌 엑셀 파일 읽기
bank_accounts_df = pd.read_excel('../bank_accounts/db/bank_accounts.xlsx')

# 입출금 계좌를 가진 유저 필터링
filtered_users = bank_accounts_df[bank_accounts_df['account_type'] == '입출금'].drop_duplicates(subset=['user_id'])

# 대출 데이터
loan_data = [
    {"company_name": "KB국민은행", "loan_type": "신용한도대출", "interest_rate": 7.04},
    {"company_name": "NH농협은행", "loan_type": "신용한도대출", "interest_rate": 6.82},
    {"company_name": "우리은행", "loan_type": "신용한도대출", "interest_rate": 6.65},
    {"company_name": "신한은행", "loan_type": "신용한도대출", "interest_rate": 6.84},
    {"company_name": "하나은행", "loan_type": "신용한도대출", "interest_rate": 6.82},
    {"company_name": "KB국민은행", "loan_type": "주택담보대출", "interest_rate": 5.36},
    {"company_name": "NH농협은행", "loan_type": "주택담보대출", "interest_rate": 5.09},
    {"company_name": "우리은행", "loan_type": "주택담보대출", "interest_rate": 5.36},
    {"company_name": "신한은행", "loan_type": "주택담보대출", "interest_rate": 5.61},
    {"company_name": "하나은행", "loan_type": "주택담보대출", "interest_rate": 5.02}
]

# 대출 금액 선택지
loan_amounts = [10000000, 100000000, 1000000000]  # 백만원, 천만원, 일억원

# 새로운 데이터프레임 생성
loan_records = []

for index, row in filtered_users.iterrows():
    loan_info = random.choice(loan_data)
    loan_amount = random.choice(loan_amounts)
    total_payments = random.randint(0, 10)
    
    loan_record = {
        "user_id": row['user_id'],
        "account_no": row['account_no'],
        "company_name": loan_info['company_name'],
        "loan_type": loan_info['loan_type'],
        "interest_rate": loan_info['interest_rate'],
        "loan_amount": loan_amount,
        "total_payments": total_payments
    }
    
    loan_records.append(loan_record)

# 데이터프레임으로 변환
loan_records_df = pd.DataFrame(loan_records)

# 엑셀 파일로 저장
loan_records_df.to_excel('./db/loans.xlsx', index=False)
# 데이터프레임을 CSV로 저장
loan_records_df.to_csv("./db/loans.csv", index=False)

print("엑셀, csv 파일이 생성되었습니다.")