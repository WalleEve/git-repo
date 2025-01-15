--# Example 10-3 Matching Package Specification and Body 

CREATE OR REPLACE PACKAGE emp_bonus AUTHID DEFINER AS 
    PROCEDURE calc_bonus (hire_date employees.hire_date%TYPE);
END emp_bonus;
/

CREATE OR REPLACE PACKAGE BODY emp_bonus AS 
    PROCEDURE calc_bonus (hire_date employees.hire_date%TYPE)
    IS 
    BEGIN 
        DBMS_OUTPUT.PUT_LINE('Employees hired on '|| hire_date || ' get bonus.');
    END;
END emp_bonus;
/




        