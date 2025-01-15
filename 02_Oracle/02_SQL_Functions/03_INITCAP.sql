--# Oracle INITCAP Function 
/*
The Oracle INITCAP() function sets the first letter of each word in Uppercase, all othere letters in Lowercase.
Words are delimited by white space or characters that are not alphanumeric. 

# Syntax:
INITCAP(string1)

string1: A string whose first character in each word will be converted to uppercase and the rest characters will be converted to lowercase. Data Type: CHAR, VARCHAR2, NCHAR, NVARCHAR2, CLOB, NCLOB


*/

select initcap('steve king') "Emp. Name"  from dual;

select initcap('STEVE1KING') ename from dual;

select initcap('STEVE@KING') ename from dual;




