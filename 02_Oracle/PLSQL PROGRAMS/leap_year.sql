-- select leapyear ('12 jan 1897')
-- drop function leapyear(date);
create or replace function leapyear(date)
returns varchar as
$$
begin
	if to_char($1,'yyyy')::number % 4 = 0 then
		if to_char($1,'yyyy')::number % 100 = 0 then
			if to_char($1,'yyyy')::number % 400 = 0 then
				raise notice 'year : %  is leap year.',  to_char($1,'yyyy');
				return  to_char($1,'yyyy')||' is leap year .';
			else 
				return to_char($1,'yyyy')||' is not leap year !';
			end if;	
		else 
			return  to_char($1,'yyyy')||' is leap year .';
		end if;	
	else
		raise notice ' Year : % is not a leap year ! ',to_char($1,'yyyy');
		return to_char($1,'yyyy')||' is not leap year !';
	end if;
end
$$
language plpgsql;
		