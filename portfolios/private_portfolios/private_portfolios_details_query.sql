use hitit;
select * from fund_products_4;
select * from user_portfolios;
select * from user_portfolios_fund_products;


CREATE TABLE private_portfolios (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    investment_type VARCHAR(255),
    summary VARCHAR(255),
    minimum_subscription_fee INT UNSIGNED,
    stock_exposure INT UNSIGNED
);



select * from private_portfolios;

INSERT INTO private_portfolios (name, investment_type, summary, minimum_subscription_fee, stock_exposure)
VALUES 
('HitIT & 신한_공격형', '공격형', 'Hit It과 신한투자증권이 선별한 공격형 포트폴리오', 100, 70),
('HitIT & 신한_중립형', '중립형', 'Hit It과 신한투자증권이 선별한 중립형 포트폴리오', 200, 50),
('HitIT & 신한_안정형', '안정형', 'Hit It과 신한투자증권이 선별한 안정형 포트폴리오', 300, 30);


select * From private_portfolios;
select * from private_portfolios_fund_products where fund_code = "K55223BV4542";
select * from private_portfolios_fund_stocks;

DROP TABLE private_portfolios_fund_products;

select * from user_portfolios;
select * from user_portfolios_fund_products where portfolio_id = 10;

DELETE FROM user_portfolios
WHERE id = 9;

delete from user_portfolios_fund_products where portfolio_id = 9;

CREATE TABLE private_portfolios_fund_products (
    fund_code VARCHAR(255),
    portfolio_id INTEGER UNSIGNED,
    fund_name VARCHAR(255),
    fund_type_detail VARCHAR(255),
    company_name VARCHAR(255),
    weight float,
    PRIMARY KEY (fund_code, portfolio_id),
    FOREIGN KEY (portfolio_id) REFERENCES private_portfolios(id)
);

select * from private_portfolios_fund_products;

INSERT INTO private_portfolios_fund_products (fund_code, portfolio_id, fund_name, weight, fund_type_detail, company_name)
VALUES 
("2117610", 1, '신한BNPP글로벌밸런스EMP[채권혼합-재간접형](C-re)', 30, '해외주식형', '신한자산운용'),
("K55370BU1789", 1, 'AB미국그로스증권투자신탁(주식-재간접형)종류형Ce-P2', 15, '해외주식형', '얼라이언스번스틴자산운용'),
("K55235BW6864", 1, '피델리티글로벌배당인컴증권자투자신탁(주식-재간접형)종류CP-e', 15, '해외주식형', '피델리티자산운용'),
("K55301BT7965", 1, '미래에셋퇴직플랜글로벌다이나믹증권자투자신탁 1(채권)종류C-P2e', 13, '해외채권형', '미래에셋자산운용'),
("K55207BU0715", 1, '교보악사파워인덱스증권자투자신탁 1(주식)ClassC-Pe', 12, '국내주식형', '교보악사자산운용'),
("K55223BV4542", 1, 'KB중국본토A주증권자투자신탁(주식)C-퇴직e', 8, '해외주식형', '케이비자산운용'),
("K55214CD4825", 1, '유진챔피언중단기채증권자투자신탁(채권)ClassC-Re', 7, '국내채권형', '유진자산운용');


CREATE TABLE private_portfolios_fund_assets (
    fund_code VARCHAR(255),
    stock FLOAT,
    stock_foreign FLOAT,
    bond FLOAT,
    bond_foreign FLOAT,
    investment FLOAT,
    etc FLOAT,
    PRIMARY KEY (fund_code),
    FOREIGN KEY (fund_code) REFERENCES private_portfolios_fund_products(fund_code)
);

SHOW CREATE TABLE private_portfolios_fund_stocks;

select * from private_portfolios_fund_assets;

INSERT INTO private_portfolios_fund_assets (fund_code, stock, stock_foreign, bond, bond_foreign, investment, etc)
VALUES 
("2117610", 0, 35.18, 0, 55.04, 4.64, 5.14),
("K55370BU1789", 0, 97.98, 0, 0, 0, 2.02),
("K55235BW6864", 1.25, 59.39, 0, 0, 32.48, 6.88),
('K55301BT7965', 0, 0, 6.67, 34.71, 5.67, 52.95),
('K55207BU0715', 90.14, 0, 0, 0, 3.85, 6.01),
('K55223BV4542', 0, 82.59, 0, 0, 16.48, 0.93),
('K55214CD4825', 0, 0, 56.79, 0, 0.07, 43.14);

