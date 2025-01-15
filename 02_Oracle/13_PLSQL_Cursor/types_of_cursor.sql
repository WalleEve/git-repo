CREATE TABLE endangered_species 
( 
   common_name    VARCHAR2 (100), 
   scientific_name   VARCHAR2 (100) 
);
/

BEGIN
   /* https://www.worldwildlife.org/species/directory?direction=desc&sort=extinction_status */
   INSERT INTO endangered_species
        VALUES ('Amur Leopard', 'Panthera pardus orientalis');

   INSERT INTO endangered_species
        VALUES ('Hawksbill Turtle', 'Eretmochelys imbricata');

   INSERT INTO endangered_species
        VALUES ('Javan Rhino', 'Rhinoceros sondaicus');


   COMMIT;
END;
/

select * from endangered_species;
/

set serveroutput on;
/

--# Implicit Cursor (aka, SELECT-INTO)
DECLARE 
    l_common_name   endangered_species.common_name%TYPE;
BEGIN 
    SELECT common_name 
        INTO l_common_name
        FROM endangered_species
    WHERE scientific_name  = 'Rhinoceros sondaicus';
    
EXCEPTION 
    WHEN NO_DATA_FOUND  
    THEN 
        DBMS_OUTPUT.PUT_LINE('Error or data condition');
    WHEN TOO_MANY_ROWS
    THEN 
        DBMS_OUTPUT.PUT_LINE('Error if primary key/unique index lookup!');
END;
/


--# Bulk Implicit Curosr (aka, SELECT BULK COLLECT INTO)
DECLARE 
    TYPE species_nt IS TABLE OF endangered_species%ROWTYPE;
    
    l_species   species_nt;
BEGIN 
    SELECT *
        BULK COLLECT INTO l_species
    FROM endangered_species
    ORDER BY common_name;
    
    DBMS_OUTPUT.PUT_LINE(l_species.COUNT);
END;
/

--# Explicit Cursor (aka, CURSOR cursor_name IS SELECT...)

DECLARE 
    CURSOR species_cur 
    IS 
        SELECT * FROM
        endangered_species 
        ORDER BY common_name;
        
    l_species   species_cur%ROWTYPE;
BEGIN 
    OPEN species_cur;
    
    FETCH species_cur into l_species;
    
    CLSOE species_cur;
END;
/

--# Parameterize Explicit Cursor 
DECLARE 
    CURSOR species_cur(filter_in IN VARCHAR2)
    IS 
        SELECT * 
            FROM endangered_species 
            WHERE scientific_name LIKE filter_in
        ORDER BY common_name;
    
    l_species   species_cur%ROWTYPE;
BEGIN
    OPEN species_cur('%u%');
    FETCH species_cur INTO l_species;
    CLOSE species_cur;
    
    /* Use same cursor a second time, avoiding copy-pate of SQL */
    
    OPEN species_cur ('%e%');
    FETCH species_cur INTO l_species;
    CLOSE species_cur;
    
    /* We can even use it in a cursor FOR loop */
    FOR rec in species_cur('%u%')
    LOOP
        DBMS_OUTPUT.PUT_LINE(rec.common_name);
    END LOOP;
END;
/


--# Explicit Cursor in Package Specification, SQL Hidden 

CREATE PACKAGE species_pkg
IS 
    CURSOR species_cur
        RETURN endangered_species%ROWTYPE;
END species_pkg;
/

--# Hide SELECT in Package Body 
CREATE PACKAGE BODY species_pkg 
IS 
    CURSOR species_cur 
        RETURN endangered_species%ROWTYPE
    IS 
        SELECT * 
            FROM endangered_species 
        ORDER BY common_name;
END species_pkg;
/


BEGIN 
    FOR rec in species_pkg.species_cur
    LOOP
        DBMS_OUTPUT.PUT_LINE('Aminal Name: '|| rec.common_name );
    END LOOP;
END;
/


--# CURSOR FOR LOOP with Explicit Cursor 
DECLARE 
    CURSOR species_cur 
    IS 
        SELECT * 
            FROM endangered_species
        ORDER BY common_name;
        
    PROCEDURE start_conservation_effort
    IS 
    BEGIN 
        DBMS_OUTPUT.PUT_LINE('Remove human presence.');
    END;
BEGIN 
    FOR rec IN species_cur
    LOOP
        DBMS_OUTPUT.PUT_LINE(rec.common_name);
    END LOOP;
    
    FOR rec IN species_cur 
    LOOP
        start_conservation_effort;
    END LOOP;
END;
/

--# Cursor Variable Based on Strong and Week Ref Cursor Types 
CREATE OR REPLACE PACKAGE refcursor_pkg authid definer
IS 
    /* Use this "strong" REF CURSOR to declare cursor variables whose
    quaries return data from the endangered_species table */
    
    TYPE endangered_species_t IS REF CURSOR
        RETURN endangered_species%ROWTYPE;
        
    /* Use a "week" REF CURSOR to declare cursor variables whose 
    quaries return any number of columns.
    or use the pre-defined SYS-REFCURSOR 
    */
    
    TYPE week_t IS REF CURSOR;
    
    FUNCTION filter_species_cv(filter_in IN VARCHAR2)
        RETURN endangered_species_t; 
        
    /* Return data from whatever quary is passed as an argument. */
    
    FUNCTION data_from_any_query_cv(query_in VARCHAR2)
        RETURN week_t;
        
    /* Return data from whatever query is passes as an argument.
    But this time, use the predefined week type. */
    
    FUNCTION data_from_any_query_cv2 (query_in IN VARCHAR2)
        RETURN SYS_REFCURSOR;
END refcursor_pkg;
/

CREATE OR REPLACE PACKAGE BODY refcursor_pkg 
IS 
    FUNCTION filter_species_cv (filter_in IN VARCHAR2)
        RETURN endangered_species_t
    IS 
        l_cursor_variable endangered_species_t;
    BEGIN 
        IF filter_in IS NULL THEN 
            OPEN l_cursor_variable FOR 
                SELECT * FROM endangered_species;
        ELSE 
            OPEN l_cursor_variable FOR 
                SELECT * 
                    FROM endangered_species
                 WHERE common_name like filter_in;
        END IF;
        RETURN l_cursor_variable;
    END filter_species_cv;
    
    FUNCTION data_from_any_query_cv (query_in IN VARCHAR2)
        RETURN week_t 
    IS
        l_cursor_variable week_t;
    BEGIN 
        OPEN l_cursor_variable FOR query_in;
        
        RETURN l_cursor_variable;
    END data_from_any_query_cv;
    
    FUNCTION data_from_any_query_cv2 (query_in IN VARCHAR2)
        RETURN SYS_REFCURSOR 
    IS 
        l_cursor_variable SYS_REFCURSOR;
    BEGIN 
        OPEN l_cursor_variable FOR query_in;
        
        RETURN l_cursor_variable;
    END data_from_any_query_cv2;
END refcursor_pkg;
/

--# Using Standard Cursor Operations with Cursor Variable 
  
 DECLARE 
    l_objects   refcursor_pkg.endangered_species_t;
    l_object    endangered_species%ROWTYPE;
BEGIN 
    l_objects   := refcursor_pkg.filter_species_cv('%u%');
    
    LOOP
        FETCH l_objects INTO l_object;
        
        EXIT WHEN l_objects%NOTFOUND;
        
        DBMS_OUTPUT.PUT_LINE(l_object.common_name);
    END LOOP;
END;
/



                    

    
    
