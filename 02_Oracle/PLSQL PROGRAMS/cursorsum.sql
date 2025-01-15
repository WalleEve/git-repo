/* Write a plsql cursor program which is used to calculate total sal from emp table without using sum() function*/
DECLARE
CURSOR SalSumCursor IS Select Sal From Emp;
v_sal Emp.Sal%type;
total_sal number :=0;
BEGIN
OPEN SalSumCursor;
LOOP
FETCH SalSumCursor INTO v_sal;
EXIT WHEN SalSumCursor%NOTFOUND;
total_sal :=total_sal+v_sal; /* total_sal :=total_sal + NVL(v_sal,0);*/
END LOOP;
DBMS_OUTPUT.PUT_LINE('Total Salary of the organization is '||total_sal);
END;
/

