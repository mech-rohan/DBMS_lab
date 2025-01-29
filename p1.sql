-- Disable safe update mode temporarily
SET SQL_SAFE_UPDATES = 0;

-- Create the table
CREATE TABLE student4 (
    roll_no VARCHAR(15), 
    name CHAR(50), 
    dept VARCHAR(25), 
    no_of_courses INT
);

-- Check table structure
DESC student4;

-- Insert data into the table
INSERT INTO student4 (roll_no, name, dept, no_of_courses)  
VALUES ("1/23/SET/196", "Rohan", "CSE", 10);

-- Select data from the correct table (student4)
SELECT * FROM student4;

-- Re-enable safe update mode
SET SQL_SAFE_UPDATES = 1;
