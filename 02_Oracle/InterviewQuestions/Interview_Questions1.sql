1. Question: Find the Second Highest Salary
Answer: To find the second-highest salary in a table, you can use a subquery with the LIMIT clause:
SELECT DISTINCT salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 1 OFFSET 1; 

2. Question: Calculate the Average Salary
Answer: To calculate the average salary, use the AVG function:
SELECT AVG(salary) 
FROM employees; 

3. Question: Identify Duplicate Rows
Answer: To find duplicate rows, use the GROUP BY clause and HAVING:
SELECT column1, column2, COUNT(*) as count
FROM table_name
GROUP BY column1, column2
HAVING COUNT(*) > 1; 

4. Question: Retrieve N Random Records
Answer: To fetch N random records, use ORDER BY and LIMIT
SELECT column1, column2 
FROM table_name
ORDER BY RANDOM()
LIMIT N; 

5. Question: Calculate Running Total
Answer: You can calculate a running total using the SUM function with the OVER clause:
SELECT date, value, 
SUM(value) OVER (ORDER BY date) AS running_total
FROM data; 

6. Question: Find Missing Numbers in a Range
Answer: To find missing numbers in a range, use a recursive common table expression (CTE)
WITH RECURSIVE MissingNumbers AS (
SELECT 1 AS number
  UNION ALL
  SELECT number + 1
  FROM MissingNumbers
  WHERE number < 100
)
SELECT number
FROM MissingNumbers
LEFT JOIN table_name ON MissingNumbers.number = table_name.column_name
WHERE table_name.column_name IS NULL;


Technical SQL Interview Questions for Beginners 
Now, let's move on to the technical SQL interview questions and some potential answers to them.

When answering technical questions, the best strategy is to give as precise answers as possible. It may look like an attempt to deviate from the main topic. In addition, it may provocate additional questions about which you can feel less confident.

1. What is SQL?
It stands for Structured Query Language. A programming language used for interaction with relational database management systems (RDBMS). This includes fetching, updating, inserting, and removing data from tables.

2. What are SQL dialects? Give some examples.
The various versions of SQL, both free and paid, are also called SQL dialects. All the flavors of SQL have a very similar syntax and vary insignificantly only in additional functionality. Some examples are Microsoft SQL Server, PostgreSQL, MySQL, SQLite, T-SQL, Oracle, and MongoDB.

3. What are the main applications of SQL?
Using SQL, we can:

create, delete, and update tables in a database
access, manipulate, and modify data in a table
retrieve and summarize the necessary information from a table or several tables
add or remove certain rows or columns from a table
All in all, SQL allows querying a database in multiple ways. In addition, SQL easily integrates with other programming languages, such as Python or R, so we can use their combined power.

4. What is an SQL statement? Give some examples.
Also known as an SQL command. It's a string of characters interpreted by the SQL engine as a legal command and executed accordingly. Some examples of SQL statements are SELECT, CREATE, DELETE, DROP, REVOKE, and so on.

5. What types of SQL commands (or SQL subsets) do you know?
Data Definition Language (DDL) – to define and modify the structure of a database.
Data Manipulation Language (DML) – to access, manipulate, and modify data in a database.
Data Control Language (DCL) – to control user access to the data in the database and give or revoke privileges to a specific user or a group of users.
Transaction Control Language (TCL) – to control transactions in a database.
Data Query Language (DQL) – to perform queries on the data in a database to retrieve the necessary information from it.
6. Give some examples of common SQL commands of each type.
DDL: CREATE, ALTER TABLE, DROP, TRUNCATE, and ADD COLUMN
DML: UPDATE, DELETE, and INSERT
DCL: GRANT and REVOKE
TCL: COMMIT, SET TRANSACTION, ROLLBACK, and SAVEPOINT
DQL: – SELECT
7. What is a database?
A structured storage space where the data is kept in many tables and organized so that the necessary information can be easily fetched, manipulated, and summarized.

8. What is DBMS, and what types of DBMS do you know?
It stands for Database Management System, a software package used to perform various operations on the data stored in a database, such as accessing, updating, wrangling, inserting, and removing data. There are various types of DBMS, such as relational, hierarchical, network, graph, or object-oriented. These types are based on the way the data is organized, structured, and stored in the system.

9. What is RDBMS? Give some examples of RDBMS.
It stands for Relational Database Management System. It's the most common type of DBMS used for working with data stored in multiple tables related to each other by means of shared keys. The SQL programming language is particularly designed to interact with RDBMS. Some examples of RDBMS are MySQL, PostgreSQL, Oracle, MariaDB, etc.

10. What are tables and fields in SQL?
A table is an organized set of related data stored in a tabular form, i.e., in rows and columns. A field is another term for a column of a table.

11. What is an SQL query, and what types of queries do you know?
A query is a piece of code written in SQL to access the data from a database or to modify the data. Correspondingly, there are two types of SQL queries: select and action queries. The first ones are used to retrieve the necessary data (this also includes limiting, grouping, ordering the data, extracting the data from multiple tables, etc.), while the second ones are used to create, add, delete, update, rename the data, etc.

12. What is a subquery?
Also called an inner query; a query placed inside another query, or an outer query. A subquery may occur in the clauses such as SELECT, FROM, WHERE, UPDATE, etc. It's also possible to have a subquery inside another subquery. The innermost subquery is run first, and its result is passed to the containing query (or subquery).

13. What types of SQL subqueries do you know?
Single-row – returns at most one row.
Multi-row – returns at least two rows.
Multi-column – returns at least two columns.
Correlated – a subquery related to the information from the outer query.
Nested – a subquery inside another subquery.
14. What is a constraint, and why use constraints?
A set of conditions defining the type of data that can be input into each column of a table. Constraints ensure data integrity in a table and block undesired actions.

15. What SQL constraints do you know?
DEFAULT – provides a default value for a column.
UNIQUE – allows only unique values.
NOT NULL – allows only non-null values.
PRIMARY KEY – allows only unique and strictly non-null values (NOT NULL and UNIQUE).
FOREIGN KEY – provides shared keys between two and more tables.
16. What is a join?
A clause used to combine and retrieve records from two or multiple tables. SQL tables can be joined based on the relationship between the columns of those tables. Check out our SQL joins tutorial for more context. 

17. What types of joins do you know?
(INNER) JOIN – returns only those records that satisfy a defined join condition in both (or all) tables. It's a default SQL join.
LEFT (OUTER) JOIN – returns all records from the left table and those records from the right table that satisfy a defined join condition.
RIGHT (OUTER) JOIN – returns all records from the right table and those records from the left table that satisfy a defined join condition.
FULL (OUTER) JOIN – returns all records from both (or all) tables. It can be considered as a combination of left and right joins.
18. What is a primary key?
A column (or multiple columns) of a table to which the PRIMARY KEY constraint was imposed to ensure unique and non-null values in that column. In other words, a primary key is a combination of the NOT NULL and UNIQUE constraints. The primary key uniquely identifies each record of the table. Each table should contain a primary key and can't contain more than one primary key.

19. What is a unique key?
A column (or multiple columns) of a table to which the UNIQUE constraint was imposed to ensure unique values in that column, including a possible NULL value (the only one).

20. What is a foreign key?
A column (or multiple columns) of a table to which the FOREIGN KEY constraint was imposed to link this column to the primary key in another table (or several tables). The purpose of foreign keys is to keep connected various tables of a database.

21. What is an index?
A special data structure related to a database table and used for storing its important parts and enabling faster data search and retrieval. Indexes are especially efficient for large databases, where they significantly enhance query performance.

22. What types of indexes do you know?
Unique index – doesn't allow duplicates in a table column and hence helps maintain data integrity.
Clustered index – defines the physical order of records of a database table and performs data searching based on the key values. A table can have only one clustered index.
Non-clustered index – keeps the order of the table records that doesn't match the physical order of the actual data on the disk. It means that the data is stored in one place and a non-clustered index – in another one. A table can have multiple non-clustered indexes.
23. What is a schema?
A collection of database structural elements such as tables, stored procedures, indexes, functions, and triggers. It shows the overall database architecture, specifies the relationships between various objects of a database, and defines different access permissions for them.

24. What is a SQL comment?
A human-readable clarification on what a particular piece of code does. SQL code comments can be single-line (preceded by a double dash --) or span over multiple lines (as follows: /*comment_text*/). When the SQL engine runs, it ignores code comments. The purpose of adding SQL code comments is to make the code more comprehensive for those people who will read it in the future.

25. What is a SQL operator?
A reserved character, a combination of characters, or a keyword used in SQL queries to perform a specific operation. SQL operators are commonly used with the WHERE clause to set a condition (or conditions) for filtering the data.

26. What types of SQL operators do you know?
Arithmetic (+, -, *, /, etc.)
Comparison (>, <, =, >=, etc.)
Compound (+=, -=, *=, /=, etc.)
Logical (AND, OR, NOT, BETWEEN, etc.)
String (%, _, +, ^, etc.)
Set (UNION, UNION ALL, INTERSECT, and MINUS (or EXCEPT))
27. What is an alias?
A temporary name given to a table (or a column in a table) while executing a certain SQL query. Aliases are used to improve the code readability and make the code more compact. An alias is introduced with the AS keyword:


SELECT col_1 AS column
FROM table_name;

28. What is a clause?
A condition imposed on a SQL query to filter the data to obtain the desired result. Some examples are WHERE, LIMIT, HAVING, LIKE, AND, OR, ORDER BY, etc.

29. What are some common statements used with the SELECT query?
The most common ones are FROM, GROUP BY, JOIN, WHERE, ORDER BY, LIMIT, and HAVING.

30. How to create a table?
Using the CREATE TABLE statement. For example, to create a table with three columns of predefined datatypes, we apply the following syntax:


CREATE TABLE table_name (col_1 datatype,
                         col_2 datatype,
                         col_3 datatype);

31. How to update a table?
Using the UPDATE statement. The syntax is:


UPDATE table_name
SET col_1 = value_1, column_2 = value_2
WHERE condition;

32. How to delete a table from a database?
Using the DROP TABLE statement. The syntax is: DROP TABLE table_name;.

33. How to get the count of records in a table?
Using the COUNT() aggregate function with the asterisk passed as its argument: SELECT COUNT(*) FROM table_name;.

34. How to sort records in a table?
Using the ORDER BY statement:


SELECT * FROM table_name
ORDER BY col_1;

We can specify that we need a descending order using the DESC keyword; otherwise, the order will be ascending by default. Also, we can sort by more than one column and specify for each one, ascending or descending order separately. For example:


SELECT * FROM table_name
ORDER BY col_1 DESC, col_3, col_6 DESC;

35. How to select all columns from a table?
Using the asterisk * with the SELECT statement. The syntax is: SELECT * FROM table_name;.

36. How to select common records from two tables?

Using the INTERSECT statement:
SELECT * FROM table_1
INTERSECT
SELECT * FROM table_1;

37. What is the DISTINCT statement and how do you use it?
This statement is used with the SELECT statement to filter out duplicates and return only unique values from a column of a table. The syntax is:


SELECT DISTINCT col_1
FROM table_name;

38. What are entities? Give some examples.
An entity is a real-world object, creature, place, or phenomenon for which the data can be gathered and stored in a database table. Each entity corresponds to a row in a table, while the table's columns describe its properties. Some examples of entities are bank transactions, students in a school, cars sold, etc.

39. What are relationships? Give some examples.
Relationships are the connections and correlations between entities, basically meaning how two or more tables of a database are related to one another. For example, we can find an ID of the same client in a table on sales data and in a customer table.

40. What is NULL value? How is it different from zero or a blank space?
A NULL value indicates the absence of data for a certain cell of a table. Instead, zero is a valid numeric value, and an empty string is a legal string of zero length.

40 Top Intermediate SQL Interview Questions and Answers
In this section, we take a look at the 40 most popular intermediate SQL questions and answers, so that you'll know what to expect from your interviewer. These questions are more suited to SQL practitioners with a few years of experience. 

1. What is a function in SQL, and why use functions?
A database object representing a set of SQL statements frequently used for a certain task. A function takes in some input parameters, performs calculations or other manipulations on them, and returns the result. Functions help improve code readability and avoid repetition of the same code snippets.

2. What types of SQL functions do you know?
Aggregate functions – work on multiple, usually grouped records for the provided columns of a table, and return a single value (usually by group).
Scalar functions – work on each individual value and return a single value.
On the other hand, SQL functions can be built-in (defined by the system) or user-defined (created by the user for their specific needs).

3. What aggregate functions do you know?
AVG() – returns the average value
SUM() – returns the sum of values
MIN() – returns the minimum value
MAX() – returns the maximum value
COUNT() – returns the number of rows, including those with null values
FIRST() – returns the first value from a column
LAST()– returns the last value from a column

4. What scalar functions do you know?
LEN() (in other SQL flavors – LENGTH()) – returns the length of a string, including the blank spaces
UCASE() (in other SQL flavors – UPPER()) – returns a string converted to the upper case
LCASE() (in other SQL flavors – LOWER()) – returns a string converted to the lower case
INITCAP() – returns a string converted to the title case (i.e., each word of the string starts from a capital letter)
MID() (in other SQL flavors – SUBSTR()) – extracts a substring from a string
ROUND() – returns the numerical value rounded to a specified number of decimals
NOW() – returns the current date and time

5. What are case manipulation functions? Give some examples.
Case manipulation functions represent a subset of character functions, and they're used to change the case of the text data. With these functions, we can convert the data into the upper, lower, or title case.
UCASE() (in other SQL flavors – UPPER()) – returns a string converted to the upper case
LCASE() (in other SQL flavors – LOWER()) – returns a string converted to the lower case
INITCAP() – returns a string converted to the title case (i.e., each word of the string starts from a capital letter)

6. What are character manipulation functions? Give some examples.
Character manipulation functions represent a subset of character functions, and they're used to modify the text data.
CONCAT() – joins two or more string values appending the second string to the end of the first one
SUBSTR() – returns a part of a string satisfying the provided start and end points
LENGTH() (in other SQL flavors – LEN()) – returns the length of a string, including the blank spaces
REPLACE() – replaces all occurrences of a defined substring in a provided string with another substring
INSTR() – returns the numeric position of a defined substring in a provided string
LPAD() and RPAD() – return the padding of the left-side/right-side character for right-justified/left-justified value
TRIM() – removes all the defined characters, as well as white spaces, from the left, right, or both ends of a provided string

