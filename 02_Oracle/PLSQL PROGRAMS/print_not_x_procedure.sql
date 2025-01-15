-- NOT Operator

CREATE PROCEDURE print_not_x (x BOOLEAN)
IS
BEGIN
 print_boolean ('x ' ,x);
 print_boolean (' NOT x ',NOT x);
END;

BEGIN
  print_not_x (TRUE);
  print_not_x (FALSE);
  print_not_x (NULL);
END;
