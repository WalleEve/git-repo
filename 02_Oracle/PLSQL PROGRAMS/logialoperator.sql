-- Changing Evaluation order of logical operator
DECLARE
  x BOOLEAN :=FALSE;
  y BOOLEAN :=FALSE;
BEGIN
  print_boolean ('NOT x AND y', NOT x AND y);
  print_boolean ('NOT(x AND y)', NOT(x AND y));
  print_boolean ('(NOT x) AND y',(NOT x)AND y);
END;
/
