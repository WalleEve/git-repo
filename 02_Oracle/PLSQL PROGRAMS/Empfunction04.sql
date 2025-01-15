-- Write a pl/sql stored Function for passing empno,date ad parameters then return no of employee that employee for the organization for how long 

CREATE OR REPLACE FUNCTION EmpFunction04(f_Empno NUMBER,f_date DATE)
RETURN NUMBER
IS
v_months number;
v_years number(2);
BEGIN
SELECT MONTHS_BETWEEN(f_date,Hiredate) INTO v_months From Emp Where Empno=f_Empno;
v_years :=v_months/12;
RETURN v_years;
END;

-- Featching the Empfunction
Select Empno,Ename,Hiredate,ROUND(EmpFunction(Empno,SYSDATE))||' Years'|| Exp from Emp Where Empno=&Empno;
