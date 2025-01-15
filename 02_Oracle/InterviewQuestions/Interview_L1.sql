Q1. Delete Duplicate rows:
	Ans: 1st Method we can use the distinct keyword, but you need to recreate all oracle indexes, triggers
	> Create table my_table1 as select distinct * from my_table;
	> drop my_table;
	> rename my_table1 to my_table;
	
	
	2nd Method using the rowid we can delete the duplicate records
	How to find and delete duplicate records in Oracle using rowid. 
	The below example shows one column. if you have deleted based on two-column ,you can specify two column
	> Delete from my_table where rowid not in (
	  select max(rowid) from my_table group by my_col_name );
	  
	3rd method we can use oracle self-join to delete duplicate rows
	> DELETE FROM my_table A WHERE ROWID > 
		(SELECT min(rowid) FROM my_table B WHERE A.key_values = B.key_values);
		
	4th using exists clause
	> delete from my_table t1
	  where exists (select 'x' from my_table t2
					where t2.key_value1 = t1.key_value1
					and t2.key_value2 = t1.key_value2
					and t2.rowid > t1.rowid);
	5th delete duplicate records by using oracle analytic functions				
	> delete from my_table
	  where rowid in
	  (select rid
		from
		( select
			rowid rid,
			row_number() over (partition by column_name order by rowid) rn
			from my_table)
		where rn <> 1
	  )
	  
Q2: Fetch the top n salary 

# PostgreSQL 
> select sal from (
	select sal,  rank() over(partition by sal order by empno ) rn, 
	dense_rank () over(partition by sal order by empno ) drn
	from emp) a
	where rn = 1 order by sal desc limit 3;
	
# Oracle 
>	select sal, rownum from (
	select distinct sal
	from emp
	order by sal desc) a
	where rownum <=3
	
> select * from (
  select sal, rownum rn from (
  select distinct sal
  from emp
  order by sal desc) a
  where rownum <=5 )
  where rn=5g
  
> select * from (
	select sal, rownum rn
	from (
	select distinct sal
	from emp
	order by sal desc)
	where rownum <=2
	order by sal )
	where rn=2
	
	
	

class Parent:
    def print_name(self):
        print("Print Parent Class")
class Child(Parent):
    def print_name(self):
        print("Print Child Class")
        super().print_name()
c1=Child()
c1.print_name()

a = 10 
b = 20 
l = [x if ]

range(1, 20)
xrange()

generator : yeild 
iter()

temp = 10
def func():
    temp global
    
     temp = 20
     return temp
print(temp)
print(func()) 
print(temp)

__init__ 

__new__ 
__str__ 

class Parent:
    def print_name(self):
        print("Print Parent Class")
class Child(Parent):
    def print_name(self):
        print("Print Child Class")
        super().print_name
c1=Child()
c1.print_name()



# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

l = [4, 5, 2, 3]


sorted_list = []
def sort_list(l):
    for i in range(0, len(l)):
        if i not in sorted_list:
            sorted_list.append(i)
        else:
            for j in range(0, len(sorted_list)):
                if l[i]<=sorted_list[i]:
                    sorted_list.insert(j, l[i])
                    break 
                else:
                    if j == len(i)-1:
                        sort_list.append(l[i])
                    else:
                        continue

sort_list (l)
print(sorted_list)


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
l = list((i for i in range(1, 11)))
print(l)
print(l[::-1])

v_even = []
def even(l):
    for i in l:
        if i%2 == 0:
            v_even.append(i)
            
even(l)            
print(v_even)

{}
    
	
	
	class A:
	def __init__(self):
		self.a = 'Hi' 
	def setter(self):
		
	
		

class B(A):
	def __init__(self):
		super().setter()
	
	def getter(slef):
		
		
a = B()
a.getter()

a = {1: 'a', 2: 'b'}

for key, value in a.items():
	try:
		
		print(key)
		print(value)
	except:
		print("No value")
	else:
		print("HU")
	finally:
		print("Hello")
	

emp, dept 

select sal from (
select sal, rownum() rn
	
from (select emp e, dept d
where e.deptid = d.deptid
)
select sal (
slect sal, rownum  rn 
distinct sa
)where rn 2

select e.emp_name, m.emp_name as mgr_name
from emp e, emp m 
where m.mrg = e.empno 


'aaabcd'
select 'aaabcd', reg_exp.count('aaabcd', 'a')
from dual; 

select ename 
from emp 
where name like  '_a%'

select * from (
select items, rowcount rn
slect 
from (
select items, count(1)cnt from 
returns 
where year = 2023 
group by items
ordeer by cnt desc
fetch first 5 rows only)
)
where rn >=10 

-------------------------------------------------------------------

select sal from (
		select sal, rownum as rn from (
			(select distinct sal from emp order by sal desc)
		)	 
	 )
where rn=2;

select max(e.sal), e.deptno 
from 
emp e, (select max(emp.sal) as sal, emp.deptno 
from emp, dept 
where emp.deptno = dept.deptno
group by emp.deptno) emp2
where e.deptno = emp2.deptno
and e.sal < emp2.sal 
group by e.deptno;

select distinct * from (
select sal, deptno, dense_rank() over(partition by deptno order by sal desc) rn
from emp)
where rn=1;

select * from emp;

select e.ename mgr_name, m.ename 
from emp e, emp m 
where m.mgr = e.empno (+);

select 'aaabcdaa', regexp_count('aaabcdaa', 'a')
from dual; 

select ename
from emp 
where ename like '_A%';

select ename 
from emp 
where substr(ename, 2, 1)='A';

select ename from emp
order  by ename desc 
fetch  first 10 rows only;













	
	
	
	
		