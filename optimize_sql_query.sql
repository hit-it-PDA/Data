SELECT * FROM hitit.fund_stocks;
show create table fund_stocks;

drop table fund_stocks;
drop table fund_bonds;

CREATE TABLE `fund_stocks` (
   `fund_code` varchar(255) NOT NULL COMMENT '펀드코드',
   `stock_name` varchar(255) NOT NULL COMMENT '주식종목명',
   `size` varchar(255) DEFAULT NULL COMMENT '주식구분_규모',
   `style` varchar(255) DEFAULT NULL COMMENT '주식구분_스타일',
   `weight` float DEFAULT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 CREATE TABLE `fund_bonds` (
   `fund_code` varchar(255) NOT NULL COMMENT '펀드코드',
   `bond_name` varchar(255) NOT NULL COMMENT '채권종목명',
   `expire_date` date DEFAULT NULL COMMENT '만기일자',
   `duration` float DEFAULT NULL COMMENT '듀레이션',
   `credit` float DEFAULT NULL COMMENT '신용등급',
   `weight` float DEFAULT NULL,
   PRIMARY KEY (`fund_code`,`bond_name`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 show create table fund_stocks;
 CREATE TABLE `fund_stocks` (
   `fund_code` varchar(255) NOT NULL COMMENT '펀드코드',
   `stock_name` varchar(255) NOT NULL COMMENT '주식종목명',
   `size` varchar(255) DEFAULT NULL COMMENT '주식구분_규모',
   `style` varchar(255) DEFAULT NULL COMMENT '주식구분_스타일',
   `weight` float DEFAULT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 show create table fund_bonds;
 CREATE TABLE `fund_bonds` (
   `fund_code` varchar(255) NOT NULL COMMENT '펀드코드',
   `bond_name` varchar(255) NOT NULL COMMENT '채권종목명',
   `expire_date` date DEFAULT NULL COMMENT '만기일자',
   `duration` float DEFAULT NULL COMMENT '듀레이션',
   `credit` float DEFAULT NULL COMMENT '신용등급',
   `weight` float DEFAULT NULL,
   PRIMARY KEY (`fund_code`,`bond_name`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 select * from fund_bonds;
 select * from fund_stocks;
 
 select * from user_select;
 drop table user_select;
 

 
 select * from user_portfolios;
 show create table user_portfolios;CREATE TABLE `user_portfolios` (
   `id` int unsigned NOT NULL AUTO_INCREMENT,
   `name` varchar(255) DEFAULT NULL,
   `investment_type` varchar(255) DEFAULT NULL,
   `summary` varchar(255) DEFAULT NULL,
   `minimum_subscription_fee` int unsigned DEFAULT NULL,
   `stock_exposure` int unsigned DEFAULT NULL,
   PRIMARY KEY (`id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 ALTER TABLE `user_portfolios`
ADD COLUMN `user_id` int unsigned DEFAULT NULL;
UPDATE `user_portfolios`
SET `user_id` = 1
WHERE `id` = 1;



 select * from user_portfolios;
 show create table user_portfolios;
 select * from user_portfolios;
 select * from user_portfolios_fund_products where portfolio_id = 1;
 select * from fund_stocks where fund_code = "K55301B73766";
 
 CREATE TABLE `user_portfolios` (
   `id` int unsigned NOT NULL AUTO_INCREMENT,
   `name` varchar(255) DEFAULT NULL,
   `investment_type` varchar(255) DEFAULT NULL,
   `summary` varchar(255) DEFAULT NULL,
   `minimum_subscription_fee` int unsigned DEFAULT NULL,
   `stock_exposure` int unsigned DEFAULT NULL,
   `user_id` int unsigned DEFAULT NULL,
   PRIMARY KEY (`id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 -- insert into user_portfolios values (1, "스마트세이버", "안정형", "이 포트폴리오는 어떤 포트폴리오입니다.", 100,20);
 
 select * from user_portfolios_fund_products;
 select * from user_portfolios_fund_stocks;
 
 DELETE FROM user_portfolios_fund_products where fund_code = " 'K55101C35403"; 

 
 
 
 insert into user_portfolios_fund_products values 
 ("K55101B47624", 1,  "신한더드림러시아증권모투자신탁[주식]", "해외주식형", "신한자산운용", 15, 4.31);
 
 
 
  insert into user_portfolios_fund_products values 
 ("K55301B73766", 1,  "미래에셋TIGER화장품증권상장지수투자신탁(주식)", "국내주식형", "미래에셋자산운용", 20, 59.12);
 
 select * from fund_stocks;
 select * from stocks_products;
 
 select count(*) from stocks_products where sentiment = 0;
 select * from stocks_products;
 select * from user_portfolios;
 select * from user_portfolios_fund_products;
 
 select * from user_portfolios;
 
 UPDATE `user_portfolios_fund_products`
SET `weight` = 15
WHERE `fund_code` = "K55101B46238";

select * from fund_bonds;
select * from fund_stocks;
select * from fund_assets;
select count(*) from fund_assets;

show create table fund_stocks;

drop table fund_assets;
show create table fund_assets;
CREATE TABLE `fund_assets` (
   `fund_code` varchar(255) NOT NULL,
   `stock` float DEFAULT NULL,
   `stock_foreign` float DEFAULT NULL,
   `bond` float DEFAULT NULL,
   `bond_foreign` float DEFAULT NULL,
   `investment` float DEFAULT NULL,
   `etc` float DEFAULT NULL,
   PRIMARY KEY (`fund_code`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 select * from fund_assets;
select count(*) from fund_assets;

show create table fund_assets;
CREATE TABLE `fund_assets` (
   `fund_code` varchar(255) NOT NULL,
   `stock` float DEFAULT NULL,
   `stock_foreign` float DEFAULT NULL,
   `bond` float DEFAULT NULL,
   `bond_foreign` float DEFAULT NULL,
   `investment` float DEFAULT NULL,
   `etc` float DEFAULT NULL,
   PRIMARY KEY (`fund_code`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 drop table fund_assets;
 
 show create table fund_products_4;
 CREATE TABLE `fund_products_4` (
   `fund_code` varchar(255) DEFAULT NULL,
   `fund_name` varchar(255) DEFAULT NULL,
   `hashtag` varchar(255) DEFAULT NULL,
   `std_price` float DEFAULT NULL,
   `set_date` date DEFAULT NULL,
   `fund_type` varchar(255) DEFAULT NULL,
   `fund_type_detail` varchar(255) DEFAULT NULL,
   `set_amount` int DEFAULT NULL,
   `company_name` varchar(255) DEFAULT NULL,
   `risk_grade` int DEFAULT NULL,
   `risk_grade_txt` varchar(255) DEFAULT NULL,
   `drv_nav` float DEFAULT NULL,
   `bond` float DEFAULT NULL,
   `bond_foreign` float DEFAULT NULL,
   `stock` float DEFAULT NULL,
   `stock_foreign` text,
   `investment` float DEFAULT NULL,
   `etc` float DEFAULT NULL,
   `return_1m` float DEFAULT NULL,
   `return_3m` float DEFAULT NULL,
   `return_6m` float DEFAULT NULL,
   `return_1y` float DEFAULT NULL,
   `return_3y` float DEFAULT NULL,
   `return_5y` float DEFAULT NULL,
   `return_idx` float DEFAULT NULL,
   `return_ytd` float DEFAULT NULL,
   `arima_price` double DEFAULT NULL,
   `arima_update` date DEFAULT NULL,
   `arima_percent` double DEFAULT NULL,
   `stock_ratio` float DEFAULT NULL,
   `bond_ratio` float DEFAULT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 
 select * from fund_products_4;

 ALTER TABLE `fund_products_4`
ADD PRIMARY KEY (`fund_code`);

select count(*) from fund_products_4;

ALTER TABLE `fund_products_4`
MODIFY COLUMN `stock_foreign` FLOAT;

select * from user_portfolios;
select * from user_portfolios_fund_products;

select * from user_portfolios_fund_bonds;
select * from user_portfolios_fund_stocks;
select * from user_portfolios_fund_assets;
select * from fund_assets;
drop table user_portfolios_fund_bonds;

select * from private_portfolios;
select * from private_portfolios_fund_products;

show create table user_portfolios;
select * from user_portfolios_fund_products;
select * from fund_products_4 where fund_name = "신한";

SELECT * FROM fund_products_4
WHERE fund_name LIKE '신한%' and fund_type_detail = "해외주식형";

select * from fund_bonds where fund_code = "K55210BT7106";


-- K55210BT7106

select * from private_portfolios;
select * from private_portfolios_fund_products;

DELETE FROM private_portfolios_fund_products
WHERE fund_code = '2117610';

Delete from private_portfolios_fund_assets where fund_code = '2117610';
Delete from private_portfolios_fund_stocks where fund_code = '2117610';
Delete from private_portfolios_fund_bonds where fund_code = '2117610';
delete from user_portfolios_fund_products where fund_code = 'K55210BT7106';

select fund_code, fund_name, fund_type_detail, company_name, return_3m from fund_products_4 where fund_code = "K55210BT7106"; 

 insert into user_portfolios_fund_products values 
 ("K55101B47624", 1,  "신한더드림러시아증권모투자신탁[주식]", "해외주식형", "신한자산운용", 15, 4.31);
 
  insert into private_portfolios_fund_products values 
 ("K55210BT7106", 3,  "신한해피라이프연금중국본토중소형주증권자투자신탁 1(H)[주식](종류C-re)", "해외주식형", "신한자산운용", 25, 1.14);
 
 select * from private_portfolios;
 select * from user_portfolios;
 select * from user_portfolios_fund_products;
 select * from private_portfolios_fund_products;
 select * from private_portfolios;
 
 Delete from user_portfolios_fund_products where fund_code = "K55207BU0715";
 

 
  insert into user_portfolios_fund_products values 
 ("K55301B73766", 1,  "미래에셋TIGER화장품증권상장지수투자신탁(주식)", "국내주식형", "미래에셋자산운용", 20, 59.12);
 
 select * from fund_products_4;
 
 select * from fund_products_4 where fund_code = "K55213BU7688";
 
 insert into fund_products_4 values 
('K55207BU0715', '교보악사파워인덱스증권자투자신탁 1(주식)ClassC-Pe', '#국내주식형#퇴직연금', '1329.14', '2017-08-14', '인덱스주식코스피200', '국내주식형', '840', '교보악사자산운용', '2', '높은 위험', '3757.42', '0', '0', '87.97', '0.12', '3.76', '8.15', '1.85', '5.18', '11.52', '11.73', '-6.94', '55.96', '45.99', '6.2', null, null, null, null, null);

 insert into fund_products_4 values 
('K55214CD4825', '유진챔피언중단기채증권자투자신탁(채권)ClassC-Re', '#국내채권형#퇴직연금', '1080', '2018-10-17', '일반채권', '국내채권형', '387', '유진자산운용', '5', '낮은 위험', '2049.54', '58.28', '0', '0', '0.00', '0.06', '41.66', '0.59', '1.45', '2.75', '5.71', '9.79', '13.6', '16.21', '2.43', null, null, null, null, null);

insert into fund_products_4 values
('K55223BV4542', 'KB중국본토A주증권자투자신탁(주식)C-퇴직e', '#해외주식형#퇴직연금#중국', '1085.17', '2017-09-06', '중국주식', '해외주식형', '514', '케이비자산운용', '2', '높은 위험', '4651.17', '0', '0', '0', '84.95', '15.67', '0', '-1.97', '2.2', '1.06', '-11.07', '-34.49', '12.27', '8.52', '0.22', null, null, null, null, null);

insert into fund_products_4 values
('K55235BW6864', '피델리티글로벌배당인컴증권자투자신탁(주식-재간접형)종류CP-e', '#해외주식형#퇴직연금#인컴#배당주펀드#글로벌', '1606.61', '2017-09-20', '글로벌주식', '해외주식형', '1285', '피델리티자산운용', '2', '높은 위험', '9072.9', '0', '0', '0', '', '0', '0', '-1.99', '2.52', '7.98', '11.64', '17.39', '42.41', '63.88', '7.33', null, null, null, null, null);

insert into fund_products_4 values
('K55301BT7965', '미래에셋퇴직플랜글로벌다이나믹증권자투자신탁 1(채권)종류C-P2e', '#해외채권형#퇴직연금#글로벌', '957.27', '2017-08-03', '글로벌채권', '해외채권형', '1104', '미래에셋자산운용', '5', '낮은 위험', '2908.53', '7.81', '33.33', '0', '0.00', '5.86', '53', '0.49', '1.17', '1.51', '4.13', '-3.87', '2.26', '6.2', '1.02', null, null, null, null, null);

insert into fund_products_4 values
('K55370BU1789', 'AB미국그로스증권투자신탁(주식-재간접형)종류형Ce-P2', '#해외주식형#퇴직연금#북미', '2579.83', '2017-08-04', '북미주식', '해외주식형', '2138', '얼라이언스번스틴자산운용', '2', '높은 위험', '20809.8', '0', '0', '0', '98.33', '0', '1.67', '5.19', '7.12', '20.47', '29.39', '24.38', '100.64', '157.98', '19.03',  null, null, null, null, null);

insert into fund_products_4 values
('K55213BU7688', '한화코리아밸류채권증권자투자신탁(채권)종류C-RPe(퇴직연금)', '#국내채권형#퇴직연금', '1058.52', '2017-08-17', '회사채권', '국내채권형', '117', '한화자산운용', '3', '다소 높은 위험', '1000', '84.39', '0', '0', '0', '12.59', '3.02', '0.66', '1.38',	'2.83',	'5.82',	'7.49',	'10.74', '10.1', '10.1' ,  null, null, null, null, null);
