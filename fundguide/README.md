## 펀드 크롤러

### 데이터 수집 출처
[펀드가이드-간편검색](https://www.fundguide.net/Fund/SimpleSearch)

### 실행 방법 

1. 필요 패키지 설치 
```shell
pip freeze > requirements.txt
```

2. fundlist.py 실행 
- 기능 : 사이트 내의 펀드 목록을 csv파일, DB에 저장합니다.
- 특이사항 : 아래 `sel_peers` 변수로 수집할 유형을 선택합니다.
```python
    sel_peers = {
        # "국내주식형": "HS001|HSA01|HSAG1|HSAM1|HSAD1|HSAS1|HSAT1|HSP01|HSPP1|HSPX1|HSPS1|HSPO1",
        # "국내혼합형": "HM001|HMA01|HMS01|HMB01|HMBM1|HMBA1|HMBH1",
        # "국내채권형": "HB001|HBG01|HBC01|HBB01|HBBO1|HBBS1|HBH01",
        # "해외주식형": "FS001|FSC01|FSCJ1|FSCC1|FSCI1|FSCV1|FSCB1|FSCR1|FSCO1|FSS01|FSSE1|FSSM1|FSSH1|FSSF1|FSSI1|FSSP1|FSSC1|FSSN1|FSSO1|FSR01|FSRG1|FSRD1|FSRM1|FSRU1|FSRE1|FSRN1|FSRS1|FSRP1|FSRX1|FSRA1|FSRI1|FSRO1|FSO01",
        "해회혼합형": "FM001|FMA01|FMAD1|FMS01|FMB01|FMO01",
        # "해외채권형": "FB001|FBG01|FBGB1|FBGH1|FBR01|FBRM1|FBRP1|FBRN1|FBRS1|FBRU1|FBO01"
    }
```
- output : `펀드리스트_{~~형}.csv` & `fund_products` 테이블에 저장
  ```csv
    'fund_code', 'fund_name', 'std_price', 'set_date', 'fund_type', 'fund_type_detail', 'set_amount', 'risk_grade', 'risk_grade_txt', 'company_name'
    펀드코드, 펀드이름, 기준가, 설정일, 펀드유형, 펀드유형세부, 펀드규모(설정액), 위험등급(숫자), 위험등급(텍스트), 운용사
    
  ```

3. fund_porfolio.py 실행
- 기능 : DB에 저장된 펀드 코드들의 자산구성, 보유채권, 보유주식을 수집하여 DB에 업로드합니다.  
- 특이사항 : 데이터 양이 많아 아래 `UNIT` 변수를 통해 끊어서 크롤링하였습니다. 
```python
UNIT = 2000
# ...
for fund_code in tqdm(fund_code_list[:UNIT]):
    #...
```

- output : 
  - 자산 구성 : `fund_assets` 테이블에 저장 
     ```csv
    'fund_code', 'stock', 'stock_foreign', 'bond', 'bond_foreign', 'investment', 'etc'    
    펀드코드, 국내주식, 해외주식, 국내채권, 해외채권, 수익증권, 기타
     ```
  - 보유 주식 : `fund_stocks` 테이블에 저장 
     ```csv
    'fund_code', 'stock_name', 'size', 'style', 'rate'
     펀드코드, 주식명, 주식구분_규모, 주식구분_스타일, 비중
     ```
  - 보유 채권 : `fund_bonds` 테이블에 저장 
     ```csv
     'fund_code', 'bond_name', 'expire_date', 'duration', 'credit', 'rate'
     펀드코드, 채권명, 만기일, 듀레이션, 신용등급, 비중
     ```