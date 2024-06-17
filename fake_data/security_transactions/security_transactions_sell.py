import pandas as pd
from datetime import datetime, timedelta
import random

# 엑셀 파일에서 데이터 불러오기
transactions_df = pd.read_excel('./db/security_transactions.xlsx')
stock_prices_df = pd.read_excel('../../public_data_api/stock/stocks_products_details/db/stocks_products_details.xlsx')

# 매수 행만 필터링
buy_transactions = transactions_df[transactions_df['tx_type'] == '매수']

# 매도 거래 데이터를 저장할 리스트 초기화
sell_transactions = []

# 날짜 형식 변환 함수
def convert_date_format(date_str):
    return datetime.strptime(date_str, "%Y%m%d")

# stock_prices_df의 날짜 형식을 문자열로 변환한 후 datetime 형식으로 변환
stock_prices_df['date'] = stock_prices_df['date'].astype(str).apply(convert_date_format)

# 매도 거래 생성
for index, row in buy_transactions.iterrows():
    # 매도 수량을 매수 수량의 일부로 설정 (예: 1에서 매수 수량 사이의 임의의 값)
    sell_qty = random.randint(1, row['tx_qty'])
    
    # 매도 거래 생성
    sell_transaction = row.copy()
    sell_transaction['id'] = transactions_df['id'].max() + len(sell_transactions) + 1
    sell_transaction['tx_type'] = '매도'
    
    # 매도 시점은 매수 시점 이후로 설정 (예: 1일 후)
    sell_transaction['tx_datetime'] = row['tx_datetime'] + timedelta(days=1)
    
    # 매도 수량 설정
    sell_transaction['tx_qty'] = sell_qty
    
    # 매도 시점과 종목 코드로 가격 정보 필터링
    sell_date = sell_transaction['tx_datetime'].date()
    stock_price_row = stock_prices_df[(stock_prices_df['date'].apply(lambda x: x.date()) == sell_date) &
                                     (stock_prices_df['stock_code'] == row['stock_code'])]
    
    if not stock_price_row.empty:
        # 매도 시점의 가격 가져오기
        sell_price = stock_price_row['price'].values[0]
        # 매도 금액 계산
        sell_transaction['tx_amount'] = sell_qty * sell_price
        # 매도 후 잔액은 매수 후 잔액에 매도 금액을 더한 값
        sell_transaction['bal_after_tx'] = row['bal_after_tx'] + sell_transaction['tx_amount']
        
        # sell_transactions 리스트에 추가
        sell_transactions.append(sell_transaction)
    else:
        # 해당 날짜에 가격 정보가 없으면 경고 메시지를 출력
        print(f"경고: {sell_transaction['tx_datetime'].date()}에 {row['stock_code']}의 가격 정보를 찾을 수 없습니다.")

# 매도 거래를 DataFrame으로 변환
if sell_transactions:
    sell_transactions_df = pd.DataFrame(sell_transactions)

    # 기존 거래 데이터에 매도 거래 추가
    all_transactions_df = pd.concat([transactions_df, sell_transactions_df], ignore_index=True)

    # 새 엑셀 파일로 저장
    all_transactions_df.to_excel('./db/updated_security_transactions.xlsx', index=False)
    
    print("매도 거래가 성공적으로 추가되었습니다.")
else:
    print("추가된 매도 거래가 없습니다.")
