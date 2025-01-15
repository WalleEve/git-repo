create table hData(
n  number,
p number);


insert into hdata values(1, 2);
insert into hdata values(3, 2);
insert into hdata values(6, 8);
insert into hdata values(9, 8);
insert into hdata values(2, 5);
insert into hdata values(8, 5);
insert into hdata values(5, null);

commit;


select * from hdata;

select n, p from hdata
start with n = (select n from hdata where p is null)
connect by prior n=p;


--#     HIRARCHICAL QUERY 
Hierarchical Queries are  queries that are executed upon tables that contains hierarchical data.
To execute the hierarchical queries we need the following clauses.

# START WITH 
It specifies the root rows of the hierarchy 
# CONNECT BY 
It is used to specify the relationship between parent rows and child rows of the hierarchy



create table states(
id number,
sname varchar2(20));


create table dist(
id number,
state_id number,
dist_name varchar2(20));


insert into states values(1, 'Odisha');
insert into states values(2, 'West Bangal');
insert into states values(3, 'Telangana');


insert into dist values(1, 1, 'Jajpur');
insert into dist values(2, 1, 'Khorda');
insert into dist values(3, 1, 'Cuttack');
insert into dist values(4, 1, 'Puri');
insert into dist values(5, 1, 'Keonjhar');

insert into dist values(1, 2, 'Alipurduar');
insert into dist values(2, 2, 'Bankura');
insert into dist values(3, 2, 'Birbhum');
insert into dist values(4, 2, 'Cooch Behar');
insert into dist values(5, 2, 'Dakshin Dinajpur');

insert into dist values(1, 3, 'ADILABAD');
insert into dist values(2, 3, 'BHADRADRI KOTHAGUDEM');
insert into dist values(3, 3, 'HANUMAKONDA');
insert into dist values(4, 3, 'HYDERABAD');
insert into dist values(5, 3, 'JAGTIAL');

commit;

--truncate table dist;

select  stid, did from (
select s.id stid, d.id did, s.sname, d.dist_name, d.state_id from 
states s, dist d
where s.id = d.state_id)
start with stid = (select id from states where sname='Odisha')
connect by prior stid = state_id

ORA-01436: CONNECT BY loop in user data
01436. 00000 -  "CONNECT BY loop in user data"


select ename, empno, mgr, job
from emp
connect by prior empno=mgr;

select ename, empno, mgr, job
from emp
start with job='PRESIDENT'
connect by  prior empno=mgr;


select ename, empno, mgr, job
from emp
start with ename = 'KING'
connect by prior empno=mgr;


select ename, empno, mgr, job, sal
from emp
start with sal = 5000
connect by prior empno=mgr;

select ename, empno, mgr, job, sal 
from emp
start with ename = 'KING'
connect by prior empno=mgr 
and job='MANAGER';


select e.ename, m.ename
from emp e, emp m
where e.mgr = m.empno



# CONNECT_BY_ROOT 

select ename as name, 
connect_by_root(ename) as boss
from emp
start with empno=7839
connect by prior empno=mgr;

# SYS CONNECT BY PATH Function 

select ename,
sys_connect_by_path(ename, '/') "Path"
from emp
start with ename='KING'
connect by prior empno=mgr;


# NOCYCLE Keyword 

Select ename, 
sys_connect_by_path(sal, '/') "Path"
from emp
start with ename='KING'
connect by nocycle prior empno=mgr; 

# SIBLINGS Keyword 

select ename, empno, mgr
from emp
start with empno=7839
connect by prior empno=mgr;

select ename, empno, mgr
from emp
start with ename='KING'
connect by prior empno=mgr
order by ename;

select ename, empno, mgr
from emp
start with ename='KING'
connect by prior empno=mgr
order siblings by ename;



create table temp_emp as select * from emp;

drop trigger update_temp_emp;
create or replace trigger update_temp_emp
after delete on temp_emp for each row
begin
update temp_emp set mgr = null where mgr=:OLD.empno;
end;
/

select e.ename, e.empno, e.job, e.deptno, m.ename as manager_name, m.empno manager_id
from temp_emp e , temp_emp m
where e.mgr=m.empno
and e.deptno=30;

delete from temp_emp where empno=7698;

Error report -
ORA-04091: table SCOTT.TEMP_EMP is mutating, trigger/function may not see it
ORA-06512: at "SCOTT.UPDATE_TEMP_EMP", line 2
ORA-04088: error during execution of trigger 'SCOTT.UPDATE_TEMP_EMP'

drop table temp_dept;
create table temp_dept as select * from dept;

drop trigger update_temp_emp_dept;
create or replace trigger update_temp_emp_dept
before delete on temp_dept for each row
begin
update temp_emp set deptno = null where deptno=:OLD.deptno;
end;
/

delete from temp_dept where deptno=30;

select e.ename, e.empno, e.job, e.deptno, m.ename as manager_name, m.empno manager_id
from temp_emp e , temp_emp m
where e.mgr=m.empno
and e.deptno is null;


 
















