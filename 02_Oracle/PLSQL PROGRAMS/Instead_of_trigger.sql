-- INSTEAD OF TRIGGERS
-- The INSTEAD OF TRIGGERS are special kind that are defines in database views.
-- the Instead of triggers is created as ROW TRIGGERS only.
-- The INSTEAD OF TRIGGER fires Instead of the TRIGGERING STATEMENT that has been Issued Against a view.
--SYNTAX
CREATE OR REPLACE TRIGGER trigger_name
INSTEAD OF TRIGGER_event ON ViewName
FOR EACH ROW
BEGIN
ECECUTION Statement;
END;
/
sql> CREATE VIEW deptview
     AS
     SELECT Deptno,Dname,Loc From From Dept
/
sql> CREATE OR REPLACE TRIGGER DeptDel
     INSTEAD OF Delete ON Deptview
     FOR EACH ROW
     BEGIN
     DELETE FROM Dept
     WHERE Deptno = :OLD.Deptno;
     DBMS_OUTPUT.PUT_LINE('Department Deleted...');
     END;
     /


