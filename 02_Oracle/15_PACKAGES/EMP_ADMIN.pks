CREATE OR REPLACE PACKAGE emp_admin AS
/******************************************************************************
   NAME:       emp_admin
   PURPOSE:

   REVISIONS:
   Ver        Date        Author           Description
   ---------  ----------  ---------------  ------------------------------------
   1.0        04/05/2024      sayed       1. Creating emp_admin Package
   
******************************************************************************/

-- Declare public type, cusror, and exception:
  TYPE EmpRecType IS RECORD (emp_id NUMBER, sal NUMBER);
  CURSOR desc_salary RETURN EmpRecType;
  invalid_salary EXCEPTION;
  
  -- Declare public subprograms:
  
  FUNCTION hire_employee(
    last_name  VARCHAR2,
    first_name varchar2,
    email      varchar2,
    phone_number    varchar2,
    job_id  varchar2,
    salary  number,
    commission_pct  number,
    manager_id  number,
    department_id   number
    ) RETURN NUMBER;
    
  -- Overload preceding public subprogram:  
  PROCEDURE fire_employee(emp_id IN NUMBER);
  PROCEDURE fire_employee(emp_email varchar2);
  
  PROCEDURE raise_salary(emp_id number, amount number);
  FUNCTION nth_highest_salary (n NUMBER) RETURN EmpRecType;

END emp_admin;

/


-- Package body;

CREATE OR REPLACE PACKAGE BODY emp_admin AS 
    number_hired NUMBER; -- Private varibale
    
    --Define cursor declared in package specification;
    
    CURSOR desc_salary RETURN EmpRecType IS 
        SELECT employee_id, salary
        FROM employees 
        ORDER BY salary DESC;
        
    -- Define subprograms declared in package specifications 
    FUNCTION hire_employee (
        last_name   VARCHAR2,
        first_name  VARCHAR2,
        email       VARCHAR2,
        phone_number    VARCHAR2,
        job_id      VARCHAR2,
        salary      NUMBER,
        commission_pct  NUMBER,
        manager_id  NUMBER,
        department_id   NUMBER
    ) RETURN NUMBER
    IS 
        new_emp_id  NUMBER;
    BEGIN 
        new_emp_id  := employees_seq.NEXTVAL;
        INSERT INTO employees (
            employee_id,
            last_name,
            first_name,
            email,
            phone_number,
            hire_date,
            job_id,
            salary,
            commission_pct,
            manager_id,
            department_id
        )
        VALUES (
            new_emp_id,
            hire_employee.last_name,
            hire_employee.first_name,
            hire_employee.email,
            hire_employee.phone_number,
            sysdate,
            hire_employee.job_id,
            hire_employee.salary,
            hire_employee.commission_pct,
            hire_employee.manager_id,
            hire_employee.department_id
        );
        
        number_hired    := number_hired + 1;
        DBMS_OUTPUT.PUT_LINE('THe number of employees hired is '
            || TO_CHAR(number_hired));
        return new_emp_id;
    END hire_employee;
    
    PROCEDURE fire_employee (emp_id NUMBER) IS 
    BEGIN
        DELETE FROM employees WHERE employee_id = emp_id;
    END fire_employee; 
    
    PROCEDURE fire_employee (emp_email VARCHAR2) IS 
    BEGIN 
        DELETE FROM employees WHERE email = emp_email;
    END fire_employee;
    
    -- Define private function, available only inside package 
    
    FUNCTION sal_ok (
        jobid   VARCHAR2,
        sal     NUMBER
    ) RETURN BOOLEAN 
    IS 
        min_sal NUMBER;
        max_sal NUMBER;
    BEGIN 
        SELECT MIN(salary), MAX(salary)
        INTO min_sal, max_sal
        FROM employees
        WHERE job_id = jobid;
        
      RETURN (sal >= min_sal) and (sal <= max_sal);
       
    END sal_ok;
    
    PROCEDURE raise_salary (
        emp_id  NUMBER,
        amount  NUMBER
    ) IS 
        sal NUMBER(8, 2);
        jobid   VARCHAR2(10);
    BEGIN 
        SELECT job_id, salary 
        INTO jobid, sal 
        FROM employees 
        WHERE employee_id = emp_id;
        
        IF sal_ok(jobid, sal+amount) THEN   -- Invoke Private functio 
            UPDATE employees
                SET salary = salary + amount
            WHERE employee_id = emp_id;
        ELSE 
            raise invalid_salary;
        END IF;
        
        EXCEPTION 
            WHEN invalid_salary THEN 
                DBMS_OUTPUT.PUT_LINE('The salary is out of the specified range.');
    END raise_salary;
    
    FUNCTION nth_highest_salary(
        n number
    ) RETURN EmpRecType
    IS 
        emp_rec EmpRecType;
    BEGIN 
        OPEN desc_salary;
        FOR i IN 1..n LOOP
            FETCH desc_salary INTO emp_rec;
        END LOOP;
        RETURN emp_rec;
    END nth_highest_salary;
    
BEGIN 
    INSERT INTO log (date_of_action, user_id, package_name)
    VALUES (SYSDATE, USER, 'EMP_ADMIN');
    number_hired :=0;
    
END emp_admin;