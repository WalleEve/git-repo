-- Write a pl/sql stored function for passing emp number as a parameter from emp table return 1 if the emp salary is more than the avg salary of the department otherwise return 0

CREATE OR REPLACE FUNCTION salfunction(f_Empno NUMBER)
RETURN NUMBER
IS
v_Sal NUMBER(10);
v_AvgSal NUMBER(10);
BEGIN
SELECT Sal INTO v_Sal FROM emp Where Empno=f_Empno;
SELECT avg(Sal) INTO v_AvgSal FROM emp WHERE Deptno=(SELECT Deptno FROM Emp Where Empno=f_Empno);
IF v_Sal>v_AvgSal THEN
RETURN 1;
ELSE 
RETURN 0;
END IF
END;


-- Executing the function 
DECLARE
v_Empno NUMBER :=&Empno;
v_emp Emp%ROWTYPE;
BEGIN
Select * INTO v_Emp From Emp Where Empno=v_Empno;
IF salfunction(v_Empno)=1 THEN
DBMS_OUTPUT.PUT_LINE('Name Of the Employee is: '|v_emp.Ename);
DBMS_OUTPUT.PUT_LINE('Working for Department number: '|v_emp.Deptno);
DBMS_OUTPUT.PUT_LINE('As a : '|v_emp.Job);
DBMS_OUTPUT.PUT_LINE('Getting Salary: '|v_emp.Sal);
DBMS_OUTPUT.PUT_LINE('His salary is more than tha average slaray of the department..');
ELSIF salfunction(v_Empno)=0 THEN
DBMS_OUTPUT.PUT_LINE('Sorry Employee is not elegible for the process');
END IF;
END;
/

