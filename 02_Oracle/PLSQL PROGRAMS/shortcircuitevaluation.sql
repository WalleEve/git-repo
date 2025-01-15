-- Short-circuit evaluation prevents the or expression from causing a divide-by-zero error. When the value of on-hand is ZERO the value of the left operand is TRUE , os PL/SQL does not evaluate the right operand. If PL/SQL evaluated both operands before applying the OR operator the right operand would cause a division by zero error

-- Short-Circuit Evaluation

DECLARE
  on_hand INTEGER :=0;
  on_order INTEGER :=100;
BEGIN
-- Does not cause divide-by-zero error;
-- evaluation stops after first expression

IF (on_hand = 0) OR ((on_order/on_hand) <5) THEN
  DBMS_OUTPUT.PUT_LINE(' On hand quantify is zero. ');
END IF;
END;
/
