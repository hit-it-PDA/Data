import requests
import csv

def to_csv_format(stocks):
    stock_list = [{} for i in range(len(stocks))]

    for i in range(len(stocks)):
        stock_list[i] = {
            "code": stocks[i]["symbolCode"],
            "stockName": stocks[i]["stockName"],
            "stockNameEng": stocks[i]["stockNameEng"],
            "openPrice": None if stocks[i]["openPrice"] == "-" else float(stocks[i]["openPrice"].replace(",","")),
            "nationType": stocks[i]["nationType"],
        }

    return stock_list

def crawling():
    stocks = []

    for i in range(10):
        response = requests.get("https://api.stock.naver.com/stock/exchange/NASDAQ/marketValue", {
            "page": 1+(20*i),
            "pageSize": 20
        })

        if response.status_code == 200:
            stocks.extend(response.json()["stocks"])
        else:
            print(f"{response.status_code}: error")

    print(f"Foreign Stock's found {len(stocks)}")

    stocks_list = to_csv_format(stocks)

    with open("foreign_stocks.csv", 'w') as f:
        field_names = stocks_list[0].keys()
        w = csv.DictWriter(f, fieldnames=field_names)

        w.writeheader()
        w.writerows(stocks_list)

        f.close()

if __name__ == '__main__':
    crawling()