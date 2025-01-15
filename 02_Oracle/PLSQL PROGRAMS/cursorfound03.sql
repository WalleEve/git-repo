/* write a plsql cursor program to dispaly all the employee's and their salary from the emp table by using %found attribute */
DECLARE
CURSOR TableCursor IS Select * From all_tables;
v_table All_tables%ROWTYPE;
BEGIN
OPEN TableCursor;
Fetch TableCursor INTO v_table;
IF TableCursor%Found THEN
LOOP
DBMS_OUTPUT.PUT_LINE(v_table.&column1||' '||v_table.&column1||' '||v_table.&column3);
FETCH TableCursor INTO v_table;
EXIT WHEN TableCursor%NOTFOUND;
END LOOP;
ELSIF TableCursor%notfound THEN
DBMS_OUTPUT.PUT_LINE('Sorry please check the table name...');
END IF;
Close TableCursor;
END;
/


