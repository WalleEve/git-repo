/*
Ques: Write a pl/sql program to diapaly all employee name and salary from Emp tbale by using  %notfound attributes.
*/
DECLARE
CURSOR EmpCur02 IS Select Ename,Job,Sal From Emp;
v_ename emp.ename%type;
v_job emp.job%type;
v_sal emp.sal%type;
BEGIN
OPEN EmpCur02;
DBMS_OUTPUT.PUT_LINE(RPAD('ENAME',20)||RPAD('JOB',20)||RPAD('SAL',10));
DBMS_OUTPUT.PUT_LINE(RPAD('-',60,'-'));
LOOP
FETCH EmpCur02 INTO v_ename,v_job,v_sal ;
EXIT WHEN EmpCur02%NOTFOUND;
DBMS_OUTPUT.PUT_LINE(RPAD(v_ename,20)||RPAD(v_job,20)||RPAD(v_sal,10));
END LOOP;
CLOSE EmpCur02;
END;
/
