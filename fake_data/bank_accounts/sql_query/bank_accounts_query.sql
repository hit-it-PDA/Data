#### hitit DB 사용
use hitit;
show databases;

#### 은행_계좌 - 외래키 지정 X
CREATE TABLE bank_accounts (
    account_no VARCHAR(255),
    bank_name VARCHAR(255),
    type VARCHAR(255),
    name VARCHAR(255),
    balance INT,
    created_at DATE,
    user_id INT,
    PRIMARY KEY (account_no)
);

## 은행_계좌 조회
select * from bank_accounts;


## 은행_계좌 삭제
DROP TABLE bank_accounts;

# bank_accounts 모든 행 갯수 출력
SELECT COUNT(*) AS total_rows
FROM bank_accounts;


SELECT DISTINCT user_id
FROM bank_accounts
WHERE user_id NOT IN (
    SELECT id
    FROM users
);

-- bank_accounts 테이블에 외래키 제약 추가
ALTER TABLE bank_accounts
ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id) REFERENCES users(id);