SELECT * FROM V$VERSION;
SELECT PRODUCT, VERSION, STATUS FROM PRODUCT_COMPONENT_VERSION;
SELECT BANNER_FULL FROM V$VERSION;


select commission_pct from employees order by 1;

select sal from (
select sal, rownum rn
from (select distinct sal from emp order by sal desc)
)
where rn=2;
select * from (
select sal, row_number() over(order by sal desc) rn
from emp)
where rn=2;

select * from (
select sal,deptno,  row_number() over(partition by deptno order by sal desc) rn
from emp)
where rn=2;

create table sample_emp as (
select deptno from emp);
select * from sample_emp;

delete from 
sample_emp where rowid not in 
(
select max(rowid) as rid from sample_emp
group by deptno
);




