-- select calender_days('12 feb 2018');
-- drop function calender_days(date);
create or replace function calender_days(fromdate date)
returns varchar
as
$body$
declare
	monthenddate date;
	totaldays number;
	i number;
	vmonth numeric;  
	vyear varchar;
	result varchar := '';
	
begin
	vmonth := (select to_char($1,'mm') ); -- select to_char(to_date('1-02-19','dd-mm-yy'),'mm')
	vyear := (select to_char($1,'yyyy') ); -- select to_char(to_date('1-02-19','dd-mm-yy'),'yyyy')
	/*
	01 jan - 31	05 may - 31	09 sep - 30
	02 feb - 28 	06 jun - 30	10 oct - 31
	03 mar - 31	07 jul - 31	11 nov - 30	
	04 mar - 30	08 aug - 31	12 dec - 31

	*/
	if vmonth in (1,3,5,7,8,10,12) then 
	monthenddate := (select '31-'|| vmonth::varchar || '-' || vyear );
	elsif vmonth in (4,6,9,11) then
	monthenddate := (select '30-'|| vmonth::varchar || '-' || vyear );
	elsif vmonth in (2) then
	monthenddate := (select '28-'|| vmonth::varchar || '-' || vyear );
	else
	raise notice 'Please enter valid Data';
	end if;
	totaldays := (select monthenddate-$1);
	raise notice 'totaldays:%',totaldays;
	for i in 1..totaldays
	loop
	--raise notice 'i: %',i;
	raise notice 'Month remaing Date: %',$1+i;
	result :=( result ||'
	'||to_char($1+i,'day-dd-mon-yyyy') );
	raise notice '** result: %',result;
	end loop;
return substring(result,2);
end;
$body$
language plpgsql;
	