7. What is the difference between local and global variables?
Local variables can be accessed only inside the function in which they were declared. Instead, global variables, being declared outside any function, are stored in fixed memory structures and can be used throughout the entire program.

8. What is the default data ordering with the ORDER BY statement, and how do you change it?
By default, the order is ascending. To change it to descending, we need to add the DESC keyword as follows:
SELECT * FROM table_name
ORDER BY col_1 DESC;

9. What set operators do you know?
UNION – returns the records obtained by at least one of two queries (excluding duplicates)
UNION ALL – returns the records obtained by at least one of two queries (including duplicates)
INTERSECT – returns the records obtained by both queries
EXCEPT (called MINUS in MySQL and Oracle) – returns only the records obtained by the first query but not the second one

10. What operator is used in the query for pattern matching?
The LIKE operator in combination with the % and _ wildcards. The % wildcard represents any number of characters including zero, while _ – strictly one character.

11. What is the difference between a primary key and a unique key?
While both types of keys ensure unique values in a column of a table, the first one identifies uniquely each record of the table, and the second one prevents duplicates in that column.

12. What is a composite primary key?
The primary key of a table, based on multiple columns.

13. What is the order of appearance of the common statements in the SELECT query?
SELECT – FROM – JOIN – ON – WHERE – GROUP BY – HAVING – ORDER BY – LIMIT

14. In which order the interpreter executes the common statements in the SELECT query?
FROM – JOIN – ON – WHERE – GROUP BY – HAVING – SELECT – ORDER BY – LIMIT

15. What is a view, and why use it?
A virtual table containing a subset of data retrieved from one or more database tables (or other views). Views take very little space, simplify complex queries, limit access to the data for security reasons, enable data independence, and summarize data from multiple tables.

16. Can we create a view based on another view?
Yes. This is also known as nested views. However, we should avoid nesting multiple views since the code becomes difficult to read and debug.

17. Can we still use a view if the original table is deleted?
No. Any views based on that table will become invalid after deleting the base table. If we try to use such a view anyway, we'll receive an error message.

18. What types of SQL relationships do you know?
One-to-one – each record in one table corresponds to only one record in another table
One-to-many – each record in one table corresponds to several records in another table
Many-to-many – each record in both tables corresponds to several records in another table

19. What are the possible values of a BOOLEAN data field?
In some SQL flavors, such as PostgreSQL, the BOOLEAN data type exists explicitly and takes values TRUE, FALSE, or NULL. In other flavors, such as Microsoft SQL Server, the BIT datatype is used to store Boolean values as integers 1 (true) or 0 (false).

20. What is normalization in SQL, and why use it?
Normalization is a process of database design that includes organizing and restructuring data in a way to reduce data redundancy, dependency, duplication, and inconsistency. This leads to enhanced data integrity, more tables within the database, more efficient data access and security control, and greater query flexibility.

21. What is denormalization in SQL, and why use it?
Denormalization is the process opposite of normalization: it introduces data redundancy and combines data from multiple tables. Denormalization optimizes the performance of the database infrastructure in situations when read operations are more important than write operations since it helps avoid complex joins and reduces the time of query running.

22. What is the difference between renaming a column and giving an alias to it?
Renaming a column means permanently changing its actual name in the original table. Giving an alias to a column means giving it a temporary name while executing an SQL query, with the purpose to make the code more readable and compact.

23. What is the difference between nested and correlated subqueries?
A correlated subquery is an inner query nested in a bigger (outer) query that refers to the values from the outer query for its execution, meaning that a correlated subquery depends on its outer query. Instead, a non-correlated subquery doesn't rely on the data from the outer query and can be run independently of it.

24. What is the difference between clustered and non-clustered indexes?
While a clustered index defines the physical order of records of a table and performs data searching based on the key values, a non-clustered index keeps the order of records that doesn't match the physical order of the actual data on the disk. A table can have only one clustered index but many non-clustered ones.

25. What is the CASE() function?
The way to implement the if-then-else logic in SQL. This function sequentially checks the provided conditions in the WHEN clauses and returns the value from the corresponding THEN clause when the first condition is satisfied. If none of the conditions is satisfied, the function returns the value from the ELSE clause in case it's provided, otherwise, it returns NULL. The syntax is:


CASE
    WHEN condition_1 THEN value_1
    WHEN condition_2 THEN value_2
    WHEN condition_3 THEN value_3
    ...
    ELSE value
END;

26. What is the difference between the DELETE and TRUNCATE statements?
DELETE is a reversible DML (Data Manipulation Language) command used to delete one or more rows from a table based on the conditions specified in the WHERE clause. Instead, TRUNCATE is an irreversible DDL (Data Definition Language) command used to delete all rows from a table. DELETE works slower than TRUNCATE. Also, we can't use the TRUNCATE statement for a table containing a foreign key.

27. What is the difference between the DROP and TRUNCATE statements?
DROP deletes a table from the database completely, including the table structure and all the associated constraints, relationships with other tables, and access privileges. TRUNCATE deletes all rows from a table without affecting the table structure and constraints. DROP works slower than TRUNCATE. Both are irreversible DDL (Data Definition Language) commands.

28. What is the difference between the HAVING and WHERE statements?
The first one works on aggregated data after they are grouped, while the second one checks each row individually. If both statements are present in a query, they appear in the following order: WHERE – GROUP BY – HAVING. The SQL engine interprets them also in the same order.

29. How do you add a record to a table?
Using the INSERT INTO statement in combination with VALUES. The syntax is:
INSERT INTO table_name
VALUES (value_1, value_2, ...);

30. How to delete a record from a table?
Using the DELETE statement. The syntax is:
DELETE FROM table_name
WHERE condition;

In this way, we can also delete multiple records if they satisfy the provided condition.

31. How to add a column to a table?
Using the ALTER TABLE statement in combination with ADD. The syntax is:
ALTER TABLE table_name
ADD column_name datatype;

32. How to rename a column of a table?
Using the ALTER TABLE statement in combination with RENAME COLUMN ... TO ... The syntax is:
ALTER TABLE table_name
RENAME COLUMN old_column_name TO new_column_name;

33. How to delete a column from a table?
Using the ALTER TABLE statement in combination with DROP COLUMN. The syntax is:
ALTER TABLE table_name
DROP COLUMN column_name;

34. How to select all even or all odd records in a table?
By checking the remainder of the division by 2. In some SQL versions (e.g., PostgreSQL and My SQL), we use the MOD function, in the others (Microsoft SQL Server and SQLite) – the modulo operator (%). To select all even records using MOD:
SELECT * FROM table_name
WHERE MOD(ID_column, 2) = 0;

To select all even records using %:
SELECT * FROM table_name 
WHERE ID_column % 2 = 0;
To select all odd records, the syntax is identical in both cases, only that we would use the inequality operator <> instead of =.

35. How to prevent duplicate records when making a query?
Using the DISTINCT statement in combination with SELECT or creating a unique key for that table.

36. How to insert many rows in a table?
Using the INSERT INTO statement in combination with VALUES. The syntax is:
INSERT INTO table_name
VALUES (value_1, value_2, ...),
      (value_3, value_4, ...),
      (value_5, value_6, ...),
      ...;

37. How to find the nth highest value in a column of a table?
Using the OFFSET clause. For example, to find the 6th highest value from a column, we would use the following syntax:
SELECT * FROM table_name
ORDER BY column_name DESC
LIMIT 1
OFFSET 5;

38. How to find the values in a text column of a table that start with a certain letter?
Using the LIKE operator in combination with the % and _ wildcards. For example, we need to find all surnames in a table that start with "A". The query is:
SELECT * FROM table_name
WHERE surname LIKE 'A_';

Here, we assume that a surname must contain at least two letters. Without this assumption (meaning that a surname can be just A), the query is as follows:
SELECT * FROM table_name
WHERE surname LIKE 'A%';

39. How to find the last id in a table?
Using the MAX() function. Otherwise, in many SQL versions, we can use the following syntax:
SELECT id
FROM table_name
ORDER BY id DESC
LIMIT 1;

or in Microsoft SQL Server:

SELECT TOP 1 id
FROM table_name
ORDER BY id DESC

40. How to select random rows from a table?
Using the RAND() function in combination with ORDER BY and LIMIT. In some SQL flavors, such as PostgreSQL, it's called RANDOM(). For example, the following code will return five random rows from a table in MySQL:
SELECT * FROM table_name
ORDER BY RAND()
LIMIT 5;
-----------------------------------------------------------------------------------------------------------------
What are the five basic SQL commands?
The five most basic SQL commands are ALTER, UPDATE, DELETE, INSERT, and CREATE. 

How are SQL commands classified?
The SQL commands are classified into: 

Data Definition Language (DDL)
Data Manipulation Language (DML)
Data Control Language (DCL)
Transaction Control Language (TCL)
Data Query Language (DQL)

What is DBMS?
A database management system (DBMS) is a software system used to oversee the operations of a database. It helps manage the structure of the database and manipulate the data stored within it.

Define the term database.
Sql interview questions - database
A database is a repository of structured data stored in a computer system. 

What is RDBMS? Is it different from DBMS?
An RDBMS (relational database management system) is used to store, query, and manage the data in a relational database. 

An RDBMS is used to manage a relational database, which means that data can be stored only in the form of tables. This makes relational databases a more advanced and structured alternative to traditional DBMS systems. 

Define tables and fields.
When you store data that is structured in the form of rows and columns, it is known as a table. The columns that form the table are known as fields. 

How do you create a table in SQL?
Use the following command: 

CREATE TABLE
How do you delete a table in SQL?
The following command deletes a table in SQL: 

DROP TABLE

What are constraints in SQL?
Constraints are the rules that are set for the data that can be placed inside a table. It ensures that the data in a table is relevant and accurate. Here are the constraints that you can place on data in SQL: 

NOT NULL: The data in this column cannot include any null values. 

UNIQUE: Every entry in this column needs to be unique. 

PRIMARY KEY: These are columns that have data that are unique for each record in the column. 

CHECK: This constraint checks every entry in a column for a specific condition. 

FOREIGN KEY: These are columns with attributes that refer to the primary key of a different table. 

DEFAULT: This constraint sets a default value for when no value is entered. 

CREATE INDEX: This is used to create indexes in tables so that data can be retrieved quickly. 

What is a unique constraint?
Sql interview questions - unique constraint
A unique constraint implies that every value in a column should be different from every other value in that column. In other words, every value should be unique. 

How do you change a table name in SQL?
The RENAME command is used to change table names in SQL. 

Let’s say you have a table named Customers and want to change the name to New_Customers. You’d type the following command: 

Rename Customers to New_Customers
How do you delete a row in SQL?
You can use the DELETE SQL query. 

Assume that you have a table named “Cars” which has a column for serial numbers with the name “sno.” If you want to delete the row with serial number 6, then you’d use the following SQL query: 

DELETE FROM Cars
WHERE sno=6
How do you create a database in SQL?
Use the CREATE DATABASE query. If you want to create a database named StudentInfo, then type the query as follows. 

CREATE DATABASE StudentInfo
What is normalization in SQL?
Normalization is the process of eliminating redundant entries from a database. This enhances the referential integrity of the data. It also helps reduce update, deletion, and insertion anomalies. 

Define a primary key.
In a relational database, a primary key is a key for which every record has a unique value. For example, if you created a database with customers’ information, their phone number could serve as a primary key because no two people are given the same phone number. 

The database administrator determines which column needs to be chosen as the primary key based on the available data. 

Define a foreign key. 
A foreign key is a column, or multiple columns, whose data is linked in a relational database. 

Say that you have two tables—one with customer data and one with order data. You could create a foreign key relationship between a customer ID column and an order column because these two are logically linked. This maintains the referential integrity of the table and ensures that there are no redundant or repeated values. 

What is a “join” in SQL?
Sql interview questions - join in SQL
A join is a way to combine rows that are in two different columns by using a field that they have in common. 

What is the difference between a self join and a cross join?
A join SQL query combines data that is in two different rows in the same table or in rows that are in different tables. 

A self join involves joining a table with itself, which means that the rows are replicated. A cross join implies joining every row in two tables. Read more about joins here. 

Define an index, along with its different types.
An index is a table that has two columns. The first column is a duplicate of the primary key of a table. The second column has pointers to where the key value of each record is stored. 

The following are the types of indexes in SQL: 

Primary index (dense index and sparse index)
Secondary index
Clustering index 
Multi-level index
B-tree index 
Read more about indexes here. 

How do you insert a date in SQL?
Sql interview questions - insert date 
You can use the DATE command, which inserts the date in the YYYY-MM-DD format. 

Alternatively, you can use the DATETIME format, which inserts the time along with the date in the YYYY-MM-DD HH:MI:SS format. 

Define data integrity. 
The data integrity of a database refers to the accuracy and consistency of the data. It is a key feature of the design and implementation of any system used to store and retrieve data. 

What is PL/SQL?
PL/SQL is short for Procedural Language Extensions to the Structured Query Language. It gives software developers a way to combine SQL with procedural statements like the ones used in general-purpose programming languages. 

What is MySQL?
MySQL is an open-source relational database management system software. It was created by Oracle and based on SQL. 

What are the different types of relationships in SQL?
There are three main types of relationships between data values in SQL. They are: 

One-to-one relationship: This implies that a record in the first table is related to only one record in the second table. 
One-to-many relationship: In a one-to-many relationship, a record in the first table can be related to one or more records in the second table. But the records in the second table can be related only to one record in the first table. 
Many-to-many relationship: In this kind of relationship, multiple records in the first table are related to multiple records in the second table. 
Read more about relationships in SQL here. 

What is an alias in SQL?
An alias is an alternative name that is given to a table. It is only available for the duration of a specific SQL query. Aliases are created to make columns easier to refer to or to make their names more readable. 

Define query
A query is how you can request information that is stored in a database.

What is a subquery?
A subquery is a query that is nested within another query in SQL.

What do you mean by denormalization?
Denormalization is a method of optimizing databases that involves adding redundant data to the tables in the database. Read more about denormalization here.

List the various forms of normalization.
The following are the different kinds of normalization that can be carried out on a database in SQL: 

First Normal Form (1 NF)
Second Normal Form (2 NF)
Third Normal Form (3 NF)
Fourth Normal Form aka Boyce Codd Normal Form (BCNF or 4 NF)
Fifth Normal Form (5 NF)
Sixth Normal Form (6 NF)
What is ETL in SQL?
ETL is short for extract, transform and load. Each of these is a basic operation in database management combined into one ETL tool to simplify the process. Extraction involves getting data out of a database; the transform operation modifies that data; load places that data into another database. 

