--write a pl/sql stored procedure for passing deptno as a paqrameter  from emp table then display employee details from emp emp tables based on passed deptno..
--
CREATE OR REPLACE PROCEDURE empprocedure02 (f_deptno NUMBER)
IS
CURSOR empcursor IS Select * from Emp where Deptno=f_deptno;
v_emp emp%ROWTYPE;
BEGIN
FOR v_emp IN empcursor
LOOP
DBMS_OUTPUT.PUT_LINE(v_emp.Ename||' '||v_emp.job||' '||v_emp.sal);
END LOOP;
END;
/

