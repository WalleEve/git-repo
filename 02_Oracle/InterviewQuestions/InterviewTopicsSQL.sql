select * from emp;

--# Get the second highest sal based on Deptno.
select * from (
select sal, deptno, row_number() over (partition by deptno order by sal desc) rn
from emp)
where rn=2;

--# How to Delete Duplicate Rows from a table
Drop table Duplicate_Record;

Create table Duplicate_Records as  
Select e1.* from emp e1, emp e2;

select distinct * from Duplicate_Records where empno=7844;
delete from Duplicate_Records where rowid not in (
select rid from (
select rowid as rid, empno, ename, job, mgr, hiredate, sal, comm, deptno,
row_number() over(partition by empno order by rowid) rn
from Duplicate_Records )
where rn=1 );

select * from duplicate_records;


--# Get the second highest salary:
select sal from (
select sal, row_number() over (order by sal desc) as rn 
from emp)
where rn=2;

select sal from (
select sal, rank() over (order by sal desc) as rn
from emp
)
where rn=2;

select max(sal) from emp
where sal < (
select max(sal) from emp);

--# SQL Functions 

--NVL() 
-- To handel NULL values 
-- Syntax: NVL(column_name, value)
select ename, sal, comm, nvl(comm, 0) comm_with_nvl 
from emp;

-- NVL2()
-- To handel the NULL values with the default value if it is not null
-- Syntax: NVL2(column_name, value1, value2)
Select ename, sal, comm, NVL2(comm, 1000, 2000) comm_with_nvl2
from emp;


-- Substr() : SUBSTRING 
-- To get the nested string from a string.
-- Syntax: substr(column, start, end)
-- start: starting index of the nested string
-- end: number of position forward to go.

select ename, substr(ename, 1, 3) first_3_letter
from emp;

-- Instr(): INSTRING 
-- To get the index value of a particular nested string (nested string: string inside string)
-- Syntax: instr(string, value, start, occerance)
-- String can be any stirng or column name 
-- Value is the nested string need to be search
-- start is the starting position of the search
-- occerance is the number of times the string present in the search stirng

select ename, instr(ename, 'E', 1, 1) index_starting_occracnce
from emp;

-- Note: if there is no search string found it will return 0

select ename, instr(ename, 'E', 1, 2) index_starting_occracnce
from emp;







-- LPAD() LEFT SIDE PADDING 
-- Syntax: lpad(string, Padding, value)
-- String can be a coated string or column name
-- padding will be the number of length we are expexting including padding
-- value: will be the value in the place of padding it can be space or any spacific value
select ename, lpad(ename, 10, '_') lpadof10 
from emp;




-- RPAD()


-- TRIM()

-- LTRIM()

-- RTRIM()

-- TO_CHAR()


-- TO_DATE()


-- TO_NUMBER()

-- COALEASE()


-- NULLIF 


 


-- NESTED-QUERY 

-- SUBQUERY

-- CO-RELATED SUBQUERY

-- Joins
    --. INNER JOIN
    --. LEFT JOIN
    --. RIGHT JOIN
    --. FULL OUTER JOIN
    --. SELF JOIN


-- ANSI JOINS
    --. EQUI JOIN
    --. CROSS JOIN 
    --. LEFT JOIN
    --. RIGHT JOIN 
    --. NATURAL JOIN
    --. NON-EQUIJOIN
    

-- SET Operators:
    -- UNION 
    -- MINUS
    -- INTERSECT 
    -- UNION ALL 
    
-- HIERARCHY QUERY 


-- AGGREGATE FUNCTIONS 



-- ANALYTICAL FUNCTIONS 


-- OBJECT TYPE 


--###########################################################

create table tbl1 (srno number);
create table tbl2 (srno number);

insert into tbl1 values(null);
insert into tbl1 values(null);

--insert into tbl1 values(null);

insert into tbl2 values(null);
insert into tbl2 values(null);
insert into tbl2 values(null);

select * from tbl1;
select * from tbl2;

select A.SRNO,B.SRNO
from tbl1 a , tbl2 b
where A.SRNO=B.SRNO  ; -- 0

select *
from tbl1 a left join tbl2 b on a.srno = b.srno; -- 2 

select * from  
tbl1 a right join tbl2 b on a.srno = b.srno;

select * from tbl1 a
UNION 
select * from tbl2 b;


select * from tbl1 a 
UNION ALL 
select * from tbl2 b; 
























