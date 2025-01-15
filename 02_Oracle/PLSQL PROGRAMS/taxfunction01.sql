-- Write a pl/sql stored procedure for passing employee no then terurn tax of the employee based on folling (1) if annsal more than 10000 then tax 10% of annsal (2) if annsal more than 15000 then tax 20% of annsal (3)- if annsal more than 20000 then tax 30% of annsal else tax 0..
CREATE OR REPLACE FUNCTION taxfunction (f_Empno NUMBER)
RETURN NUMBER
IS
v_Sal number(10);
v_annsal NUMBER(10);
v_tax number(10);
BEGIN
Select Sal INTO v_Sal From Emp Where Empno=p_Empno;
v_annsal :=v_Sal*12;
IF v_annsal <10000 THEN
v_tax :=(0)*TO_NUMBER(v_annsal,999999D99);
RETURN v_tax;
ELSIF v_annsal >10000 AND v_Sal <15000 THEN
v_tax :=(10/100)*TO_NUMBER(v_annsal,999999D99);
RETURN v_tax;
ELSIF v_annsal >15000 AND v_Sal <20000 THEN
v_tax :=(20/100)*TO_NUMBER(v_annsal,999999D99);
RETURN v_tax;
ELSIF v_annsal >20000 THEN
v_tax :=(30/100)*TO_NUMBER(v_annsal,999999D99);
RETURN v_tax;
END IF;
END;

-- Execute the taxfunction
sql> Select Ename,Job,Sal,taxfunction(Empno) tax From Emp Where Empno=&Empno;
