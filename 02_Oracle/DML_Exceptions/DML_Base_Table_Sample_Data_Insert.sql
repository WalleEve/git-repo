-- Default Insert Valeus to the Base Tabels for Amazon App 

insert into amazon_products ap 
    (ap.PRODUCT_ID, ap.PRODUCT_NAME, ap.PRODUCT_CATAGORY, ap.UNIT_PRICE, ap.STOCK_UNIT, ap.START_DATE, ap.END_DATE) 
values (2312, 'SUGAR', 'FOOD', 45.00, 100.00, sysdate, null);

commit;
select * from amazon_products;


begin 
    util_base_table.p_amazon_products_ins_upd(
        In_product_id => 5432, 
        Iv_product_name => 'RICE', 
        Iv_product_catagory => 'FOOD', 
        In_unit_price => 56.00, 
        In_stock_unit  => 250.00, 
        Id_start_date => sysdate, 
        Id_end_date => null
        );
        
    commit;
end;
