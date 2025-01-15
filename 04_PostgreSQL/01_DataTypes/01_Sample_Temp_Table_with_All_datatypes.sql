CREATE TABLE sample_temp_table (
    -- Numeric Types
    small_int_col_1 SMALLINT,             -- 2-byte integer
    small_int_col_2 SMALLINT,
    integer_col_1 INTEGER,                -- 4-byte integer
    integer_col_2 INTEGER,
    big_int_col_1 BIGINT,                 -- 8-byte integer
    big_int_col_2 BIGINT,
    decimal_col_1 DECIMAL(10, 2),         -- Arbitrary precision
    decimal_col_2 DECIMAL(10, 2),
    numeric_col_1 NUMERIC(15, 4),         -- Arbitrary precision (alias for DECIMAL)
    numeric_col_2 NUMERIC(15, 4),
    real_col_1 REAL,                      -- 4-byte floating-point
    real_col_2 REAL,
    double_col_1 DOUBLE PRECISION,        -- 8-byte floating-point
    double_col_2 DOUBLE PRECISION,
    serial_col_1 SERIAL,                  -- Auto-incrementing integer
    serial_col_2 SERIAL,
    bigserial_col_1 BIGSERIAL,            -- Auto-incrementing large integer
    bigserial_col_2 BIGSERIAL,

    -- Monetary Type
    money_col_1 MONEY,                    -- Currency amount
    money_col_2 MONEY,

    -- Character Types
    char_col_1 CHAR(10),                  -- Fixed-length string
    char_col_2 CHAR(10),
    varchar_col_1 VARCHAR(50),            -- Variable-length string
    varchar_col_2 VARCHAR(50),
    text_col_1 TEXT,                      -- Variable-length text
    text_col_2 TEXT,

    -- Date/Time Types
    date_col_1 DATE,                      -- Date (year, month, day)
    date_col_2 DATE,
    time_col_1 TIME,                      -- Time (hour, minute, second)
    time_col_2 TIME,
    time_tz_col_1 TIME WITH TIME ZONE,    -- Time with time zone
    time_tz_col_2 TIME WITH TIME ZONE,
    timestamp_col_1 TIMESTAMP,            -- Date and time
    timestamp_col_2 TIMESTAMP,
    timestamp_tz_col_1 TIMESTAMP WITH TIME ZONE,  -- Date and time with time zone
    timestamp_tz_col_2 TIMESTAMP WITH TIME ZONE,
    interval_col_1 INTERVAL,              -- Time span
    interval_col_2 INTERVAL,

    -- Boolean Type
    boolean_col_1 BOOLEAN,                -- True/False
    boolean_col_2 BOOLEAN,

    -- UUID Type
    uuid_col_1 UUID,                      -- Universally unique identifier
    uuid_col_2 UUID,

    -- JSON Types
    json_col_1 JSON,                      -- JSON data
    json_col_2 JSON,
    jsonb_col_1 JSONB,                    -- Binary JSON
    jsonb_col_2 JSONB,

    -- Array Type
    array_col_1 INTEGER[],                -- Array of integers
    array_col_2 INTEGER[],

    -- Range Types
    int_range_col_1 INT4RANGE,            -- Integer range
    int_range_col_2 INT4RANGE,
    num_range_col_1 NUMRANGE,             -- Numeric range
    num_range_col_2 NUMRANGE,
    ts_range_col_1 TSRANGE,               -- Timestamp range (no time zone)
    ts_range_col_2 TSRANGE,
    tstz_range_col_1 TSTZRANGE,           -- Timestamp range (with time zone)
    tstz_range_col_2 TSTZRANGE,
    date_range_col_1 DATERANGE,           -- Date range
    date_range_col_2 DATERANGE,

    -- Geometric Types
    point_col_1 POINT,                    -- Geometric point
    point_col_2 POINT,
    line_col_1 LINE,                      -- Infinite line
    line_col_2 LINE,
    lseg_col_1 LSEG,                      -- Line segment
    lseg_col_2 LSEG,
    box_col_1 BOX,                        -- Rectangular box
    box_col_2 BOX,
    path_col_1 PATH,                      -- Geometric path
    path_col_2 PATH,
    polygon_col_1 POLYGON,                -- Geometric polygon
    polygon_col_2 POLYGON,
    circle_col_1 CIRCLE,                  -- Geometric circle
    circle_col_2 CIRCLE,

    -- Network Address Types
    cidr_col_1 CIDR,                      -- IPv4 or IPv6 network
    cidr_col_2 CIDR,
    inet_col_1 INET,                      -- IPv4 or IPv6 host address
    inet_col_2 INET,
    macaddr_col_1 MACADDR,                -- MAC address
    macaddr_col_2 MACADDR,
    macaddr8_col_1 MACADDR8,              -- MAC address (EUI-64 format)
    macaddr8_col_2 MACADDR8,

    -- Bit String Types
    bit_col_1 BIT(8),                     -- Fixed-length bit string
    bit_col_2 BIT(8),
    varbit_col_1 BIT VARYING(16),         -- Variable-length bit string
    varbit_col_2 BIT VARYING(16),

    -- XML Type
    xml_col_1 XML,                        -- XML data
    xml_col_2 XML,

    -- Full-Text Search Types
    tsvector_col_1 TSVECTOR,              -- Full-text search vector
    tsvector_col_2 TSVECTOR,
    tsquery_col_1 TSQUERY,                -- Full-text search query
    tsquery_col_2 TSQUERY,

    -- Logical Replication Types
    txid_col_1 TXID_SNAPSHOT,             -- Transaction ID snapshot
    txid_col_2 TXID_SNAPSHOT
);


