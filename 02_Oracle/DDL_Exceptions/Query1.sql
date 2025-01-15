select * from user_objects  uo where uo.object_type='FUNCTION';

select GET_PRIME(6) as prime_staus from dual;

-- Log to Track chagnes 

DROP table log;
CREATE TABLE log (
    date_of_action  date,
    user_id         varchar2(20),
    package_name    varchar2(30)
);