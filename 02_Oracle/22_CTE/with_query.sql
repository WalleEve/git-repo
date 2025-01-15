create table buyer(
buyer_id    varchar2(10),
property_id varchar2(10)
);
/
create table property(
property_id varchar2(10),
price   numeric
);
/
insert into property values('PL2341', 60);
insert into property values('PL2342', 20);
insert into property values('PL2343', 120);
insert into property values('PL2344', 40);
insert into property values('PL2345', 30);
insert into property values('PL2346', 90);
insert into property values('PL2347', 70);
insert into property values('PL2348', 10);
insert into property values('PL2349', 55);
insert into property values('PL23410', 73);

insert into buyer values('09781', 'PL2341');
insert into buyer values('09782', 'PL2343');
insert into buyer values('09783', 'PL2344');
insert into buyer values('09781', 'PL2345');
insert into buyer values('09784', 'PL2342');
insert into buyer values('09781', 'PL2346');
insert into buyer values('09782', 'PL2347');
insert into buyer values('09785', 'PL2348');
insert into buyer values('09782', 'PL2349');
insert into buyer values('09783', 'PL23410');
/
commit;



select BUYER_ID ,
PROPERTY_ID  from buyer;

select PROPERTY_ID ,
PRICE  from property;

select b.buyer_id, b.property_id, p.price
from buyer b, property p
where p.property_id = b.property_id
and b.buyer_id = '09783';


with final_value as
(select b.buyer_id, b.property_id, p.price
from buyer b, property p
where p.property_id = b.property_id)

select fv.buyer_id, sum(fv.price), count(1)
from final_value fv
group by fv.buyer_id
having sum(fv.price) > 100 and count(1) >1


