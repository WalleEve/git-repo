-- Show AND returns TRUE if and only if both operands are TRUE
-- AND Operator

CREATE PROCEDURE print_x_and_y (x BOOLEAN,y BOOLEAN)
IS
BEGIN
  print_boolean ('x',x);
  print_boolean ('y',y);
  print_boolean ('x AND y',x AND y);
END;

BEGIN
print_x_and_y (FALSE , FALSE);
print_x_and_y (FALSE , TRUE);
print_x_and_y (TRUE , FALSE);
print_x_and_y (TRUE , TRUE);

print_x_and_y (TRUE , NULL);
print_x_and_y (FALSE , NULL);
print_x_and_y (NULL , TRUE);
print_x_and_y (NULL , FALSE);
END;
/
