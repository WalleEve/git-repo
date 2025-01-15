-- DROP function some_func();
CREATE FUNCTION some_func() RETURNS NUMERIC AS $$
	<<outerblock>>
	DECLARE 
		quantity NUMERIC := 50;
	BEGIN 
		RAISE NOTICE 'Quantity here is %', quantity;  -- Prints 30 
		quantity := 50;

		-- Create a subblock 
		DECLARE 
			quantity NUMERIC := 80;
		BEGIN 
			RAISE NOTICE 'Quantity here is %', quantity; -- Prints 80
			RAISE NOTICE 'Outer quantity here is %', outerblock.quantity; 	-- Prints 50 

		END;

		RAISE NOTICE 'Quantity here is %', quantity; -- Prints 50

		RETURN quantity;
	END;
	$$
	LANGUAGE plpgsql;
	

select some_func();	
	