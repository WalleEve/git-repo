
create table purchase_master(
id serial,
purchase_date date,
item text,
brand text,
quantity numeric,
unit text,
unit_price numeric,
sale_price numeric);

create table current_purchase(
id serial,
purchase_date date,
item text,
brand text,
quantity numeric,
unit text,
unit_price numeric,
sale_price numeric
);

select * from current_purchase;
select * from purchase_master;
(purchase_date, item, brand, quantity, unit, unit_price, sale_price)

insert into current_purchase(purchase_date, item, brand, quantity, unit, unit_price, sale_price) values('2021-Mar-29','RICE','RUCHI', 100, 'KG', 40, 48 );

create table users(
id serial,
user_name varchar,
password varchar);
insert into users(user_name, password) values('Admin', 'Admin');




create table current_stock(
id serial,
purchase_date date,
item text,
brand text,
quantity numeric,
unit text,
unit_price numeric,
sale_price numeric);

select * from purchase_master ;
insert into purchase_master values(3, '1-Apr-2021', 'RICE', 'RUCHI', 50, 'KG', 45, 55);
select * from current_stock;
insert into current_stock select * from purchase_master;
select * from current_stock;

truncate current_stock;

