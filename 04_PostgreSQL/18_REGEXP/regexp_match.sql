select regexp_match('Sayed Mahfuze', '') 
create table tb1 (name text);
insert into tb1 values('SAYED-MAHFUZE'), 
('SAYED MAHFUZE'),
('SAYEDMAHFUZE'),
('SAYED$MAHFUZE');
select * from tb1;
select regexp_match(name, '\s', 'i') from tb1;
select regexp_match(name, '\W', 'i') from tb1;
