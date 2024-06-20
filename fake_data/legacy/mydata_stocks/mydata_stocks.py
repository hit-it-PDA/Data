import pandas as pd
import random
import string

# 고객 ID 생성
customer_ids = list(range(1, 101))

# 증권사 리스트
securities_firms = [
    "신한투자증권", "KB증권", "하나증권", 
    "키움증권", "미래에셋증권", "한국투자증권"
]

# 계좌번호 생성 함수
def generate_account_number(used_accounts):
    while True:
        account_number = ''.join(random.choices(string.digits, k=random.randint(10, 14)))
        if account_number not in used_accounts:
            used_accounts.add(account_number)
            return account_number

# 잔액 범위 리스트
balance_ranges = [
    (1_000, 9_999),  # 1만원대
    (10_000, 99_999),  # 10만원대
    (100_000, 999_999),  # 100만원대
    (1_000_000, 9_999_999),  # 1000만원대
    (10_000_000, 99_999_999),  # 1억원대
    (100_000_000, 999_999_999)  # 10억원대
]

# 데이터 저장 리스트
data = []

# 사용된 계좌번호 및 고객ID-증권사-계좌종류 조합을 저장하기 위한 집합
used_accounts = set()
used_combinations = set()

# 데이터 생성
for customer_id in customer_ids:
    for _ in range(random.randint(1, 3)):  # 각 고객당 1~3개의 계좌를 생성
        while True:
            account_number = generate_account_number(used_accounts)
            securities_firm = random.choice(securities_firms)
            account_type = random.choice(["종합매매계좌", "종합매매+CMA 계좌"])
            combination_key = (customer_id, securities_firm, account_type)
            if combination_key not in used_combinations:
                used_combinations.add(combination_key)
                break
        
        balance_range = random.choice(balance_ranges)
        balance = random.randint(balance_range[0], balance_range[1])  # 선택된 범위 내에서 랜덤 정수 잔액 생성
        
        data.append({
            "고객 ID": customer_id,
            "계좌번호": account_number,
            "증권사": securities_firm,
            "계좌종류": account_type,
            "잔액": balance
        })

# 데이터프레임 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
df.to_excel("마이데이터_증권_가짜데이터.xlsx", index=False)

