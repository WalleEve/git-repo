# MYAAP DDL SCRIPTS
create table myaap_users(
user_id integer primary key,
user_name char(18) unique,
user_password char(20));
