-- show OR returns TRUE if either operand is TRUE .
-- OR Operator

CREATE PROCEDURE print_x_or_y (x BOOLEAN , y BOOLEAN)
IS
BEGIN
  print_boolean ('x', x);
  print_boolean ('y', y);
  print_boolean ('x or y', x OR y );
END;

BEGIN
 print_x_or_y (FALSE , FALSE);
 print_x_or_y (FALSE , TRUE);
 print_x_or_y (TRUE , FALSE);
 print_x_or_y (TRUE , TRUE);

 print_x_or_y (TRUE , NULL);
 print_x_or_y (FALSE , NULL);
 print_x_or_y (NULL , FALSE);
 print_x_or_y (NULL , TRUE);
END;
s
