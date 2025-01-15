--# Oracle -Charactr Functions 
The Oracle character functions that take the input argument is CHAR or VARCHAR2 or NCHAR or NVARCHAR2
and the value return is VARCHAR2 or NVARCHAR2 type.

CHR : The CHR function is used to return the character having the binary equivalent to n as a VARCHAR2 value in either the Database character set ot, from the NCHAR_CS.
CONCAT:  The Oracle CONCAT() function returns the result (a string) of concatenating two string values. This function is equivalent to the concatination operator || 
INITCAP: The Oracle INITCAP() function sets the first letter of each word in Uppercase, all other letters in lowercase. Words are delimited by white space or characters that not alphanumeric.
LOWER: The Oracle LOWER() function returns a specified character expression in lowercase letters.
LPAD: The Oracle LPAD() function is used to pad the left side of a string with a specific set of characters. The function is useful for formatting the output of a query.
LTRIM: The oracle LTRIM() function is used to remove all specified characters from the left end side of a string. Opetionally we can specify an initial character or characters to trim to, or it will default to a blank.
NCHAR: The Oracle NCHAR() function is used to get the character having the binary equivalent to the number in the national character ser. This function is equivalent to using the CHAR function with the USING NCHAR_CS clause.
NLS_INITCAP: The oracle NLS_INITCAP() function sets the first letter of each word in Uppercase. all other letters in lowercase. Words are delimited by white space or characters that are not alphanumeric.
NLS_LOWER: The Oracle NLS_LOWER() function returns a specified character expression in lowercase letters.
NLS_UPPER: The NLS_UPPER() Function is used to return all letters of a given string in Uppercase.
NLSSORT: The NLSSORT function is used to replce a character string with the equivalent sort string used by the linguistic sort mechanism.
REGEXP_SUBSTR: The REGEXP_SUBSTR function use used to return the substring that matches a regular expression within a string.
REPLACE: The REPLACE function is used to return char with every occurrence of search_string replaced with replacement _string.
RPAD: The Oracle RPAD function is used to pas the right side of a string with a specific set of characters. This function is useful for formatting the output of a query.
RTRIM: The Oracle RTRIM function us used to remove spaces  if no characters is provided as trimming text or set of characters which are matching with the trimming text. from the end of a string.
SOUNDEX: The Oracle SOUNDEX function returns a character string containing the phonetic representation of char. This function lets us compare words that are spelled differently, but sound alike in English.
 SUBSTR: The SUBSTR function returns the specified number (substring length) of characters from a particular position of a given string. SUBSTR uses bytes instead of characters. 
 TRANSLATE: The Oracle TRANSLATE function returns a string with all occurrence of each character specified in another string as 2nd argument replaced by its corresponding character specified in the 3rd argument.
 TRANSLATE_USING: The Oracle TRANSLATE_USING converts char into the character set specified for conversions between the database character set and the national character set.
 TRIM: The Oracle TRIM function is used to remove all leading or trailing characters() or both from a character string. If trim_character or trim_source is a character literal, than it is necessary to enclose it in single quotaion marks.
 UPPER: The Oracle UPPER() function returns a specified character expression in UPPERCASE letters.
 ASCII: The ASCII() function returns the decimal representaion of the first character of a character expression.
 INSTR: The Oracle INSTR function is used to search string for substring and find the location of the substring in the string.If a substring that id equal to substring is found, then the function returns an integer indicating the position of the first character of this substring. If no such substring is found, then the function returns zero.
 LENGTH: The Oracle LENGTH function is used to return the length of a given string. If the string has data type CHAR, then the length includes all trailing blanks. If the string is null, then this function returns null.
 REGEXP_COUNT:  The Oracle REGEXP_COUNT function is used to count the number of times that a pattern occurs in a string. It returns an integer indicating the number of occurrence of the pattern. If no match is found then the function returns 0.
 REGEXP_INSTR: The Oracle REGEXP_INSTR function is used to return the location of a regular expression pattern in a string. This function allows us to find a substring in a string using regular expression pattern matching,if no match is found, then the function returns 0.
 NLS_CHARSET_DECL_LEN: The Oracle NLS_CHARSET_DECL_LEN function is used to returns the declarion length(in a number of characters) of an NCHAR column.
 NLS_CHARSET_ID: The Oracle NLS_CHARSET_ID function is used to return the character set ID number corresponding to character set name string.
 NLS_CHARSET_NAME: The Oracle NLS_CHARSET_NAME is used to return the name of the character set corresponding to ID number number1. When the number is not recognized as a valid character set ID , then this function returns null.
 
