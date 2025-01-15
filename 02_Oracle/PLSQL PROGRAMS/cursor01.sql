DECLARE
CURSOR empcur IS Select Ename,Job,Sal From Emp;
v_Ename varchar2(10);
v_Job varchar2(10);
v_Sal number(10);
BEGIN
OPEN empcur;
FETCH empcur INTO v_ename,v_job,v_sal ;
DBMS_OUTPUT.PUT_LINE('The Name od the Employee is '||v_Ename||' And Is working in the organization as '||v_job||' and getting salary '||v_sal);
CLOSE empcur;
END;
/
