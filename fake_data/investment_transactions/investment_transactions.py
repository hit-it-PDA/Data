import pandas as pd
import random
import string
import datetime
import FinanceDataReader as fdr

# 증권사 리스트
securities_firms = [
    "신한투자증권", "KB증권", "하나증권", "삼성증권",
    "키움증권", "미래에셋증권", "한국투자증권", "대신증권"
]

# 잔액 범위 리스트
balance_ranges = [
    (1_000, 9_999),  # 1만원대
    (10_000, 99_999),  # 10만원대
    (100_000, 999_999),  # 100만원대
    (1_000_000, 9_999_999),  # 1000만원대
    (10_000_000, 99_999_999),  # 1억원대
]

# 고객 ID 생성
customer_ids = list(range(1, 101))

# 계좌번호 생성 함수
def generate_account_number(used_accounts):
    while True:
        account_number = ''.join(random.choices(string.digits, k=random.randint(10, 14)))
        if account_number not in used_accounts:
            used_accounts.add(account_number)
            return account_number

# 주식 코드 가져오기 함수
def get_stock_codes(market: str) -> pd.DataFrame:
    return fdr.StockListing(market)

try:
    kospi_stocks = get_stock_codes('KOSPI')
    kosdaq_stocks = get_stock_codes('KOSDAQ')

    if 'Symbol' in kospi_stocks.columns and 'Symbol' in kosdaq_stocks.columns:
        stock_codes = kospi_stocks['Symbol'].tolist() + kosdaq_stocks['Symbol'].tolist()
    else:
        print("DataFrame에 'Symbol' 열이 존재하지 않습니다.")

except Exception as e:
    print(f"오류 발생: {e}")
    stock_codes = []

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
df_mydata = pd.DataFrame(data)

# 엑셀 파일로 저장
df_mydata.to_excel("마이데이터_증권_가짜데이터.xlsx", index=False)

# 투자_거래내역 데이터 생성
def generate_datetime(start, end):
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

start_date = datetime.datetime(2000, 1, 1)
end_date = datetime.datetime(2024, 6, 10)

transactions = []
transaction_id = 1
account_balances = {account['계좌번호']: account['잔액'] for account in data}

# 각 계좌마다 거래 내역 생성
for account in data:
    account_number = account['계좌번호']
    balance = account['잔액']
    stock_holdings = {}

    for _ in range(random.randint(5, 15)):  # 각 계좌당 5~15개의 거래를 생성
        transaction_type = random.choice(["매수", "매도"])

        if transaction_type == "매도" and not stock_holdings:
            transaction_type = "매수"  # 매도할 주식이 없으면 매수로 변경

        stock_code = random.choice(stock_codes)
        quantity = random.randint(1, 100)  # 거래 수량
        price = random.randint(1_000, 1_000_000)  # 주식 가격
        transaction_date = generate_datetime(start_date, end_date)

        if transaction_type == "매수":
            total_price = price * quantity
            if balance < total_price:
                continue  # 잔액 부족 시 거래 무시

            balance -= total_price
            stock_holdings[stock_code] = stock_holdings.get(stock_code, 0) + quantity
        else:  # 매도
            if stock_code not in stock_holdings or stock_holdings[stock_code] < quantity:
                continue  # 보유 주식 부족 시 거래 무시

            total_price = price * quantity
            balance += total_price
            stock_holdings[stock_code] -= quantity
            if stock_holdings[stock_code] == 0:
                del stock_holdings[stock_code]

        transactions.append({
            "거래 ID": transaction_id,
            "계좌번호": account_number,
            "거래 유형": transaction_type,
            "거래 일시": transaction_date,
            "금액": price,
            "거래후잔액": balance,
            "종목코드": stock_code,
            "수량": quantity
        })

        transaction_id += 1

# 데이터프레임 생성
df_transactions = pd.DataFrame(transactions)

# 엑셀 파일로 저장
df_transactions.to_excel("투자_거래내역_가짜데이터.xlsx", index=False)

print("엑셀 파일 '마이데이터_증권_가짜데이터.xlsx'와 '투자_거래내역_가짜데이터.xlsx'가 생성되었습니다.")
