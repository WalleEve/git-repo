BEGIN
IF 8 <= LENGTH(:P22_PASSWORD) AND  LENGTH(:P22_PASSWORD) <= 15  THEN
    IF REGEXP_LIKE(:P22_PASSWORD, '^.*[0-9]') THEN
 IF REGEXP_LIKE(:P22_PASSWORD, '^.*[a-z]', 'c') THEN
 IF REGEXP_LIKE(:P22_PASSWORD, '^.*[A-Z]', 'c') THEN
 IF REGEXP_LIKE(:P22_PASSWORD, '^.*[!@#$%^&*()_]', 'c') THEN
 RETURN '';
 ELSE
    RETURN 'Password has not one special character';
 END IF;
 ELSE
    RETURN 'Password has not one UpperCase';
 END IF;   
 ELSE
    RETURN 'Password has not one LowerCase';
 END IF;
 ELSE
    RETURN 'Password has not a numeric value';
 END IF; 
ELSE
RETURN 'Password Length Must be min 8 char and max 15 char
and your password length is'||' '||LENGTH(:P22_PASSWORD);
END IF;