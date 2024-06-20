select * from fund_products;
select * from fund_stocks;
select * from fund_products where fund_name like "유진챔피언중단기채증권자투자신탁%";

select * from fund_stocks where fund_code = "K55223BV4542";
select * from fund_bonds where fund_code =  "K55207BC6318";
select * from fund_assets where fund_code = "K55214CD4825";

ALTER TABLE fund_bonds CHANGE COLUMN rate weight float;
select * from fund_stocks;
select * from fund_bonds;
