/* -- Row Triggers
 -- A row triggers is fired as many times as there are rows affected by triggering event.
 -- When the statemnt FOR EACH ROW is present in the CREATE TRIGGER clause the trigger is a ROW TRIGGER.
 --Illustration
CREATE OR REPLACE TRIGGER
DeptUpdate
AFTER UPDATE ON Dept
FOR EACH ROW
--. The ROW LEVEL TRIGGER fires as many times as the number of ROWS are affected when the transaction takes place.
-- Statement Level Triggers
-- A Statement Triggers is Fired Once for the entire triggering statement. This terigger fires once regardless of the number of rows affected  by  the Triggering statement .
--Illustration:
CREATE OR REPLACE TRIGGER
DeptDelete
AFTER DELETE ON Dept
-- Statement Trigger should be used when the operations performed by the trigger do not by on hte data in the individula records.
-- Correlation Identifiers In ROW  Level
-- AS a ROW Level TRIGGER Fires once per row inside the trigger  we can access the data in the ROW taht is currently being processed 
-- The Two correlation Identifiers provided by pl/sql are ":OLD" and ":NEW".
-- A correlation Identifier is a special  kind of PL/SQl bind variable.
-- The PL/SQL Compiler Treats the correlation Identifiers as Records of type Triggering_Table%ROWTYPE;

*/

CREATE TABLE recycle
(
Empno NUMBER(6),
Ename VARCHAR2(10),
Job VARCHAR2(10),
Mgr NUMBER(6),
Hiredate DATE,
Sal NUMBER(10),
comm NUMBER(7,2),
Deptno NUMBER(2)
);

CREATE OR REPLACE TRIGGER empbin
BEFORE DELETE
ON Emp
FOR EACH ROW
BEGIN
INSERT INTO recycle VALUES(:OLD.Empno,:OLD.Dname,:OLD.Job,:OLD.Mgr,:OLD.Hiredate,:OLD.Sal,:OLD.Comm,:OLD.Deptno);
END;
/