How do you install MySQL?
Sql interview questions - install MySQL
SQL is free to install and use. Follow the instructions laid out here to start using MySQL. 

Is there a difference between DELETE and TRUNCATE statements?
Here are the key differences:

DELETE is a DML (Data Manipulation Language) command whereas TRUNCATE is a DDL (Data Definition Language) command. 
The DELETE command deletes rows in a table based on a specific set of conditions. TRUNCATE doesn’t use any conditions and removes all the rows in a table. 
What do you mean by aggregate and scaler functions?
Aggregate functions are applied to multiple values and return a single value. Think of how the average of a set of numbers is calculated. That’s an example of an aggregate function. 

Scalar functions, on the other hand, return a single output from one input value. A function that converts a string from uppercase to lowercase would be considered a scaler function. 

What is OLTP?
Online Transaction Processing (OLTP) are software systems that are able to handle transaction-based applications. Software used to book a hotel or send money to a friend are examples of OLTP systems. Read more about OLTP here. 

What is OLAP?
Online Analytical Processing (OLAP) is a term used to describe software that extracts insights from raw data in a consistent, interactive manner. OLAP systems are often used in finance, sales, marketing, and accounting departments. 

OLTP vs. OLAP: What’s the difference?
Sql interview questions - OLTP vs OLAP
OLTP is a software application that facilitates transactions that need to be carried out in a system. OLAP is a family of applications that can be used to mine data, analyze it, and produce business intelligence. Read more about OLT and OLAP here. 

Define collation. 
Collation refers to the rules based on which the characters stored in an SQL database are encoded. This determines how the information is represented in the memory of a computer, and how data is retrieved or compared. Read more about collation here. 

What is a schema in SQL?
A schema is a logical representation of the different objects in the database. Think of it as a mapping of all the tables, functions, stored procedures, and indexes that are part of a database. Creating schemas allows you to give different users different levels of access and easily share the logical structure of the database with multiple users. Read more about schema in SQL here. 

What is a unique key in SQL?
Sql interview questions - unique key in SQL
A unique key is a constraint requiring every value in a particular column to be different from every other value in that single column. 

What does the SELECT statement do?
SELECT is the most common data manipulation language command used in SQL. It retrieves one or more rows in a table based on a certain set of conditions described by the user. 

What is a clause in SQL?
Clauses are functions built into SQL that refer to particular types of data. Here are examples of clauses in SQL: 

WHERE: Specify the conditions based on which a query returns data
OR: Used when there are multiple conditions involved and data is returned if any one of those conditions is satisfied
AND: Sets at least two conditions, both of which need to be satisfied for a value to be returned by a query 
Discuss standard clauses used with SELECT query in SQL?
These are the clauses used with a SELECT query in SQL: 

WHERE: Used to select items based on a specific set of conditions 
GROUP BY: Used to group rows whose values match that of the result set
ORDER BY: Arranges the resulting set in descending or ascending order
TOP: Sets a limit on the number of records returned by a query
HAVING: Serves the same function as the WHERE clause except that it can be used with aggregate functions 
Read more about clauses used with the SELECT query here. 

Explain UNION, MINUS, and INTERSECT commands. 
Sql interview questions - union minus and intersect
These commands are commonly applied to result sets in relational databases. Here’s what each of these commands does. 

UNION
The UNION command combines the output of two select queries into a single result, meaning that it unifies the result set from two tables, making it a binary set operator. There are two conditions that need to be fulfilled for the UNION command to work: 

The two SELECT statements in question should have the same number of fields listed in the same order. 
The data types of the fields should either be the same or compatible with each other. 
INTERSECT
INTERSECT is also a binary set operator like the UNION command, except that it outputs the rows that are in common between the results of two SELECT queries. This command always displays only distinct rows. Any duplicates that are present are ignored. 

MINUS
The MINUS command is the opposite of the INTERSECT command. When you apply MINUS to the results of two SELECT queries, it returns the rows that are in the first selection but not in the second one. 

The conditions that need to be fulfilled by the UNION command also apply to MINUS. That is, the two tables need to have the same number of fields in the same order and the data types need to be compatible. 

What is a cursor and how do you use it?
A cursor is an object that makes it possible to traverse the rows that have been produced by a query. 

These are the steps that you need to follow to use a cursor: 

Declare the cursor object along with the name of the cursor. 
Open the cursor by executing a SELECT query. 
Fetch one of the rows into one or multiple variables. 
Close the cursor and deallocate it. 
Read more about cursors in SQL here. 

Define entities and relationships. 

An entity is a real-world object, which means that it has certain attributes or properties. For example, a database could have entities like employees and department names. A relationship shows how different entities are related to each other. 

Read more about SQL entities and relationships here. 

What is pattern matching in SQL?
This is the process of identifying particular strings in a database using rules defined with regular expressions or wildcard characters. Read more about pattern matching here. 

Advanced SQL Interview Questions
What is SQL injection?
This is a code injection technique used to access unauthorized data stored in a database. An attacker exploiting an SQL injection vulnerability will often be able to view data belonging to other users in a system and in some cases even be able to modify that data. Read more about SQL injection here. 

What is a trigger in SQL?
A trigger is a specialized procedure in SQL which runs automatically when a particular event occurs or a certain condition has been met. 

For example, let’s say you want to know which of the orders coming into your store need to be fulfilled within a day. In that case, you could create a trigger that looks for one-day delivery orders and transfers their information into a new table. That way you have easy access to that data in a separate table. 

Read more about triggers in SQL. 

What is PostgreSQL?
PostgreSQL is an open-source relational database system with advanced features for enterprise use cases. It offers support for most of the popular programming languages, including Python, C, Javascript, Java, and Ruby. Read more about PostgreSQL.

How to insert multiple rows in SQL?

You can use the INSERT statement to insert multiple rows into a table in SQL. Read more about inserting rows in SQL.

How to find the nth highest salary in SQL?
There are multiple ways that you can go about finding the nth highest salary in a table that stores employee salaries. 

Below is an example of how you can use the TOP clause in SQL to write a query that returns the nth highest salary, without using a subquery. 

sql interview questions, example of how you can use the TOP clause in SQL to write a query
How do you copy a table in SQL?
You can use the SELECT INTO command to copy the contents of one table and place it into another. 

Let’s assume that you have two tables, T1 and T2, and you want to copy the contents of the former into the latter. To do this, you would type out the following query: 

SELECT * INTO T2 FROM T1; 
How to add a new column in SQL?
You can use the ALTER TABLE command to add a new column in SQL. 

Let’s say you have a table titled “Employees” and you want to add a new column titled “EmployeeID.” The following syntax is what you would use to add a new column in the “Employee” table: 

ALTER TABLE Employees
ADD EmployeeID data_type column_constraints;
Here, data_type refers to the data type you want to set for the column. That’s followed by any constraints that you want to set on the values in the column. 

Define a live lock. 
A live lock is when a table requires access to an exclusive lock, but is denied access because there are multiple overlapping shared locks. Read more about live locks. 

Define COMMIT and give an example?
COMMIT is a command used to permanently store the changes that have been made to a table. 

Let’s say you have a table that stores employee data and want to delete the data of an employee who has left the company. The syntax for that would be: 

DELETE from Employees where EmployeeName = ‘X’
If you want to save this change that you’ve made, you would use the COMMIT command, which has the following simple syntax: 

COMMIT;
What is the difference between NVL and NVL2 functions?
An NVL function requires only two parameters, whereas NVL2 functions take three parameters. 

What are the different types of SQL sandbox?
A sandbox is where you can test scripts. It gives you a safe place to try out scripts and observe the effects that they have on the database that you’re working in. 

There are three different types of sandboxes in SQL. They are: 

External access sandbox: You can access the file system and use classes, but you don’t get access to memory allocations or manipulated threads. 

Safe access sandbox: You can use commands, triggers, functions, and other basic features but you can’t access the memory or create files. 

Unsafe access sandbox: You can access the memory and have the ability to manipulate threads. 

Difference between CHAR and VARCHAR2 datatype in SQL?
CHAR is used to declare a string that has a fixed length. VARCHAR2 specifies a character string that can be of variable length. 

Difference between COALESCE & ISNULL?
The COALESCE command returns the very first non-null value that is present in the arguments that are provided to it. ISNULL provides a specific replacement value when there is a NULL value present in a table. Read more about COALESCE and NULL.

What is a deadlock?

A deadlock is a situation in which two SQL processes contend for access to resources that have been locked by the other. As a result of this, both processes cannot continue because they’re waiting for the other one to release access to the resource that it requires. SQL intervenes in this situation and kills off one process so that the deadlock doesn’t continue forever. 

Read more about deadlocks in SQL. 

What is a UNION operator?
The UNION operator is used in SQL to combine the results obtained from multiple queries into a single result set. 

What are the nonstandard string types?
The following are the nonstandard string types in SQL: 

TEXT
MEDIUMTEXT
LONGTEXT
TINYTEXT
Compare SQL vs. PL/SQL. 
The following are the differences between SQL and PL/SQL. 

SQL is a structured query language used to access the data in a database. PL/SQL is a procedural language that enhances the way in which SQL commands can be used to interact with databases. 
SQL queries execute one operation at a time whereas groups of commands can be executed in blocks in PL/SQL. 
PL/SQL supports data types and constraints on variables. SQL does not support data variables. 
SQL transacts directly with the database through commands. PL/SQL does not interact directly with the database. 
Compare MySQL vs. SQL Server. 
The following are the differences between MySQL and SQL Server: 

MySQL was developed by Oracle whereas an SQL Server is a Microsoft product. 
MySQL supports languages like Haskey and Perl. SQL Server has support for more popular modern languages like Java, Ruby, R, and C++. 
MySQL doesn’t require a large amount of space in the memory to create and run databases. SQL Server requires large volumes of operational storage space. 
MySQL is an open-source database system and is available for free use. SQL Server is a paid software. 
MySQL blocks access to the database when it is carrying out backups. This is not the case with SQL Server. 
You can manipulate files in the database while SQL Server is running. This is not possible with MySQL. 
What are the differences between NoSQL and SQL?

Here are the differences between NoSQL and SQL: 

SQL is a database management software that supports the storage and analysis of structured data. NoSQL allows you to store and retrieve structured data but also offers support for unstructured and polymorphic data. 
SQL was created in the year 1970 to deal with problems relating to file storage. NoSQL came about in the early 2000s as a way to allow databases to handle semi-structured and unstructured data. 
SQL is vertically scalable, which means that you can add resources so that the existing hardware and software can handle greater capacities. NoSQL is horizontally scalable and lets you add larger nodes to smaller nodes to enhance its capacity. 
There is no support for storing data hierarchically in SQL whereas NoSQL is especially suited to handling hierarchical data. 
SQL doesn’t support the distribution of data, which means that one installation can only run on one system. Features like partition and repetition mean that NoSQL allows data distribution. 
What are the differences between MongoDB and SQL?
Here are the major differences between MongoDB and SQL: 

SQL databases are relational in nature whereas MongoDB has non-relational databases. 
SQL uses the commands and statements in the SQL query language. MongoDB uses JSON as its query language. 
SQL is vertically scalable, whereas MongoDB is horizontally scalable. 
SQL focuses on the properties of ACID: atomicity, consistency, isolation, and durability. MongoDB emphasizes CAP properties: consistency, availability, and partition tolerance. 
What are the differences between SQL and Transact Structured Query Language (TSQL)?
Here are the key differences between SQL and TSQL: 

SQL was developed by IBM whereas TSQL was developed by Microsoft. 
SQL is used to execute one query at a time to insert, update, or delete the data in a database. TSQL makes it possible to carry out transactional activities in a database using various programmatic techniques. 
SQL is focused on manipulating the data in a database. TSQL is used to build applications and implement business logic within them. 
SQL Interview Questions for Developers
How do you find duplicate records in SQL?
You can use the GROUP BY command to find the duplicate records in a row in SQL as shown below. 

sql interview questions, group by clause
Read more about duplicate records. 

How do you delete duplicate rows in SQL?
Much like identifying duplicate rows, you can use the GROUP BY command to delete duplicate rows in SQL. To do this, delete the duplicate rows that surface when you identify the duplicates using GROUP BY. Read more about deleting rows in SQL. 

What is CASE in SQL?
The CASE command is how you use if/then logic in SQL. 

The CASE command is followed by a WHEN statement, which corresponds to the ‘if’ in if/then logic. The WHEN clause sets a condition for the query. It then moves to the THEN part of the query, which defines what occurs if the condition is satisfied. 

Read more about the use of CASE statements in SQL. 

How do you find the 2nd highest salary in a table in SQL?
You can use the following query:

sql interview questions, finding the 2nd highest salary
What is the command used to create an index in SQL?
The CREATE INDEX command can be used to create an index in SQL. Read more about creating indexes in SQL. 

How to change the column data type in SQL?
The ALTER TABLE statement can be used to change the data type of a column in SQL. 

Assume you have a table named CarData and a column called CarNames. If you wanted to change the data type of that column from char to varchar, then you’d use the following query: 

ALTER TABLE CarData

ADD CarNames varchar (100); 

How to change column names in SQL?
You can use the ALTER TABLE command to change the name of a column in SQL. The syntax for the command is as shown below: 

sql interview questions, alter table command
What is a “view” in SQL?
A view is a table that holds data from one or multiple tables in an SQL database, but doesn’t actually physically exist in the memory. In that sense, a view can be thought of as a virtual table in the database. 

Views are made up using predefined queries to gather data that exists in the database. Much like any other table, views need to be given unique names. They don’t take up any space in the memory since they don’t have a physical existence there. 

Read more about SQL views.

How do you drop a column in SQL?
Use the ALTER TABLE command. 

Let’s say you have a table named Employees and want to drop the Salary column. You would type a query out as follows: 

ALTER TABLE Employees

DROP Salary; 

How do you join rows from two tables in SQL?
You can use the JOIN statement. There are four types of joins that you can use to achieve that: 

INNER JOIN 
LEFT JOIN 
RIGHT JOIN 
FULL JOIN 
The syntax for an inner join is as shown below: 

sql interview questions, JOIN statement
Read more about joining tables. 

