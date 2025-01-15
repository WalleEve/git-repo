create table sample1(
sample_id number,
sample_name varchar2(100),
sample_serial_no    varchar2(10) 
);


create table sample2(
sample_id number,
sample_name varchar2(100),
sample_serial_no number 
);

--# Insert Data into sample1 table 

insert into sample1 (sample_id, sample_name, sample_serial_no) values (345006, 'Sample A', '1230051891');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345007, 'Sample B', '1230051892');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345008, 'Sample C', '1230051893');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345009, 'Sample D', '1230051894');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (346000, 'Sample E', '1230051895');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (346001, 'Sample F', '1230051896');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (346002, 'Sample G', '1230051897');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345603, 'Sample G', '1230051898');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345604, 'Sample I', '1230051899');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345605, 'Sample J', '1230051810');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345606, 'Sample K', '1230051811');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345607, 'Sample L', '1230051812');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345608, 'Sample M', '1230051813');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345608, 'Sample N', '1230051814');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345609, 'Sample O', '1230051815');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345670, 'Sample P', '1230051816');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345671, 'Sample Q', '1230051817');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345672, 'Sample R', '1230051818');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345673, 'Sample S', '1230051819');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345674, 'Sample T', '1230051820');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345675, 'Sample U', '1230051821');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345676, 'Sample V', '123005182A');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345677, 'Sample W', '1230051822');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345678, 'Sample X', '1230051822');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345679, 'Sample Y', '123005182Y');
insert into sample1 (sample_id, sample_name, sample_serial_no) values (345689, 'Sample Z', '1230051829');

select * from sample1;

begin 
    FOR i in 
        (select  
            sample_id as said,
            sample_name as sname,
            sample_serial_no as sno
        from sample1)
    loop
        begin 
        insert into sample2 (sample_id, sample_name, sample_serial_no) 
        values (i.said, i.sname, i.sno);
            
        exception 
            when INVALID_NUMBER  then 
                dbms_output.put_line('Data Type Miss match ID: '|| i.said ||' Name: '|| i.sname || ' Serial No: '|| i.sno);
            when others then 
                dbms_output.put_line('Error Code: '|| SQLCODE || ' Error Message: '|| SQLERRM);
          
        end;
    end loop;
    
end;


        




