--Assigning  values to variable with assignment statement
DECLARE -- We can assign initial values here
wages NUMBER;
hours_worked NUMBER := 40;
hours_salary NUMBER := 22.50;
bonus NUMBER := 150;
country VARCHAR2(128);
counter NUMBER := 0;
done BOOLEAN;
valid_id  BOOLEAN;
emp_rec1 emp%ROWTYPE;
emp_rec2 emp%ROWTYPE;
TYPE commissions IS TABLE  OF NUMBER INDEX BY PLS_INTEGER;
comm_tab commissions;

BEGIN -- We can assign values values here too
wages := (hours_worked * hours_salary) + bonus;
country := 'France';
country := UPPER('Canada');
done := TRUE;
valid_id := TRUE;
emp.rec1.first_name := 'Antonio';
emp_rec1 := emp_rec2;
comm_tab(5) := 2000*0.15;
END;
/
 
