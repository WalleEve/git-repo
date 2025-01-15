drop table temp_dept;
create table temp_dept as select * from dept;

create or replace procedure emp_mgr_update(in_mgr_id number)
as
begin
    update temp_emp set mgr = null where mgr = in_mgr_id;
    commit;
end;
/

create or replace trigger temp_emp_mgr_upd
after delete 
on emp for each row
declare 
 olg_mgr number;
begin
olg_mgr := :OLD.mgr;
--emp_mgr_update(olg_mgr);
 update temp_emp set mgr = null where mgr = olg_mgr ;
end;
/


delete from temp_emp where empno=7698;
Error report -
ORA-04091: table SCOTT.TEMP_EMP is mutating, trigger/function may not see it
ORA-06512: at "SCOTT.UPDATE_TEMP_EMP", line 2
ORA-04088: error during execution of trigger 'SCOTT.UPDATE_TEMP_EMP'

# Mutating Table Error 
Mutating error normally occurs when we are performing some DML operatios and we are trying to select the affected records
from the same trigger. so Basically we are trying to select records inn the trigger from the table that owns the trigger.
This creates inconsistency and Oracle throws a mutating error.

create table etest(
eid number,
ename varchar2(10),
salary number(10),
status varchar2(10)
);

insert into etest values(102, 'Ankit', 8000, 'Active');
insert into etest values(104, 'Nikhil', 68000, 'Active');
insert into etest values(105, 'Rajan', 18000, 'Active');
insert into etest values(107, 'Karan', 101000, 'Active');
insert into etest values(110, 'Sajal', 88000, 'Active');
insert into etest values(101, 'Ravi', 89000, 'Active');
insert into etest values(109, 'Manu', 777000, 'Active');

# Mutating Trigger 

create or replace trigger etest_status_trigger /* Row Level TRIGGER*/
after update of status on etest
for each row 
declare
v_count number;
begin
select count(*) into v_count from etest
where status='Active';
dbms_output.put_line('Total Number of Active Records: '|| v_count);
end;
/


update etest 
set status='InActive' where eid in (109, 110);

Error report -
ORA-04091: table SCOTT.ETEST is mutating, trigger/function may not see it
ORA-06512: at "SCOTT.ETEST_STATUS_TRIGGER", line 4
ORA-04088: error during execution of trigger 'SCOTT.ETEST_STATUS_TRIGGER'

# Solution 

create or replace trigger etest_status_trigger /* Statement Level TRIGGER */
after update of status on etest
declare 
v_count number;
begin
select count(*) into v_count from etest
where status='Active';
dbms_output.put_line('The Total Number of Active Records: '||v_count);
end;
/
set serveroutput on;
update etest 
set status='InActive' where eid in (109, 110);

drop trigger UPDATE_TEMP_EMP;


drop table temp_emp;
create table temp_emp as select * from emp;
--drop trigger temp_emp_mgr_upd;
create or replace trigger temp_emp_mgr_upd
for delete
on temp_emp 
compound trigger
v_empno number;

before each row is 
begin 
    v_empno := :old.empno;
end before each row;

after statement is 
begin
    update temp_emp set mgr=null where mgr = v_empno;
    dbms_output.put_line(v_empno);
end after statement;
end;


delete from temp_emp where empno=7698;

select * from temp_emp where deptno=30;




 











