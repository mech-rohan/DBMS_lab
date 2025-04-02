-- grouping clauses in sql
-- grouping2april

CREATE TABLE customers (
    custID INT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(50)
);

INSERT INTO customers (custID, name, country)
VALUES 
(1, 'Rohan', 'India'),
(2, 'Jishu', 'India'),
(3, 'Charlie', 'Canada'),
(4, 'David', 'USA'),
(5, 'Elon', 'Canada'),
(6, 'Frank', 'USA'),
(7, 'Grace', 'USA'),
(8, 'Aman', 'India'),
(9, 'Ivy', 'USA'),
(10, 'Sanjay', 'India');

-- step1
SELECT COUNT(custID), country 
FROM customers 
GROUP BY country;

-- step2
SELECT COUNT(custID), country 
FROM customers 
GROUP BY country 
HAVING COUNT(custID) > 2;

-- step 3
SELECT COUNT(custID), country 
FROM customers 
GROUP BY country 
HAVING COUNT(custID) > 2 
ORDER BY COUNT(custID) ASC, country DESC;

-- step 4 
CREATE VIEW custview AS 
SELECT * FROM customers;

-- step 5
DROP VIEW custview;

SELECT * FROM customers;
