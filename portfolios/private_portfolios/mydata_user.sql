select * from fund_products where fund_code = "K55223BV4542";
select * from fund_products_2;
select * from fund_products_3;
select * from fund_prices;

alter table fund_products_3
    add arima_price double null;

alter table fund_products_3
    add arima_update DATE null;

alter table fund_products_3
    add arima_percent double null;
    
select * from user_style;