How to use BETWEEN in SQL?
The BETWEEN statement in SQL is used to select values that fall within a particular range. These values can be text, numbers, or dates. Read more about the BETWEEN command. 

SQL Interview Questions for Data Analysts
Define normalization. 
Normalization is the process of restructuring the data in a database so that it adheres to a certain set of rules, which are known as normal forms. This is done to improve data integrity and reduce the amount of data redundancy. 

Data redundancy is undesirable in a database for a few reasons, including: 

It is tougher to maintain a database when there are many redundant records in tables. 
Inconsistencies begin to emerge in the data. 
Updating, inserting, and deleting anomalies becomes more arduous when there is a high degree of data redundancy. 
Redundant data occupies space in the memory and increases the storage requirements of a database. 
Normalization is undertaken so that all of this can be avoided. There are three normal forms that are used to normalize databases. Let’s find out what criteria each normal form requires. 

First Normal Form
The rows and columns in the database are not ordered. 
Duplicate data is present in the database. 
The records in the intersections of rows and columns are always unique. 
There are no hidden values in any columns. 
Second Normal Form
The table must adhere to the criteria for the first normal form. 
All non-key tables should have a dependency on the PRIMARY KEY. 
All partial dependencies are transferred into a separate table. 
Third Normal Form
The table adheres to the criteria for the second normal form. 
Columns that are not the primary key columns shouldn’t have any dependencies on other non-primary key columns. 
There are no instances of transitive functional dependencies in the table. 
What does it mean to denormalize a database? 
Denormalization is the process of enhancing the performance of a database that has already undergone the normalization process. Read more about denormalization.

How do you identify duplicate email IDs in an SQL table?
You can use the following query to identify whether there are duplicate email IDs in an SQL table: 

sql interview questions, identifying duplicate email IDs
Read more about identifying duplicate entries. 

What is the difference between clustered and non-clustered indexes?
Here are the differences between clustered and non-clustered indexes in SQL: 

The main data in a clustered index is the index itself. Non-clustered indexes have only a copy of the data. 
Clustered indexes are able to store data on the disk, which non-clustered indexes cannot do. 
The records in a clustered index are physically reordered so that they match the index. In non-clustered indexes, the order within the index isn’t the same as that on the physical disk. 
Clustered indexes are faster and require less memory. Non-clustered indexes are slower and have higher memory requirements. 
What is the difference between an inner join and an outer join?
An inner join focuses on the data that two tables have in common. It is essentially the intersection of the two datasets. 

An outer join also includes the data that two tables have in common. But along with that, it also returns rows for which there is no match in the other table. 

Read more about inner and outer joins.

What is the difference between B-Tree and hash indexing in SQL?
Balanced trees, or B-trees, are used to make comparisons between columns that use the =, >, >=, <, <= operators or the BETWEEN clause. Hash indexes are used for comparisons using only the operators = or ⇔. 

Read more about B-trees and hash indexing.

What is the difference between UNION and UNION ALL?
The difference between the UNION and UNION ALL commands lies in the way they treat duplicate records. 

When you use the UNION command, it combines the data in two tables, but also eliminates duplicate data. UNION ALL doesn’t remove duplicate values and combines all of the data in the two tables. 

What do you mean by collation?

Collation refers to the rules based on which characters are encoded in an SQL database. Read more about SQL collation.

What do you mean by ACID?
ACID is an acronym that stands for atomicity, consistency, isolation, and durability. Let’s take a look at what each of these terms mean: 

Atomicity
Atomicity refers to the way all of the different operations within a command are treated. It implies that every operation is executed when it can be. If any of the operations cannot be completed, then the entire operation is rolled back. 

Consistency
The consistency property of SQL means that any transaction that needs to occur leaves the database only if it has been completed fully. If there is an error in the way the transaction occurs, then all of the changes that it affects are rolled back. Any system errors that crop up during execution will also result in the changes being negated. 

Isolation
Every transaction that occurs in SQL is independent and isolated. Any transaction that requires access to the result of another transaction can occur only after the latter has been executed to completion. This implies that you cannot perform one operation that requires data from multiple transactions parallelly. 

Durability
Durability refers to the way changes to the database are treated after a transaction has been completed. If a transaction has been fully executed, then any changes that it made to the database are permanent. This is true regardless of whether there are any system errors that occurred or abnormal behaviors in the system afterward. This property protects against data loss in the system. 

How and when do you use the GROUP BY function?
The GROUP BY command quite simply groups rows in a table that have the same values. In effect, it summarizes the data that is in the database. Read more about the GROUP BY command. 

What are the most common aggregate functions in SQL?
The most common aggregate functions that are used in SQL are: 

COUNT – Counts the number of rows in a specific table or a view
AVG – Calculates the average value from a given set of values
MAX – Identifies the maximum value in a given set of values 
MIN – Identifies the minimum value in a given set of values
SUM – Outputs the sum of a given set of values
Assume that you have a table with columns titled idnumber and employeename. The table has 100 million rows. How would you sample a random row without affecting the performance of the database?
The following query can be used to sample a random row from the given columns: 

select * from table order by rand()

Related Read: What Is Data Analytics? and What Does a Data Analyst Do?

SQL Server Interview Questions
What is an SQL server?
An SQL server is a relational database management system created by Microsoft. 

What is CTE in SQL Server?
CTE (common table expressions) is a temporary name given to the result of a query which you can then reference in an INSERT, DELETE, UPDATE, or SELECT statement. 

There are two kinds of CTEs in SQL servers. They are: 

Non-recursive CTEs: The subroutines in these CTEs are not repeated during processing. 

Recursive CTEs: These CTEs use looped procedures in their execution. 

How do you change an SQL server password?
Use the following query to change the password in an SQL server: 

sql interview questions, changing the password in an SQL server
Read more about changing the password of an SQL server. 

How do you uninstall an SQL server?
Make sure that you’ve backed up the SQL server that you’re deleting before continuing with this process. Once that’s done, follow these steps: 

Go to Settings in the start menu and select Apps. 
Enter ‘sql’ in the search box. 
Select the option which says Microsoft SQL Server along with the version number listed. 
Click Uninstall. 
Select the Remove option in the popup. 
You will now see a page with the Select Instance dropdown. Here you can select the SQL server that you want to remove. Click Next. 
You will now see the Select Features page and can select the features that you want to remove, along with that instance. 
You will now be able to review the items that you’re removing on the Ready to Remove page. 
Hit Remove to initiate the uninstallation process. 

############################################################################################################

Question 1: What is SQL?
SQL (Structured Query Language) is a standard programming language for managing and communicating with relational databases. It enables users to query data; insert, update, and delete records; create and modify database schemas, and manage access permissions.

Question 2: List the basic elements of an SQL query.
An SQL query typically contains a:

SELECT statement that retrieves data from one or more tables.
FROM clause that specifies the table(s) where the data resides.
WHERE clause (optional) that filters results based on specified criteria.
GROUP BY clause (optional) that groups results by column(s).
HAVING clause (optional) that filters grouped results.
ORDER BY clause (optional) that sorts the results in ascending (or descending) order.
Question 3: How do you select all the data from a table?
To retrieve all the data from a table, use:

SELECT *
FROM employees;
This query fetches all rows of all columns from the employees table:

SELECT *: Selects all columns from the specified table; the asterisk (*) represents all columns in a table.
FROM employees: Specifies the table from which data will be retrieved.
Question 4: How do you select certain columns from a table?
To retrieve specific columns from a table, you must list the desired column names in the SELECT statement:

SELECT first_name, last_name, department
FROM employees;
This query retrieves data only from the specified columns, providing a focused view of relevant information from the employees table.

SELECT first_name, last_name, department: This returns only the data in the first_name, last_name, and department
FROM employees: Specifies the table from which data will be retrieved.
We can also name selected columns using AS:

SELECT first_name,
last_name AS surname,
department
FROM employees;
In the query results, the last_name column will be shown as surname. You can use this to differentiate between two columns with similar names or to add more context to a column. For example, renaming the number column to part_id_number allows readers to quickly identify what kind of data is stored in that column.

Question 5: Explain the syntax of the WHERE clause.
The WHERE clause filters rows to meet specific conditions. Here is an example of its syntax:

SELECT first_name, last_name
FROM employees
WHERE department = 'Sales';
In this query, WHERE limits the results to data for employees in the Sales department.

SELECT first_name, last_name: Specifies which columns to retrieve data from.
FROM employees: Specifies the table from which data will be retrieved.
WHERE department = 'Sales': Limits the results to the employees in the Sales department.
WHERE can be applied to different data types. When filtering by numbers or dates, you can use direct comparisons or operators like <,<=,>,>=, or =.

SELECT first_name, last_name
FROM employees
WHERE salary > 50000;
When filtering NULL values, the IS NULL or IS NOT NULL operators can be used:

SELECT *
FROM employees
WHERE manager_id IS NULL;
Question 6: How do you filter query results based on multiple conditions?
To filter results based on multiple conditions, logical operators such as AND, OR, and NOT are used in the WHERE clause.

The AND operator returns rows that meet all of the specified conditions.
The OR operator returns rows that meet at least one of the specified conditions.
The NOT operator returns rows that do not meet the condition(s).
Consider the following example:

SELECT first_name, last_name
FROM employees
WHERE department = 'Sales' AND salary > 50000;
This query will only return employees who work in sales and whose salary is greater than $50,000. If the employee works in any other department or works in sales and earns less than $50,000, they won’t be shown in the results.

SELECT first_name, last_name: Determines which columns to retrieve data from.
FROM employees: Specifies the table from which data will be retrieved.
WHERE department = 'Sales' AND salary > 50000: Filters the results to include only employees from the Sales department with a higher salary.
You can combine multiple conditions using parentheses:

SELECT first_name, last_name
FROM employees
WHERE (department = 'Sales' AND salary > 50000)
  OR manager_id IS NULL;
In this query, only employees who don’t report to a manager (i.e. whose manager ID is NULL) or who work in sales and earn $50k+ will be included in the results.

Question 7: How do you filter results for a given text value?
To filter results based on a specific value in a text column, use the LIKE operator. You’ll also need the pattern matching symbols % (matches zero or more characters) and/or _ (matches any single character). Consider the following example:

SELECT product_name, description
FROM products
WHERE description LIKE '%apple%';
This query demonstrates using LIKE with pattern matching:

SELECT product_name, description: specifies which columns to retrieve data from.
FROM products: Specifies the table from which data will be retrieved.
WHERE description IS LIKE '%apple%': Filters the results to only show products that have the word "apple" in their description.
Another example could be:

SELECT *
FROM employees
WHERE first_name LIKE 'Mar_a';
Imagine you are looking for all employees named María or Maria. This query will return all employees whose first names begin with 'Mar', followed by any character in place of 'i', then an 'a'. This pattern can be used to match both 'Maria' and 'María' in a database where the name may not have the accent on the 'i'. (It would also return ‘Marta’, ‘Marla’, ‘Marja’, and any other names that fit the pattern.)

Question 8: How do you update rows in a database?
To update existing rows in a database table, use the UPDATE statement:

UPDATE employees
SET salary = 60000, department = 'Marketing'
WHERE employee_id = 101;
This query demonstrates how to update existing columns with new values for rows that satisfy the specified condition.

UPDATE employees: Specifies which table will be updated.
SET salary = 60000, department = 'Marketing': Specifies the columns and their new (updated) values.
WHERE employee_id = 101: Defines which rows will be updated – in this case, the row where the employee ID is 101. You can also use AND, OR, NOT, number filtering, etc. to specify more complex update conditions.
Question 9: How do you remove rows from a database?
To remove rows from a database table, use the DELETE FROM statement, followed by the table name and the condition indicating which rows to delete:

DELETE FROM employees
WHERE department = 'Human Resources';
This query shows how to delete rows from a database table based on a specified condition:

DELETE FROM employees: Indicates the table from which rows will be deleted.
WHERE department = 'Human Resources': Specifies the condition that determines which rows should be deleted – in this case, all employees in the Human Resources department. You can specify deletion conditions using standard WHERE
Question 10: How do you sort results from a SQL query?
Use the ORDER BY clause, followed by the column name(s) by which you want to sort the results:

SELECT product_name, price
FROM products
ORDER BY price DESC;
This query demonstrates how to sort results based on a specified column, allowing data to be presented in the desired order.

SELECT product_name, price: Determines which columns to retrieve data from.
FROM products: Defines the table where this data resides.
ORDER BY price DESC: Sorts the results (from highest to lowest, aka descending order) by the price SQL’s default sort order is ascending, with text values sorted from A to Z and numerical values sorted from lowest to highest. If DESC is not specified, the sorting will be done in ascending order.
Intermediate SQL Questions
Question 11: How do you combine data from multiple tables in one query?
SQL queries use JOIN clauses to combine results from multiple tables. JOINs allow you to retrieve data from related tables (i.e. tables with one or more columns in common) based on specific criteria. Here’s an example of JOIN:

SELECT orders.order_id, customers.customer_name
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
This query retrieves the order ID and customer name from the orders and customers tables. It joins the information where records in both tables contain a matching customer ID. For more information on how JOINs work, see An Illustrated Guide to the SQL INNER JOIN. You can find more examples of JOIN interview questions in The Top 10 SQL JOIN Interview Questions and How to Answer Them.

Question 12: Describe the JOIN types.
JOIN types include several variations, each serving a specific purpose in combining results from multiple tables:

INNER JOIN: Retrieves only records where both tables have matching values based on the specified condition.
LEFT JOIN: Returns all records from the left table and any matching records from the right table. If no match is found, NULL values are returned for the right table’s columns.
RIGHT JOIN: Returns all records from the right table and any matching records from the left table. If no match is found, NULL values are returned for the left table's columns.
FULL JOIN: Returns all records when there is a match in either the left or right tables. If no match is found, the non-matching rows are returned with NULLs.
CROSS JOIN: Returns the Cartesian product of the two tables – i.e. all possible combinations of rows.
Although a self-JOIN uses the same syntax as other JOINs, it actually involves joining a table to itself. This allows for comparisons between rows within the same table.

Question 13: Describe LEFT JOIN and the difference between LEFT JOIN and INNER JOIN.
LEFT JOIN is a type of OUTER JOIN that returns all rows from the left table plus any matching rows from the right table. If there is no match, NULL values are returned for the columns in the right table.

The main distinction between LEFT JOIN and INNER JOIN is their behavior with unmatched rows:

