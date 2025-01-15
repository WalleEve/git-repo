CREATE TABLE admin_login (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    reg_email VARCHAR(100) UNIQUE NOT NULL,
    status VARCHAR(10) NOT NULL,
    last_login TIMESTAMP,
    user_created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    old_password VARCHAR(100)
);


CREATE TABLE stock (
    sr_no SERIAL PRIMARY KEY,
    item_name VARCHAR(100),
    brand VARCHAR(50),
    date_of_entry DATE,
    unit_price DECIMAL(10, 2),
    unit_type VARCHAR(20),
    total_stock INT,
    current_stock INT
);
