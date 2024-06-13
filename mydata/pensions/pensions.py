import pandas as pd
import random
from datetime import datetime, timedelta

# 엑셀 파일 경로
file_path = "../../db/은행_계좌.xlsx"

# 엑셀 파일 읽기
df = pd.read_excel(file_path)

# 연금 상품 데이터
pension_products = [
    {"company_name": "NH농협은행", "type": "DB", "name": "농협은행 퇴직연금 정기예금", "interest_rate": 3.39},
    {"company_name": "NH농협은행", "type": "DC", "name": "농협은행 퇴직연금 정기예금", "interest_rate": 3.29},
    {"company_name": "NH농협은행", "type": "IRP", "name": "농협은행 퇴직연금 정기예금", "interest_rate": 3.29},
    {"company_name": "신한은행", "type": "DB", "name": "신한은행 퇴직연금 정기예금", "interest_rate": 3.39},
    {"company_name": "신한은행", "type": "DC", "name": "신한은행 퇴직연금 정기예금", "interest_rate": 3.29},
    {"company_name": "신한은행", "type": "IRP", "name": "신한은행 퇴직연금 정기예금", "interest_rate": 3.29},
    {"company_name": "우리은행", "type": "DC", "name": "우리은행 퇴직연금 정기예금", "interest_rate": 3.40},
    {"company_name": "우리은행", "type": "IRP", "name": "우리은행 퇴직연금 정기예금", "interest_rate": 3.40},
    {"company_name": "하나은행", "type": "DB", "name": "하나은행 퇴직연금 정기예금", "interest_rate": 3.45},
    {"company_name": "하나은행", "type": "DC", "name": "하나은행 퇴직연금 정기예금", "interest_rate": 3.35},
    {"company_name": "하나은행", "type": "IRP", "name": "하나은행 퇴직연금 정기예금", "interest_rate": 3.35},
    {"company_name": "KB국민은행", "type": "DB", "name": "국민은행 퇴직연금 정기예금", "interest_rate": 3.39},
    {"company_name": "KB국민은행", "type": "DC", "name": "국민은행 퇴직연금 정기예금", "interest_rate": 3.29},
    {"company_name": "KB국민은행", "type": "IRP", "name": "국민은행 퇴직연금 정기예금", "interest_rate": 3.29},
]

# 평가 금액 범위
balance_ranges = [
    (0, 999),  # 0~999
    (1_000, 9_999),  # 1,000~9,999
    (10_000, 99_999),  # 10,000~99,999
    (100_000, 999_999),  # 100,000~999,999
    (1_000_000, 9_999_999),  # 1,000,000~9,999,999
    (10_000_000, 99_999_999),  # 10,000,000~99,999,999
]

# 결과를 저장할 리스트
results = []

# 평가 금액과 만기일 생성 함수
def generate_evaluation_amount():
    selected_range = random.choice(balance_ranges)
    return round(random.randint(selected_range[0], selected_range[1]), 2)

def generate_expiration_date():
    start_date = datetime(2024, 6, 13)
    end_date = datetime(2025, 6, 13)
    return (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime("%Y-%m-%d")

# 조건에 따라 연금 상품 가입
for _, row in df.iterrows():
    if row['type'] == 'IRP':
        for product in pension_products:
            if product['type'] == 'IRP':
                results.append({
                    "account_no": row['account_no'],
                    "user_id": row['user_id'],
                    "company_name": product['company_name'],
                    "name": product['name'],
                    "type": product['type'],
                    "interest_rate": product['interest_rate'],
                    "evaluation_amount": generate_evaluation_amount(),
                    "expiration_date": generate_expiration_date()
                })
    elif row['type'] == 'DC':
        for product in pension_products:
            if product['type'] == 'DC':
                results.append({
                    "account_no": row['account_no'],
                    "user_id": row['user_id'],
                    "company_name": product['company_name'],
                    "name": product['name'],
                    "type": product['type'],
                    "interest_rate": product['interest_rate'],
                    "evaluation_amount": generate_evaluation_amount(),
                    "expiration_date": generate_expiration_date()
                })
    elif row['type'] == 'DB':
        for product in pension_products:
            if product['type'] == 'DB':
                results.append({
                    "account_no": row['account_no'],
                    "user_id": row['user_id'],
                    "company_name": product['company_name'],
                    "name": product['name'],
                    "type": product['type'],
                    "interest_rate": product['interest_rate'],
                    "evaluation_amount": generate_evaluation_amount(),
                    "expiration_date": generate_expiration_date()
                })

# 결과를 데이터프레임으로 변환
result_df = pd.DataFrame(results)

# 결과를 엑셀 파일로 저장
result_df.to_excel("../../db/연금.xlsx", index=False)