LEFT JOIN returns all rows from the left table, regardless of whether a match exists in the right table. If there is no match in the right table, NULL values are assigned to those columns.
INNER JOIN returns only matching rows from both tables. Unmatched rows from either table are removed from the results set.
Imagine you have a table of students’ names and another containing their grades. Using a LEFT JOIN, you'd get a list of all students – including those who have NULL grades. In contrast, an INNER JOIN would only show students who have grades, excluding records with NULL grades.

Question 14: What does GROUP BY do?
The GROUP BY clause groups rows with the same values into summary rows. It is frequently combined with aggregate functions (such as SUM(), COUNT(), and AVG()) to perform calculations on grouped data.

SELECT department, COUNT(employee_id)
FROM employees
GROUP BY department;
In this example, the query groups the rows based on the values in the department column and counts the employee_id values for each department. For more examples of similar queries, see our article Top 9 SQL GROUP BY Interview Questions.

What's your SQL level? Apply for a test.
Question 15: What are aggregate functions?
SQL aggregate functions calculate a set of values and return a single value. These functions are frequently used to summarize data and perform calculations on multiple rows.

The most common SQL aggregate functions are:

SUM(): Returns the sum of the numeric values in a set.
COUNT(): Counts the number of rows in a set, optionally including non-null values.
AVG(): Determines the average of numeric values in a set.
MIN(): Returns the set's minimum value.
MAX(): Returns the set's maximum value.
SELECT
    AVG(salary) AS avg_salary,
    COUNT(*) AS total_employees,
    MAX(age) AS max_age
FROM
    employees;
In this example, aggregate functions compute the average salary, count the total number of employees, and determine the greatest age among all employees in the employees table. Check out our SQL Aggregate Functions Cheat Sheet for more examples of these functions.

Question 16: What does HAVING do?
The HAVING clause filters the results of the GROUP BY clause. It is only used with aggregated data, allowing you to apply filtering criteria to grouped results.

Imagine you have a table of orders and you want to find the total sales amount for each customer. However, you only want to include customers with a total of $1,000 or more. This is the query you’d use:

SELECT customer_id, SUM(amount) AS total_sales
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 1000;
Here, the HAVING clause filters the groups (customers) based on the condition that the customer’s total sales amount exceeds $1,000. It is applied following the GROUP BY operation and allows you to filter the grouped results.

Question 17: What is the difference between WHERE and HAVING?
HAVING filters groups of rows and is applied after the GROUP BY statement. It is intended specifically for aggregated data and allows you to apply filtering criteria to grouped results. WHERE filters individual rows and is applied before GROUP BY.

Imagine you have a table of orders and want to calculate the total sales amount for each product, but only for products whose total sales exceed $10,000. Here's how you’d use the HAVING clause:

SELECT
    product_id,
    SUM(quantity_sold * price_per_unit) AS total_sales
FROM
    sales
GROUP BY
    product_id
HAVING
    SUM(quantity_sold * price_per_unit) > 10000;
Now consider the same scenario, but this time you only want need sales where the product’s price per unit is greater than $10 and the total sale is over $10,000. Some of this information is found in individual rows, so the rows must be filtered before grouping. We also have to filter for total sales, so the groups will be filtered too.

SELECT
    product_id,
    SUM(quantity_sold * price_per_unit) AS total_sales
FROM
    sales
WHERE
    price_per_unit > 10
GROUP BY
    product_id
HAVING
    SUM(quantity_sold * price_per_unit) > 10000;
This demonstrates how the WHERE clause filters individual rows based on conditions, whereas the HAVING clause filters groups of rows based on aggregated data. For a deeper dive into this subject, check out our article HAVING vs. WHERE in SQL: What You Should Know.

Question 18: Give an example of an SQL subquery.
A SQL subquery, also known as a nested query or inner query, is a query contained within another query. It is used in SELECT, INSERT, UPDATE, and DELETE statements to execute operations based on the results of another query. Consider the following example:

SELECT product_name
FROM products
WHERE category_id IN (SELECT category_id FROM categories WHERE category_name = 'Electronics');
In this query, the WHERE clause uses a subquery to retrieve category_id values from the categories table with the category_name 'Electronics'. The outer query then retrieves product names for electronics products based on the subquery results.

Advanced SQL Questions
Question 19: What is the difference between UNION and UNION ALL?
UNION removes duplicate rows from the combined result set. In contrast, UNION ALL keeps all rows, including duplicates.

Let's imagine we have two tables, employees and managers, both of which contain the column employee_id. We want to combine the employee IDs from the two tables.

SELECT employee_id FROM employees
UNION
SELECT employee_id FROM managers;
In this query, if employee_id appears in both employees and managers, UNION will remove the duplicate, but UNION ALL will keep both occurrences. You can read more about this in UNION vs. UNION ALL in SQL: What’s the Difference?

Question 20: What are SQL window functions and what are they used for?
SQL window functions perform calculations on a subset of table rows that are related to the current row. They are used on a window, which is a collection of rows related to the current row.

Window functions differ from GROUP BY queries because GROUP BY aggregates data based on specific columns, collapsing multiple rows into summary rows. In contrast, window functions perform calculations across a set of rows related to the current row within the query result, without collapsing the result set. You can read more in SQL Window Functions vs. GROUP BY: What’s the Difference?

To apply window functions, the OVER clause is used with the following syntax:

<function>(column) OVER (PARTITION BY partition_column ORDER BY order_column)
Where:

<function> indicates the window function being used (e.g., AVG(), SUM(), RANK()).
(column): The column or expression to which the window function is applied.
PARTITION BY partition_column: An optional clause that splits the result set into subsets based on one or more columns. The function is then applied to each partition individually.
ORDER BY order_column: An optional clause specifying the order of rows within each partition. This determines which rows appear in the window frame for each calculation.
Window functions are frequently used to compute aggregate values such as averages, totals, and counts over a set of rows. They are also used to compare values to other rows in the result set; this aids in determining rankings, row numberings, and maximum and minimum values within a window. To find out more, read When Do I Use SQL Window Functions?

Imagine we have a table called employees with the columns employee_id, department_id, and salary. We can calculate the average salary per department using the AVG() window function:

SELECT
    employee_id,
    department_id,
    salary,
    AVG(salary) OVER (PARTITION BY department_id) AS avg_salary_per_department
FROM
    employees;
SQL window functions are great for calculating aggregates over specific subsets of data – as shown in this example of calculating average salaries within departments. They are invaluable for data ranking, which can be useful in tasks like performance evaluation. These functions make it easier to perform analytical comparisons and identify trends, such as in  quarterly revenue. We'll look at more examples in the following questions.

Question 21: How do you rank rows in SQL?
To rank rows in SQL, use the window functions RANK(), DENSE_RANK(), PERCENT_RANK() and ROW_NUMBER(). These functions assign a rank or row number to each row in the result set based on predefined criteria:

RANK(): Assigns a unique rank to each distinct row. Rows with the same value receive the same rank, but there are gaps in the ranking (e.g. 1,2,3,3,5).
DENSE_RANK(): Also assigns a unique rank to each row and gives tied rows the same rank, but it eliminates gaps in the ranking sequence. Instead, it assigns the next consecutive rank to the row following the tied rows (e.g. 1,2,3,3,4).
PERCENT_RANK() returns the ranking for each row in the partition/result set as a percentile (from 0 to 1).
ROW_NUMBER() assigns a unique row number to each row in the result set, regardless of duplicates or tie values.
Read our Overview of Ranking Functions in SQL for more differences between these functions.

Imagine we have a table called employees with the columns employee_id, employee_name, and salary. We can rank the employees based on their salary in descending order using the RANK() window function:

SELECT
    employee_id,
    employee_name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM
    employees;
This query returns employee IDs, names, and salaries from the employees table. It then ranks each employee according to their salary, with higher salaries receiving lower ranks. The result includes the original columns as well as a new column, salary_rank, which indicates each employee's salary rank.

Question 22: What is a CTE? When do you use it?
A CTE, or common table expression, is a temporary named result set that can be used in a SELECT, INSERT, UPDATE, or DELETE statement. It allows you to divide complex queries into manageable and reusable chunks.

A CTE, introduced with the WITH keyword, allows you to create a temporary table-like structure that exists only during query execution. The temporary table can then be referred to in the same query. CTEs are especially useful for breaking down complex computations into multiple steps; this improves code organization and enables code reuse.

Assume we have a table called employees with the columns employee_id, employee_name, and salary. We can create a CTE to select high-paid employees who earn more than $100,000:

WITH high_paid_employees AS (
  SELECT
      employee_id,
      employee_name,
      salary
  FROM
      employees
  WHERE
      salary > 100000
)
SELECT
    *
FROM
    high_paid_employees;
Question 23: What is a running total and how do you compute it in SQL?
A running total, also known as a cumulative sum, is the sum of a value over a set of rows in a particular order. In SQL, a running total can be calculated using SUM() and the OVER() clause.

The following query computes the running total of order_amount over all rows in the orders table sorted by order_date:

SELECT
    order_date,
    order_amount,
    SUM(order_amount) OVER (ORDER BY order_date) AS running_total
FROM
    orders;
Question 24: What is a moving average and how do you compute it in SQL?
A moving average represents the average of a set of values over a set of times, where the window "moves" along the data set. In SQL, you can compute a moving average using AVG() with OVER() and specifying a window frame.

The following query calculates the moving average of value for the current row and the two preceding rows, ordered by date.

SELECT
    date,
    value,
    AVG(value) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_average
FROM
    dataset;
Question 25: How do you compute the year-to-year difference in SQL?
To calculate the year-to-year difference in SQL, use functions like LAG() to compare values between consecutive rows.

The following query calculates the year-to-year difference in revenue by subtracting the current year's revenue from the previous year's revenue:

SELECT
    year,
    revenue,
    revenue - LAG(revenue, 1) OVER (ORDER BY year) AS year_to_year_difference
FROM
    yearly_revenue;
	
#######################################################################################################



Let’s attack these questions frontally, without further ado!

What Is a JOIN in SQL?
What Is the Difference Between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN?
What Is a CROSS JOIN?
What Is a Self-Join in SQL?
Join Two Tables Using a Two-Column JOIN
Join Two Tables Using a Non-Equi Join
What Does DISTINCT Do?
What Does GROUP BY Do in SQL?
How Do You Filter GROUP BY Groups?
What’s the Difference Between WHERE and HAVING?
What Will the Following Query Attempting to Filter NULLs Return?
Write a Query That Finds the Number of Songs by Artist. Use LEFT JOIN and COUNT().
What’s the Difference Between JOIN and UNION?
What’s the Difference Between UNION and UNION ALL?
What Is a Subquery in SQL?
Write a Query to Return Salespersons and Their Monthly Sales Data Above Their Personal Sales Average. Use a Correlated Subquery. 
What Are Window Functions in SQL?
What’s the Difference Between Window Functions and GROUP BY?
What Window Functions Do You Know?
How Do You Create a Ranking in SQL?
What’s the Difference Between RANK() and DENSE_RANK()?
Find the Top n Rows in SQL Using a Window Function and a CTE.
Compute the Difference Between Two Rows (Delta) Using Window Functions
Use Window Functions to Compute a Running Total
Find a Moving Average Using Window Functions
What’s the Difference Between ROWS and RANGE?
Use a Recursive Query to Find all Employees Under a Given Manager.
1.  What Is a JOIN in SQL?
JOIN is an SQL command that allows you to combine two or more tables. This is done via a common column (i.e. a column that has the same values in both tables), which allows using data from two or more tables at the same time. Joining tables in SQL is essential due to the nature of relational databases: data is atomized into tables, with each table holding only a part of the data available in the database.

We’ll use two tables to showcase how this works. The first table is football_players.

id	first_name	last_name	national_team_id	games_played
1	Gianfranco	Zola		1					35
2	Virgil		van Dijk	2					53
3	Marcus		Rashford	3					51
4	Kylian		Mbappé		5					66
5	Phil		Foden		3					22
6	Frenkie		de Jong		2					22
7	Mario		Balotelli	1					36
8	Erling		Haaland		6					23
The second is national_team.

id	country
1	Italy
2	Netherlands
3	England
4	Croatia
Here’s a query that joins two tables:

SELECT
  fp.id,
  first_name,
  last_name,
  national_team_id,
  country,
  games_played
FROM football_players fp
JOIN national_team nt
ON fp.national_team_id = nt.id
ORDER BY fp.id;
It selects columns from both tables. To join them, we first reference one table in the FROM clause. This is followed by JOIN, and after that comes the second table. We use the ON clause to specify the condition with which the tables will be joined: the national_team_id in the football_players table must be equal to the id column in the national_team table.

The output of the query is:

id	first_name	last_name	national_team_id	country		games_played
1	Gianfranco	Zola		1					Italy		35
2	Virgil		van Dijk	2					Netherlands	53
3	Marcus		Rashford	3					England		51
5	Phil		Foden		3					England		22
6	Frenkie		de Jong		2					Netherlands	22
7	Mario		Balotelli	1					Italy		36
INNER JOIN is one of the several distinct joins in SQL. Its characteristic is that it only returns data from the joined tables where the joining condition is true. Here are more details on how the SQL INNER JOIN works. 

2.  What Is the Difference Between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN?
There are different types of joins in SQL. The most commonly used joins are INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.  LEFT JOIN, RIGHT JOIN, and FULL JOIN are so-called outer joins. JOIN (aka INNER JOIN) is an inner join. In this case, ‘inner’ means that it returns only the rows from both tables that satisfy the joining condition; outer joins return all the rows in one table, plus matching rows in the other table(s). The exception is FULL JOIN, which returns all rows from both tables.

Here’s the result of the INNER JOIN from the previous example. Let’s have it here again. That way, it’ll be easier to see the difference between different joins. 

id	first_name	last_name	national_team_id	country		games_played
1	Gianfranco	Zola		1					Italy		35
2	Virgil		van Dijk	2					Netherlands	53
3	Marcus		Rashford	3					England		51
5	Phil		Foden		3					England		22
6	Frenkie		de Jong		2					Netherlands	22
7	Mario		Balotelli	1					Italy		36
LEFT JOIN returns all the data from the left table (i.e. the first table, which is listed before\to the left of the JOIN keyword) and only the matching rows from the right table (the second table, listed after/to the right of the JOIN keyword). If there is no matching data in the right table, the missing values are shown as NULLs. Here’s the same query with LEFT JOIN substituting for INNER JOIN:

