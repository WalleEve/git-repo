--# Declaration 
--# Here are some examples of Variable declarations:
/***********************************************************************************
|	user_id integer;
|	quantity numeric(5);
|	url varchar;
|	myrow table_name%rowtype;
|	myfields table_name.columnname%TYPE;
|	arow RECORD;
|	
|	--# The general syntax of a variable decalration is:
|	
|	name [CONSTANT] type [COLLATE collection_name] [ NOT NULL ]
|	[ {DEFAULT | := | = } expression];
|
|
|	quantity integer DEFAULT 32;
|	url varchar := 'http://mysite.com';
|	transaction_time CONSTANT timestamp with time zone := now();
|
*************************************************************************************/

--# Declaring Function Parameters 
--# Parameter passed to functions are names with the identifiers $1, $2, etc. 
--# Optionally, aliases can be declared for $n.

CREATE FUNCTION sales_tax (subtotal real) RETURNS real AS $$
BEGIN 
	RETURN subtotal * 0.06;
END;
$$ LANGUAGE plpgsql;


-- Name ALIAS 

CREATE FUNCTION sales_tax_1(real) RETURNS real AS $$
DECLARE
	subtotal ALIAS FOR $1;
BEGIN 
	RETURN subtotal * 0.06;
END;
$$ LANGUAGE plpgsql;



CREATE FUNCTION instr(varchar, integer) RETURNS integer AS $$
DECLARE 
	v_string ALIAS FOR $1;
	index ALIAS FOR $2;
BEGIN 
	-- Body part
END;
$$ LANGUAGE plpgsql;


CREATE FUNCTION concat_selected_fields(in_t sometablename) RETURNS 
text AS $$
BEGIN 
	RETURN in_t.f1 || in_t.f3 || in_t.f5 || in_t.f7;
END;
LANGUAGE plpgsql;



CREATE FUNCTION sales_tax_2(subtotal real, OUT tax real) AS $$
BEGIN 
	tax := subtotal * 0.06;
END;
$$ LANGUAGE plpgsql;

--# Notice that we omitted RETURNS real - we could have included it, but it would be redundant.
--# To call a function with OUT parameters, omit the output parameter(s) in the function call:

SELECT sales_tax_2(100.00);

--# Output parameters are most useful when returning multiple values. 

CREATE FUNCTION sum_n_product(x int, y int, OUT sum int, OUT prod int) AS $$
BEGIN 
	sum := x + y;
	prod := x * y;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM sum_n_product(2, 4);

--#######################################################################################################################

CREATE FUNCTION extended_sales(p_itemno int)
RETURNS TABLE (quantity int, total numeric) as $$
BEGIN
	RETURN QUERY SELECT s.quantity, s.quantity * s.price from sales as s
		WHERE s.itemno = p_itemno;
END;
$$ LANGUAGE plpgsql;



--#######################################################################################################################

select * from kakiri.mt_loan_details;
select mt.scheme_name, sum(mt.sanction_amount) as sanction_amount, sum(mt.requested_amount) as requested_amount  from kakiri.mt_loan_details as mt
group by mt.scheme_name;

CREATE FUNCTION get_scheme_report()
	RETURNS TABLE (scheme_name varchar, requested_amount numeric, sanction_amount numeric) AS $$
	BEGIN 
		RETURN QUERY SELECT mt.scheme_name, sum(mt.sanction_amount) as sanction_amount, sum(mt.requested_amount) as requested_amount  
		from kakiri.mt_loan_details as mt
		group by mt.scheme_name;
	END;
	$$ LANGUAGE plpgsql;


select * from get_scheme_report();

--#######################################################################################################################

/***********************************************************************************************************************
|	In PostgreSQL, we can use ANYELEMENT to create functions that can accept arguments of any data type. 
|	This is particularly useful for writing generic functions. Here's a basic example of how to use ANYELEMENT in a function:
************************************************************************************************************************/
--# When the return type of a PL/pgSQL function is seclared as a polymorphic type, a special paramter $0 is created.
--# $0, Its data type is the actual return type of the function, as deduced from the actual input types. 
--# $0 can also be given as alias.


CREATE FUNCTION add_three_values(v1 anyelement, v2 anyelement, v3 anyelement)
RETURNS anyelement as $$
DECLARE 
	result ALIAS for $0;
BEGIN 
	result := v1 + v2 + v3;
	RETURN result;
END;
$$ LANGUAGE plpgsql;


select add_three_values(1::int, 2::int, 4::int);



CREATE OR REPLACE FUNCTION get_first_element(array_input ANYARRAY)
RETURNS ANYELEMENT AS $$
BEGIN
    RETURN array_input[1];  -- Returns the first element of the input array
END;
$$
LANGUAGE plpgsql;


SELECT get_first_element(ARRAY[1, 2, 3]);          -- Returns 1
SELECT get_first_element(ARRAY['a', 'b', 'c']);    -- Returns 'a'
SELECT get_first_element(ARRAY[1.1, 2.2, 3.3]);     -- Returns 1.1	


CREATE FUNCTION add_three_valeus(v1 anyelement, v2 anyelement, v3 anyelement, OUT sum_is anyelement) 
AS $$
BEGIN 	
	sum_is := v1 + v2 + v3;
END;
$$ LANGUAGE plpgsql;

SELECT * from add_three_valeus(4::int, 10::int, 1::int);


/***********************************************************************************************************************
|	In PostgreSQL, ANYCOMPATIBLE is a type used in function signatures to indicate that a parameter can accept any data type that is compatible with a specified type. 
|	This is useful for functions that need to handle multiple data types while still enforcing some type safety.	
************************************************************************************************************************/

CREATE FUNCTION add_three_values(v1 anycompatible, v2 anycompatible, v3 anycompatible)
RETURNS anycompatible AS $$
BEGIN 
	RETURN v1 + v2 + v3;
END;
$$ LANGUAGE plpgsql;

select add_three_values(1, 2, 4.7);








