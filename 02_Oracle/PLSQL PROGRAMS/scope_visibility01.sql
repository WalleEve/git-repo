-- SCOPE AND VISIBILITY OF IDENTIFIERS
--
-- outer block
DECLARE
a CHAR :='A'; --Scope of c(CHAR) begins
b REAL :=9; --Scopr of b begins
BEGIN
-- Visibility of c(CHAR) and b begins

	-- First sub-block
	DECLARE
	a INT :=5; -- Scope of a(INT) begins
	c REAL :=8; -- Scope of c begins
	BEGIN
	-- Visibility of a(INT),b,c begins
	DBMS_OUTPUT.PUT_LINE('The value of a(INT) is: ' ||a);
	DBMS_OUTPUT.PUT_LINE('The value of c(REAL) is: '||c);
	DBMS_OUTPUT.PUT_LINE('The Value of b(REAL) is: '||b);
	END; -- Scope of a(INT) and c(REAL) is end
	
	--Second sub-block
	DECLARE
	d INT :=6; -- Scope of d(INT) begins
	e REAL :=8; -- Scope of e begins
	BEGIN
	-- Visibility of d(INT),a(CHAR),b,e begins
	DBMS_OUTPUT.PUT_LINE('The value of d(INT) is: ' ||d);
	DBMS_OUTPUT.PUT_LINE('The value of a(CHAR) is: '||a);
	DBMS_OUTPUT.PUT_LINE('The Value of b(REAL) is: '||b);
	DBMS_OUTPUT.PUT_LINE('The value of e(REAL) is: '||e);
	END; -- Scope of d(INT) and e(REAL) is end

DBMS_OUTPUT.PUT_LINE('The value of a(CHAR) is: '||a);
DBMS_OUTPUT.PUT_LINE('The value of d(REAL) is: '||b);
END; --Scope of a(CHAR) and b(REAL) is end
/

	
	
