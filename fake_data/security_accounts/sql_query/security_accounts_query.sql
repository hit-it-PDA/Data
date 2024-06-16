#### hitit DB 사용
use hitit;
show databases;

#### 증권_계좌 - 외래키 지정 X
CREATE TABLE security_accounts (
    account_no VARCHAR(255) PRIMARY KEY,
    security_name VARCHAR(255),
    account_type VARCHAR(255),
    balance INTEGER,
    created_at DATE,
    user_id INTEGER
);


## 컬럼 수정
ALTER TABLE pensions CHANGE evalutation_amount evaluation_amount VARCHAR(255);

## 연금 조회
select * from security_accounts;

## 연금 삭제
DROP TABLE security_accounts;

# pensions 모든 행 갯수 출력
SELECT COUNT(*) AS total_rows
FROM security_accounts;

## users의 id와 비교
SELECT DISTINCT user_id
FROM security_accounts
WHERE user_id NOT IN (
    SELECT id
    FROM users
);

## bank_accounts 테이블의 account_no와 비교
-- SELECT DISTINCT account_no
-- FROM pensions
-- WHERE account_no NOT IN (
--     SELECT account_no
--     FROM bank_accounts
-- );

-- users 테이블에 외래키 제약 추가
ALTER TABLE security_accounts
ADD CONSTRAINT fk_user_id_security_accounts
FOREIGN KEY (user_id) REFERENCES users(id);

-- bank_accounts 테이블에 외래키 제약 추가
-- ALTER TABLE pensions
-- ADD CONSTRAINT fk_account_no_pensions
-- FOREIGN KEY (account_no) REFERENCES bank_accounts(account_no);