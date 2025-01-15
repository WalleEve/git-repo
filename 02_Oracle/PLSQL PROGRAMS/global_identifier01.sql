-- Qualifying Redeclared Global Identifier with Block Lable
<<outer>> --lable1
DECLARE
birthdate date :=&birth_date;
BEGIN
	DECLARE
	birthdate date :=&birth_date;
	BEGIN
	IF birthdate=outer.birthdate THEN
	DBMS_OUTPUT.PUT_LINE('Same birth date');
	ELSE 
	DBMS_OUTPUT.PUT_LINE('Different Birth date');
	END IF;
	END;
END;
/
