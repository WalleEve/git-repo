CREATE TABLE billing_items(
    item_no NUMBER,
    billing_no NUMBER NOT NULL,
    product_id NUMBER NOT NULL,
    price NUMBER(10,2) DEFAULT 0 NOT NULL,
    PRIMARY KEY(item_no, billing_no),
    FOREIGN KEY(billing_no) 
        REFERENCES billing_headers(billing_no)
);



select * from billing_headers;
select * from billing_items;

insert into billing_headers (billing_no, billing_date, amount, customer_id, note)
values()


select * from tab;



SELECT * FROM BILLING_HEADERS;
SELECT * FROM BILLING_ITEMS;

SELECT * FROM CONTACTS ;
SELECT * FROM COUNTRIES;
SELECT * FROM CUSTOMERS;
SELECT * FROM DEPARTMENTS ;
SELECT * FROM EMP ;
SELECT * FROM EMPLOYEES;
SELECT * FROM EMP_DETAILS_VIEW ;
SELECT * FROM INVENTORIES ;
SELECT * FROM JOBS;
SELECT * FROM JOB_HISTORY ;
SELECT * FROM LOCATIONS;
SELECT * FROM LOG ;
SELECT * FROM ORDERS ;
SELECT * FROM ORDER_ITEMS ;
SELECT * FROM PRODUCTS ;
SELECT * FROM PRODUCT_CATEGORIES;
SELECT * FROM REGIONS;
SELECT * FROM SAMPLEA;
SELECT * FROM SAMPLEB;
SELECT * FROM SAMPLE_A ;
SELECT * FROM WAREHOUSES;

select * from 
products p,
order_items oi,
orders o
where p.PRODUCT_ID = oi.PRODUCT_ID
and oi.ORDER_ID = o.ORDER_ID
and p.product_id = 235;

