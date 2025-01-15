select * from pg_attribute;
SELECT *
FROM pg_catalog.pg_tables

CREATE PROCEDURE table_details()
LANGUAGE SQL
AS $$
declare
i record;
begin
for i in SELECT *
FROM pg_catalog.pg_tables
loop
raise notice 'table name: %', i.table_name;
end loop;
end;
$$;

create table emp()

VACUUM (VERBOSE, ANALYZE) sample;


do $$ 
<<first_block>>
declare
   i record;
   query_string text;
begin
   for i in SELECT * FROM pg_catalog.pg_tables
   loop   
   query_string = 'VACUUM (VERBOSE, ANALYZE) '||i.tablename;
   raise notice 'Vacume Table: %  Query: %', i.tablename, query_string;
   EXECUTE  query_string;
   --sprintf(command, "VACUUM (VERBOSE, ANALYZE) i.tablename");
   --EXEC SQL EXECUTE IMMEDIATE :command;
   
   end loop;   
   --return film_count;
end first_block;
$$;

call pro_table_details()