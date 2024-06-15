## 채권 크롤러 

### 데이터 수집 출처

[공공 데이터 포털 - 금융위원회_채권시세정보](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15094784)

### 실행 방법

1. 필요 패키지 설치 
```shell
pip freeze > requirements.txt
```

2. public_data_api/bond 폴더 내의 bondlist.py 실행
- 아래 두 변수를 설정해 원하는 기간의 데이터를 수집합니다.
```python
begin_base_date = "20240601" # 시작 일자 
end_base_date = "20240612" # 이하일자 
# -> 20240601 ~ 20240611 
```

main에서 아래 두 함수를 실행하면 csv 파일이 나옵니다. 
- 채권상품 : fetch_bond_product_list(last_page)
```csv
'종목코드', '코드이름', '시장_구분'
```

- 채권시세 : fetch_bond_price_list(last_page)
```csv
 '기준일자', '종목코드', '종가', '전일대비등락', '종가_수익률', '최초가', '시가_수익률', '최고가', '최고가_수익률', '최저가', '최저가_수익률'
```
