#### hitit DB 사용
use hitit;
show databases;

#### 증권_거래내역 - 외래키 지정 X
CREATE TABLE security_transactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tx_datetime DATETIME,
    tx_type VARCHAR(255),
    tx_amount INT,
    bal_after_tx INT,
    tx_qty INT,
    account_no VARCHAR(255),
    stock_code VARCHAR(255)
);


## 컬럼 수정
ALTER TABLE security_transactions CHANGE evalutation_amount evaluation_amount VARCHAR(255);

## 증권_거래내역 조회
select * from security_transactions;

## 증권_거래내역 삭제
DROP TABLE security_transactions;

# security_transactions 모든 행 갯수 출력
SELECT COUNT(*) AS total_rows
FROM security_transactions;

## users의 id와 비교
SELECT DISTINCT stock_code
FROM security_transactions
WHERE stock_code NOT IN (
    SELECT stock_code
    FROM stocks_products
);

## bank_accounts 테이블의 account_no와 비교
SELECT DISTINCT account_no
FROM security_transactions
WHERE account_no NOT IN (
    SELECT account_no
    FROM security_accounts
);

-- users 테이블에 외래키 제약 추가
ALTER TABLE security_transactions
ADD CONSTRAINT fk_account_no_security_transactions
FOREIGN KEY (account_no) REFERENCES security_accounts(account_no);

-- bank_accounts 테이블에 외래키 제약 추가
ALTER TABLE security_transactions
ADD CONSTRAINT fk_stock_code_security_transactions
FOREIGN KEY (stock_code) REFERENCES stocks_products(stock_code);