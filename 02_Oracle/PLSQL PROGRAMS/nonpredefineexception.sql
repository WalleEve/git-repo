-- Exception 05
DECLARE
e_empRemaining EXCEPTION
PRAGMA EXCEPTION_INIT(e_empRemaining,-2292);
v_Deptno Emp.Deptno%TYPE :=&GiveDeptno;
BEGIN
DELETE FROM Dept
WHERE Deptno=v_Deptno;
IF SQL%NOTFOUND THEN
DBMS_OUTPUT.PUT_LINE('The Given Information is Missing in the Database ,Check proper value');
END IF;
ROLLBACK;
EXCEPTION
WHEN e_empRemaining THEN
DBMS_OUTPUT.PUT_LINE('Unable to delete the department number'||v_deptno||' as the employees are existing . validate your relation and then try once again.');
WHEN NO_DATA_FOUND THEN
DBMS_OUTPUT.PUT_LINE('The given information is missing in the database check for prpper values.');
END;
/
