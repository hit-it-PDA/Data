## 채권 크롤러

### 데이터 수집 출처

[신한투자증권-장내채권시세](https://www.shinhansec.com/siw/wealth-management/bond-rp/590401/view.do)

### 실행 방법

1. 필요 패키지 설치 
```shell
pip freeze > requirements.txt
```

2. bondlist.py 실행 
- 실행시간 기준 사이트 내의 채권상품 목록을 저장합니다.
```csv
'종목명', '종목코드', '현재가', '등락률', '거래량', '거래대금', '매수 수익률', '매도 수익률'
```
