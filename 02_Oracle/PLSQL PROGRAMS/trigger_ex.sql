/* Trigger
 Oracle allows us to define procedures that are implicitly executed when an INSERT,UPDATE or DELETE statement is issued against the associated table.
Triggers are similar to stred procedures. A triggers can include SQL and PL/SQL statement to execute as a unit and can invoke stroed procedure.
- Notice that triggers are stored in the database separately from their associated tables.
Triggers can be defined only on tables, not on views. Triggers on the tables of a view are fired if an INSERT UPDATE or DELETE statemnet is issued against a view.
-- CASCADING TRIGGERS:
   When a trigger is fired a SQL statement within its trigger action potentially can fire other triggers. When a statement in a  
   trigger body causes another trigger to be fired the triggers are said to be cascading .
PARTS OF A TRIGGER:
A trigger has three basic parts:
. a triggering event or statement
. a trigger restriction
. a trigger action
ex:
AFTER UPDATE OF parts_on_hand ON inventory -- Triggering Statement
WHEN (new.part_on_hand < new.reorder_poin) -- Trigger Restriction

FOR  EACH ROW          -- Triggered ACTION
DECLARE
 x NUMBER;
BEGIN
 SELECT COUNT(1) INTO x From pending_orders
 WHERE part_no=now.part_no;
 IF x=0
 THEN 
  INSERT INTO pending_orders VALUES(newlpart_no,new.reorder_quantity,sysdate);
 END IF;
END;


-- TYPES OF TRIGGERS:
ROW TRIGGERS
STATEMENT TRIGGERS
BEFORE TRIGGERS
AFTER TRIGGERS

COMBINATION:
BEFORE ROW TRIGGER
BEFORE STATEMENT TRIGGER
AFTER STATEMENT TRIGGER
AFTER ROW TRIGGER

EX:

*/
// testing table creation: 
CREATE TABLE stat_tab (utype CHAR(8),rowcnt INTEGER,uhour INTEGER);

// package head creation:
CRETE OR REPLACE PACKAGE stat IS
rowcnt INTEGER;
END;
/

// Creating Trigger bt_1
CREATE TRIGGER bt BEFORE UPDATE OR DELETE OR INSERT ON sal
BEGIN
 stat.rowcnt :=0;
END;
/

// Creating second trigger
CREATE TRIGGER rt BEFORE  UPDATE OR DELETE OR INSERT ON sal
FOR EACh ROW 
BEGIN
stat.rowcnt :=stat.rowcnt+1;
END;
/

// Creating main Trigger

CREATE TRIGGER at  AFTER UPDATE OR DELETE OR INSERT sal
DECLARE
 type CHAR(8);
 hour NUMBER;
BEGIN
 IF updating
 THEN
  ty[e :='update';
 END IF;
 IF deleting 
 THEN
  type :='delete';
 END IF;
 IF inserting 
 THEN 
  type :='insert' ;
 END IF;

hour := TRUNC((SYSDATE - TRUNC(SYSDATE)) * 12);
 UPDATE stat_tab
  SET rowcnt :=rowcnt+stat.rowcnt
 WHERE utype =type
 AND uhour = hour;

IF SQL%ROWCOUNT =0 THEN
  INSERT INTO stat_tab VALUES (type,stat.rowcnt,hour);
END IF;

EXCEPTION
WHEN 
  dup_val_on_index THEN
  SET rowcnt =rowcnt+stat.rowcnt
  WHERE utype =type
  AND uhour =hour;
END;
/


/*Example

Assume the following definition of the TOTAL_SALARY trigger, a trigger to maintain a derived column that stores the total salary of all members in a department:*/

CREATE TRIGGER total_salary 

AFTER DELETE OR INSERT OR UPDATE OF deptno, sal ON emp 

  FOR EACH ROW BEGIN 

  /* assume that DEPTNO and SAL are non-null fields */ 

   IF DELETING OR (UPDATING AND :old.deptno != :new.deptno) 

   THEN UPDATE dept 

	SET total_sal = total_sal - :old.sal 

	WHERE deptno = :old.deptno; 

   END IF; 

   IF INSERTING OR (UPDATING AND :old.deptno != :new.deptno) 

   THEN UPDATE dept 

    SET total_sal = total_sal + :new.sal 

    WHERE deptno = :new.deptno; 

   END IF; 

   IF (UPDATING AND :old.deptno = :new.deptno AND 

	  :old.sal != :new.sal ) 

   THEN UPDATE dept 

    SET total_sal = total_sal - :old.sal + :new.sal 

   WHERE deptno = :new.deptno; 

  END IF; 

 END; 

 
