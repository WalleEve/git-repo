--# Bulk Binds (BULK COLLECT and FORALL) 
/*----------------------------------------------------------------------------------------------------------------
Oracle uses two engines to process PL/SQL code.
All procedural code is handled by the PL/SQL engine
while all SQL is nadled by the SQL statement executor or SQL engine.

There is an overhead associated with each context switch between the two engines.
If PL/SQL code loops through a collection performing the same DML operation for each item in the collection it is 
possible to reduce context switches by bulk binding the whole collection to the DML statement in one operation.

--# BULK COLLECT 
Bulk bind can improve the performace when loading collections from a queries.
The BULK COLLECT INTO construct binds the output of the query to the collection.
------------------------------------------------------------------------------------------------------------------*/
CREATE TABLE bulk_collect_test AS 
    SELECT owner,
        object_name,
        object_id
    FROM all_objects;

select * from   bulk_collect_test;  
--# The following code compares the time taken to populate a collection 
--  manually and using a bulk bind.

SET SERVEROUTPUT ON;

DECLARE 
    TYPE t_bulk_collect_test_tab IS TABLE OF bulk_collect_test%ROWTYPE;
    
    l_tab   t_bulk_collect_test_tab := t_bulk_collect_test_tab();
    l_start NUMBER;
BEGIN 
    -- Time a regular population.
    l_start := DBMS_UTILITY.get_time;
    
    FOR cur_rec in (
        SELECT * 
            FROM bulk_collect_test)
    LOOP
        l_tab.extend;
        l_tab(l_tab.last) := cur_rec;
    END LOOP;
    
    DBMS_OUTPUT.PUT_LINE(
    'Regular ( ' || l_tab.count || ' rows ): '||
    (DBMS_UTILITY.get_time - l_start)
    );
    
    -- Time bulk population.
    l_start := DBMS_UTILITY.get_time;
    
    SELECT * 
        BULK COLLECT INTO l_tab
    FROM bulk_collect_test;
    
    DBMS_OUTPUT.PUT_LINE(
    'Bulk ( '|| l_tab.count || ' rows): '||
    (DBMS_UTILITY.get_time - l_start)
    );    
    
END;
/



DECLARE 
    TYPE t_bulk_collect_test_tab IS TABLE OF bulk_collect_test%ROWTYPE;
    
    l_tab   t_bulk_collect_test_tab;
    
    CURSOR c_data IS 
        SELECT * 
        FROM bulk_collect_test;
        
BEGIN 
    OPEN c_data;
    LOOP
        FETCH c_data
            BULK COLLECT INTO l_tab LIMIT 10000;
        EXIT WHEN l_tab.count = 0;
    -- Process content of collection here.
    DBMS_OUTPUT.PUT_LINE(l_tab.count || ' rows');
    
    END LOOP;
    CLOSE c_data;
    
END;
/


--# The optimizing PL/SQL compiler converts cursor FOR LOOP into BULK
--  COLLECTs with an array size of 100.

DECLARE 
    TYPE t_bulk_collect_test_tab IS TABLE OF bulk_collect_test%ROWTYPE;
    
    l_tab  t_bulk_collect_test_tab;
    
    CURSOR c_data IS 
        SELECT * 
        FROM bulk_collect_test;
    l_start NUMBER;
    
