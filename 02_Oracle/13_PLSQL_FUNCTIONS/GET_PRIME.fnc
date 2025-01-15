set serveroutput on;
CREATE OR REPLACE function HR.get_prime(in_number number)
return varchar2
as 
flag varchar2(5) := 'True';
begin 
    for i in 2..round(in_number/2)
    loop
        if mod(in_number, i) = 0 then
            flag := 'False';
            exit;
        end if;
    end loop;
    return flag;
end;
/



