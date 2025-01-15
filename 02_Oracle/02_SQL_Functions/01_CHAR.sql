--# ORACLE CHR FUNCTION 
/*
The CHR function is used to return the character having the binary equivalent to n as a VARCHAR2
value in either the database character set, or from the NCHAR_CS
for single-byte character sets, when n > 256, then returns by binary equivalent of n mod 256.
This function takes a number as an argument a, or any value that can be implicitly converted to NUMBER, 
and returns a character.

Syntax: CHR(n [USING NCHAR_CS])
n: a number 
NCHAR_CS: national character set 

*/

SELECT CHR(72)||CHR(65)||CHR(84) "Cap" 
FROM dual;

SELECT CHR(210 USING NCHAR_CS) 
FROM dual;