BEGIN
    -- Time a regular cursor for loop.
    l_start := DBMS_UTILITY.get_time;
    
    FOR cur_rec IN (
        SELECT * from 
        bulk_collect_test)
    LOOP
        NULL;
    END LOOP;
    
    DBMS_OUTPUT.PUT_LINE('Regular: '|| (DBMS_UTILITY.get_time - l_start));
    
    -- Time bulk with LIMIT 10.
    l_start := DBMS_UTILITY.get_time;
    
    OPEN c_data;
    LOOP
        FETCH c_data 
        BULK COLLECT INTO l_tab LIMIT 10;
        EXIT when l_tab.count = 0;
        
    END LOOP;
    CLOSE c_data;
    
    DBMS_OUTPUT.PUT_LINE('LIMIT 10 '|| (DBMS_UTILITY.get_time - l_start));
    
    -- Time bulk with LIMIT 100
    l_start := DBMS_UTILITY.get_time;
    
    OPEN c_data;
    LOOP
        FETCH c_data 
        BULK COLLECT INTO l_tab LIMIT 100;
        EXIT WHEN l_tab.count = 0;
    END LOOP;
    CLOSE c_data;
    
    DBMS_OUTPUT.PUT_LINE('LIMIT 100 '|| (DBMS_UTILITY.get_time - l_start));
    
    -- Time bulk with LIMIT 1000
    l_start := DBMS_UTILITY.get_time;
    
    OPEN c_data;
    LOOP
        FETCH c_data 
        BULK COLLECT INTO l_tab LIMIT 1000;
        EXIT WHEN l_tab.count = 0;
    END LOOP;
    CLOSE c_data;
    
    DBMS_OUTPUT.PUT_LINE('LIMIT 1000: '|| (DBMS_UTILITY.get_time - l_start));
    
    

END;



--# FORALL 
-- The FORALL syntax allows us to bind the contents of a collection to a single DML statement,
-- allowing the DML to be run for each row in the collection without requiring a context switch each time.

CREATE TABLE forall_test(
id  number(10),
code    varchar2(10),
description varchar2(50)
);


Alter table forall_test ADD(
CONSTRAINT forall_test_pk PRIMARY KEY(id));

Alter table forall_test ADD(
CONSTRAINT forall_test_uk UNIQUE(code));


DECLARE 
    TYPE t_forall_test_tab IS TABLE OF forall_test%ROWTYPE;
    
    l_tab   t_forall_test_tab := t_forall_test_tab();
    l_start NUMBER;
    l_size  NUMBER  := 10000;
BEGIN
    -- Population collection.
    FOR i IN 1..l_size LOOP
        l_tab.extend;
        
        l_tab(l_tab.last).id    := i;
        l_tab(l_tab.last).code  := TO_CHAR(i);
        l_tab(l_tab.last).description := 'Description: '|| TO_CHAR(i);
    END LOOP;
    
    EXECUTE IMMEDIATE 'TRUNCATE TABLE forall_test';
    
    -- Time regular inserts.
    l_start := DBMS_UTILITY.get_time;
    
    FOR i IN l_tab.first..l_tab.last LOOP
        INSERT INTO forall_test(id, code, description)
        VALUES (l_tab(i).id, l_tab(i).code, l_tab(i).description);
    END LOOP;
    
    DBMS_OUTPUT.put_line('Normal Inserts: '||(DBMS_UTILITY.get_time - l_start));
    
    EXECUTE IMMEDIATE 'TRUNCATE TABLE forall_test';
    
    -- Time bulk inserts.
    l_start := DBMS_UTILITY.get_time;
    
    FORALL i IN l_tab.first..l_tab.last
        INSERT INTO forall_test VALUES l_tab(i);
        
    DBMS_OUTPUT.PUT_LINE('Bulk Inserts : '|| (DBMS_UTILITY.get_time - l_start));

    COMMIT;
END;  
/

DECLARE 
    TYPE t_id_tab IS TABLE OF forall_test.id%TYPE;
    TYPE t_forall_test_tab IS TABLE OF forall_test%ROWTYPE;
    
    l_id_tab    t_id_tab    := t_id_tab();
    l_tab       t_forall_test_tab   := t_forall_test_tab();
    l_start     NUMBER;
    l_size      NUMBER  := 10000;
