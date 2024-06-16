#### hitit DB 사용
use hitit;
show databases;

#### 증권_보유_주식 - 외래키 지정 X
CREATE TABLE security_stocks (
    account_no VARCHAR(255),
    stock_code VARCHAR(255),
    PRIMARY KEY (account_no, stock_code)
);


## 컬럼 수정
-- ALTER TABLE pensions CHANGE evalutation_amount evaluation_amount VARCHAR(255);

## 연금 조회
select * from security_stocks;

## 연금 삭제
DROP TABLE security_stocks;

# pensions 모든 행 갯수 출력
SELECT COUNT(*) AS total_rows
FROM security_stocks;

set sql_safe_updates=0;
delete from security_stocks where stock_code = "950160";

## security_accounts의 account_no와 비교
SELECT DISTINCT account_no
FROM security_stocks
WHERE account_no NOT IN (
    SELECT account_no
    FROM security_accounts
);

## bank_accounts 테이블의 account_no와 비교
SELECT DISTINCT stock_code
FROM security_stocks
WHERE stock_code NOT IN (
    SELECT stock_code
    FROM stocks_products
);

-- security_accounts 테이블에 외래키 제약 추가
ALTER TABLE security_stocks
ADD CONSTRAINT fk_account_no_security_stocks
FOREIGN KEY (account_no) REFERENCES security_accounts(account_no);

-- stocks_products 테이블에 외래키 제약 추가
ALTER TABLE security_stocks
ADD CONSTRAINT fk_stock_code_security_stocks
FOREIGN KEY (stock_code) REFERENCES stocks_products(stock_code);