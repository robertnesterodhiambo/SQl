-- Connect to PostgreSQL in the psql terminal
CREATE DATABASE test_db;

-- Connect to test_db in the psql terminal or execute through a Python script
\c test_db;

-- Create customer table
CREATE TABLE customer (
    c_custkey SERIAL PRIMARY KEY,
    c_name VARCHAR(50),
    c_address VARCHAR(100),
    c_nationkey INT,
    c_phone VARCHAR(15),
    c_acctbal DECIMAL(10, 2)
);

-- Create orders table
CREATE TABLE orders (
    o_orderkey SERIAL PRIMARY KEY,
    o_custkey INT REFERENCES customer (c_custkey),
    o_orderstatus CHAR(1),
    o_totalprice DECIMAL(10, 2),
    o_orderdate DATE
);

-- Insert dummy data into customer
INSERT INTO customer (c_name, c_address, c_nationkey, c_phone, c_acctbal)
VALUES 
('Customer A', '123 Elm St', 1, '555-1234', 1000.00),
('Customer B', '456 Maple St', 2, '555-5678', 1500.00);

-- Insert dummy data into orders
INSERT INTO orders (o_custkey, o_orderstatus, o_totalprice, o_orderdate)
VALUES 
(1, 'O', 500.00, '2023-01-01'),
(2, 'F', 800.00, '2023-02-15');
