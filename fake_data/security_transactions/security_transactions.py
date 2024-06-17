import pandas as pd
import random
from datetime import datetime

# 엑셀 파일에서 데이터 불러오기
stocks_df = pd.read_excel('../../public_data_api/stock/stocks_products_details/db/stocks_products_details.xlsx')
accounts_df = pd.read_excel('../security_accounts/db/security_accounts.xlsx')

# 계좌 번호 리스트
account_numbers = accounts_df['account_no'].tolist()

# 거래 데이터를 저장할 리스트 초기화
transactions = []

# 거래 데이터 생성
id_counter = 1
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 6, 12)

# 주식별 매수 수량 추적 딕셔너리 초기화
stock_holdings = {account_no: {} for account_no in account_numbers}

for _ in range(10000):  # 10000개의 거래 생성
    stock = stocks_df.sample().iloc[0]
    account_no = random.choice(account_numbers)
    stock_code = stock['stock_code']
    date = str(stock['date']).split('.')[0]  # "20240606.0" 형식에서 ".0" 제거
    price = stock['price']
    
    # tx_datetime을 'YYYYMMDD' 형식의 문자열로 변환하여 날짜 생성
    tx_datetime = datetime.strptime(date, '%Y%m%d')

    tx_qty = random.randint(1, 100)
    tx_amount = tx_qty * price
    bal_after_tx = random.randint(0, 100000000)
    
    # 매도 거래는 매수 수량 내에서만 발생할 수 있음
    if stock_code in stock_holdings[account_no] and stock_holdings[account_no][stock_code] >= tx_qty:
        tx_type = '매도'
        stock_holdings[account_no][stock_code] -= tx_qty
    else:
        tx_type = '매수'
        if stock_code not in stock_holdings[account_no]:
            stock_holdings[account_no][stock_code] = 0
        stock_holdings[account_no][stock_code] += tx_qty

    transaction = {
        'id': id_counter,
        'tx_datetime': tx_datetime,
        'tx_type': tx_type,
        'tx_amount': tx_amount,
        'bal_after_tx': bal_after_tx,
        'tx_qty': tx_qty,
        'account_no': account_no,
        'stock_code': stock_code
    }
    
    transactions.append(transaction)
    id_counter += 1

# DataFrame으로 변환 후 저장
transactions_df = pd.DataFrame(transactions)
transactions_df.to_excel('./db/security_transactions.xlsx', index=False)
# 데이터프레임을 CSV로 저장
transactions_df.to_csv("./db/security_transactions.csv", index=False)

print("엑셀, csv 파일이 생성되었습니다.")