SELECT
  fp.id,
  first_name,
  last_name,
  national_team_id,
  country,
  games_played
FROM football_players fp
LEFT JOIN national_team nt
ON fp.national_team_id = nt.id
ORDER BY fp.id;
The left table here is football_players, and the right is national_team. As you’d expect, the output is different:

id	first_name	last_name	national_team_id	country		games_played
1	Gianfranco	Zola		1					Italy		35
2	Virgil		van Dijk	2					Netherlands	53
3	Marcus		Rashford	3					England		51
4	Kylian		Mbappé		5					NULL		66
5	Phil		Foden		3					England		22
6	Frenkie		de Jong		2					Netherlands	22
7	Mario		Balotelli	1					Italy		36
8	Erling		Haaland		6					NULL		23
All the football players from the left table are here. However, Kylian Mbappe and Erling Haaland don’t have a matching country in the right table, so there are NULLs in the country column for those players. These rows were not present in the INNER JOIN result. They were added by the LEFT JOIN.

The RIGHT JOIN does the opposite: it returns all the data from the right table and only the matching data from the left table. When there is no matching data in the left table, the missing values are shown as NULLs.

Here’s the code:

SELECT
  fp.id,
  first_name,
  last_name,
  national_team_id,
  country,
  games_played
FROM football_players fp
RIGHT JOIN national_team nt
ON fp.national_team_id = nt.id
ORDER BY fp.id;
Everything stays the same, except we’re using RIGHT JOIN instead of LEFT JOIN. This is the output:

id	first_name	last_name	national_team_id	country	games_played
1	Gianfranco	Zola	1	Italy	35
2	Virgil	van Dijk	2	Netherlands	53
3	Marcus	Rashford	3	England	51
5	Phil	Foden	3	England	22
6	Frenkie	de Jong	2	Netherlands	22
7	Mario	Balotelli	1	Italy	36
NULL	NULL	NULL	NULL	Croatia	NULL
We now have all the national teams and their players. But you can see there’s one country (Croatia) that has no players in the left table. The player columns for Croatia are filled with NULLs.

FULL JOIN outputs all the data from all the joined tables. Again, if there is no matching data in the corresponding table, the missing values will appear as NULL.

Once again, we change the join type in the query:

SELECT
  fp.id,
  first_name,
  last_name,
  national_team_id,
  country,
  games_played
FROM football_players fp
FULL JOIN national_team nt
ON fp.national_team_id = nt.id
ORDER BY fp.id;
It will return all data from both tables. Any non-matching data is replaced by NULLs. All players are in the result, even if they don’t have a corresponding country in the other table. All countries are in the result, even if they don’t have players in the football_player table. The FULL JOIN result is the union of LEFT JOIN and RIGHT JOIN:

id	first_name	last_name	national_team_id	country		games_played
1	Gianfranco	Zola		1					Italy		35
2	Virgil		van Dijk	2					Netherlands	53
3	Marcus		Rashford	3					England		51
4	Kylian		Mbappé		5					NULL		66
5	Phil		Foden		3					England		22
6	Frenkie		de Jong		2					Netherlands	22
7	Mario		Balotelli	1					Italy		36
8	Erling		Haaland		6					NULL		23
NULL	NULL	NULL	NULL					Croatia		NULL
You can find more info in the article about different JOIN types. You can also see our SQL JOINs Cheat Sheet for a quick refresher.

Earth Day Sale. -75% OFF. All 60+ SQL Courses in One Package. Check now.
3.  What Is a CROSS JOIN?
A CROSS JOIN is another join type available in SQL. It returns a Cartesian product. This means that CROSS JOIN will return each row from the first table combined with each row from the second table.

It is not used very often. But if you’re tempted to use it, think twice. Returning all the row combinations might take some time – if the query finishes at all!

As an example, let’s use the tables as in the previous two questions. To write the query, use the CROSS JOIN keyword. Since this is a join type that returns all the row combinations from all tables, there’s no ON clause. Have a look:

SELECT
  fp.id,
  first_name,
  last_name,
  national_team_id,
  country,
  games_played
FROM football_players fp
CROSS JOIN national_team nt;
Here’s the output. All players in the football_players table are listed with all countries in the national_team table.

id	first_name	last_name	national_team_id	country		games_played
1	Gianfranco	Zola		1					Italy		35
2	Virgil		van Dijk	2					Italy		53
3	Marcus		Rashford	3					Italy		51
4	Kylian		Mbappé		5					Italy		66
5	Phil		Foden		3					Italy		22
6	Frenkie		de Jong		2					Italy		22
7	Mario		Balotelli	1					Italy		36
8	Erling		Haaland		6					Italy		23
1	Gianfranco	Zola		1					Netherlands	35
2	Virgil		van Dijk	2					Netherlands	53
3	Marcus		Rashford	3					Netherlands	51
4	Kylian		Mbappé		5					Netherlands	66
5	Phil		Foden		3					Netherlands	22
6	Frenkie		de Jong		2					Netherlands	22
7	Mario		Balotelli	1					Netherlands	36
8	Erling		Haaland		6					Netherlands	23
1	Gianfranco	Zola		1					England		35
2	Virgil		van Dijk	2					England		53
3	Marcus		Rashford	3					England		51
4	Kylian		Mbappé		5					England		66
5	Phil		Foden		3					England		22
6	Frenkie		de Jong		2					England		22
7	Mario		Balotelli	1					England		36
8	Erling		Haaland		6					England		23
1	Gianfranco	Zola		1					Croatia		35
2	Virgil		van Dijk	2					Croatia		53
3	Marcus		Rashford	3					Croatia		51
4	Kylian		Mbappé		5					Croatia		66
5	Phil		Foden		3					Croatia		22
6	Frenkie		de Jong		2					Croatia		22
7	Mario		Balotelli	1					Croatia		36
8	Erling		Haaland		6					Croatia		23
You can learn more about the CROSS JOIN in this illustrated guide to the SQL CROSS JOIN.

4.  What Is a Self-Join in SQL?
As you probably suspect, a self-join occurs when the table is joined with itself. It’s important to note that it’s not a distinct command in SQL: any JOIN type can be used to join a table with itself.

The joining is done like any other JOIN, but this time you’ll reference the same table on both sides of the JOIN keyword. Self-joining is especially useful when a table has a foreign key referencing its primary key. This lets you query hierarchical data, such as family trees or a company’s organizational hierarchy. It’s also helpful when you want to find pairs of values. In the example below, we are looking for players from the same national team:

SELECT
  fp1.id,
  fp1.first_name,
  fp1.last_name,
  fp1.national_team_id,
  fp2.id AS id_2,
  fp2.first_name AS first_name_2,
  fp2.last_name AS last_name_2,
  fp2.national_team_id as national_team_id_2
FROM football_players fp1
JOIN football_players fp2
ON fp1.id <> fp2.id
AND fp1.national_team_id = fp2.national_team_id;
Self-joining means instead of two tables, you’re specifying the same table twice: once in the FROM clause and once after the JOIN clause. Since you’re using the same table twice, you must use aliases for the tables. Each occurrence of the table should be given a distinct alias (fp1, fp2 in our query) so that it is clear which occurrence of the table we’re referring to.

We’re joining players from the same national team (their national_team_id values are equal). However, we don’t want to list a player with himself, so we exclude the case when fp1.id and fp2.id are equal.

The query’s output is this:

id	first_name	last_name	national_team_id	id_2	first_name_2	last_name_2	national_team_id_2
1	Gianfranco	Zola	1	7	Mario	Balotelli	1
2	Virgil	van Dijk	2	6	Frenkie	de Jong	2
3	Marcus	Rashford	3	5	Phil	Foden	3
5	Phil	Foden	3	3	Marcus	Rashford	3
6	Frenkie	de Jong	2	2	Virgil	van Dijk	2
7	Mario	Balotelli	1	1	Gianfranco	Zola	1
You can use the national_team_id columns from both tables to confirm that, really, Gianfranco Zola and Mario Balotelli played for the same team.

You can learn more about this in our article on self-join examples.

5.  Join Two Tables Using a Two-Column JOIN
You’re given two tables. The first one is employee, which has the following data:

id	first_name	last_name
1	Steve	Bergman
2	Steve	Johnson
3	Steve	King
The second table is customer, which has the following data:

id	first_name	last_name
1	Ann	Coleman
2	Steve	Bergman
3	Steve	Young
4	Donna	Winter
5	Steve	King
Your task is to return all the employees that are also the company’s customers. Unfortunately, you can’t use the id column because it’s the employee ID in one table and the customer ID in another. In other words, there’s no single column in one table that references the other.

The solution is to join tables on the first and last name, i.e. to use a two-column JOIN.

The code below will first join the tables on the first name. After that, the keyword AND sets the second joining condition, which is the last name. That way, you’ll get data from both tables where the first name/last name combination is the same. If we used only one of these columns, we could’ve gotten the wrong data because employees and customers can have the same first name but different surnames (or vice versa). Here’s the query:

SELECT
  e.first_name,
  e.last_name
FROM employee e
JOIN customer c
ON e.first_name = c.first_name
AND e.last_name = c.last_name;
Here’s the code output.:

first_name	last_name
Steve	Bergman
Steve	King
The result shows that Steve Bergman and Steve King are both the company’s employees and customers.

6.  Join Two Tables Using a Non-Equi Join
Up till now, we’ve been using equi-joins: joins where there’s an equality sign in the ON condition. Conversely, the non-equi join is a join that has a non-equality condition in the ON clause.

This time, we have data on mobile users and their data usage. The first table is mobile_user, which shows mobile users and their monthly mobile data limit in MB:

id	first_name	last_name	mobile_data_limit
1	Michael	Watson	5,000
2	Nicole	Gomez	10,000
3	Sam	Stone	8,000
The second table is data_usage, which shows the user's actual monthly data usage in MB:

id	mobile_user_id	data_used	period
1	1	4,987	2022_10
2	2	6,875	2022_10
3	3	12,547	2022_10
4	1	5,037	2022_11
5	2	11,111	2022_11
6	3	4,897	2022_11
The task is to find all the data where the actual usage was above the monthly limit. We want to see the user’s first and last name, monthly limit, actual data used, and the time period.

The solution is to use the non-equi join, as shown below:

SELECT
  first_name,
  last_name,
  mobile_data_limit,
  data_used,
  period
FROM mobile_user mu
JOIN data_usage du
ON mu.id = du.mobile_user_id
AND mobile_data_limit < data_used;
The query selects all the required info from two tables. The tables are joined using an INNER JOIN. We first join them where the user ID is the same. Then, we add the second condition after the AND keyword. Here we have a non-equality condition that will get us data where the limit is below the monthly usage.

You can see the result below:

first_name	last_name	mobile_data_limit	data_used	period
Sam	Stone	8,000	12,547	2022_10
Michael	Watson	5,000	5,037	2022_11
Nicole	Gomez	10,000	11,111	2022_11
If you’re interested, here are some more non-equi join examples.

7.  What Does DISTINCT Do?
DISTINCT’s purpose, in general, is to remove duplicate values. Or, put another way, to show unique values in your query’s output.

Imagine you’re working with this loans table that shows loan IDs and their durations in months.

loan_id	loan_duration
100112	60
100205	60
100208	48
100333	120
100357	48
100398	120
Different loans can have the same duration, so you want to extract the list of possible loan durations. You can do this by using DISTINCT:

SELECT DISTINCT loan_duration
FROM loans
ORDER BY loan_duration;
The output shows there are loans with durations of 48, 60, and 120 months:

loan_duration
48
60
120
DISTINCT  can be used in SELECT with one column to show only the unique values of that column, as in the above example. If it’s used in SELECT but with multiple columns, then the output will show the unique combinations of all these columns.

You can also use DISTINCT with aggregate functions. If you do that, your query will eliminate duplicate aggregation results.

You can see examples of these usages in our article talking about the role of DISTINCT in SQL.

8.  What Does GROUP BY Do in SQL?
GROUP BY is an SQL clause used for arranging data into groups based on a common value or values. It is most commonly used with aggregate functions; this combination will return aggregated data for every group. However, it’s important to know that using aggregate functions within the GROUP BY clause is not allowed.

The general GROUP BY syntax is:

SELECT
  column_1,
  column_2,
  …,
FROM table_name
WHERE …
GROUP BY column_1, column_2
HAVING …
ORDER BY column_1, column_2;
Suppose there’s the table salaries:

id	first_name	last_name	salary	department
1	Nicholas	Poirot	4,798.44	IT
2	Samantha	Wolf	5,419.24	IT
3	Stewart	Johnsons	5,419.24	IT
4	Jackie	Biden	8,474.54	Sales
5	Mark	Hamilton	10,574.84	Sales
6	Mariana	Costa	9,747.54	Sales
7	Paul	Stewart	3,498.12	Accounting
8	Mary	Rutte	4,187.23	Accounting
9	Thomas	Schwarz	3,748.55	Accounting
We’ll use GROUP BY and AVG() to find the average salary by department:

SELECT
  department,
  AVG(salary) AS average_salary
FROM salaries
GROUP BY department;
We want to see the departments, so we select this column. To calculate the average salary, we apply the AVG() function to the column salary.

All the columns listed in GROUP BY define the data groups. In our example, the groups are defined by the department column: we calculate the average salary for each department.

Our data grouping and aggregation looks like this:

department	average_salary
Accounting	3,811.30
Sales	9,598.97
IT	5,212.31
The average salary in Accounting is 3,811.30. The average salaries in the other two departments are 9,598.97 and 5,212.31, respectively.

When writing a query, GROUP BY always has to come after WHERE but before the HAVING clause. You can learn more about it in this article about GROUP BY in SQL.

9.  How Do You Filter GROUP BY Groups?
Once you get the groups you specified in GROUP BY, sometimes you’ll want to filter them. The clue to doing that lies in the syntax from the previous question. The clause that allows you to filter groups is HAVING.

After the filtering criteria are specified in HAVING, the query will return all the data that satisfies the criteria. All other data will be filtered out.

What's your SQL level? Apply for a test.
Here’s how it works on the data from the previous question if we had to show only departments with an average salary below 5.500 dollars.

SELECT
  department,
  AVG(salary) AS average_salary
FROM salaries
GROUP BY department
HAVING AVG(salary) < 5500;
The code is very similar to the one in the previous question. The difference is the HAVING clause. We use it to filter the results and show only departments with salaries below 5,500.

