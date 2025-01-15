select * from sample;

create view sample_view as 
select * from sample;


select * from sample_view;
update sample_view set user_name='sayed_mahfuze' where id=1;

create table app_users(
id numeric,
user_name char(16),
user_passwd char(16),
constraint app_users_id_pk primary key (id),
constraint app_users_user_name unique (user_name));

insert into app_users values(1, 'sayed', 'Sayed08@sabeeha'),
(2, 'mahfuze', 'Sayed@080631'),
(3, 'sabiha', 'sabiha@06041997');


drop table app_user_details;
create table app_user_details(
user_id numeric,
first_name char(20),
last_name char(20),
address text,
phone numeric,
constraint app_user_dtl_user_id_fk foreign key (user_id) references app_users(id));

insert into app_user_details values(1, 'sayed', 'mahfuze', 'Haladigadia',9692392243);

create or replace view user_view as
select aud.*, au.user_name, au.user_passwd  
from app_user_details aud, app_users au
where aud.user_id = au.id;

select * from user_view;

update user_view set user_name = 'Sayed' where user_id=1;
ERROR:  cannot update view "user_view"
DETAIL:  Views that do not select from a single table or view are not automatically updatable.
HINT:  To enable updating the view, provide an INSTEAD OF UPDATE trigger or an unconditional ON UPDATE DO INSTEAD rule.
SQL state: 55000
