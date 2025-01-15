 CREATE OR REPLACE PROCEDURE avgprocedure IS
    CURSOR avgCursor IS
    Select E.Ename,E.job,E.Sal,E.Deptno,AE.Asal
    From Emp E,(Select Deptno,AVG(Sal) asal From Emp GROUP BY Deptno) AE
    WHERE E.Sal>AE.Asal AND E.Deptno=AE.Deptno;
    v_Ename varchar2(10);
    v_Job varchar2(10);
    v_Sal number(10);
    v_Deptno number(4);
    v_avgsal number(10,2);
    BEGIN
    OPEN  avgCursor;
    LOOP
    FETCH avgCursor INTO v_Ename,v_Job,v_Sal,v_Deptno,v_avgsal;
    EXIT WHEN avgCursor%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(v_Ename||' '||v_Job||' '||v_Sal||' '||v_Deptno||' '||v_avgsal);
    END LOOP;
    END;
   /
