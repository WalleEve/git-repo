-- Procedure 
CREATE OR REPLACE PROCEDURE DeptDataDisplay
AS
v_Rowcount NUMBER(4);
TYPE GenericCursor
IS REF CURSOR;
v_GenericCursor GenericCursor;
TYPE tablesRecordType IS RECORD
(
Deptno NUMBER(4),
Dname VARCHAR2(10),
Loc VARCHAR2(10)
);
v_DeptRecordType tablesRecordType;
BEGIN
OPEN FenericCursor
FOR 
Select * from Dept;
DBMS_OUTPUT.PUT_LINE(RPAD(LPAD('Department Information',29,'*'),49,'*'));
DBMS_OUTPUT.PUT_LINE(RPAD('-',40,'-'));
DBMS_OUTPUT.PUT_LINE(RPAD('Deptno',8)||RPAD('Dname',12)||RPAD('Loc',12));

LOOP
FETCH v_GenericCursor INTO v_DeptRecordType.Deptno,v_DeptRecordType.Dname,v_DeptRecordType.Loc;
EXIT WHEN v_GenericCursor%NOTFOUND;
v_Rowcount :=v_GenericCursor%ROWCOUNT;
DBMS_OUTPUT.PUT_LINE(RPAD(v_DeptRecordType.Deptno,8)||RPAD(v_DeptRecordType.Dname,12)||RPAD(v_DeptRecordType.Loc,12));
END LOOP;
CLOSE v_GenericCursor;
DBMS_OUTPUT.PUT_LINE(v_Rowcount||' Rows Processed so far..');
END DeptDataDisplay