Here’s what the code returns:

department	average_salary
Accounting	3,811.30
IT	5,212.31
The department missing from the output is Sales because its average salary is 9,598.97.

You can find additional practical examples of this clause in this article explaining HAVING in SQL. 

10.  What’s the Difference Between WHERE and HAVING?
If you know the answers to the previous two questions, you probably know the answer to this question.

The main difference is that WHERE is used for filtering data before it’s grouped. Its position in the SELECT statement shows this: it comes before GROUP BY. Due to its purpose, no aggregate functions are allowed in WHERE.

HAVING, on the contrary, is used to filter data after grouping; that’s why it is used after GROUP BY. Also, HAVING allows conditions that include aggregate functions.

The best way to learn the distinction is to read this article on WHERE vs. HAVING in SQL.

11.  What Will the Following Query Attempting to Filter NULLs Return?
You’ll often get this type of question at your advanced SQL interview: you’ll be given a code and have to describe the query's return. While writing and reading SQL code go hand-in-hand, it still feels different when you have to analyze the code someone else wrote.

You have data in the table contributors:

id	first_name	last_name	start_date	termination_date
1	Valeria	Bogdanov	2022-10-11	NULL
2	Nicholas	Bertolucci	2022-04-07	2022-11-11
3	Mathilde	Bauman	2022-05-25	2022-10-01
4	Trevor	Trucks	2022-01-28	NULL
5	Maria	Szabo	2022-03-15	NULL
What will this code return?

SELECT
  first_name,
  last_name,
  start_date,
  termination_date
FROM contributors
WHERE termination_date != '2022-10-01';
If you answer that it will return all rows except ID = 3, you’re wrong! This is a kind of trick question. When reading the WHERE condition, you could read it as: return all the data where the termination date is different from 2022-10-01. By looking at the table, you would think it’s all rows except one.

It is, but not for SQL! As you can see, there are three rows with NULL values. For SQL, NULL doesn’t equal a value; it’s a non-value. So when you set up the condition in WHERE like that, you will be excluding all dates that are not equal to 2022-10-01 and NULL values.

Here’s the output as proof:

first_name	last_name	start_date	termination_date
Nicholas	Bertolucci	2022-04-07	2022-11-11
You can learn more about this and other comparison operators used with NULL.

12.  Write a Query That Finds the Number of Songs by Artist. Use LEFT JOIN and COUNT().
Suppose you’re given two tables: artist and song.

Here’s the artist data:

id	artist_name
1	Prince
2	Jimi Hendrix
3	Santana
4	Otis Redding
5	Lou Rawls
Below is the song data:

id	artist_id	song_title
1	1	Purple Rain
2	2	Purple Haze
3	3	Europa
4	1	Cream
5	1	Bambi
6	1	Why You Wanna Treat Me So Bad?
7	2	Spanish Castle Magic
8	3	Taboo
9	3	Incident at Neshabur
10	3	Flor D' Luna
You need to use LEFT JOIN and COUNT() to find all the artists, their IDs, and the number of their songs in the database.

You could be tempted to suggest this solution:

SELECT
  a.id,
  artist_name,
  COUNT(*) AS number_of_songs
FROM artist a
LEFT JOIN song s
ON a.id = s.artist_id
GROUP BY a.id, artist_name
ORDER BY a.id;
Let’s take a look at the output:

id	artist_name	number_of_songs
1	Prince	4
2	Jimi Hendrix	2
3	Santana	4
4	Otis Redding	1
5	Lou Rawls	1
The output shows all the artists; that’s OK. However, the number of songs for Otis Redding and Lou Rawls is one, which is wrong! Take a look at the table song, and you’ll see there are no artist IDs equal to 4 or 5.

What went wrong? When using COUNT(*) with LEFT JOIN, the aggregate function will count all the non-matched values (NULLs). That’s why the result showed one song each for Otis Redding and Lou Rawls, even though they have no songs in the table.

COUNT(*) is used to count all the rows. To give a correct answer, you should use COUNT(song_title) instead.

SELECT
  a.id,
  artist_name,
  COUNT(song_title) AS number_of_songs
FROM artist a
LEFT JOIN song s
ON a.id = s.artist_id
GROUP BY a.id, artist_name
ORDER BY a.id;
This code will give you the right output:

id	artist_name	number_of_songs
1	Prince	4
2	Jimi Hendrix	2
3	Santana	4
4	Otis Redding	0
5	Lou Rawls	0
The number of songs by Prince, Jimi Hendrix, and Santana stayed the same as in the previous output. However, the number of songs by the other two artists is now zero, and that’s the correct count.

13.  What’s the Difference Between JOIN and UNION?
JOIN is an SQL clause used for joining two or more tables. It allows using data from all the joined tables. In other words, columns from all tables are shown next to each other, meaning data is stacked horizontally.

UNION is a set operator used for combining the results of two or more SELECT statements. Data is stacked vertically. One of the requirements when using UNION is there has to be an equal number of columns in all unionized SELECT statements. Also, all the selected columns have to be of the same data type. 

14.  What’s the Difference Between UNION and UNION ALL?
What they have in common is that both are set operators. Also, both operators are used for the same purpose: merging data from two or more SELECT statements.

The requirements regarding the number of columns and their data type are also the same.

Now, the difference is that UNION returns only unique records. On the other hand, UNION ALL returns all the records, which includes duplicates.

Usually, UNION ALL is faster because it doesn’t sort the result to remove the duplicates. The rule of thumb is to use UNION ALL by default. Use UNION only if you need unique results or you’re absolutely sure your query won’t return duplicate data.

You can learn more about their syntax and use in this article about the differences between UNION and UNION ALL.

15.  What Is a Subquery in SQL?
A subquery is a query written inside another SQL query. The ‘another’ query is called the main query, while a subquery is sometimes also called a nested query.

Subqueries can be used in the SELECT, INSERT, UPDATE, and DELETE statements. They can also be used in clauses like FROM or WHERE, which is the most common use.

Here’s an example. The table is products, and it stores information on product names, quantities, and categories:

id	product_name	quantity	product_category
1	Apple MacBook Air (2020) MGN63N/A Space Gray	319	Laptop
2	Fairphone 4 128GB Green 5G	208	Mobile phone
3	Apple iMac 24" (2021) 16GB/512GB Apple M1 with 8 core GPU Silver	157	Desktop
4	HP 17-cp0971nd	487	Laptop
5	Huawei P30 Pro - 128GB - Blue	148	Mobile phone
6	Lenovo Legion T5 - AMD Ryzen 9 - 32 GB - 2TB HDD+SSD - Windows 10 Home PC	514	Desktop
7	Toshiba Dynabook Satellite Pro E10-S-101 Notebook	207	Laptop
8	Samsung Galaxy S23 5G - 256GB - Phantom Black	56	Mobile phone
9	Intel Compleet PC | Intel Core i7-10700	459	Desktop
We’ll use a subquery and show the total quantity by product category, but only for the individual products whose quantity is above the average quantity for all products.

Here’s the solution:

SELECT
  product_category,
  SUM(quantity) AS product_quantity
FROM products
WHERE quantity > (SELECT AVG(quantity)
            FROM products)
GROUP BY product_category;
The query selects the product category and sums the quantity using the SUM() aggregate function. There’s a condition in WHERE that says only those individual products with a quantity above the average will be included in the sum. We use the subquery and the AVG() function to get this average.

The query returns two rows:

product_category	product_quantity
Laptop	806
Desktop	973
One category is missing because it doesn’t satisfy the filtering criteria – mobile phones.

There are different types of subqueries, such as scalar, multiple-row, and correlated queries. You can learn more about them in our article on subquery types.

Earth Day Sale. -75% OFF. All 60+ SQL Courses in One Package. Check now.
16.  Write a Query to Return Salespersons and Their Monthly Sales Data Above Their Personal Sales Average. Use a Correlated Subquery. 
A correlated subquery is a type of subquery that uses values from the outer query. It is checked once for each row the outer query returns, which can slow performance.

However, the question insists on using it, so let’s see the data.

The first table is salesperson:

id	first_name	last_name
1	Nina	Lee
2	Carolina	Green
3	Mick	Johnson
The other table is sales:

id	salesperson_id	monthly_sales	period
1	1	1,200.47	2021_10
2	2	5,487.22	2021_10
3	3	700.47	2021_10
4	1	15,747.54	2021_11
5	2	16,700.87	2021_11
5	3	14,322.87	2021_11
6	1	9,745.55	2021_12
7	2	9,600.97	2021_12
8	3	6,749.58	2021_12
Your task is to use a correlated subquery and return the salesperson’s full name, their monthly sales, and the periods where their sales are above their personal average.

Here’s the solution:

SELECT
  first_name,
  last_name,
  monthly_sales,
  period
FROM salesperson sp
JOIN sales s
ON sp.id = s.salesperson_id
WHERE monthly_sales >
   (SELECT AVG(monthly_sales)
    FROM sales
    WHERE salesperson_id = sp.id);
The query selects all the required columns. This data is from both tables, so we joined them.

Now comes the crucial part. To filter data, we use the WHERE clause. The condition says the query should return all data where monthly sales are higher than each salesperson’s average sales. How do we calculate these individual average sales? By using the AVG() function in the subquery that we write in the WHERE clause.

Here’s the output:

first_name	last_name	monthly_sales	period
Nina	Lee	15,747.54	2021_11
Carolina	Green	16,700.87	2021_11
Mick	Johnson	14,322.87	2021_11
Nina	Lee	9,745.55	2021_12
There are some more examples in this article on correlated subqueries.

17.  What Are Window Functions in SQL?
SQL window functions get their name from the fact they are applied to a data window. This window is simply a set of rows related to the current row.

Window functions are initiated by the OVER() clause. Another important clause is PARTITION BY, which defines data partitions within a window frame. When this clause is omitted, the partition is the entire result table. When PARTITION BY is used, you can define one or more columns by which data will be partitioned. You can look at it as GROUP BY for window functions.

Another important clause is ORDER BY. It sorts data within the window. In the context of window functions, this clause gives instructions on the order in which the function will be executed.

To learn more, refer to this window functions article.

18.  What’s the Difference Between Window Functions and GROUP BY?
The only similarity they share is that both GROUP BY and window functions can be – and very often are – used with the aggregate functions, and they both work on a set of rows.

However, when using GROUP BY, the output is shown as groups, and you can’t see the individual rows forming the group.

Window functions don’t have such problems. One of their characteristics is that they don’t collapse the individual rows when showing aggregated data. This means it’s possible to show aggregated and non-aggregated data simultaneously.

Window functions are used for more than data aggregation, as you’ll see in the following question. But if you want to know more about the current topic, we have an article that explains window functions vs. GROUP BY.

19.  What Window Functions Do You Know?
SQL window functions can be generally divided into four categories:

Ranking Functions
Distribution Functions
Analytic Functions
Aggregate Functions
The ranking functions are:

ROW_NUMBER() – Returns a unique number for each row within a partition; tied values have different row numbers.
RANK() – Ranks data within a partition; tied values have the same rank, and there’s a gap following ties (e.g. 1, 2, 3, 3, 5).
DENSE_RANK() – Ranks data within a partition; tied values have the same rank and there’s no ranking gap (e.g. 1, 2, 3, 3, 4).
The distribution functions are:

PERCENT_RANK() – Returns the relative rank within a partition.
CUME_DIST() – Returns the cumulative distribution within a partition.
The analytic functions are:

LEAD() – Allows accessing values from a subsequent row in relation to the current row.
LAG() – Allows accessing values from a previous row in relation to the current row.
NTILE() – Divides rows within a partition into approximately equal groups.
FIRST_VALUE() – Allows accessing values from the first row within a partition.
LAST_VALUE() – Allows accessing values from the last row within a partition.
NTH_VALUE() – Allows accessing the n-th row within a partition.
Finally, the aggregate functions are:

AVG() – Returns an average value for the rows in a partition.
COUNT() – Returns the number of values in the rows in a partition.
MAX() – Returns the maximum value for the rows in a partition.
MIN() – Returns the minimum value for the rows in a partition.
SUM() – Returns the sum value of the rows in a partition.
Our Window Functions Cheat Sheet will provide you with more information about all these functions.

What's your SQL level? Apply for a test.
20.  How Do You Create a Ranking in SQL?
The easiest way to rank data in SQL is to use one of three ranking window functions:

ROW_NUMBER()
RANK()
DENSE_RANK()
You’re given this dataset named album_sales with the following data:

id	artist	album	copies_sold
1	Eagles	Hotel California	42,000,000
2	Led Zeppelin	Led Zeppelin IV	37,000,000
3	Shania Twain	Come On Over	40,000,000
4	Fleetwood Mac	Rumours	40,000,000
5	AC/DC	Back in Black	50,000,000
6	Bee Gees	Saturday Night Fever	40,000,000
7	Michael Jackson	Thriller	70,000,000
8	Pink Floyd	The Dark Side of the Moon	45,000,000
9	Whitney Houston	The Bodyguard	45,000,000
10	Eagles	Their Greatest Hits (1971-1975)	44,000,000
These are the sales of the ten best-selling albums in history. As you can see, the albums are not ranked. That’s what we’ll do here: rank them from best- to worst-selling using window functions.

If you use ROW_NUMBER(), the query will look like this:

SELECT
  ROW_NUMBER() OVER (ORDER BY copies_sold DESC) AS rank,
  artist,
  album,
  copies_sold
FROM album_sales;
The syntax is simple. First, you choose the window function. Then you use the mandatory OVER() clause that signals it’s a window function. In ORDER BY, you sort data descendingly. This now means the row numbers will be assigned according to the copies sold from high to low.

Of course, list all other columns you need and reference the table to get the same output:

rank	artist	album	copies_sold
1	Michael Jackson	Thriller	70,000,000
2	AC/DC	Back in Black	50,000,000
3	Whitney Houston	The Bodyguard	45,000,000
4	Pink Floyd	The Dark Side of the Moon	45,000,000
5	Eagles	Their Greatest Hits (1971-1975)	44,000,000
6	Eagles	Hotel California	42,000,000
7	Shania Twain	Come On Over	40,000,000
8	Fleetwood Mac	Rumours	40,000,000
9	Bee Gees	Saturday Night Fever	40,000,000
10	Led Zeppelin	Led Zeppelin IV	37,000,000
As you can see, the albums are ranked from one to ten. Two albums sold 45 million copies. However, they are ranked differently (third and fourth) according to random criteria. The same happens with three albums that sold 40 million copies.

