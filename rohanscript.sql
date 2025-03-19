<!--
 * Title:          <code> saveScript.jsp   </code> <BR> 
 * Description:    Handler to set content 
 * 
 * <BR> 
 * Date:           23 JAN 2002               <BR> 
 * <p> 
 * Company:        Oracle <BR> 
 * Copyright:      Copyright (c) 2002, 2003 
 *                 All rights reserved. 
 * 
 * @author  Marcus Pecher 
 * @version 1.0 
 * 
 * MODIFIED   (MM/DD/YY)
 *   asamuel   12/05/03 - softcoding save mime type
 *   agoggin   10/10/03 - Add support for 'hiding' input (bug 2905440)

-->

CREATE TABLE emp1(
    empid number(10) PRIMARY KEY,
                
    name VARCHAR2(100) NOT NULL,              
    dept VARCHAR2(50)  ,
    FOREIGN KEY(empid) REFERENCES Account1 (empid));

create table Account1(empid number(10) PRIMARY KEY , salary number(10) , check (salary > 0));

desc emp1;
desc Account1 ;



INSERT INTO Account1 (empid, salary) 
VALUES (1, 15000);

INSERT INTO Account1 (empid, salary) 
VALUES (2, 12000);

INSERT INTO Account1 (empid, salary) 
VALUES (3, 18000);

SELECT * FROM Account1;


SELECT empid, salary 
FROM Account1
WHERE salary > 0;



