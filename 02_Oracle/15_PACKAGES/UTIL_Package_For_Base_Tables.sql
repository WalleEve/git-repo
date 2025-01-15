
create or replace package util_base_table as 
    procedure p_amazon_products_ins_upd(
        In_product_id in number, 
        Iv_product_name in varchar2 default 'NA', 
        Iv_product_catagory in varchar2, 
        In_unit_price in number, 
        In_stock_unit in number, 
        Id_start_date in date default sysdate, 
        Id_end_date in date default null);
end util_base_table;
/
create or replace package body util_base_table as 
--# Procedure
procedure p_amazon_products_ins_upd(
        In_product_id in number, 
        Iv_product_name in varchar2 default 'NA', 
        Iv_product_catagory in varchar2, 
        In_unit_price in number, 
        In_stock_unit in number, 
        Id_start_date in date default sysdate, 
        Id_end_date in date default null)
as 
begin 
    begin  
        insert into amazon_products values 
        (
            In_product_id,
            Iv_product_name,
            Iv_product_catagory,
            In_unit_price,
            In_stock_unit, 
            Id_start_date,
            Id_end_date
        );
    exception 
        when DUP_VAL_ON_INDEX then 
            UPDATE amazon_products SET                 
                product_name = Iv_product_name,
                product_catagory = Iv_product_catagory,
                unit_price = In_unit_price,
                stock_unit = In_stock_unit, 
                start_date = Id_start_date,
                end_date = Id_end_date
            WHERE 
                product_id = In_product_id;
       
        when others THEN
            dbms_output.put_line('Error Code: '|| SQLCODE ||' ' || ' Error Message: '|| SQLERRM);
    end;
            
end p_amazon_products_ins_upd;

end util_base_table;