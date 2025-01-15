--# Oracle LOWER function 
/*
The Oracle LOWER() FUnction returns a specified character expression in lowercase letters.

# Syntax: 
LOWER(cExpression)

cExpression: The given character expression. Data Type: CHAR, VARCHAR2, NCHAR, NVARCHAR2, CLOB, NCLOB
*/

select LOWER(ename) from emp;

select lower('SAYED MAHFUZE RAHEMAN')  ename from dual;

select lower('ABC123EFG')  str from dual;

select lower(1234) nmb from dual;

select lower('abc@EFG') str from dual;





