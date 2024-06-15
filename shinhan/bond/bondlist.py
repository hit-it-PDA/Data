from utils.date import get_date_sdt
import requests
import pandas as pd
from tqdm import tqdm

if __name__ == "__main__":
    # 요청할 API URL
    url = f'https://www.shinhansec.com/siw/wealth-management/bond-rp/590401/data.do'

    sdt = get_date_sdt()

    data = {
        "header": {
            "TCD": "S",
            "SDT": sdt,
            "SVW": "/siw/wealth-management/bond-rp/590401/view.do"
        },
        "body": {}
    }

    # API 요청 보내기
    response = requests.post(url, data=data)

    # 응답 상태 코드 확인
    if response.status_code == 200:
        data_list = response.json()['body']['반복데이타0']
        all_items = []

        for data in tqdm(data_list):
            item_name = data[0].strip()
            item_code = data[6]
            current_price = data[7]
            change_rate = data[19]
            trading_volume = data[18]
            trading_value = data[3]
            buy_return_rate = data[13]
            sell_return_rate = data[1]

            all_items.append([item_name, item_code, current_price, change_rate, trading_volume,
                              trading_value, buy_return_rate, sell_return_rate])

        # DataFrame 생성
        df = pd.DataFrame(all_items, columns=['종목명', '종목코드', '현재가', '등락률', '거래량', '거래대금', '매수 수익률', '매도 수익률'])


        # 파일로 저장
        df.to_csv(f'채권상품_{sdt}.csv', index=False)
        df.to_excel(f'채권상품_{sdt}.xlsx', index=False)
        print(f'저장 완료 : 채권상품_{sdt}')
    else:
        print("연결 실패")
