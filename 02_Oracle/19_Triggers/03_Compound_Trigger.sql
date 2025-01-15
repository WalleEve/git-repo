# Compound Trigger 

The compound trigger is a trigger that allows us to specify for each of four timing 
points in the single trigger body. The four different timing point it supports is  as
. Before Statement -Level 
. Before Row -Level 
. After Row - Level 
. After Statement - Level 

It Provides the facility to combine the actions for different timing into the same trigger.

Syntax:

CREATE OR REPLACE TRIGGER <trigger_name>
FOR 
INSERT OR UPDATE OR DELETE 
--OF <column name>
ON <table_name>
<Declarative Part>

BEFORE STATEMENT IS 
BEGIN
    <Execution Part>;
END BEFORE STATEMENT;

BEFORE EACH ROW IS 
BEGIN
    <Execution Part>;
END EACH ROW;

AFTER EACH ROW IS
BEGIN 
    <Execution Part>;
END AFTER EACH ROW;

AFTER STATEMENT IS 
BEGIN 
    <Execution Part>;
END AFTER STATEMENT;


CREATE TRIGGER emp_trig
FOR INSERT 
ON emp 
COMPOUND TRIGGER 
BEFORE EACH ROW IS 
BEGIN
:new.salary : = 5000;
END BEFORE EACH ROW;
END emp_trig;
/



