-- Block with Multiple and Duplicate Labels
<<compute_ratio>>
<<another_lable1>>
DECLARE
 numerator NUMBER :=22;
 denominatior NUMBER:=7;
BEGIN
 <<another_lable1>>
 DECLARE
 denominator NUMBER :=0;
 BEGIN
  DBMS_OUTPUT.PUT_LINE('Ratio with computer_ratio.denominator = ');
  DBMS_OUTPUT.PUT_LINE(numerator/compute_ratio.denominator);

  DBMS_OUTPUT.PUT_LINE('Ratio with another_lable1.denominator = ');
  DBMS_OUTPUT.PUT_LINE (numerator/another_lebel1.denominator);
EXCEPTION
 WHEN ZERO_DIVIDE THEN
 DBMS_OUTPUT.PUT_LINE('Divide-by-zero: can''t divide'||numerator||' by '||denominator);
 WHEN OTHERS THEN
 DBMS_OUTPUT.PUT_LINE('Unexpected error.');
 END another_lable1;
END computer_lable;
/

output:
Ratio with compute_ratio.denominator =
2.75
Ratio with another_lable1.denominator =
Divide by zero error: can't divide 22 by 0

PL/SQL procedure successfully completed.
