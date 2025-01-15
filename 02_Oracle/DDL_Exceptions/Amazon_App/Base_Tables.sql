create table amazon_products (
    product_id  number ,
    product_name    varchar2(100) not null,
    product_catagory    varchar2(100),
    unit_price  number(10,2),
    stock_unit  number,
    start_date  date not null,
    end_date    date,
    constraint amz_products_prd_id_pk primary key (product_id),
    constraint amz_products_prd_name_unq unique (product_name)
 );
 
 create table amazon_users(
    user_id numeric,
    user_name   varchar2(20) not null,
    user_phone  number(10),
    user_address    varchar2(10),
    constraint amz_users_user_id_pk primary key (user_id)   
    );
 create table amazon_user_login(
    user_id numeric,
    login_id    varchar2(100),
    login_password  varchar2(200),
    current_status  varchar2(1),
    constraint amz_users_login_user_id_pk primary key (user_id),
    constraint amz_users_login_user_id_fk foreign key (user_id) references amazon_users(user_id),
    constraint amz_users_login_login_id_unq   unique (login_id)
    );
    
    
    
    
 