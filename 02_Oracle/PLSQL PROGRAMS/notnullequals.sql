-- The two IF statements appear to be equivalent. However if either x or y is NULL then first IF statement assigns the value  of y to high and the second IF statement assigns the value of x to high.
-- NOT NULL Equals NULL

DECLARE
  x INTEGER :=2;
  y INTEGER :=5;
BEGIN
 IF (x > y) -- if x or y is NULL then (x > y) is NULL
 THEN high :=x; --run if (x > y) is TRUE
 ELSE high :=y; -- run if (x > y) is FALSE or NULL
 END IF;

 IF NOT (x > y) --if x ot y is NULL then NOT(x > y) is NULL
 THEN high :=y; -- run if NOT(x > y) is TRUE
 ELSE high :=x; -- run if NOT (x > y) is FALSE or NULL 
 END IF;
END;
 
