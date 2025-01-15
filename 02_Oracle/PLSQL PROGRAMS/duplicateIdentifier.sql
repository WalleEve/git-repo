-- Duplicate Identifiers inthe same scope
DECLARE
id BOOLEAN;
id VARCHAR2(10); --duplicate identifier
BEGIN
id :=FALSE;
END;
/

-- OUTPUT
id :=FALSE;
*
ERROR at line 5:
ORA-06550: line 5, column 1:
PLS-00371: at most one declaration for 'ID' is permitted
ORA-06550: line 5, column 1:
PL/SQL: Statement ignored
ORA-06550: line 6, column 22:
PLS-00371: at most one declaration for 'ID' is permitted
ORA-06550: line 6, column 1:
PL/SQL: Statement ignored

