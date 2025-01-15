
CREATE TABLE MyAudit 
(
username varchar2(10),
moddate date,
message
);


DECLARE
v_Deptno Dept.Deptno%TYPE :=&Deptno;
v_Dname Dept.Dname%TYPE :='&Danme';
v_Loc Dept.Loc%TYPE :='&Loc';
e_InvalidDept EXCEPTION;
BEGIN
UPDATE Dept
SET Dname=v_Dname,Loc=v_Loc 
WHERE Deptno=v_Deptno;
IF SQL%NOTFOUND THEN
RAISE e_InvalidDept;
END IF;
EXCEPTION
WHEN e_InvalidDeptno THEN
DBMS_OUTPUT.PUT_LINE('The Specific Department number '||v_Deptno||' You wanted to update is not available please conform the data..');
INSERT INTO myaudit (username,moddate,message) VALUES (user,sysdate,'Tried Illegal update.');
END;
/
