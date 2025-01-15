--# ORACLE CONCAT FUNCTION 
/*
The Oracle CONCAT() function returns the result (a string) of concatenating two string values.
This function is equivalent to the concatenation operator (||).

Syntax: 
CONCAT(char1, char2)

char1 : A string value to concatinate to the other values. Data Types: CHAR, VARCHAR2, NCHAR, NVARCHAR2, CLOB, NCLOB
char2 : A string value to concatinate to the other values. Data Types: CHAR, VARCHAR2, NCHAR, NVARCHAR2, CLOB, NCLOB

If there are two different data types in concatenations Oracle Database returns the data type that results in a  lossless conversion.
Therefore if one of the arguments is a LOB, then the returned value is a LOB. If one of the arguments is a national data type, then
the returned value is a national data type.

CONCAT(CLOB, NCLOB) returns NCLOB 
CONCAT(NCLOB, NCHAR) returns NCLOB 
CONCAT(NCLOB, CHAR) returns NCLOB 
CONCAT(NCHAR, CLOB) returns NCLOB 
*/

SELECT CONCAT('w3resource', '.com') as comainName from dual;

CREATE TABLE temp1 (
student_firstname varchar(200) NOT NULL,
student_lastname varchar(200)
);

INSERT INTO temp1 VALUES('Steven', 'King');
INSERT INTO temp1 VALUES('Neena', '');
INSERT INTO temp1 VALUES('Lex', 'De Haan');

SELECT CONCAT(student_firstname, student_lastname) from temp1;

SELECT CONCAT('SAYED', NULL) from dual;

SELECT CONCAT('SAYED', 123) from dual; -- SAYED123

