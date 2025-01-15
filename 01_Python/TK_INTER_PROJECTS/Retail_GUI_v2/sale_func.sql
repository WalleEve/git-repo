create or replace function sale(pitem text, pbrand text, pqty numeric)
returns numeric
as
$$
declare
vQuantity numeric = 0;
vtotalPrice numeric = 0;
vtemp numeric = 0;
i record;
begin
vQuantity = pqty;
for i in select * from current_stock where item = pitem and brand = pbrand order by purchase_date
loop
if vQuantity < i.quantity then
	

end loop;
return vtotalPrice;
end;
$$
language plpgsql;

select sale('RICE', 'RUCHI', 101) ;
