CREATE OR REPLACE PACKAGE util AUTHID DEFINER
AS 

TYPE TimeRec IS RECORD(
    minutes SMALLINT,
    hours   SMALLINT 
    );
    TYPE TransRec IS RECORD(
    catagory VARCHAR2(10),
    account  INT,
    amount   REAL,
    time_of  TimeRec
    );
    
    minimum_balance     CONSTANT REAL := 10.00;
    number_processed    INT;
    insufficient_funds  EXCEPTION;
    PRAGMA EXCEPTION_INIT(insufficient_funds, -4097);
    
    TYPE array_type is VARRAY(10) OF VARCHAR2(20);
    TYPE nested_type IS TABLE OF VARCHAR2(20);
    TYPE ass_array  IS TABLE OF VARCHAR2(20) INDEX BY PLS_INTEGER;
END util;
/

DECLARE 
    n1 util.array_type := util.array_type('SAYED', 'MAHFUZE', 'RAHEMAN');
BEGIN 
    for i in 1..3
    loop
        dbms_output.put_line(n1(i));
    end loop;
END;

set serveroutput on;

DECLARE 
    TYPE foursome IS VARRAY(4) OF VARCHAR2(15);
    
    team foursome := Foursome('Jony', 'Mary', 'Albert', 'Juanita');

    PROCEDURE print_team(heading varchar2) IS 
    BEGIN 
        DBMS_OUTPUT.PUT_LINE(heading);
        
        FOR i IN 1..4 LOOP
            DBMS_OUTPUT.PUT_LINE(i ||'.'|| team(i));
        END LOOP;
    END print_team;
BEGIN 
    print_team('2001 Team');
    
    team(3) := 'Pierre';
    team(4) := 'Yvonne';
    
    print_team('2005 Team');
END;
/

DECLARE 
    name util.array_type := util.array_type('SAYED');
BEGIN 
    DBMS_OUTPUT.PUT_LINE(name(1));
END;
/


    

