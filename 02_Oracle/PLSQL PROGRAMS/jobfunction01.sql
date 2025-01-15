--Write a pl/sql stored function for passing employee name in a parameter then return job of the employee from emp table based in passed emp name..

CREATE OR REPLACE FUNCTION jobfunction (f_ename VARCHAR2)
RETURN VARCHAR2
IS
CURSOR JobCursor IS SELECT Job FROM Emp WHERE Ename=f_ename;
v_job emp.job%TYPE;
BEGIN
OPEN JobCursor;
LOOP
FETCH JobCursor INTO v_job;
EXIT WHEN JobCursor%NOTFOUND;
RETURN v_job;
END LOOP;
RETURN v_job;
END;
/


--testing with other data

CREATE OR REPLACE FUNCTION jobfunction (f_ename VARCHAR2)
RETURN VARCHAR2
IS
CURSOR JobCursor IS SELECT Job FROM testemp WHERE name=f_name;
c_job varchar2(200);
BEGIN
FOR v_job IN JobCursor
LOOP
c_job :=c_job||','||v_job
END LOOP;
RETURN c_job;
END;
/


