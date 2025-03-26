CREATE TABLE customer (
    c_id INT PRIMARY KEY,
    c_name VARCHAR(50),
    addr VARCHAR(50)
);

CREATE TABLE orders (
    o_id INT PRIMARY KEY,
    o_name VARCHAR(50),
    c_id INT  
);

INSERT INTO customer VALUES 
(1, 'Aman', 'Delhi'),
(2, 'Rohan', 'Mumbai'),
(3, 'Sanjay', 'Kolkata'),
(4, 'Dev', 'Pune'),
(5, 'Kiran', 'Chennai');

INSERT INTO orders VALUES 
(101, 'Laptop', 1),
(102, 'Phone', 2),
(103, 'Tablet', 3),
(104, 'Mouse', 6),  
(105, 'Chair', NULL);

SELECT * FROM customer;
SELECT * FROM orders;

-- IINER JOIN
SELECT customer.c_id, customer.c_name, orders.o_id, orders.o_name
FROM customer
INNER JOIN orders ON customer.c_id = orders.c_id;

-- LEFT JOIN 
SELECT customer.c_id, customer.c_name, orders.o_id, orders.o_name
FROM customer
LEFT JOIN orders ON customer.c_id = orders.c_id;

-- RIGHT JOIN 
SELECT customer.c_id, customer.c_name, orders.o_id, orders.o_name
FROM customer
RIGHT JOIN orders ON customer.c_id = orders.c_id;

-- LEFT JOIN where customer 2 is null
SELECT customer.c_id, customer.c_name
FROM customer
LEFT JOIN orders ON customer.c_id = orders.c_id
WHERE orders.o_id IS NULL;

--  RIGHT JOIN (WHERE Customers Are NULL)
SELECT orders.o_id, orders.o_name
FROM customer
RIGHT JOIN orders ON customer.c_id = orders.c_id
WHERE customer.c_id IS NULL;

-- FULL OUTER JOIN 
SELECT customer.c_id, customer.c_name, customer.addr, orders.o_id, orders.o_name, orders.c_id
FROM customer
LEFT JOIN orders ON customer.c_id = orders.c_id

UNION

SELECT customer.c_id, customer.c_name, customer.addr, orders.o_id, orders.o_name, orders.c_id
FROM customer
RIGHT JOIN orders ON customer.c_id = orders.c_id;

-- full outer join where a key is null or b key isnull

SELECT customer.c_id, customer.c_name, customer.addr, orders.o_id, orders.o_name, orders.c_id
FROM customer
LEFT JOIN orders ON customer.c_id = orders.c_id
WHERE orders.o_id IS NULL

UNION

SELECT customer.c_id, customer.c_name, customer.addr, orders.o_id, orders.o_name, orders.c_id
FROM customer
RIGHT JOIN orders ON customer.c_id = orders.c_id
WHERE customer.c_id IS NULL;











