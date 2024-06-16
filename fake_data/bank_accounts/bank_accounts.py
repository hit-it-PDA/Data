import pandas as pd
import random
import string
from datetime import datetime, timedelta

# 은행 정보 및 계좌 종류
banks = {
    "KB국민은행": {
        "예금": "KB Star 정기예금",
        "적금": "KB내맘대로적금",
        "입출금": "KB 올인원급여통장",
        "DC": "KB DC 통장",
        "DB": "KB DB 통장",
        "IRP": "KB IRP 통장"
    },
    "IBK기업은행": {
        "예금": "1석7조통장",
        "적금": "IBK D-day적금",
        "입출금": "IBK평생주거래기업통장",
        "DC": "IBK DC 통장",
        "DB": "IBK DB 통장",
        "IRP": "IBK IRP 통장"
    },
    "NH농협은행": {
        "예금": "NH올원e예금",
        "적금": "NH주거래우대적금",
        "입출금": "NH주거래우대통장",
        "DC": "NH DC 통장",
        "DB": "NH DB 통장",
        "IRP": "NH IRP 통장"
    },
    "신한은행": {
        "예금": "쏠편한 정기예금",
        "적금": "신한 안녕, 반가워 적금",
        "입출금": "신한 슈퍼SOL 통장",
        "DC": "신한 DC 통장",
        "DB": "신한 DB 통장",
        "IRP": "신한 IRP 통장"
    },
    "우리은행": {
        "예금": "우리 첫거래우대 정기예금",
        "적금": "WON 적금",
        "입출금": "우리 SUPER주거래 통장",
        "DC": "우리 DC 통장",
        "DB": "우리 DB 통장",
        "IRP": "우리 IRP 통장"
    },
    "하나은행": {
        "예금": "3*6*9 정기예금",
        "적금": "(내맘) 적금",
        "입출금": "주거래하나 통장",
        "DC": "하나 DC 통장",
        "DB": "하나 DB 통장",
        "IRP": "하나 IRP 통장"
    },
    "DGB대구은행": {
        "예금": "DGB주거래우대예금",
        "적금": "고객에게 진심이지 적금",
        "입출금": "iM스마트통장",
        "DC": "DGB DC 통장",
        "DB": "DGB DB 통장",
        "IRP": "DGB IRP 통장"
    },
    "카카오뱅크": {
        "예금": "카카오뱅크 정기예금",
        "적금": "카카오뱅크 자유적금",
        "입출금": "카카오뱅크 입출금통장",
        "DC": "카카오 DC 통장",
        "DB": "카카오 DB 통장",
        "IRP": "카카오 IRP 통장"
    }
}

account_formats = {
    "KB국민은행": "XXXXXX-XX-XXXXXX",
    "IBK기업은행": "XXX-XXXXXX-XX-XXX",
    "NH농협은행": "XXX-XXXX-XXXX-XX",
    "신한은행": "XXX-XXX-XXXXXX",
    "우리은행": "XXXX-XXX-XXXXXX",
    "하나은행": "XXX-XXXXXX-XXXXX",
    "DGB대구은행": "XXX-XX-XXXXXX-X",
    "카카오뱅크": "XXXX-XX-XXXXXXX"
}

def generate_account_number(bank):
    format = account_formats[bank]
    account_no = ""
    for char in format:
        if char == "X":
            account_no += random.choice(string.digits)
        else:
            account_no += char
    return account_no

# 중복 방지를 위한 세트
existing_account_numbers = set()
user_account_types = {}

def unique_account_number(bank):
    while True:
        account_no = generate_account_number(bank)
        if account_no not in existing_account_numbers:
            existing_account_numbers.add(account_no)
            return account_no

# 데이터 생성
data = []
start_date = datetime(2010, 1, 1)
end_date = datetime(2024, 6, 12)
date_range = (end_date - start_date).days

user_ids = list(range(1, 301))
random.shuffle(user_ids)

balance_ranges = [
    (0, 999), # 0~999
    (1_000, 9_999),  # 1000~9999
    (10_000, 99_999),  # 10000~99999
    (100_000, 999_999),  # 100000~999999
    (1_000_000, 9_999_999),  # 1000000~9999999
    (10_000_000, 99_999_999),  # 10000000~99999999
]

for user_id in user_ids:
    user_account_types[user_id] = set()

for _ in range(300):
    while True:
        bank = random.choice(list(banks.keys()))
        account_type = random.choice(list(banks[bank].keys()))
        user_id = random.choice(user_ids)

        # 조건 1: 유저는 DC나 DB 계좌 중 1개만 가질 수 있음
        if account_type in ["DC", "DB"]:
            # 유저가 이미 DC나 DB 계좌를 가지고 있는지 확인
            if any(acc in ["DC", "DB"] for _, acc in user_account_types[user_id]):
                continue

        if (bank, account_type) not in user_account_types[user_id]:
            user_account_types[user_id].add((bank, account_type))
            break

    account_no = unique_account_number(bank)
    account_name = banks[bank][account_type]
    balance_range = random.choice(balance_ranges)
    balance = random.randint(balance_range[0], balance_range[1])
    created_at = (start_date + timedelta(days=random.randint(0, date_range))).strftime("%Y-%m-%d")
    
    data.append({
        "account_no": account_no,
        "bank_name": bank,
        "account_type": account_type,
        "name": account_name,
        "balance": balance,
        "created_at": created_at,
        "user_id": user_id
    })

# 데이터프레임 생성 및 엑셀로 저장
df = pd.DataFrame(data)
df.to_excel("./db/bank_accounts.xlsx", index=False)
# 데이터프레임을 CSV로 저장
df.to_csv("./db/bank_accounts.csv", index=False)