#### hitit DB 사용
use hitit;
show databases;

#### 증권_보유_주식 - 외래키 지정 X
CREATE TABLE security_funds (
    account_no VARCHAR(255),
    fund_code VARCHAR(255),
    PRIMARY KEY (account_no, fund_code)
);


## 컬럼 수정
-- ALTER TABLE pensions CHANGE evalutation_amount evaluation_amount VARCHAR(255);

## 연금 조회
select * from security_funds;

## 연금 삭제
DROP TABLE security_funds;

# pensions 모든 행 갯수 출력
SELECT COUNT(*) AS total_rows
FROM security_funds;

set sql_safe_updates=0;
delete from security_stocks where stock_code = "950160";

## security_accounts의 account_no와 비교
SELECT DISTINCT account_no
FROM security_funds
WHERE account_no NOT IN (
    SELECT account_no
    FROM security_accounts
);

## bank_accounts 테이블의 account_no와 비교
SELECT DISTINCT fund_code
FROM security_funds
WHERE fund_code NOT IN (
    SELECT fund_code
    FROM fund_products
);

-- security_accounts 테이블에 외래키 제약 추가
ALTER TABLE security_funds
ADD CONSTRAINT fk_account_no_security_funds
FOREIGN KEY (account_no) REFERENCES security_accounts(account_no);

-- stocks_products 테이블에 외래키 제약 추가
ALTER TABLE security_funds
ADD CONSTRAINT fk_fund_code_security_funds
FOREIGN KEY (fund_code) REFERENCES fund_products(fund_code);