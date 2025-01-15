--# Copying Types:
--# variable%TYPE
--# user_id users.user_id%TYPE;

--# Row Types:
--# name table_name%ROWTYPE
--# name composite_type_name;


--# Here an example of using composite types. Table1 and Table2 are extisting at least the mentioed fields:
drop table table1;
CREATE TABLE Table1 
(
	cid	numeric primary key,
	cname VARCHAR(10)
	
);

INSERT INTO table1 VALUES(1, 'SAYED'),(2, 'MAHFUZE'), (3, 'RAHEMAN');
select * from table1;

CREATE TABLE Table2
(
	aid	numeric,
	add_line1 varchar(20),
	add_line2 varchar(20),
	city varchar(20),
	state varchar(20),
	pin numeric,
	country varchar(10),
	cid numeric references Table1(cid)
);
INSERT INTO Table2 VALUES (1, 'Haladigadia', 'Korai', 'Jajpur', 'Odisha', 755022, 'India', 1),
(2, 'Alkapur', 'Sekpet', 'Hyderabad', 'Hyderabad', 5500034, 'India', 2),
(3, 'Neknam Pur', 'Kondapur', 'Hyderabad', 'Hyderabad', 5500032, 'India', 3);

select * from table2;

--DROP function merge_fields;
CREATE FUNCTION merge_fields(t_row table1) RETURNS text AS $$
DECLARE 
	t2_row table2%ROWTYPE;
BEGIN 
	SELECT * INTO t2_row from table2 where cid = t_row.cid;
	RETURN 'Name: '|| t_row.cname ||' Address: '|| t2_row.add_line1 ||' '||  t2_row.add_line2 ||' '|| t2_row.city || ' ' || t2_row.state || ' ' || t2_row.pin || ' ' || t2_row.country;    
END;
$$ LANGUAGE plpgsql;


SELECT merge_fields(t.*) FROM table1 t where cid=1;

SELECT merge_fields(t.*) FROM table1 t;



