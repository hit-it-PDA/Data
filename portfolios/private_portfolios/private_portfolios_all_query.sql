select * from fund_stocks where fund_code = "K55214CD4825"; 
select * from fund_bonds where fund_code = "K55214CD4825";

select * from fund_products_3;
select return_3m from fund_products_3 where fund_code = "K55214CD4825";

select * from fund_stocks;

## PK 추가
ALTER TABLE fund_stocks
ADD PRIMARY KEY (fund_code, stock_name);

## FK 추가
ALTER TABLE fund_stocks
ADD CONSTRAINT fk_fund_code2
FOREIGN KEY (fund_code) REFERENCES fund_products(fund_code);

## 테이블 생성문 조회 - 제약 확인 가능
SHOW CREATE TABLE fund_stocks;


 ## 외래키 제약 삭제
 ALTER TABLE fund_stocks
DROP FOREIGN KEY fk_fund_code2;

## KEY 제약 삭제
ALTER TABLE fund_stocks
DROP KEY fk_fund_code2;

## 테이블 생성문 조회 - 제약 확인 가능
SHOW CREATE TABLE fund_bonds;

## PK 추가
ALTER TABLE fund_bonds
ADD PRIMARY KEY (fund_code, bond_name);

## FK 추가
ALTER TABLE fund_stocks
ADD CONSTRAINT fk_fund_code3
FOREIGN KEY (fund_code) REFERENCES fund_products(fund_code);

 ## 외래키 제약 삭제
ALTER TABLE fund_bonds
DROP FOREIGN KEY fk_fund_code3;

ALTER TABLE fund_bonds
DROP INDEX fk_fund_code3;


## KEY 제약 삭제
ALTER TABLE fund_bonds
DROP KEY fk_fund_code3;




 
 