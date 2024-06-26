#### hitit DB 사용
use hitit;
show databases;

#### 연금 - 외래키 지정 X
CREATE TABLE pensions (
    company_name VARCHAR(255),
    pension_name VARCHAR(255),
    pension_type VARCHAR(255),
    user_id INTEGER,
    interest_rate DOUBLE,
    evalutation_amount INTEGER,
    expiration_date DATE,
    account_no VARCHAR(255),
    PRIMARY KEY (company_name, pension_name, pension_type, user_id)
);

## 컬럼 수정
ALTER TABLE pensions CHANGE evalutation_amount evaluation_amount VARCHAR(255);

## 연금 조회
select * from pensions;

## 연금 삭제
DROP TABLE pensions;

# pensions 모든 행 갯수 출력
SELECT COUNT(*) AS total_rows
FROM pensions;

## users의 id와 비교
SELECT DISTINCT user_id
FROM pensions
WHERE user_id NOT IN (
    SELECT id
    FROM users
);

## bank_accounts 테이블의 account_no와 비교
SELECT DISTINCT account_no
FROM pensions
WHERE account_no NOT IN (
    SELECT account_no
    FROM bank_accounts
);

-- users 테이블에 외래키 제약 추가
ALTER TABLE pensions
ADD CONSTRAINT fk_user_id_pensions
FOREIGN KEY (user_id) REFERENCES users(id);

-- bank_accounts 테이블에 외래키 제약 추가
ALTER TABLE pensions
ADD CONSTRAINT fk_account_no_pensions
FOREIGN KEY (account_no) REFERENCES bank_accounts(account_no);