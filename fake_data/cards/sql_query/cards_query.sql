#### hitit DB 사용
use hitit;
show databases;

#### 카드 - 외래키 지정 X
CREATE TABLE cards (
    card_no VARCHAR(255) PRIMARY KEY,
    company_name VARCHAR(255),
    name VARCHAR(255),
    card_type VARCHAR(255),
    created_at DATE,
    expired_at DATE,
    account_no VARCHAR(255),
    user_id INT
);


## 카드 조회
select * from cards;


## 카드 삭제
DROP TABLE cards;

# bank_accounts 모든 행 갯수 출력
SELECT COUNT(*) AS total_rows
FROM cards;

## users 테이블의 id와 비교
SELECT DISTINCT user_id
FROM cards
WHERE user_id NOT IN (
    SELECT id
    FROM users
);

## bank_accounts 테이블의 account_no와 비교
SELECT DISTINCT account_no
FROM cards
WHERE account_no NOT IN (
    SELECT account_no
    FROM bank_accounts
);


-- users 테이블에 외래키 제약 추가
ALTER TABLE cards
ADD CONSTRAINT fk_user_id_cards
FOREIGN KEY (user_id) REFERENCES users(id);

-- bank_accounts 테이블에 외래키 제약 추가
ALTER TABLE cards
ADD CONSTRAINT fk_account_no
FOREIGN KEY (account_no) REFERENCES bank_accounts(account_no);