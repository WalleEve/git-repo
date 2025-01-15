-- Cursor 
--# Explicit Cursor 
/*
There are four steps that should be performed by an Explicit Cursors.
. Cursor Declaration 
. Cursor Opening 
. Cursor Fetching 
. Cursor Closing 

--# The Pseudo Structure 
declare
    cursor declaration
begin 
    opening of cursor
        fetching of cursor
    close cursor.
end;
*/

declare  
    v_deptno dept.deptno%type := &deptno;
    v_empno emp.empno%type;
    v_ename emp.ename%type;
    v_sal emp.sal%type;
    v_job emp.job%type;
    
    cursor eDeptCursor
        is
        select empno, ename, deptno, sal, job
        from emp 
        where deptno = v_deptno;
begin
        open eDeptCursor;
        fetch eDeptCursor into v_empno, v_ename, v_deptno, v_sal, v_job;
        dbms_output.put_line('Empno: '||v_empno || ' Name: '|| v_ename||' Deptno: ' || v_deptno|| 'Sal:  '|| v_sal ||' Job: '|| v_job);
        close eDeptCursor;
end;



--# 

Declare 
cursor empDetailsCursor
is
select e.empno, e.ename, d.deptno, d.dname
from emp e, dept d 
where e.deptno = e.deptno;
v_empdept  empDetailsCursor%ROWTYPE;
begin
open empDetailsCursor;
fetch empDetailsCursor into v_empdept;
dbms_output.put_line('Details:  '||v_empdept.empno ||' - '|| v_empdept.ename||' - '||v_empdept.deptno||' - '||v_empdept.dname);
close empDetailsCursor;
end;

--# CURSOR DECLARATION 
--# The cursor is declared in the declarative block and is provided with a name and a Select statement.
--# SYNTAX
/*
CURSOR cursorName {parameter List}
[RETURN returnType]
IS QUERY 
[FOR UPDATE [OF(columnList)] [NOWAIT]];
*/

