INSERT INTO sample_temp_table (
    small_int_col_1, small_int_col_2,
    integer_col_1, integer_col_2,
    big_int_col_1, big_int_col_2,
    decimal_col_1, decimal_col_2,
    numeric_col_1, numeric_col_2,
    real_col_1, real_col_2,
    double_col_1, double_col_2,
    serial_col_1, bigserial_col_1,
    money_col_1, money_col_2,
    char_col_1, char_col_2,
    varchar_col_1, varchar_col_2,
    text_col_1, text_col_2,
    date_col_1, date_col_2,
    time_col_1, time_col_2,
    time_tz_col_1, time_tz_col_2,
    timestamp_col_1, timestamp_col_2,
    timestamp_tz_col_1, timestamp_tz_col_2,
    interval_col_1, interval_col_2,
    boolean_col_1, boolean_col_2,
    uuid_col_1, uuid_col_2,
    json_col_1, json_col_2,
    jsonb_col_1, jsonb_col_2,
    array_col_1, array_col_2,
    int_range_col_1, int_range_col_2,
    ts_range_col_1, ts_range_col_2,
    tstz_range_col_1, tstz_range_col_2,
    date_range_col_1, date_range_col_2,
    point_col_1, point_col_2,
    line_col_1, line_col_2,
    lseg_col_1, lseg_col_2,
    box_col_1, box_col_2,
    path_col_1, path_col_2,
    polygon_col_1, polygon_col_2,
    circle_col_1, circle_col_2,
    cidr_col_1, cidr_col_2,
    inet_col_1, inet_col_2,
    macaddr_col_1, macaddr_col_2,
    macaddr8_col_1, macaddr8_col_2,
    bit_col_1, bit_col_2,
    varbit_col_1, varbit_col_2,
    xml_col_1, xml_col_2,
    tsvector_col_1, tsvector_col_2,
    tsquery_col_1, tsquery_col_2,
    txid_col_1, txid_col_2
)
VALUES
-- Row 1 (Example)
(1, 2,                          -- SMALLINT
 1000, 2000,                   -- INTEGER
 100000, 200000,               -- BIGINT
 123.45, 678.90,               -- DECIMAL
 98765.4321, 54321.9876,       -- NUMERIC
 1.23, 4.56,                   -- REAL
 3.14159, 2.71828,             -- DOUBLE PRECISION
 DEFAULT, DEFAULT,             -- SERIAL, BIGSERIAL
 '100.00', '200.00',         -- MONEY
 'A', 'B',                     -- CHAR
 'Hello', 'World',             -- VARCHAR
 'Sample text 1', 'Sample text 2',  -- TEXT
 '2024-01-01', '2024-12-31',   -- DATE
 '12:30:45', '23:59:59',       -- TIME
 '12:30:45+02', '23:59:59-05', -- TIME WITH TIME ZONE
 '2024-01-01 12:30:00', '2024-12-31 23:59:00', -- TIMESTAMP
 '2024-01-01 12:30:00+02', '2024-12-31 23:59:00-05', -- TIMESTAMP WITH TIME ZONE
 '1 day', '2 hours',           -- INTERVAL
 TRUE, FALSE,                  -- BOOLEAN
 gen_random_uuid(), gen_random_uuid(), -- UUID
 '{"key": "value"}', '{"array": [1, 2, 3]}', -- JSON
 '{"nested": {"key": "value"}}', '{"bool": true}', -- JSONB
 ARRAY[1, 2, 3], ARRAY[4, 5, 6], -- ARRAY
 '[1,10]', '[20,30]',           -- INT4RANGE
 '[2024-01-01,2024-12-31)', '[2025-01-01,2025-12-31)', -- TSRANGE
 '[2024-01-01 12:00:00+00,2024-12-31 12:00:00+00)', '[2025-01-01 12:00:00+00,2025-12-31 12:00:00+00)', -- TSTZRANGE
 '[2024-01-01,2024-12-31]', '[2025-01-01,2025-12-31]', -- DATERANGE
 '(1,1)', '(2,2)',             -- POINT
 '{1,2,3}', '{4,5,6}',         -- LINE
 '[(1,1),(2,2)]', '[(3,3),(4,4)]', -- LSEG
 '(1,1),(2,2)', '(3,3),(4,4)', -- BOX
 '((0,0),(1,1))', '((1,1),(2,2))', -- PATH
 '((0,0),(1,1),(1,0),(0,1))', '((1,1),(2,2),(2,1),(1,2))', -- POLYGON
 '<(0,0),1>', '<(1,1),2>',     -- CIRCLE
 '192.168.0.0/24', '10.0.0.0/8', -- CIDR
 '192.168.1.1', '10.0.0.1',    -- INET
 '08:00:2b:ff:01:02', '08:00:2b:ff:01:03', -- MACADDR
 '08:00:2b:ff:fe:01:02:03', '08:00:2b:ff:fe:01:02:04', -- MACADDR8
 B'10101010', B'11110000',     -- BIT
 B'1010', B'1111',             -- VARBIT
 '<tag>XML 1</tag>', '<tag>XML 2</tag>', -- XML
 'a fat cat', 'the quick brown', -- TSVECTOR
 'cat', 'quick & brown',       -- TSQUERY
 txid_current_snapshot(), txid_current_snapshot()              -- TXID
);


select * from sample_temp_table;
/*
In PostgreSQL, you can use the inet_server_addr() function to get the IP address of the server's local listening interface. 
This function returns the IP address of the server for the current connection as an inet type. 
If you want the loopback IP address (127.0.0.1), you can use:
*/
SELECT inet_server_addr(); --
/*
To Ensure 127.0.0.1:
If you explicitly want the loopback address (127.0.0.1) regardless of the server's actual IP configuration, use:
*/
SELECT '127.0.0.1'::inet;

1. Database Name
Use the built-in function current_database():

SELECT current_database();

2. Port Number
Use the built-in function inet_server_port():

SELECT inet_server_port();

3. Username
Use the built-in function current_user or session_user:

SELECT current_user;

4. Password
Passwords are not retrievable from the PostgreSQL server, as they are securely hashed and stored in the pg_authid catalog table. 
Only superusers can access this table, but even then, only hashed values are visible. To manage passwords:

Use ALTER USER to reset a password if necessary:

ALTER USER username WITH PASSWORD 'new_password';

SELECT
    current_database() AS database_name,
    inet_server_port() AS port_number,
    current_user AS username;


