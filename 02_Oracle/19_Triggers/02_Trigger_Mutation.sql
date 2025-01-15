create or replace trigger check_raise_on_avg
for update of sal on emp
compound trigger 

twelve_percent constant number :=0.12;

-- Declare collection type and variables 

TYPE department_salaries_t  is table of emp.sal%type
index by varchar2(80);

department_avg_salaries  department_salaries_t ;
type sal_t is table of emp.sal%type;
avg_salaries sal_t;

type deptno_t is table of emp.deptno%type;
department_ids deptno_t;

before statement is 
begin

    select  avg(e.sal), nvl(e.deptno, -1)
    bulk collect into avg_salaries, department_ids
    from emp e 
    group by e.deptno;
    
    for j in 1..department_ids.count() loop
        department_avg_salaries(department_ids(j)) := avg_salaries(j);
    end loop;
    
    end before statement;
    
    after each row is 
    begin
        if :new.sal - :old.sal >
        twelve_percent * department_avg_salaries(:new.deptno)
        then 
        raise_application_error(-20000, 'Raise too large');
        end if;
    end after each row;    
end check_raise_on_avg;



update emp set sal = sal*1.10 where empno = 7369;

select * from emp;