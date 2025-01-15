create table amazon_user(
user_id number(8),
first_name  varchar2(20),
middle_name varchar2(20),
last_name   varchar2(20),
dob         date,
gender      CHAR(2),
country_code    varchar2(5),
reg_phone   number(10),
email_id    varchar2(100),
date_of_join    date,
status  CHAR(2)
);

insert into amazon_user 
    (user_id, first_name, middle_name, last_name, dob, gender, country_code, reg_phone, email_id, date_of_join, status)
values 
    (96923922, 'SAYED', 'MAHFUZUR', 'RAHEMAN', '12-APR-1991', 'M', '+91', 9692392243, 'sayed@live.in', sysdate, 'A');
  
create table address_type(
address_type_id number(2),
add_type    varchar2(10),
constraint address_type_id_pk primary key(address_type_id),
constraint address_type_chk check (add_type in( 'PRIMARY', 'SHIPPING', 'BILLING'))
);
  
create table amazon_address(
address_id number,
user_id     number(8),
address_type_id number(2),
address_falg char(2), -- 
address_1 varchar2(30),
address_2 varchar2(30),
city    varchar2(30),
state   varchar2(20),
country varchar2(20),
zip_code varchar2(6)
);

COMMENT ON COLUMN amazon_address.address_falg 
   IS 'Holdes A for Active and C for Closed';
   
create table amazon_payment_method(
payment_method_id   numeric,
user_id numeric(8),
card_number varchar2(16),
card_type   varchar2(20),
card_marchant   varchar2(50),
card_exp_date   date,
card_limit  numeric,
utilized    numeric
);

create table amazon_cart(
card_id numeric,
user_id numeric(8),
item    varchar2(100),
item_quantity   numeric,
item_unit_price numeric
);



create table amazon_order(
order_id    numeric,
user_id     numeric(8),
item_id     numeric,
unit        numeric,
price       numeric(10, 2),
discount    numeric,
final_price numeric,
order_date  date,
deliviry_date   date,
payment_type    varchar2(20),
payment_method_id numeric  
);


create table amazon_transactions(
trans_id    numeric,
user_id     numeric(8),
order_id    numeric,
order_date  numeric,
total_unit  numeric,
total_price numeric
);


   INSERT INTO endangered_species
        VALUES ('Amur Leopard', 'Panthera pardus orientalis');
INSERT INTO endangered_species
        VALUES ('Black Rhino', 'Diceros bicornis');
INSERT INTO endangered_species
        VALUES ('Bornean Orangutan', 'Pongo pygmaeus');
INSERT INTO endangered_species
        VALUES ('Cross River Gorilla', 'Gorilla gorilla diehli');
INSERT INTO endangered_species
        VALUES ('Javan Rhino', 'Rhinoceros sondaicus');
INSERT INTO endangered_species
        VALUES ('Javan Rhino', 'Rhinoceros sondaicus');
INSERT INTO endangered_species
        VALUES ('Javan Rhino', 'Rhinoceros sondaicus');
INSERT INTO endangered_species
        VALUES ('Javan Rhino', 'Rhinoceros sondaicus');
INSERT INTO endangered_species
        VALUES ('Javan Rhino', 'Rhinoceros sondaicus');
INSERT INTO endangered_species
        VALUES ('Javan Rhino', 'Rhinoceros sondaicus');
INSERT INTO endangered_species
        VALUES ('Javan Rhino', 'Rhinoceros sondaicus');