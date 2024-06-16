import pandas as pd

# 엑셀 파일 읽기
df = pd.read_excel('./db/stocks_products_details.xlsx')

# 'code' 열을 6자리로 만들고 앞에 나머지 자리 숫자는 0으로 채우기
df['stock_code'] = df['stock_code'].astype(str).str.zfill(6)

# CSV 파일로 저장
df.to_csv('./db/stocks_products_details.csv', index=False)

print('CSV 파일 저장 완료: ./db/stocks_products_details.csv')