BEGIN 
    -- Populte collections.
    FOR i IN 1..l_size 
    LOOP
        l_id_tab.extend;
        l_tab.extend;
        
        l_id_tab(l_id_tab.last) := i;
        l_tab(l_tab.last).id    := i;
        l_tab(l_tab.last).code  := TO_CHAR(i);
        l_tab(l_tab.last).description   := 'Description: '|| TO_CHAR(i);
                
    END LOOP;
    
    -- Time regular updates.
    l_start := DBMS_UTILITY.get_time;
    
    FOR i in l_tab.FIRST..l_tab.LAST LOOP
        UPDATE forall_test
        SET ROW = l_tab(i)
        WHERE id = l_tab(i).id;
    END LOOP;
    
    DBMS_OUTPUT.PUT_LINE('Normal Updates: '|| (DBMS_UTILITY.get_time - l_start));
    
    
    l_start := DBMS_UTILITY.get_time;
    
    -- Time bulk updates.
    FORALL i IN l_tab.first .. l_tab.last
    UPDATE forall_test
    SET ROW = l_tab(i)
    WHERE id = l_id_tab(i);
    
    
    DBMS_OUTPUT.PUT_LINE('Bulk Updates: '|| (DBMS_UTILITY.get_time - l_start));
    
    COMMIT;
END;
/




--# SQL%BULK_ROWCOUNT 
--  The SQL%BULK_ROWCOUNT cursor attribute gives granular information about the rows affected by each
--  iteration of the FORALL statement.

CREATE TABLE bulk_rowcount_test AS 
SELECT *
FROM all_users;

DECLARE 
    TYPE t_array_tab IS TABLE OF VARCHAR2(30);
    l_array t_array_tab := t_array_tab('SCOTT', 'SYS', 'SYSTEM', 'DBSNMP', 'HR', 'BANANA');
BEGIN 
    -- Perform bulk delete operation.
    FORALL i IN l_array.first..l_array.last
    DELETE FROM bulk_rowcount_test
    WHERE username = l_array(i);
    
    -- Report affected rows.
    FOR i IN l_array.first .. l_array.last 
    LOOP
        DBMS_OUTPUT.PUT_LINE('Element: '|| RPAD(l_array(i), 15, ' ')|| 
        ' Rows affected: '|| SQL%BULK_ROWCOUNT(i));
    END LOOP;
END;    
/


--# SAVE EXCEPTIONS and SQL%BULK_EXCEPTION 

CREATE TABLE exception_test(
id  NUMBER(10) NOT NULL
);


DECLARE 
    TYPE t_tab IS TABLE OF exception_test%ROWTYPE;
    
    l_tab   t_tab := t_tb();
    l_error_count   NUMBER;
    
    ex_dml_errors   EXCEPTION;
    PRAGMA EXCEPTION_INIT(ex_dml_errors, -24381);
BEGIN 
    -- Fill the collection.
    FOR i IN 1..100 LOOP
        l_tab.extend;
        l_tab(l_tab.last).id := i;
    END LOOP;
    
    -- Cause a failure 
    l_tab(50).id := NULL;
    l_tab(51).id := NULL;
    
    EXECUTE IMMEDIATE 'TRUNCATE TABLE exception_test';
    
    -- Perform a bulk operation.
    
    BEGIN 
        FORALL i IN l_tab.first .. l_tab.last SAVE EXCEPTIONS
        INSERT INTO exception_test
        VALUES (l_tab(i));
        
    EXCEPTION
        WHEN ex_dml_errors THEN 
            l_error_count := SQL%BULK_EXCEPTIONS.count;
            DBMS_OUTPUT.PUT_LINE('Number of failures: '|| l_error_count);
            FOR i in 1..l_error_count 
            LOOP            
            DBMS_OUTPUT.PUT_LINE('Error: '|| i ||
            'Array Index: '|| SQL%BULK_EXCEPTIONS(i).error_index ||
            'Message: '|| SQLERRM(-SQL%BULK_EXCEPTIONS(i).ERROR_CODE));
            END LOOP;
    END;
       
END;
    



select * from orders o
where o.ORDER_DATE between to_date('01/05/2021', 'MM/DD/YYYY') and to_date(sysdate, 'MM/DD/YYYY')
and o.item_name like '%LAPTOP%'
and o.item_catagory like '%Intel%';



select extract (month from sysdate) from dual; -- 5
select left('sayed', 2) from dual;

