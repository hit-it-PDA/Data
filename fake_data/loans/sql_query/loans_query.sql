#### hitit DB 사용
use hitit;
show databases;

#### 대출 - 외래키 지정 X
CREATE TABLE loans (
    company_name VARCHAR(255),
    loan_type VARCHAR(255),
    user_id INTEGER,
    loan_amount INTEGER,
    interest_rate DOUBLE,
    total_payments INTEGER,
    account_no VARCHAR(255),
    PRIMARY KEY (company_name, loan_type, user_id)
);


## 대출 조회
select * from loans;


## 대출 삭제
DROP TABLE loans;

# loans 모든 행 갯수 출력
SELECT COUNT(*) AS total_rows
FROM loans;

## users의 id와 비교
SELECT DISTINCT user_id
FROM loans
WHERE user_id NOT IN (
    SELECT id
    FROM users
);

## bank_accounts 테이블의 account_no와 비교
SELECT DISTINCT account_no
FROM loans
WHERE account_no NOT IN (
    SELECT account_no
    FROM bank_accounts
);

-- users 테이블에 외래키 제약 추가
ALTER TABLE loans
ADD CONSTRAINT fk_user_id_loans
FOREIGN KEY (user_id) REFERENCES users(id);

-- bank_accounts 테이블에 외래키 제약 추가
ALTER TABLE loans
ADD CONSTRAINT fk_account_no_loans
FOREIGN KEY (account_no) REFERENCES bank_accounts(account_no);