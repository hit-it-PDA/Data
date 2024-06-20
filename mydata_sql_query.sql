#### hitit DB 사용
use hitit;
show databases;

## 주식상품
CREATE TABLE stocks_products (
    code VARCHAR(20) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    market_type VARCHAR(255),
    region VARCHAR(20)
);

## 주식상품 전체 조회
select * from stocks_products;
select * from stocks_products_details;

## 주식상품 테이블 삭제
DROP TABLE stocks_products; 
DROP TABLE stocks_products_details;

## 권한 확인
GRANT REFERENCES ON hitit.* TO 'hitit-user';
FLUSH PRIVILEGES;

CREATE TABLE stocks_products_details (
    date DATE NOT NULL,
    code VARCHAR(20) NOT NULL,
    price INT,
    amount INT,
    volume INT,
    per DECIMAL(10, 2),
    eps DECIMAL(10, 2),
    PRIMARY KEY (date, code),
    FOREIGN KEY (code) REFERENCES stocks_products(code)
);

commit;

# stocks_products_details 모든 행 갯수 출력
SELECT COUNT(*) AS total_rows
FROM stocks_products;


LOAD DATA INFILE 'C:/Users/프로디지털S009/Desktop/HitIt/Data/public_data_api/stock/stocks_products_details.csv'
INTO TABLE stocks_products_details
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT @@GLOBAL.secure_file_priv;

-- stocks_products_details 테이블에 외래키 제약 추가
ALTER TABLE stocks_products_details
ADD CONSTRAINT fk_stock_code
FOREIGN KEY (stock_code) REFERENCES stocks_products(stock_code);


set sql_safe_updates=0;

SELECT DISTINCT stock_code
FROM stocks_products_details
WHERE stock_code NOT IN (
    SELECT stock_code
    FROM stocks_products
);

DELETE FROM stocks_products_details
WHERE stock_code NOT IN (
    SELECT stock_code
    FROM stocks_products
);



