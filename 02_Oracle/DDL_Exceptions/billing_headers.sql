CREATE TABLE billing_headers(
    billing_no NUMBER,
    billing_date DATE NOT NULL,
    amount NUMBER(19,4) DEFAULT 0 NOT NULL,
    customer_id NUMBER NOT NULL,
    note VARCHAR2(100),
    PRIMARY KEY(billing_no)
);