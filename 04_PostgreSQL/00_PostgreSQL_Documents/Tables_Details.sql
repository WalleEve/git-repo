select * from employees;
select * from departments; 
select * from jobs;
select * from locations;
select * from regions;
select * from countries;
select * from job_history;
select * from emp_details_view;

create table emp_details as select * from emp_details_view;
select * from emp_details;

select ed.first_name, ed.last_name, ed.employee_id, ed.job_id, 
edm.first_name, edm.last_name, edm.employee_id, edm.job_id
from 
emp_details ed, emp_details edm
where ed.manager_id = edm.employee_id;


