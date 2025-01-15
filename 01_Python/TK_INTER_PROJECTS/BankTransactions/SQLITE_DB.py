# SQLITE:

import sqlite3 

conn = sqlite3.connect("test_db")
print("Opend database successfully")

conn.execute("""
	CREATE TABLE isl_bank(
	id int primary key not null,
	name text not null,
	account_no int not null,
	balance numeric);
	""")

conn.execute("""
	CREATE TABLE user(
	id int primary key,
	user_name text,
	password text);
	""")