If you use RANK(), the syntax is the same, except you use a different window function:

SELECT
  RANK() OVER (ORDER BY copies_sold DESC) AS rank,
  artist,
  album,
  copies_sold
FROM album_sales;
However, the output is different:

rank	artist	album	copies_sold
1	Michael Jackson	Thriller	70,000,000
2	AC/DC	Back in Black	50,000,000
3	Whitney Houston	The Bodyguard	45,000,000
3	Pink Floyd	The Dark Side of the Moon	45,000,000
5	Eagles	Their Greatest Hits (1971-1975)	44,000,000
6	Eagles	Hotel California	42,000,000
7	Shania Twain	Come On Over	40,000,000
7	Fleetwood Mac	Rumours	40,000,000
7	Bee Gees	Saturday Night Fever	40,000,000
10	Led Zeppelin	Led Zeppelin IV	37,000,000
You can see that the tied albums are ranked as third (two times). The next non-tie album is ranked fifth. The same happens with the albums ranked seventh.

Let’s see what happens if we use DENSE_RANK():

SELECT
  DENSE_RANK() OVER (ORDER BY copies_sold DESC) AS rank,
  artist,
  album,
  copies_sold
FROM album_sales;
Here’s the result:

rank	artist	album	copies_sold
1	Michael Jackson	Thriller	70,000,000
2	AC/DC	Back in Black	50,000,000
3	Whitney Houston	The Bodyguard	45,000,000
3	Pink Floyd	The Dark Side of the Moon	45,000,000
4	Eagles	Their Greatest Hits (1971-1975)	44,000,000
5	Eagles	Hotel California	42,000,000
6	Shania Twain	Come On Over	40,000,000
6	Fleetwood Mac	Rumours	40,000,000
6	Bee Gees	Saturday Night Fever	40,000,000
7	Led Zeppelin	Led Zeppelin IV	37,000,000
The first tied albums are ranked as third, which is the same as in the previous result. But the difference is that the next non-tie rank is fourth – meaning the ranking is not skipped.

The three other tied albums are now ranked sixth, not seventh as before. Also, the highest rank is seventh, not tenth.

As you can see, each method returns different results. You should use the one that best suits your data and what you want to achieve with ranking. To learn more, read the article on ranking rows in SQL.

21.  What’s the Difference Between RANK() and DENSE_RANK()?
We already touched on the difference in the previous question. You saw it there in a practical example, and now let’s formulate it to answer this question.

RANK() assigns the same rank to rows with the same values. When it gets to the following non-tied row, it skips the rank by the number of tied ranks.

DENSE_RANK() also gives the same rank to tied values. However, the rank is not skipped when it reaches the following non-tied row. In other words, DENSE_RANK() ranks data sequentially.

More details are explained in this article about RANK() and DENSE_RANK() differences.

22.  Find the Top n Rows in SQL Using a Window Function and a CTE.
This is a common question and can be solved in several ways. We will use the window function in a CTE to return the desired result.

The available data is stored in the salary table:

id	first_name	last_name	salary	department
1	Tim	Thompson	10,524.74	Sales
2	Martina	Hrabal	7,895.14	Accounting
3	Susan	Truman	15,478.69	Sales
4	Ciro	Conte	8,794.41	Accounting
5	Jorge	De Lucia	7,489.15	Sales
6	Carmen	Lopez	10,479.15	Accounting
7	Catherine	Molnar	8,794.89	Sales
8	Richard	Buchanan	12,487.69	Accounting
9	Mark	Wong	9,784.19	Sales
10	Silvia	Karelias	9,748.64	Accounting
The task here is to return the top three highest paid employees in each department, together with their salary and department.

The approach is this:

WITH ranking AS (
  SELECT
    first_name,
    last_name,
    salary,
    department,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank
  FROM salary
)
 
SELECT *
FROM ranking
WHERE salary_rank <= 3
ORDER BY department, salary_rank;
The first part of the code is a Common Table Expression, or CTE. It’s initiated using the keyword WITH. The CTE is named ranking. After the AS keyword, we write the CTE definition as a SELECT statement in parentheses.

After selecting all the required columns comes ranking, we use the DENSE_RANK() function. You could use any other ranking window function if you wish.

The syntax is familiar. To get the rankings by department, we need to partition data by that column. Also, we want to rank salaries from high to low. In other words, data in the partition needs to be arranged by salary in descending order.

The second SELECT statement (i.e. the outer query) selects all the columns from the CTE and sets the condition in the WHERE clause for filtering only the top three salaries by the department. Finally, the output is sorted by department and salary rank.

Here’s the result:

first_name	last_name	salary	department	salary_rank
Richard	Buchanan	12,487.69	Accounting	1
Carmen	Lopez	10,479.15	Accounting	2
Silvia	Karelias	9,748.64	Accounting	3
Susan	Truman	15,478.69	Sales	1
Tim	Thompson	10,524.74	Sales	2
Mark	Wong	9,784.19	Sales	3
23.  Compute the Difference Between Two Rows (Delta) Using Window Functions
This problem is most elegantly solved using the LAG() window function. Remember, this is a function that accesses the previous row’s value.

The example data can be found in the table revenue:

id	actual_revenue	period
1	8,748,441.22	2022_07
2	10,487,444.59	2022_08
3	7,481,457.15	2022_09
4	7,497,441.89	2022_10
5	8,697,415.36	2022_11
6	12,497,441.56	2022_12
You need to show the actual revenue, time period, and monthly difference (delta) between the actual and the previous month.

Here’s how to do it.

SELECT
  actual_revenue,
  actual_revenue - LAG(actual_revenue) OVER (ORDER BY period ASC) AS monthly_revenue_change,    
 period
FROM revenue
ORDER BY period;
A delta is calculated by subtracting the previous month from the actual month. That’s exactly what this query does! To get the previous month's revenue, the LAG() function comes in handy. The actual_revenue column is the function’s argument, since we want to access the revenue data from the previous row. As with every window function, there is an OVER() clause. In it, we sorted data by period ascendingly because it’s logical to calculate the delta chronologically.

This is the query’s output:

actual_revenue	monthly_revenue_change	period
8,748,441.22	NULL	2022_07
10,487,444.59	1,739,003.37	2022_08
7,481,457.15	-3,005,987.44	2022_09
7,497,441.89	15,984.74	2022_10
8,697,415.36	1,199,973.47	2022_11
12,497,441.56	3,800,026.20	2022_12
The first shows revenue change as NULL. This is expected because there’s no earlier month to deduct from. In 2022_08, there was a revenue increase of 1,739,003.37 = actual month revenue - the previous month's revenue = 10,487,444.59 - 8,748,441.22.  The same logic applies to all the other results.

You can find similar examples in the article about calculating the difference between two rows in SQL.

24.  Use Window Functions to Compute a Running Total
A running or cumulative total is a sum of a number sequence. The running total is updated every time a new value is added to the sequence. Think of monthly revenues: the current month's total revenue will include the current month's and all the previous months’ revenue sum.

The window function that’s perfect for calculating a running total (cumulative sum) is SUM().

Let’s show the approach on the same data as in the previous question. The goal is to calculate the cumulative revenue for all available months in 2022.

Here’s the solution:

SELECT
  actual_revenue,
  SUM(actual_revenue) OVER (ORDER BY period ASC) AS cumulative_revenue,
  period
FROM revenue;
The cumulative sum is the sum of the actual month's revenue and the sum of all the previous months’ revenue. The SUM() window function applies this logic. The function’s argument is actual revenue, because that’s what we’re summing. To get it to sum all the previous revenue and the current revenue, sort the data ascendingly by period. Again, it’s logical to calculate a cumulative total from the earliest to the latest month.

This is what the code returns:

actual_revenue	cumulative_revenue	period
8,748,441.22	8,748,441.22	2022_07
10,487,444.59	19,235,885.81	2022_08
7,481,457.15	26,717,342.96	2022_09
7,497,441.89	34,214,784.85	2022_10
8,697,415.36	42,912,200.21	2022_11
12,497,441.56	55,409,641.77	2022_12
The cumulative revenue in the first row is the same as the actual revenue. For the second row, the cumulative is 19,235,885.81 = 8,748,441.22 + 10,487,444.59. In September, the cumulative is 26,717,342.96 =  8,748,441.22 + 10,487,444.59 + 7,481,457.15.

The same logic applies to the rest of the table.

You can learn more about the running total and how to calculate it here. 

Earth Day Sale. -75% OFF. All 60+ SQL Courses in One Package. Check now.
25.  Find a Moving Average Using Window Functions
A moving average is used when analyzing a series. You can find it under other names, such as rolling mean, rolling average, or running average. It is an average of the current value and the defined number of preceding values. For example, a 7-day moving average is the average of the current day and the six preceding days.

To show you how to calculate it, we’ll use the eur_usd_rate table:

id	exchange_rate	date
1	1.0666	2022-12-30
2	1.0683	2023-01-02
3	1.0545	2023-01-03
4	1.0599	2023-01-04
5	1.0601	2023-01-05
6	1.0500	2023-01-06
6	1.0696	2023-01-09
7	1.0723	2023-01-10
8	1.0747	2023-01-11
9	1.0772	2023-01-12
10	1.0814	2023-01-13
We’ll calculate the 3-day moving average in the following way:

SELECT
  exchange_rate,
  AVG(exchange_rate) OVER (ORDER BY date ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS eur_usd_moving_average,
  date
FROM eur_usd_rate;
We use the AVG() window function on the exchange_rate column. In the OVER() clause, data is sorted by date in ascending order. Now comes the important part! Remember, we need a 3-day moving average involving the current and two previous rows. We specify that in the BETWEEN clause: we tell the function to include two preceding rows and the current row.

Let’s have a look at the result:

exchange_rate	eur_usd_moving_average	date
1.0666	1.0666	2022-12-30
1.0683	1.0675	2023-01-02
1.0545	1.0631	2023-01-03
1.0599	1.0609	2023-01-04
1.0601	1.0582	2023-01-05
1.0500	1.0567	2023-01-06
1.0696	1.0599	2023-01-09
1.0723	1.0640	2023-01-10
1.0747	1.0722	2023-01-11
1.0772	1.0747	2023-01-12
1.0814	1.0778	2023-01-13
The first date’s moving average is the same as the exchange rate because: 1.0666/1 = 1.0666. For 2023-01-02, it’s calculated like this: (1.0666 + 1.0683)/2 = 1.0675.

In 2023-01-03, we’ll finally have three dates: (1.0666 + 1.0683 + 1.0545)/3 = 1.0631. This logic applies to all the rest of the dates.

More examples can be found in this article about computing moving averages in SQL.

26.  What’s the Difference Between ROWS and RANGE?
Both ROWS and RANGE are clauses used for defining a window frame. They limit the data range used in a window function within a partition.

The ROWS clause limits the rows. It’s used for specifying a fixed number of rows preceding and following the current row. The rows’ value is not taken into account.

The RANGE clause limits the data range logically. In other words, it limits data by looking into the preceding and following rows’ values in relation to the current row. It disregards the number of rows.

How do you use them in practice? Read our article on ROWS and RANGE for more details.

27.  Use a Recursive Query to Find all Employees Under a Given Manager.
A recursive query is a special type of CTE that references itself until it reaches the end of the recursion. It’s ideal for querying graph data or hierarchical structure.

An example of the latter is the company’s organizational structure, shown in the company_organization table:

employee_id	first_name	last_name	manager_id
5529	Jack	Simmons	5125
5238	Maria	Popovich	5329
5329	Dan	Jacobsson	5125
5009	Simone	Gudbois	5329
5125	Albert	Koch	NULL
5500	Jackie	Carlin	5529
5118	Steve	Nicks	5952
5012	Bonnie	Presley	5952
5952	Harry	Raitt	5529
5444	Sean	Elsam	5329
This table shows all the employees and the ID of their direct manager.

The task here is to use recursion and return all Jack Simmons’ direct and indirect subordinates. Also, we’ll add a column that can be used for distinguishing different organizational levels. Here’s the code:

WITH RECURSIVE subordinates AS (
    SELECT
  employee_id,
      first_name,
      last_name,
      manager_id,
      0 AS level
    FROM company_organization
    WHERE employee_id= 5529
 
    UNION ALL
 
    SELECT
      co.employee_id,
      co.first_name,
      co.last_name,
      co.manager_id,
      level + 1
    FROM company_organization co
JOIN subordinates s
ON co.manager_id = s.employee_id
)
 
SELECT
  s.employee_id,
  s.first_name AS employee_first_name,
  s.last_name AS employee_last_name,
  co.employee_id AS direct_manager_id,
  co.first_name AS direct_manager_first_name,
  co.last_name AS direct_manager_last_name,
  s.level
FROM subordinates s
JOIN company_organization co
ON s.manager_id = co.employee_id
ORDER BY level;
We start the recursion using WITH RECURSIVE. (If you’re working in MS SQL Server, use only WITH.)

The first SELECT in a CTE is called anchor member. In it, we reference the dataset and select all the necessary columns. Also, we create a new column with the value zero and filter data in the WHERE clause. Why use this exact condition in WHERE? Because Jack Simmons’ employee ID is 5529, and we want to show him and his subordinates.

Then comes the UNION ALL, which combines the results of the anchor query and recursive query, i.e. the second SELECT statement.

We want recursion to go all the way down through the organizational structure. In the recursive query, we join the CTE with the company_organization table. We again list all the necessary columns from the latter table. Also, we want to add one organizational level with every recursion.

Finally, we come to the query that uses the CTE. This query serves to get data from both the CTE and the company_organization table. We use the CTE to show the employee data. The other table is used for showing the direct manager's info.

Running the code will get you this result:

employee_id	employee_first_name	employee_last_name	direct_manager_id	direct_manager_first_name	direct_manager_last_name	level
5529	Jack	Simmons	5125	Albert	Koch	0
5952	Harry	Raitt	5529	Jack	Simmons	1
5500	Jackie	Carlin	5529	Jack	Simmons	1
5012	Bonnie	Presley	5952	Harry	Raitt	2
5118	Steve	Nicks	5952	Harry	Raitt	2
The above table shows Jack Simmons’s direct manager is Albert Koch. Directly under Simmons, there are Harry Raitt and Jackie Carlin. The indirect subordinates are Bonnie Presley and Steve Nicks. Their direct manager is Harry Raitt.
