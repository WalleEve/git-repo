--Creating some test tables
sql> CREATE TABLE Education
(
srno NUMBER(4)
CONSTRAINT education_srno.PK PRIMARY KEY,
Edu_Type VARCHAR2(20)
CONSTRAINT education_type_NN NOT NULL
CONSTRAINT education_type_UNQ UNIQUE
CONSTRAINT education_type_CHK 
CHECK Edu_Type IN('PRIMARY','SECONDARY','HIGHER','VOCATIONAL','TECHNICAL','PRIVATE''HOME'),
"Enroll '%'" number(5,2)
);

CREATE TABLE acer_school
(
srno NUMBER(2)
CONSTRAINT acer_srno_PK PRIMARY KEY,
Edu_type VARCHAR2(20)
CONSTRAINT acer_school_type_FK
REFERENCES Education(edu_type),
"Duration 'Year'" number
CONSTRAINT acer_school_nn NOT NULL,
total_seat number(3)
);


