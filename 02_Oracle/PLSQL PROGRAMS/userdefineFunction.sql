-- Write a pl/sql userdefine function which behaves like a predefine agegate function for passing deptno then return employee name for each department by replace emp table.

CREATE OR REPLACE FUNCTION EmpFunction (F_Deptno NUMBER)
RETURN varchar2
IS
a varchar2(200);
CURSOR  EmpCursor IS Select Ename From Emp Where Deptno=F_Deptno;
BEGIN
FOR v_Emp IN EmpCursor
LOOP
a :=a||' '||v_Emp.Ename;
END LOOP;
RETURN a;
END;
/

-- Exection of the EmpFunction
sql> SELECT Deptno,EmpFunction(Deptno)
FROM Emp GROUP BY Deptno;
