create or replace function password_validation(pv_passwd varchar2)
return boolean 
is
sub_value varchar2(10);
punctarray varchar2(25); 
digitarray varchar2(20); 
isdigit boolean;
ispunct boolean; 
m integer;


BEGIN 

punctarray :='!"#$%&()''*+,-/:;<=>?_'; 
digitarray:= '0123456789'; 

   --Check for the minimum length of the password 
IF length(pv_passwd) < 8 THEN 
   raise_application_error(-20002, 'Password length less than 8'); 
END IF; 

IF length(pv_passwd) >15 THEN 
   raise_application_error(-20002, 'Password length greater than 15'); 
END IF; 
 
 sub_value := substr(pv_passwd, 1, 2);
 
 IF substr(pv_passwd, 1, 2) !=upper(substr(pv_passwd, 1, 2)) THEN
    raise_application_error(-20002, 'Password First Two Characters are not Upper Case'); 
 END IF;
 
  IF substr(pv_passwd, 3, 2) !=lower(substr(pv_passwd, 3, 2)) THEN
    raise_application_error(-20002, 'Password second Two Characters are not lower Case'); 
 END IF;

 --1. Check for the digit 
 isdigit:=FALSE; 
sub_value := substr(pv_passwd, 5, 2); 
FOR i IN 1..10 LOOP  
  FOR j IN 1..2 LOOP  
    IF substr(sub_value,j,1) = substr(digitarray,i,1) THEN 
      isdigit:=TRUE; 
        GOTO findpunct; 
    END IF; 
   END LOOP; 
END LOOP; 
IF isdigit = FALSE THEN 
  raise_application_error(-20003, 'Password should contain 5th and 6th character as numeric'); 
END IF; 

<<findpunct>> 
ispunct:=FALSE; 
sub_value := substr(pv_passwd, 7, 2); 
FOR i IN 1..length(punctarray) LOOP  
  FOR j IN 1..2 LOOP  
    IF substr(sub_value,j,1) = substr(punctarray,i,1) THEN 
       ispunct:=TRUE; 
         GOTO endsearch; 
       END IF; 
   END LOOP; 
END LOOP; 
IF ispunct = FALSE THEN raise_application_error(-20003, 'Password should contain 7th and 8th letter as punctuation/special character'); 
END IF; 

<<endsearch>>     
   --Everything is fine; return TRUE ;    
  RETURN(TRUE); 
    
END;

--drop table uses;

create table uses(
username varchar2(10),
upassword varchar2(15));


CREATE OR REPLACE trigger password_check_trg
BEFORE INSERT ON uses FOR EACH ROW
BEGIN
IF password_validation(:NEW.upassword)=True
THEN
    --insert into uses (username, upassword) values(:NEW.username, :NEW.upassword);
   dbms_output.put_line('Done');
END IF;
END; 
    
    
insert into uses values('sayed', 'SAye0@$');


set serveroutput on;
declare 
 v_status boolean;
begin
    v_status := password_validation( 'SAye08@$') ;
    if v_status = True then
    dbms_output.put_line('HI');
  end if;
end;