select * from private_portfolios_fund_assets;

DROP TABLE private_portfolios_fund_stocks;

CREATE TABLE private_portfolios_fund_stocks (
    fund_code VARCHAR(255),
    stock_name VARCHAR(255),
    size VARCHAR(255),
    style VARCHAR(255),
    weight FLOAT,
    PRIMARY KEY (fund_code, stock_name),
    FOREIGN KEY (fund_code) REFERENCES private_portfolios_fund_products(fund_code)
);

CREATE TABLE private_portfolios_fund_bonds (
    bond_name VARCHAR(255) NOT NULL,
    fund_code VARCHAR(255) NOT NULL,
    expire_date DATE DEFAULT NULL,
    duration FLOAT DEFAULT NULL,
    credit VARCHAR(255) DEFAULT NULL,
    weight FLOAT DEFAULT NULL,
    PRIMARY KEY (bond_name, fund_code),
    FOREIGN KEY (fund_code) REFERENCES private_portfolios_fund_products(fund_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO private_portfolios_fund_bonds (fund_code, bond_name, expire_date, duration, credit, weight)
VALUES 
('K55301BT7965', 'B 09/05/24', '0000-00-00', 0.43,	'0', 1.5),
('K55301BT7965', 'BAC 3.384 04/02/26',	'0000-00-00', 2.01,	'0', 1.58),
('K55301BT7965', 'JPM 2.005 03/13/26',	'0000-00-00', 1.95,	'0', 1.88),
('K55301BT7965', 'MS 3 7/8 04/29/24',	'0000-00-00', 0.08,	'0', 1.55),
('K55301BT7965', 'PANAMA 3 3/4 03/16/25', '0000-00-00', 0.96, '0',	2.11),
('K55301BT7965', 'T 4 1/4 01/31/26', '0000-00-00',	1.84, '0',	10.78),
('K55301BT7965', 'WFC 3.3 09/09/24', '0000-00-00',	0.44, '0',	1.54),
('K55301BT7965', '국고01875-2906(19-4)',	'2029-06-10', 4.85,	'0', 2.78),
('K55301BT7965', '국고03250-2803(23-1)',	'2028-03-10', 3.67,	'0', 5.08),
('K55301BT7965', '국고03375-3206(22-5)',	'2032-06-10', 7.03,	'0', 2.44),
('K55214CD4825', 'JB 우리캐피탈473-3',	'2026-04-28',	1.97,	'0', 3.4),
('K55214CD4825', 'JB 우리캐피탈474-3',	'2026-05-12',	2.01,	'0', 4.72),
('K55214CD4825', '국고03000-4212(12-5)',	'2042-12-10',	13.92,	'0', 3.7),
('K55214CD4825', '국고03250-2903(24-1)',	'2029-03-10',	4.52,	'0', 3.48),
('K55214CD4825', '롯데캐피탈385-2',	'2025-01-10',	0.76,	'0', 3.38),
('K55214CD4825', '산금24신이0106-0201-1',	'2025-08-01',	1.3,	'0', 6.73),
('K55214CD4825', '한국전력1360',	'2026-02-13',	1.79,	'0', 3.42),
('K55214CD4825', '한국투자캐피탈61',	'2024-04-09',	0.03,	'0', 3.55),
('K55214CD4825', '현대카드854-2',	'2024-08-09',	0.12, '0', 3.31),
('K55214CD4825', '현대카드881-1',	'2025-09-08',	1.39, '0',	3.38);



select * from private_portfolios_fund_stocks;


 
ALTER TABLE private_portfolios_fund_stocks
DROP PRIMARY KEY;


ALTER TABLE private_portfolios_fund_stocks
ADD PRIMARY KEY (fund_code);


INSERT INTO private_portfolios_fund_stocks (fund_code, stock_name, size, style, weight)
VALUES 
("2117610", 'iShares MSCI USA Quality Factor ETF', NULL, NULL, 19.94),
("2117610", 'SPDR® Portfolio Long Term Treasury ETF', NULL, NULL, 19.79),
("2117610", 'Vanguard Short-Term Corporate Bond ETF', NULL, NULL, 19.2),
("2117610", 'Global X US Infrastructure Dev ETF', NULL, NULL, 10.28),
("2117610", 'Vanguard Interm-Term Corp Bd ETF', NULL, NULL, 9.9),
("2117610", 'SPDR® Gold Shares', NULL, NULL, 5.13),
("2117610", 'iShares S&P 500 Value ETF', NULL, NULL, 5.03),
("2117610", 'WisdomTree Bloomberg US Dllr Bullish ETF', NULL, NULL, 4.5),
("2117610", 'iShares 20+ Year Treasury Bond ETF', NULL, NULL, 3.28),
("2117610", 'iShares 10-20 Year Treasury Bond ETF', NULL, NULL, 2.17),
('K55370BU1789', 'AB-American Growth Portfolio Class SK', NULL, NULL, 100),
('K55207BU0715', '삼성전자', '대형주', '성장주', 31.59),
('K55207BU0715', 'SK하이닉스', '대형주', '성장주', 8.11),
('K55207BU0715', '현대차', '대형주', '가치주', 2.63),
('K55207BU0715', '셀트리온', '대형주', '성장주', 2.61),
('K55207BU0715', 'POSCO홀딩스', '대형주', '가치주', 2.37),
('K55207BU0715', '기아', '대형주', '가치주', 2.14),
('K55207BU0715', 'NAVER', '대형주', '성장주', 2.02),
('K55207BU0715', '삼성SDI', '대형주', '성장주', 1.99),
('K55207BU0715', 'KB금융', '대형주', '가치주', 1.86),
('K55207BU0715', 'LG화학', '대형주', '성장주', 1.81),
('K55223BV4542','ZIJIN MINING GROUP', NULL, NULL, 8.19),
('K55223BV4542', 'WANHUA CHEMICAL GROUP CO -A',	NULL, NULL, 6.5),
('K55223BV4542', 'SHANDONG HUALU HEN', NULL, NULL, 6.07),
('K55223BV4542', 'CHONGQING FULING E', NULL, NULL, 5.95),
('K55223BV4542', 'SANAN OPTOELECTRON', NULL, NULL, 5.78),
('K55223BV4542', 'SHENZHEN SUNWAY CO', NULL, NULL, 5.73),
('K55223BV4542', 'BIEM L FDLKK GARMENT CO LT-A', NULL, NULL, 5.49),
('K55223BV4542', 'SANY HEAVY INDUSTR', NULL, NULL, 5.18),
('K55223BV4542', 'Shanxi Coking Coal Energy Grou', NULL, NULL, 4.34),
('K55223BV4542', 'GWMOTOR', NULL, NULL, 3.97);



INSERT INTO private_portfolios_funds (portfolio_id, name, weight, fund_type)
VALUES 
(2, '신한BNPP글로벌밸런스EMP[채권혼합-재간접형](C-re)', 30, '해외선진'),
(2, '미래에셋퇴직플랜글로벌다이나믹증권자1[채권](C-P2e)', 25, '해외채권'),
(2, '유진챔피언중단기채증권자투자신탁[채권](C-Re)', 20, '국내채권'),
(2, 'AB미국그로스증권투자신탁[주식-재간접형](Ce-P2)', 10, '해외선진'),
(2, '피델리티글로벌배당인컴자[주식-재간접형](CP-e)', 10, '해외선진'),
(2, '교보악사파워인덱스증권자1[주식](C-Pe)', 5, '국내주식');


INSERT INTO private_portfolios_funds (portfolio_id, fund_type, name, weight)
VALUES 
(3, '국내채권', '유진챔피언중단기채증권자투자신탁[채권](C-Re)', 26),
(3, '해외선진', '신한BNPP글로벌밸런스EMP[채권혼합-재간접형](C-re)', 25),
(3, '국내채권', '한화코리아밸류채권[채권](C-RPe)(퇴직연금)', 20),
(3, '해외채권', '미래에셋퇴직플랜글로벌다이나믹증권자1[채권](C-P2e)', 16),
(3, '해외선진', '피델리티글로벌배당인컴자[주식-재간접형](CP-e)', 8),
(3, '국내주식', '교보악사파워인덱스증권자1[주식](C-Pe)', 5);

select * from private_portfolios_funds;

#### 2024-06-19
select * from private_portfolios;
select * from private_portfolios_fund_products;
SHOW CREATE TABLE private_portfolios_fund_products;

-- 3.05
-- 5.18
-- 1.45
-- 2.20
-- 2.52
-- 1.17
-- 7.12

UPDATE private_portfolios_fund_products SET return_3m = 3.05 WHERE fund_code = '2117610';
UPDATE private_portfolios_fund_products SET return_3m = 5.18 WHERE fund_code = 'K55207BU0715';
UPDATE private_portfolios_fund_products SET return_3m = 1.45 WHERE fund_code = 'K55214CD4825';
UPDATE private_portfolios_fund_products SET return_3m = 2.20 WHERE fund_code = 'K55223BV4542';
UPDATE private_portfolios_fund_products SET return_3m = 2.52 WHERE fund_code = 'K55235BW6864';
UPDATE private_portfolios_fund_products SET return_3m = 1.17 WHERE fund_code = 'K55301BT7965';
UPDATE private_portfolios_fund_products SET return_3m = 7.12 WHERE fund_code = 'K55370BU1789';

INSERT INTO private_portfolios_fund_products (fund_code, portfolio_id, fund_name, weight, fund_type_detail, company_name, return_3m)
VALUES 
("2117610", 2, '신한BNPP글로벌밸런스EMP[채권혼합-재간접형](C-re)', 30, '해외주식형', '신한자산운용', 3.05),
("K55301BT7965", 2, '미래에셋퇴직플랜글로벌다이나믹증권자투자신탁 1(채권)종류C-P2e', 25, '해외채권형', '미래에셋자산운용', 1.17),
("K55214CD4825", 2, '유진챔피언중단기채증권자투자신탁(채권)ClassC-Re', 20, '국내채권형', '유진자산운용', 1.45),
("K55370BU1789", 2, 'AB미국그로스증권투자신탁(주식-재간접형)종류형Ce-P2', 10, '해외주식형', '얼라이언스번스틴자산운용', 7.12),
("K55235BW6864", 2, '피델리티글로벌배당인컴증권자투자신탁(주식-재간접형)종류CP-e', 10, '해외주식형', '피델리티자산운용', 2.52),
("K55207BU0715", 2, '교보악사파워인덱스증권자투자신탁 1(주식)ClassC-Pe', 5, '국내주식형', '교보악사자산운용', 5.18);

INSERT INTO private_portfolios_fund_products (fund_code, portfolio_id, fund_name, weight, fund_type_detail, company_name, return_3m)
VALUES 
("K55214CD4825", 3, '유진챔피언중단기채증권자투자신탁(채권)ClassC-Re', 26, '국내채권형', '유진자산운용', 1.45),
("2117610", 3, '신한BNPP글로벌밸런스EMP[채권혼합-재간접형](C-re)', 25, '해외주식형', '신한자산운용', 3.05),
("K55213BU7688", 3, '한화코리아밸류채권[채권](C-RPe)(퇴직연금)', 20, '국내채권형', '한화자산운용', 1.45),
("K55301BT7965", 3, '미래에셋퇴직플랜글로벌다이나믹증권자투자신탁 1(채권)종류C-P2e', 16, '해외채권형', '미래에셋자산운용', 1.17),
("K55235BW6864", 3, '피델리티글로벌배당인컴증권자투자신탁(주식-재간접형)종류CP-e', 8, '해외주식형', '피델리티자산운용', 2.52),
("K55207BU0715", 3, '교보악사파워인덱스증권자투자신탁 1(주식)ClassC-Pe', 5, '국내주식형', '교보악사자산운용', 5.18);



select * from private_portfolios;
select * from private_portfolios_fund_products;
SHOW CREATE TABLE private_portfolios_fund_products;

ALTER TABLE `private_portfolios`
ADD COLUMN `return_3m` float NOT NULL;

ALTER TABLE `private_portfolios`
DROP COLUMN `return_3m`;

select * from private_portfolios_fund_products;
select * from private_portfolios_fund_bonds where fund_code = "K55235BW6864";
select * from private_portfolios_fund_assets;
select * from private_portfolios_fund_stocks;
select * from private_portfolios_fund_stocks where fund_code = "K55235BW6864";

SELECT COUNT(*) FROM private_portfolios_fund_bonds where fund_code = "K55207BU0715";

select * from users_portfolio;
show create table users_portfolio;
select * from private_portfolios;


## 2024-06-23
show create table private_portfolios;
show create table private_portfolios_fund_products;
show create table private_portfolios_fund_assets;
show create table private_portfolios_fund_stocks;
show create table private_portfolios_fund_bonds;


CREATE TABLE `user_portfolios` (
   `id` int unsigned NOT NULL AUTO_INCREMENT,
   `name` varchar(255) DEFAULT NULL,
   `investment_type` varchar(255) DEFAULT NULL,
   `summary` varchar(255) DEFAULT NULL,
   `minimum_subscription_fee` int unsigned DEFAULT NULL,
   `stock_exposure` int unsigned DEFAULT NULL,
   PRIMARY KEY (`id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 CREATE TABLE `user_portfolios_fund_products` (
   `fund_code` varchar(255) NOT NULL,
   `portfolio_id` int unsigned NOT NULL,
   `fund_name` varchar(255) DEFAULT NULL,
   `fund_type_detail` varchar(255) DEFAULT NULL,
   `company_name` varchar(255) DEFAULT NULL,
   `weight` float DEFAULT NULL,
   `return_3m` float NOT NULL DEFAULT '0',
   PRIMARY KEY (`fund_code`,`portfolio_id`),
   KEY `portfolio_id` (`portfolio_id`),
   CONSTRAINT `user_portfolios_fund_products_ibfk_1` FOREIGN KEY (`portfolio_id`) REFERENCES `user_portfolios` (`id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 CREATE TABLE `user_portfolios_fund_assets` (
   `fund_code` varchar(255) NOT NULL,
   `stock` float DEFAULT NULL,
   `stock_foreign` float DEFAULT NULL,
   `bond` float DEFAULT NULL,
   `bond_foreign` float DEFAULT NULL,
   `investment` float DEFAULT NULL,
   `etc` float DEFAULT NULL,
   PRIMARY KEY (`fund_code`),
   CONSTRAINT `user_portfolios_fund_assets_ibfk_1` FOREIGN KEY (`fund_code`) REFERENCES `user_portfolios_fund_products` (`fund_code`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 CREATE TABLE `user_portfolios_fund_stocks` (
   `fund_code` varchar(255) NOT NULL,
   `stock_name` varchar(255) NOT NULL,
   `size` varchar(255) DEFAULT NULL,
   `style` varchar(255) DEFAULT NULL,
   `weight` float DEFAULT NULL,
   PRIMARY KEY (`fund_code`,`stock_name`),
   CONSTRAINT `user_portfolios_fund_stocks_ibfk_1` FOREIGN KEY (`fund_code`) REFERENCES `user_portfolios_fund_products` (`fund_code`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 CREATE TABLE `user_portfolios_fund_bonds` (
   `bond_name` varchar(255) NOT NULL,
   `fund_code` varchar(255) NOT NULL,
   `expire_date` date DEFAULT NULL,
   `duration` float DEFAULT NULL,
   `credit` varchar(255) DEFAULT NULL,
   `weight` float DEFAULT NULL,
   `expired_date` datetime(6) DEFAULT NULL,
   PRIMARY KEY (`bond_name`,`fund_code`),
   KEY `fund_code` (`fund_code`),
   CONSTRAINT `user_portfolios_fund_bonds_ibfk_1` FOREIGN KEY (`fund_code`) REFERENCES `user_portfolios_fund_products` (`fund_code`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 show create table users_portfolio;
 CREATE TABLE `user_select` (
   `id` int NOT NULL AUTO_INCREMENT,
   `portfolio_id` int unsigned DEFAULT NULL,
   PRIMARY KEY (`id`),
   KEY `portfolio_id` (`portfolio_id`),
   CONSTRAINT `user_select_ibfk_1` FOREIGN KEY (`portfolio_id`) REFERENCES `user_portfolios` (`id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 select * From user_select;
 
 CREATE TABLE `fund_prices` (
   `fund_code` varchar(255) NOT NULL,
   `Date` date NOT NULL,
   `price` float DEFAULT NULL,
   PRIMARY KEY (`Date`,`fund_code`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
 select count(*) from fund_prices;
 select * from fund_prices;
 select * from user_portfolios;
 select * from fund_prices;
 
 ALTER TABLE user_portfolios
ADD COLUMN created_at DATE;

ALTER TABLE example
MODIFY created_at DATE DEFAULT current_timestamp;


select * from user_portfolios;



UPDATE user_portfolios
SET created_at = '2024-06-05';
SET SQL_SAFE_UPDATES = 0;


 