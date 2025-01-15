-- CReating Clint table
CREATE TABLE client
(
clientid INT,
clientName varchar2(20),
CONSTRAINT client_id_PK PRIMARY KEY (clientid)
);
-- Creating table bank
CREATE TABLE bank
(
branchid INT,
branchname VARCHAR2(20),
clientid INT,
CONSTRAINT bank_id_pk PRIMARY KEY (branchid),
CONSTRAINT bank_client_id_Fk FOREIGN KEY (clientid)
REFERENCES client (clientid)
);

-- Creating table bill
CREATE TABLE bill
(
invoiceid INT,
year DATETIME,
branchID INT,
ammount INT,
CONSTRAINT bill_id_PK PRIMARY KEY(invoiceid),
CONSTRAINT bill_branchid_Fk FOREIGN KEY(branchid)
REFERENCES bank(branchid)
);


-- INSERTING VALUES
BEGIN
insert into Client values (1, 'O_A');
insert into Client values (2, 'O_B');
insert into Client values (3, 'O_C');
insert into Client values (4, 'O_D');
insert into Client values (5, 'O_E');

insert into Bank values (1, 'B_1', 1);
insert into Bank values (2, 'B_2', 2);
insert into Bank values (3, 'B_3', 3);
insert into Bank values (4, 'B_4', 4);
insert into Bank values (5, 'B_5', 5);

insert into Bill values (1, '2012-01-01 00:00:00.000',    1,    100);
insert into Bill values (2, '2013-01-01 00:00:00.000',    2,    200);
insert into Bill values (3, '2012-01-01 00:00:00.000',    3,    300);
insert into Bill values (4, '2017-01-01 00:00:00.000',    4,    400);
insert into Bill values (5, '2012-01-01 00:00:00.000',    5,    500);
insert into Bill values (6, '2012-01-01 00:00:00.000',    1,    900);
insert into Bill values (7, '2013-01-01 00:00:00.000',    1,    900);
END;

-- Selection all the table data in separate query
SQL> Select * from client;

  CLIENTID CLINETNAME
---------- --------------------
         1 O_A
         2 O_B
         3 O_C
         4 O_D
         5 O_E

SQL> Select * from bank;

  BRANCHID BRANCHNAME             CLIENTID
---------- -------------------- ----------
         1 B_1                           1
         2 B_2                           2
         3 B_3                           3
         4 B_4                           4
         5 B_5                           5

SQL> Select * from bill;

 INVOICEID YEAR        BRANCHID     AMOUNT
---------- --------- ---------- ----------
         1 13-DEC-16          1        100
         2 13-DEC-16          2        200
         3 13-DEC-16          3        300
         4 13-DEC-16          4        400
         5 13-DEC-16          5        500
         6 13-DEC-16          1        900
         7 13-DEC-16          1        900

7 rows selected.

-- Retrieve all invoices from table bill for year 2015 and 2016 which belong to client ‘O_A’:
sql> SELECT invoiceid,year From bill
     WHERE branchid=(SELECT branchid From bank WHERE clientid=(SELECT clientid FROM client WHERE clientname='O_A' ));

SQL> /

 INVOICEID YEAR
---------- ---------
         1 13-DEC-16
         6 13-DEC-16
         7 13-DEC-16

 


