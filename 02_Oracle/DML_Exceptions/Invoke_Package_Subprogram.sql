-- Invoke Package subprogram in anonymous block:

DECLARE 
    new_emp_id NUMBER(6);
BEGIN 
    new_emp_id := emp_admin.hire_employee(
        'Belden',
        'Enrique',
        'EBELDEN',
        '5551112222',
        'ST_CLERK',
        2500,
        .1,
        101,
        110
    );
    DBMS_OUTPUT.PUT_LINE('The employee id is '|| TO_CHAR(new_emp_id));
    emp_admin.raise_salary(new_emp_id, 100);
    
    DBMS_OUTPUT.PUT_LINE(
        'The 10th highest salary is '||
        TO_CHAR(emp_admin.nth_highest_salary(10).sal) ||
        ', Belongs to employee: '||
        TO_CHAR(emp_admin.nth_highest_salary(10).emp_id)
    );
    
    emp_admin.fire_employee(new_emp_id);
    -- we can aslo delete the newly added employee as follows:
    -- emp_admin.fire_employee('EBELDEN');
END;
/
