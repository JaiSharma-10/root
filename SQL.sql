Links

udemy

HackerRank

HackerEarth

LeetCode

Learn to Code | CodesDope

CCNA 200-301 Cert Guide, Volume 1 eBook and Practice Test.pdf - Google Drive

Databricks Learning
​
Daily Tracker


AZ-900 Microsoft Azure Fundamentals

Google IT Automation with Python Professional Certificate

CompTIA A+

Databricks Certified Professional Data Engineer

Databricks Certified Associate Data Engineer

Databricks Certified Associate Data Analyst         

Databricks Certified Associate Machine Learning

Databricks Certified Professional Machine Learning         

Databricks - Solution Architect Essentials Badge - [301-ADVANCED]          

Certified Tester Expert Level Assessing Test Processes (CTEL-ITP-ATP)       

Japanese- Language Proficiency Test (JLPT) Level N5        

Machine Learning - Foundation Certificate          

Data Scientist

JavaScript ES6 {101 - BASICS]

Python for Analytics

Python Programming for Beginners Using AI and ML       

PCAP - Python Certified Associate in Python Programming           

Programming with Python 3.x

Google Cloud - Professional Cloud DevOps Engineer        

Exam AZ-400 : Microsoft Azure DevOps Solutions             

Google - Professional Cloud Security Engineer    

Google - Professional Cloud Network Engineer   

Google - Professional Cloud Developer  

certificate program in c & c++ programming       

Programming with JavaScript

GOOGLE CLOUD CERTIFIED - Professiona

Google Cloud Associate Cloud Engineer 

Advance SQL

German language A1/2 Basic

German B1.2

 


======================================================================================================================================

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

======================================================================================================================================

==SQL

===================================SQL QUESTION- Hackerrank

Unique value count

/*select count(City) as total_number_of_record

from station;*/

select count(distinct city) from station;

 

select LENGTH("jaivardhan");  -- in MySQL

 

QUESTION-

Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

The STATION table is described as follows:

where LAT_N is the northern latitude and LONG_W is the western longitude.

Sample Input

For example, CITY has four entries: DEF, ABC, PQRS and WXY.

Sample Output

ABC 3

PQRS 4

Explanation

When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths  and . The longest name is PQRS, but there are  options for shortest named city. Choose ABC, because it comes first alphabetically.

 

Solution-

(select city,LENGTH(city)

from station

order by

LENGTH(city) asc

,city asc

limit 1)

 

union all

 

(select city,LENGTH(city)

from station

order by

LENGTH(city) desc

,city desc

limit 1);

 

 

Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

Solution-

select distinct city

from station

where substring(city,1,1) = 'a'

or substring(city,1,1)='e'

or substring(city,1,1)='i'

or substring(city,1,1)='o'

or substring(city,1,1)='u'

 

 

Query the list of CITY names lasting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

Solution-

select distinct city

from

station

where

substring(city,length(city),length(city)) = 'a'

or substring(city,length(city),length(city)) = 'e'

or substring(city,length(city),length(city)) = 'i'

or substring(city,length(city),length(city)) = 'o'

or substring(city,length(city),length(city)) = 'u'

 

Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

solution-

select distinct city

from station

where substring(city,1,1) not in ('a')

and substring(city,1,1) not in ('e')

and substring(city,1,1) not in ('i')

and substring(city,1,1) not in ('o')

and substring(city,1,1) not in ('u')

 

Query the list of CITY names from STATION that do not start with vowels and do not end with vowels

solution

select distinct city

from station

where

substring(city,1,1) not in ('a')

and substring(city,1,1) not in ('e')

and substring(city,1,1) not in ('i')

and substring(city,1,1) not in ('o')

and substring(city,1,1) not in ('u')

and

substring(city,length(city),length(city)) not in ('a')

and substring(city,length(city),length(city)) not in ('e')

and substring(city,length(city),length(city)) not in ('i')

and substring(city,length(city),length(city)) not in ('o')

and substring(city,length(city),length(city)) not in ('u')

 

 

Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

solution-

Enter your query here.

*/

select Name

from Students

where marks>75

order by

substring(Name,Length(Name)-2, Length(Name)) asc

,ID asc

 

Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.

solution-

select round(long_w,4)

from station

where

truncate(lat_n,4) <= 137.2345

order by lat_n desc

limit 1;

 

 

NOTE TO SELF

ABOUT JOIN WHEN YOU DO NOT PROVIDE ANY CONDITION ON THE JOIN IT WILL CROSS JOIN IT AND WILL PROVIDE N*M RESULTS OF ROWS FOR TABLE A (N rows)JOIN TABLE B(M rows)

 

--Joins

--question

 

Table: Employees

 

+---------------+---------+

| Column Name   | Type    |

+---------------+---------+

| id            | int     |

| name          | varchar |

+---------------+---------+

id is the primary key (column with unique values) for this table.

Each row of this table contains the id and the name of an employee in a company.

 

Table: EmployeeUNI

 

+---------------+---------+

| Column Name   | Type    |

+---------------+---------+

| id            | int     |

| unique_id     | int     |

+---------------+---------+

(id, unique_id) is the primary key (combination of columns with unique values) for this table.

Each row of this table contains the id and the corresponding unique id of an employee in the company.

 

Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

 

Return the result table in any order.

 

The result format is in the following example.

 

 

Example 1:

 

Input:

Employees table:

+----+----------+

| id | name     |

+----+----------+

| 1  | Alice    |

| 7  | Bob      |

| 11 | Meir     |

| 90 | Winston  |

| 3  | Jonathan |

+----+----------+

EmployeeUNI table:

+----+-----------+

| id | unique_id |

+----+-----------+

| 3  | 1         |

| 11 | 2         |

| 90 | 3         |

+----+-----------+

Output:

+-----------+----------+

| unique_id | name     |

+-----------+----------+

| null      | Alice    |

| null      | Bob      |

| 2         | Meir     |

| 3         | Winston  |

| 1         | Jonathan |

+-----------+----------+

Explanation:

Alice and Bob do not have a unique ID, We will show null instead.

The unique ID of Meir is 2.

The unique ID of Winston is 3.

The unique ID of Jonathan is 1.

 

--solution

# Write your MySQL query statement below

select COALESCE(unique_id,0) , name --calesce when null to be replaced

from

Employees emp

left outer join

EmployeeUNI uni

on emp.id = uni.id

 

 

1581. Customer Who Visited but Did Not Make Any Transactions

Easy

Topics

Companies

SQL Schema

Pandas Schema

Table: Visits

 

+-------------+---------+

| Column Name | Type    |

+-------------+---------+

| visit_id    | int     |

| customer_id | int     |

+-------------+---------+

visit_id is the column with unique values for this table.

This table contains information about the customers who visited the mall.

 

Table: Transactions

 

+----------------+---------+

| Column Name    | Type    |

+----------------+---------+

| transaction_id | int     |

| visit_id       | int     |

| amount         | int     |

+----------------+---------+

transaction_id is column with unique values for this table.

This table contains information about the transactions made during the visit_id.

 

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

 

Return the result table sorted in any order.

 

The result format is in the following example.

 

 

Example 1:

 

Input:

Visits

+----------+-------------+

| visit_id | customer_id |

+----------+-------------+

| 1        | 23          |

| 2        | 9           |

| 4        | 30          |

| 5        | 54          |

| 6        | 96          |

| 7        | 54          |

| 8        | 54          |

+----------+-------------+

Transactions

+----------------+----------+--------+

| transaction_id | visit_id | amount |

+----------------+----------+--------+

| 2              | 5        | 310    |

| 3              | 5        | 300    |

| 9              | 5        | 200    |

| 12             | 1        | 910    |

| 13             | 2        | 970    |

+----------------+----------+--------+

Output:

+-------------+----------------+

| customer_id | count_no_trans |

+-------------+----------------+

| 54          | 2              |

| 30          | 1              |

| 96          | 1              |

+-------------+----------------+

Explanation:

Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.

Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.

Customer with id = 30 visited the mall once and did not make any transactions.

Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.

Customer with id = 96 visited the mall once and did not make any transactions.

As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.

 

 

===================================solution

--query using derived table

select customer_id

                ,count(customer_id) as count_no_trans

from

              Visits

              where visit_id    not in

              (

              select visit_id from Transactions

              )

    group by customer_id

 

 

 

 

============CASE Conditions

SELECT OrderID, Quantity,

CASE

    WHEN Quantity > 30 THEN 'The quantity is greater than 30'

    WHEN Quantity = 30 THEN 'The quantity is 30'

    ELSE 'The quantity is under 30'

END AS QuantityText

FROM OrderDetails;

 

 

Nested CASE statements in SQL

One of the advanced use-cases for CASE statements in SQL is to nest CASE statements within another CASE statement. This technique is useful when you have sub-conditions that need to be evaluated.

 

SELECT personID, lastName, firstName, [state],

CASE

              WHEN [state] = 'Minnesota'

              THEN (CASE WHEN income > 100000 THEN 'over'

                                           ELSE 'not over' END)

              WHEN [state] = 'California'

THEN (CASE WHEN income > 150000 THEN 'over'

                                           ELSE 'not over' END)

              WHEN [state] = 'Kentucky'

THEN (CASE WHEN income > 75000 THEN 'over'

                                           ELSE 'not over' END)

END over_income

FROM #Temp_table

 

 

 

It is possible to use CASE to filter data in the WHERE clause of a SQL query. This can be helpful if you want to restrict records based on logical conditions.

 

SELECT personID, lastName, firstName, [state]

FROM #Temp_table

where(

CASE

              WHEN [state] = 'Minnesota' AND Income >= 100000 THEN 'MN'

              WHEN [state] = 'California' THEN 'CA'

              WHEN [state] = 'Kentucky' THEN 'KY'

END) = 'MN'

 

 

Aggregating using CASE statements in SQL

One of the popular ways to use the CASE statement in SQL is for counting records that would be cumbersome to transpose using a count() function. For example, say we want to output a single row result set that returns the number of records from each state where the income is greater than or equal to 100,000:

 

select sum(CASE

                             WHEN [state] = 'Minnesota' and income >= 100000 THEN 1

                             ELSE 0

                             END) MN_counts,

              sum(CASE WHEN [state] = 'California' and income >= 100000 THEN 1

                             ELSE 0

                             END) CA_counts,

              sum(CASE WHEN [state] = 'Kentucky' and income >= 100000 THEN 1

                             ELSE 0

                             END) KY_counts

from #temp_table

 

 

 

 

Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table

Values in the tuple  form an Isosceles triangle, because .

Values in the tuple  form an Equilateral triangle, because . Values in the tuple  form a Scalene triangle, because .

Values in the tuple  cannot form a triangle because the combined value of sides  and  is not larger than that of side .

 

--SOLUTION

select

case

    when A+B <= C then "Not A Triangle"

    when B+C <= A then "Not A Triangle"

    when C+A <= B then "Not A Triangle"

    else

        case

            when A=B and B=C and C=A then "Equilateral" 

            when A=B or B=C or C=A then "Isosceles"

            when A!=B and B!=C and C!=A then "Scalene" end     

End

from TRIANGLES

;

 

 

--QUESTION-

Generate the following two result sets:

 

Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).

Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:

 

There are a total of [occupation_count] [occupation]s.

where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.

 

Note: There will be at least two entries in the table for each type of occupation.

 

Input Format

 

The OCCUPATIONS table is described as follows:  Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.

 

Sample Input

 

An OCCUPATIONS table that contains the following records:

 

 

 

Sample Output

 

Ashely(P)

Christeen(P)

Jane(A)

Jenny(D)

Julia(A)

Ketty(P)

Maria(A)

Meera(S)

Priya(S)

Samantha(D)

There are a total of 2 doctors.

There are a total of 2 singers.

There are a total of 3 actors.

There are a total of 3 professors.

Explanation

 

The results of the first query are formatted to the problem description specifications.

The results of the second query are ascendingly ordered first by number of names corresponding to each profession (), and then alphabetically by profession (, and ).

 

 

 

============SOLUTION 2

/*

Enter your query here.

*/

select

case

    when occupation = "Doctor" then concat(name,"(D)")

    when occupation = "Professor" then concat(name,"(P)")

    when occupation = "Singer" then concat(name,"(S)")

    when occupation = "Actor" then concat(name,"(A)")

    else "none"

end

from OCCUPATIONS

order by occupation

 

union all

 

select

    concat("There are a total of ",sum(case when occupation = "Doctor" then 1 else 0 end)," doctors.")

from OCCUPATIONS

 

union all

 

select

     concat("There are a total of ",sum(case when occupation ="singer" then 1 else 0 end) ," singers.")

from OCCUPATIONS

 

union all

 

select

    concat("There are a total of ",sum(case when occupation = "Actor" then 1 else 0 end) ," actors.")

from OCCUPATIONS

 

union all

 

select

    concat("There are a total of ",sum(case when occupation ="professor" then 1 else 0 end) ," professors.")

from OCCUPATIONS

================================================

--ongoing

 

 

 

 

 

-- STORED PROCEDURE EXAMPLE OF DECLARING VALUE AND USING IT

  CREATE PROCEDURE proc_vars()

  SPECIFIC proc_vars

  LANGUAGE SQL

  BEGIN

    

    DECLARE v_rcount INTEGER;

 

    DECLARE v_max DECIMAL (9,2);

 

    DECLARE v_adate, v_another  DATE;                                  

 

    DECLARE v_total INTEGER DEFAULT 0;           -- (1)

 

    DECLARE v_rowsChanged BOOLEAN DEFAULT FALSE; -- (2)

 

    SET v_total = v_total + 1;                   -- (3)

             

    SELECT MAX(salary)                           -- (4)

      INTO v_max FROM employee;                                           

 

    VALUES CURRENT_DATE INTO v_date;             -- (5)

 

    SELECT CURRENT DATE, CURRENT DATE            -- (6)

         INTO v_adate, v_another

    FROM SYSIBM.SYSDUMMY1;

 

    DELETE FROM T;

    GET DIAGNOSTICS v_rcount = ROW_COUNT;        -- (7)

 

    IF v_rcount > 0 THEN                         -- (8)

      SET is_done = TRUE;

    END IF;

  END

 

  

========================================CTE

What are Common Table Expressions (CTEs)?

A Common Table Expression (CTE) is the result set of a query which exists temporarily and for use only within the context of a larger query. Much like a derived table, the result of a CTE is not stored and exists only for the duration of the query.

 

=Example use cases include

1.Needing to reference a derived table multiple times in a single query

2.An alternative to creating a view in the database

3.Performing the same calculation multiple times over across multiple query components

 

-- define CTE:

WITH Cost_by_Month AS

(SELECT campaign_id AS campaign,

       TO_CHAR(created_date, 'YYYY-MM') AS month,

       SUM(cost) AS monthly_cost

FROM marketing

WHERE created_date BETWEEN NOW() - INTERVAL '3 MONTH' AND NOW()

GROUP BY 1, 2

ORDER BY 1, 2)

 

-- use CTE in subsequent query:

SELECT campaign, avg(monthly_cost) as "Avg Monthly Cost"

FROM Cost_by_Month

GROUP BY campaign

ORDER BY campaign

 

--example

with derived_table AS

(select

        sum(case when occupation = "Doctor" then 1 else 0 end) as d,

        sum(case when occupation ="singer" then 1 else 0 end) as s,

        sum(case when occupation = "Actor" then 1 else 0 end) as a,

        sum(case when occupation ="professor" then 1 else 0 end) p

        from OCCUPATIONS)

                            

select d,s,a,p from derived_table;

 

--Using a derived query:

SELECT campaign, avg(monthly_cost) as "Avg Monthly Cost"

FROM

    -- this is where the derived query is used

    (SELECT campaign_id AS campaign,

       TO_CHAR(created_date, 'YYYY-MM') AS month,

       SUM(cost) AS monthly_cost

    FROM marketing

    WHERE created_date BETWEEN NOW() - INTERVAL '3 MONTH' AND NOW()

    GROUP BY 1, 2

    ORDER BY 1, 2) as Cost_By_Month

GROUP BY campaign

ORDER BY campaign

 

--ERROR 1248 (42000) at line 1: Every derived table must have its own alias

 

--example

select d,s,a,p

FROM

    (

        select

        sum(case when occupation = "Doctor" then 1 else 0 end) as d,

        sum(case when occupation ="singer" then 1 else 0 end) as s,

        sum(case when occupation = "Actor" then 1 else 0 end) as a,

        sum(case when occupation ="professor" then 1 else 0 end) p,

        from OCCUPATIONS

    )

    as derived_table;

select d,s,a,p

from derived_table;

 

 

There are two types of CTEs: Recursive and Non-Recursive

 

Non-Recursive: where the CTE doesn’t use any recursion, or repeated processing in of a sub-routine.

 

;with ROWCTE(ROWNO) as  -- ROWNO is column name it is optional

   ( 

     SELECT

  ROW_NUMBER() OVER(ORDER BY name ASC) AS ROWNO

FROM sys.databases

WHERE database_id <= 10

    ) 

 

SELECT * FROM ROWCTE

 

 

Recursive CTE:

Recursive CTEs are use repeated procedural loops aka recursion. The recursive query call themselves until the query satisfied the condition. In a recursive CTE we should provide a where condition to terminate the recursion.

 

Declare @RowNo int =1;

;with ROWCTE as 

   ( 

      SELECT @RowNo as ROWNO   

                             UNION ALL 

      SELECT  ROWNO+1 

  FROM  ROWCTE 

  WHERE RowNo < 10

    ) 

 

SELECT * FROM ROWCTE

 


====================SOLUTION 2

 

 

select

case

    when occupation = "Doctor" then concat(name,"(D)")

    when occupation = "Professor" then concat(name,"(P)")

    when occupation = "Singer" then concat(name,"(S)")

    when occupation = "Actor" then concat(name,"(A)")

    else "none"

end

from OCCUPATIONS

order by name asc;

 

 

 

with derived_table AS

(

select occupation,count(occupation) as cnt

from OCCUPATIONS

group by occupation

order by

count(occupation) asc,

occupation asc

)

select

concat("There are a total of " , cnt ," ", lower(occupation) ,"s.")

from derived_table;

 

===================================

--done

 

===================================Best solution 3

select

case

    when occupation = "Doctor" then concat(name,"(D)")

    when occupation = "Professor" then concat(name,"(P)")

    when occupation = "Singer" then concat(name,"(S)")

    when occupation = "Actor" then concat(name,"(A)")

    else "none"

end

from OCCUPATIONS

order by name asc;

 

select concat("There are a total of " , count(occupation) ," ", lower(occupation) ,"s.")

from OCCUPATIONS

group by occupation

order by

count(occupation) asc,

occupation asc

 


====================================Pivot

-----QUESTION-

 

 

Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

 

Note: Print NULL when there are no more names corresponding to an occupation.

 

Input Format

 

The OCCUPATIONS table is described as follows:

 

Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.

 

Sample Output

 

Jenny    Ashley     Meera  Jane

Samantha Christeen  Priya  Julia

NULL     Ketty      NULL   Maria

Explanation

 

The first column is an alphabetically ordered list of Doctor names.

The second column is an alphabetically ordered list of Professor names.

The third column is an alphabetically ordered list of Singer names.

The fourth column is an alphabetically ordered list of Actor names.

The empty cell data for columns with less than the maximum number of names per occupation (in this case, the Professor and Actor columns) are filled with NULL values.

 

 

 

 

---------WHAT IS PIVOT

In a pivot query, you specify the columns that you want to pivot on, as well as the aggregate function(s) that you want to apply to the values in those columns. The result of the query is a new table with the pivoted columns as its headers.

 

Assuming you have a sample table called sales_data with the following columns and data:

 

Product Name   Sales Date          Sales Amount

Product A                          2022-01-01        500

Product B                          2022-01-01        750

Product C                          2022-01-01        1000

Product A                          2022-01-02        800

Product B                          2022-01-02        900

Product C                          2022-01-02        1200

To pivot this data by Product Name, you can use the following query:

 

Code:

SELECT

  `Sales Date`,

  MAX(CASE WHEN `Product Name` = 'Product A' then `Sales Amount` END) AS `Product A`,

  MAX(CASE WHEN `Product Name` = 'Product B' then `Sales Amount` END) AS `Product B`,

  MAX(CASE WHEN `Product Name` = 'Product C' than `Sales Amount` END) AS `Product C`

FROM

  `sales_data`

GROUP BY

  `Sales Date`;

 

Output

Sales Date          Product A           Product B           Product C

2022-01-01        500                   750                 1000

2022-01-02        800                   900                 1200

 

 

---Dynamic Pivot Columns

Assuming you have a sample table called sales_data with the following columns and data:

 

Product Name   Sales Date          Sales Amount

Product A                          2022-01-01        500

Product B                          2022-01-01        750

Product C                          2022-01-01        1000

Product A                          2022-01-02        800

Product B                          2022-01-02        900

Product C                          2022-01-02        1200

Product D                         2022-01-02        1500

To pivot this data by Product Name, you can use dynamic pivot columns with the following query:

 

Code:

SET @sql = NULL;

SELECT

  GROUP_CONCAT(DISTINCT

    CONCAT('MAX(CASE WHEN `Product Name` = ''', `Product Name`, ''' THEN `Sales Amount` END) AS `', `Product Name`, '`')

  ) INTO @sql

FROM

  `sales_data`;

 

SET @sql = CONCAT('SELECT `Sales Date`, ', @sql, ' FROM `sales_data` GROUP BY `Sales Date`');

 

PREPARE stmt FROM @sql;

EXECUTE stmt;

DEALLOCATE PREPARE stmt;

 

---The GROUP_CONCAT() function in MySQL is used to concatenate data from multiple rows into one field. This is an aggregate (GROUP BY) function that returns a String value if the group contains at least one non-NULL value. Otherwise, it returns NULL.

 

Output:

The output will be:

 

Sales Date          Product A           Product B           Product C           Product D

2022-01-01        500                   750                 1000                  NULL

2022-01-02        800                   900                 1200                  1500

 

 

--explaination

In this query, the first SELECT statement uses GROUP_CONCAT to dynamically generate the pivot columns based on the distinct Product Name values in the sales_data table.

 

The generated SQL statement is then stored in a user-defined variable @sql. The PREPARE statement is used to prepare the SQL statement in @sql, and the EXECUTE statement is used to execute the prepared statement. Finally, the DEALLOCATE PREPARE statement is used to deallocate the prepared statement.

 

This query will pivot the data so that Product Name becomes the column header, Sales Date becomes the row header, and the Sales Amount is the data associated with each Product Name and Sales Date combination. The dynamic pivot columns allow for flexibility in column values, making it easy to pivot data with unknown or varying column values.

 

 

 

-----SOLUTION

/*

Enter your query here.

*/

-- select

-- (case when OCCUPATION='Doctor' then name end) as Doctor

-- from OCCUPATIONS

-- ;

-- select name

-- from OCCUPATIONS

-- where OCCUPATION='Doctor';

 

-- select name

-- from OCCUPATIONS

-- where OCCUPATION='Professor';

 

-- select name

-- from OCCUPATIONS

-- where OCCUPATION='Singer';

 

-- select name

-- from OCCUPATIONS

-- where OCCUPATION='Actor';

select distinct d1.doctor,d2.Professor

from

(

 select name as doctor

from OCCUPATIONS

where OCCUPATION='Doctor') as d1

join

(

select name as Professor

from OCCUPATIONS

where OCCUPATION='Professor') as d2;

 

-- select Doctor,Professor,Singer,Actor

-- from

--     (

--     select

--      (case when OCCUPATION='Doctor' then name end) as Doctor,

--      (case when OCCUPATION='Professor' then name end) as Professor,

--      (case when OCCUPATION='Singer' then name end) as Singer,

--      (case when OCCUPATION='Actor' then name end) as Actor

--     from OCCUPATIONS

--      )

--      as derived_table

-- (case when OCCUPATION='Professor' then name end) as Professor

 

==ongoing

 

 

===================================

FROM - Using PIVOT and UNPIVOT

Pivot operator converts the rows data of the table into the column data. The Unpivot operator does the opposite

--syntax pivot

SELECT (ColumnNames)

FROM (TableName)

PIVOT

(

   AggregateFunction(ColumnToBeAggregated)

   FOR PivotColumn IN (PivotColumnValues)

) AS (Alias) //Alias is a temporary name for a table

--syntax unpivot

SELECT (ColumnNames)

FROM (TableName)

UNPIVOT

(

   AggregateFunction(ColumnToBeAggregated)

   FOR PivotColumn IN (PivotColumnValues)

) AS (Alias)

--EXAMPLE 1

COURSENAME                 COURSECATEGORY                 PRICE

C                          PROGRAMMING                    5000

JAVA                       PROGRAMMING                    6000

PYTHON                     PROGRAMMING                    8000

PLACEMENT100 			   INTERVIEWPREPARATION           5000

 

--example pivot

SELECT CourseName, PROGRAMMING, INTERVIEWPREPARATION

FROM geeksforgeeks

PIVOT

(

SUM(Price) FOR CourseCategory IN (PROGRAMMING, INTERVIEWPREPARATION )

) AS PivotTable

 

--example 1 pivot solution

COURSENAME                 PROGRAMMING             INTERVIEWPREPARATION

C                          5000                    NULL

JAVA                       6000                    NULL

PLACEMENT100 			   NULL                    5000

PYTHON                     8000                    NULL

 

--example 2 unpivot query

SELECT CourseName, CourseCategory, Price

FROM

(

SELECT CourseName, PROGRAMMING, INTERVIEWPREPARATION FROM geeksforgeeks

PIVOT

(

SUM(Price) FOR CourseCategory IN (PROGRAMMING, INTERVIEWPREPARATION)

) AS PivotTable

) P

UNPIVOT

(

Price FOR CourseCategory IN (PROGRAMMING, INTERVIEWPREPARATION)

)

AS UnpivotTable

 

--example 2 unpivot output

CourseName                    CourseCategory                             Price

C                             PROGRAMMING                                5000

JAVA                          PROGRAMMING                                6000

PLACEMENT100 				  INTERVIEWPREPARATION               		 5000

PYTHON                        PROGRAMMING                                8000

 

====================================================================================================================-+

--solution main                                                                                                                                                                                                                                                                                                                                                                          --+

SELECT Doctor, Professor, Singer, Actor FROM (                                                                                                                                                                                                                                                         --+

SELECT ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) as rn, name, occupation FROM occupations)                                    --+

PIVOT                                                                                                                                                                                                                                                                                                                                                                                                         --+

(MAX(name) FOR occupation IN ('Doctor' as Doctor,'Professor' as Professor, 'Singer' as Singer, 'Actor' as Actor))          --+

ORDER BY rn;                                                                                                                                                                                                                                                                                                                                                                             --+

====================================================================================================================--+

--this only worked in Oracle

--having doubts about this use of pivot keyword and window function

 

 

--explanation

SELECT ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) as rn, name, occupation FROM occupations

--ROW_NUMBER function PARTITION by occupation and ORDER By name 1,2,3,4 UNIQUE

SELECT rank() OVER (PARTITION BY occupation ORDER BY name) as rn, name, occupation FROM occupations

--RANK function PARTITION by occupation and ORDER By name 1,2,3,4 UNIQUE

1 Eve Actor

2 Jennifer Actor

3 Ketty Actor

4 Samantha Actor

1 Aamina Doctor

2 Julia Doctor

3 Priya Doctor

1 Ashley Professor

2 Belvet Professor

3 Britney Professor

4 Maria Professor

5 Meera Professor

6 Naomi Professor

7 Priyanka Professor

1 Christeen Singer

2 Jane Singer

3 Jenny Singer

4 Kristeen Singer

 

 

 

 

========================================================================================

You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

 

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

 

Root: If node is root node. --main nodes.

Leaf: If node is leaf node. --lower most nodes.

Inner: If node is neither root nor leaf node.  --middle node

 

Sample input

N            P

1            2

3            2

6            8

9            8

2            5

8            5

5            null

 

Sample Output

 

1 Leaf

2 Inner

3 Leaf

5 Root

6 Leaf

8 Inner

9 Leaf

 

Explanation

 

The Binary Tree below illustrates the sample

=====================================================Nodes of binary tree.

There are three types of nodes in a binary tree.

 

Root: The root node is the tree’s starting point. e,g node 5 is the root node in the above-shown tree.

Inner: An inner node is one that has a parent and at least one child. e,g nodes 2 and 8 are the inner nodes in the above-shown tree.

Leaf: The leaf node has a parent but no children nodes. It occurs at the last level of the tree. e,g nodes 1,3,6, and 9 are the leaf nodes in the above-shown tree.

 

=====================================================

 

Approach:

 

Logical Part: Identify Node: A node is a root if its parent is null.

A node is inner if it has a parent and at least one child. If a node occurs in the ‘n’ column as well as in the ‘p’ column then it is an inner node.

 

A node is a leaf if it never appears as a parent or it does not occur in the ‘p’ column.

 

=====================================================what is the Binary tree

A Binary Search Tree (BST) is a type of Binary Tree data structure, where the following properties must be true for any node "X" in the tree:

 

The X node's left child and all of its descendants (children, children's children, and so on) have lower values than X's value.

The right child, and all its descendants have higher values than X's value.

Left and right subtrees must also be Binary Search Trees.

These properties makes it faster to search, add and delete values than a regular binary tree.

 

To make this as easy to understand and implement as possible, let us also assume that all values in a Binary Search Tree are unique.

 

 

 

Use the Binary Search Tree below to better understand these concepts and relevant terminology.

 

The size of a tree is the number of nodes in it (n).

 

A subtree starts with one of the nodes in the tree as a local root, and consists of that node and all its descendants.

 

The descendants of a node are all the child nodes of that node, and all their child nodes, and so on. Just start with a node, and the descendants will be all nodes that are connected below that node.

 

The node's height is the maximum number of edges between that node and a leaf node.

 

A node's in-order successor is the node that comes after it if we were to do in-order traversal. In-order traversal of the BST above would result in node 13 coming before node 14, and so the successor of node 13 is node 14.

 

 

https://python.plainenglish.io/part-1-binary-tree-nodes-sql-question-6b14baf0ebf0

 

 

 

========================================================================================

197. Rising Temperature

Easy

Topics

Companies

SQL Schema

Pandas Schema

Table: Weather

 

+---------------+---------+

| Column Name   | Type    |

+---------------+---------+

| id            | int     |

| recordDate    | date    |

| temperature   | int     |

+---------------+---------+

id is the column with unique values for this table.

There are no different rows with the same recordDate.

This table contains information about the temperature on a certain day.

 

Write a solution to find all dates Id with higher temperatures compared to its previous dates (yesterday).

 

Return the result table in any order.

 

The result format is in the following example.

 

 

Example 1:

 

Input:

Weather table:

+----+------------+-------------+

| id | recordDate | temperature |

+----+------------+-------------+

| 1  | 2015-01-01 | 10          |

| 2  | 2015-01-02 | 25          |

| 3  | 2015-01-03 | 20          |

| 4  | 2015-01-04 | 30          |

+----+------------+-------------+

Output:

+----+

| id |

+----+

| 2  |

| 4  |

+----+

Explanation:

In 2015-01-02, the temperature was higher than the previous day (10 -> 25).

In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

 

 

=============================solution

--solu 1

select w.*,

lag(temperature) over () as lag_T

from Weather as w

 

--output

| id | recordDate | temperature | lag_T |

| -- | ---------- | ----------- | ----- |

| 1  | 2015-01-01 | 10          | null  |

| 2  | 2015-01-02 | 25          | 10    |

| 3  | 2015-01-03 | 20          | 25    |

| 4  | 2015-01-04 | 30          | 20    |

 

--solu final

select id

from

 

(select w.*,

lag(temperature) over () as lag_T

from Weather as w) as a

 

where temperature>lag_T -- lag_T is previous day temperature

 

--it is creating problems for example this input no output 7/14 testcases passed

 

| id | recordDate | temperature |

| -- | ---------- | ----------- |

| 1  | 2000-12-16 | 3           |

| 2  | 2000-12-15 | -1          |

 

--solution order by in over

 

select id

from

(select w.*,

lag(temperature) over (order by recordDate) as lag_T

from Weather as w) as a

where temperature>a.lag_T ;

 

| id | recordDate | temperature |

| -- | ---------- | ----------- |

| 1  | 2000-12-14 | 3           |

| 2  | 2000-12-16 | 5           |

 

--it is creating problems for example this input 2 output 12/14 testcases passed

--here datediff is greater than 1 - ie 2 days gap so output should be null

 

select id

from

(select w.*,

lag(temperature) over (order by recordDate) as lag_T,

DATEDIFF(recordDate , LAG(recordDate) OVER (ORDER BY recordDate)) date_diff 

from Weather as w) as a

where temperature>a.lag_T  and date_diff = 1 ;

 

 

========================================================================================

Question:1

Ambers conglomerate corporation just acquired some new companies. Each of the companies

follows this hierarchy:

 

Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

Note:

•            The tables may contain duplicate records.

•            The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.

________________________________________

Input Format

The following tables contain company data:

•            Company: The company_code is the code of the company and founder is the founder of the company. 

•            Lead_Manager: The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company. 

•            Senior_Manager: The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company. 

•            Manager: The manager_code is the code of the manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company. 

•            Employee: The employee_code is the code of the employee, the manager_code is the code of its manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company. 

________________________________________

Sample Input

Company Table:   Lead_Manager Table:   Senior_Manager Table:   Manager Table:   Employee Table: 

Sample Output

C1 Monika 1 2 1 2

C2 Samantha 1 1 2 2

Explanation

In company C1, the only lead manager is LM1. There are two senior managers, SM1 and SM2, under LM1. There is one manager, M1, under senior manager SM1. There are two employees, E1 and E2, under manager M1.

In company C2, the only lead manager is LM2. There is one senior manager, SM3, under LM2. There are two managers, M2 and M3, under senior manager SM3. There is one employee, E3, under manager M2, and another employee, E4, under manager, M3.

 

 

select distinct

c.company_code , c.founder , lm.lm_count ,sm.sm_count,m.mc_count,e.ec_code

 

from

company c

 

join

 

(select

 count(Lead_Manager_code) as lm_count

 from Lead_Manager

group by company_code) as lm

 

join

 

(select

count(Senior_Manager_code) as sm_count

from Senior_Manager

group by Lead_Manager_code,Company_code ) as sm

 

join

 

(select

count(Manager_code) as mc_count

from Manager

group by Senior_Manager_code,Lead_Manager_code,company_code) as m

 

join

 

(select

    count(Employee_code) as ec_code

from Employee

group by Manager_code, Senior_Manager_code, Lead_Manager_code,company_code ) as e

 

order by c.company_code

==========================================

 

SELECT c.Company_code , c.founder, lm.num , sm.num , m.num ,e.num

From Company c

join

(SELECT company_code, COUNT(lead_manager_code) as num FROM Lead_Manager GROUP BY company_code) as lm

on lm.company_code = c.company_code

join

(SELECT company_code,COUNT(senior_manager_code) as num FROM Senior_Manager GROUP BY Lead_Manager_code ) as sm 

on sm.company_code = c.company_code

join

(SELECT company_code,COUNT(manager_code) as num FROM Manager GROUP BY Senior_Manager_code) as m

on m.company_code = c.company_code

join

(SELECT company_code,COUNT(employee_code) as num FROM Employee GROUP BY Manager_code) as e

on e.company_code = c.company_code

 

 

============-----ongoing

-- best solution

SELECT c.company_code, c.founder, COUNT(DISTINCT l.lead_manager_code), COUNT(DISTINCT e.senior_manager_code), COUNT(DISTINCT e.manager_code), COUNT(DISTINCT e.employee_code)

FROM company AS c

INNER JOIN lead_manager AS l

ON c.company_code = l.company_code

INNER JOIN employee AS e

ON (e.company_code=c.company_code AND e.company_code=l.company_code)

GROUP BY c.company_code, c.founder

ORDER BY c.company_code;

 

 

1661. Average Time of Process per Machine

Easy

Topics

Companies

SQL Schema

________________________________________

Pandas Schema

________________________________________

Table: Activity

+----------------+---------+

| Column Name    | Type    |

+----------------+---------+

| machine_id     | int     |

| process_id     | int     |

| activity_type  | enum    |

| timestamp      | float   |

+----------------+---------+

The table shows the user activities for a factory website.

(machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.

machine_id is the ID of a machine.

process_id is the ID of a process running on the machine with ID machine_id.

activity_type is an ENUM (category) of type ('start', 'end').

timestamp is a float representing the current time in seconds.

'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.

The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.

There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input:

Activity table:

+------------+------------+---------------+-----------+

| machine_id | process_id | activity_type | timestamp |

+------------+------------+---------------+-----------+

| 0          | 0          | start         | 0.712     |

| 0          | 0          | end           | 1.520     |

| 0          | 1          | start         | 3.140     |

| 0          | 1          | end           | 4.120     |

| 1          | 0          | start         | 0.550     |

| 1          | 0          | end           | 1.550     |

| 1          | 1          | start         | 0.430     |

| 1          | 1          | end           | 1.420     |

| 2          | 0          | start         | 4.100     |

| 2          | 0          | end           | 4.512     |

| 2          | 1          | start         | 2.500     |

| 2          | 1          | end           | 5.000     |

+------------+------------+---------------+-----------+

Output:

+------------+-----------------+

| machine_id | processing_time |

+------------+-----------------+

| 0          | 0.894           |

| 1          | 0.995           |

| 2          | 1.456           |

+------------+-----------------+

Explanation:

There are 3 machines running 2 processes each.

Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894

Machine 1's average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995

Machine 2 s average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2

 

 

 

==========================

--Queries

 

select machine_id from activity

group by machine_id;

 

select  machine_id,  count(distinct process_id) as num_process from activity group  by machine_id;

--TO GET THE NUMBBER OF PROCESS PER MACHINE CODE

--output

| machine_id | num_process |

| ---------- | ----------- |

| 0          | 2           |

| 1          | 2           |

| 2          | 2           |

 

 

select timestamp as end_time from activity where activity_type = 'end' and process_id = 0 and machine_id =0 ;

 

select

a.*,

lag(timestamp) over (partition by machine_id)

from activity a;

 

| machine_id | process_id | activity_type | timestamp | lag(timestamp) over (partition by machine_id) |

| ---------- | ---------- | ------------- | --------- | --------------------------------------------- |

| 0          | 0          | start         | 0.712     | null                                          |

| 0          | 0          | end           | 1.52      | 0.712                                         |

| 0          | 1          | start         | 3.14      | 1.52                                          |

| 0          | 1          | end           | 4.12      | 3.14                                          |

| 1          | 0          | start         | 0.55      | null                                          |

| 1          | 0          | end           | 1.55      | 0.55                                          |

| 1          | 1          | start         | 0.43      | 1.55                                          |

| 1          | 1          | end           | 1.42      | 0.43                                                                                                                          

 

 

select derv3.*,

sum_per_machine/num_process

from

(

  select derv2.*,

  sum(derv2.diff) over (partition by machine_id) as sum_per_machine

  from

  (

    select derv1.*, (timestamp - derv1.prev) as diff

    from

    (select

    a.*,

    (lag(timestamp) over (partition by machine_id) ) as prev ,

    (count(process_id) over (partition by machine_id,process_id)) as num_process

    from activity a) as derv1

    where activity_type= 'end'

   ) as derv2

) as derv3

 

output

 

 

--ROUND OFF TO 3

--crt given testcase

select

distinct machine_id,

ROUND((sum_per_machine/num_process) ,3 ) as processing_time

from

(

  select

  derv2.*,

  sum(derv2.diff) over (partition by machine_id) as sum_per_machine

  from

  (

    select

              derv1.*,

              (timestamp - derv1.prev) as diff

    from

    (

              select

                             a.*,

                             (lag(timestamp) over (partition by machine_id) ) as prev ,

                             (count(process_id) over (partition by machine_id,process_id)) as num_process

    from activity a

              ) as derv1

    where activity_type= 'end'

   ) as derv2

) as derv3

 

--OUTPUT

outputmachine_id          avg_time_per

0                         0.894

1                         0.995

2                         1.456

 

--EXCEPTED OUTPUT

 

| machine_id | processing_time |

| ---------- | --------------- |

| 0          | 0.894           |

| 1          | 0.995           |

| 2          | 1.456           |

 

--for below input error

| machine_id | process_id | activity_type | timestamp |

| ---------- | ---------- | ------------- | --------- |

| 0          | 1          | start         | 18.891    |

| 1          | 0          | end           | 81.874    |

| 0          | 0          | start         | 37.019    |

| 0          | 1          | end           | 38.098    |

| 1          | 0          | start         | 25.135    |

| 1          | 1          | start         | 23.355    |

| 0          | 0          | end           | 40.222    |

| 1          | 1          | end           | 90.302    |

 

--output is wrong

--Output

| machine_id | processing_time |

| ---------- | --------------- |

| 0          | 1.601           |

| 1          | 33.474          |

Expected

| machine_id | processing_time |

| ---------- | --------------- |

| 1          | 61.843          |

| 0          | 11.205          |

 

 

 

====================================================================================================

 

 

--testcase 1:

-- we are encounting problem we this test case where data is not sorted by machine_id and process_id

| machine_id | process_id | activity_type | timestamp |

| ---------- | ---------- | ------------- | --------- |

| 0          | 1          | start         | 18.891    |

| 1          | 0          | end           | 81.874    |

| 0          | 0          | start         | 37.019    |

| 0          | 1          | end           | 38.098    |

| 1          | 0          | start         | 25.135    |

| 1          | 1          | start         | 23.355    |

| 0          | 0          | end           | 40.222    |

| 1          | 1          | end           | 90.302    |

 

--ordered TABLE

 

select * from activity

order by machine_id ,process_id,activity_type desc;

 

--for machine_id 0

--(40.222-37.019 + 38.098-18.891)/2 = (3.202+19.207)/2

 

Output

| machine_id | processing_time |

| ---------- | --------------- |

| 0          | 1.601           |

| 1          | 33.474          |

Expected

| machine_id | processing_time |

| ---------- | --------------- |

| 1          | 61.843          |

| 0          | 11.205          |

 

--query for schema for online

 

drop table Activity;

 

Create table If Not Exists Activity (machine_id int, process_id int, activity_type char, timestamp float);

 

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'start', '18.891');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'end', '81.874');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'start', '37.019');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'end', '38.098');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'start', '25.135');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'end', '23.355');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'start', '40.222');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'end', '90.302');

 

 

--- here we are trying to order table by "order by machine_id ,process_id,activity_type desc" in inner most query in order to get sequential data by  machine_id , process_id and activity_type start and end

select

                             a.*,

                             (lag(timestamp) over (partition by machine_id order by machine_id ,process_id,activity_type desc) ) as prev ,

                             (count(process_id) over (partition by machine_id,process_id)) as num_process

    from activity a

             

==================

--this output is crt for testcase 1 but not for given testcase 0

select

distinct machine_id,

ROUND((sum_per_machine/num_process) ,3 ) as processing_time

from

(

  select

  derv2.*,

  sum(derv2.diff) over (partition by machine_id) as sum_per_machine

  from

  (

    select

              derv1.*,

              (timestamp - derv1.prev) as diff

    from

    (

              select

                             a.*,

                             (lag(timestamp) over (partition by machine_id order by machine_id ,process_id,activity_type desc) ) as prev ,

                             (count(process_id) over (partition by machine_id,process_id)) as num_process

    from activity a

              ) as derv1

   where activity_type = 'end'

   ) as derv2

   where diff > 0

) as derv3

 

--output

machine_id        processing_time

0                 9.604

1                 61.843

 

--Expected

| machine_id | processing_time |

| ---------- | --------------- |

| 1          | 61.843          |

| 0          | 11.205          |

 

drop table Activity;

 

Create table If Not Exists Activity (machine_id int, process_id int, activity_type char, timestamp float);

 

 

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'start', '0.712');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'end', '1.52');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'start', '3.14');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'end', '4.12');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'start', '0.55');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'end', '1.55');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'start', '0.43');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'end', '1.42');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '0', 'start', '4.1');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '0', 'end', '4.512');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '1', 'start', '2.5');

insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '1', 'end', '5');

 

 

select

distinct machine_id,

ROUND((sum_per_machine/num_process) ,3 ) as processing_time

from

(

  select

  derv2.*,

  sum(derv2.diff) over (partition by machine_id) as sum_per_machine

  from

  (

    select

              derv1.*,

              (timestamp - derv1.prev) as diff

    from

    (

              select

                             a.*,

                             (lag(timestamp) over (partition by machine_id order by machine_id ,process_id,activity_type desc) ) as prev ,

                             (count(process_id) over (partition by machine_id,process_id)) as num_process

    from activity a

              ) as derv1

   where activity_type = 'end'

   ) as derv2

   where diff > 0

) as derv3

 

--output

machine_id        processing_time

0                 0.894

1                 0.995

2                 1.456

 

--expected output

| machine_id | processing_time |

+------------+-----------------+

| 0          | 0.894           |

| 1          | 0.995           |

| 2          | 1.456           |

+------------+-----------------+


--self join

select

machine_id ,

a.timestamp - b.timestamp

from

              activity a

                             inner join

              activity b

              on a.machine_id = b.machine_id

             

             

-------------------------------------------------------------trying with self join

 

select * from

activity a join activity b

on a.machine_id = b.machine_id

and a.process_id = b.process_id

and a.activity_type = b.activity_type

 

-- for this query activity join with activity with same id's for all machine_id ,  process_id ,  activity_type

 

 

select * from

activity a join activity b

on a.machine_id = b.machine_id

and a.process_id = b.process_id

and a.activity_type not in ('b.activity_type') --here it is not in ('b.activity_type') causes opposite

 

 

-- for this query activity join with activity with same id's for all machine_id ,  process_id but activity_type is opposite

-- for A activity start we have B activity end




select *,

(a.timestamp - b.timestamp) as diff

from

activity a join activity b

on a.machine_id = b.machine_id

and a.process_id = b.process_id

and a.activity_type not in (b.activity_type)

 

 
SELECT

distinct

machine_id

,(sum(diff) over(PARTITION by machine_id)) / 2 as sum_per_machine

 

FROM

 

(

              SELECT *,

              (a.timestamp - b.timestamp) as diff

 

              from

              activity a join activity b

              on a.machine_id = b.machine_id

              and a.process_id = b.process_id

              and a.activity_type not in (b.activity_type)

 

              where diff > 0 -- diff > 0 will give you  end - start

)

as derv

 

--using derived_table distinct and dividing by num of process

 

 

--output

machine_id        sum_per_machine

0                 0.894

1                 0.995

2                 1.456

 

--expected output

| machine_id | processing_time |

+------------+-----------------+

| 0          | 0.894           |

| 1          | 0.995           |

| 2          | 1.456           |

+------------+-----------------+

 

---trying to generalized num of process

 

              SELECT *,

              (a.timestamp - b.timestamp) as diff,

    (count(a.process_id) over (partition by a.machine_id)) as num_of_process

 

              from

              activity a join activity b

              on a.machine_id = b.machine_id

              and a.process_id = b.process_id

              and a.activity_type not in (b.activity_type)

 

              where diff > 0 -- diff > 0 will give you  end - start

             

-- here we can get number of process

----output
            

             
SELECT

distinct

              derv.machine_id

              ,round(((sum(derv.diff) over(PARTITION by derv.machine_id)) / derv.num_of_process), 3) as processing_time

 

FROM

 

(            

              SELECT *,

              (a.timestamp - b.timestamp) as diff,

    (count(a.process_id) over (partition by a.machine_id)) as num_of_process

 

              from

              activity a join activity b

              on a.machine_id = b.machine_id

              and a.process_id = b.process_id

              and a.activity_type not in (b.activity_type)

 

              where diff > 0 -- diff > 0 will give you  end - start

             

)

as derv

 ---Output

machine_id        processing_time

0                 0.894

1                 0.995

2                 1.456

 

--expected output

| machine_id | processing_time |

+------------+-----------------+

| 0          | 0.894           |

| 1          | 0.995           |

| 2          | 1.456           |

+------------+-----------------+

 

--SUCCESSFUL output matches expected output success in online compiler

--so above query is ok for given testcase in online complier

Input:

Activity table:

+------------+------------+---------------+-----------+

| machine_id | process_id | activity_type | timestamp |

+------------+------------+---------------+-----------+

| 0          | 0          | start         | 0.712     |

| 0          | 0          | end           | 1.520     |

| 0          | 1          | start         | 3.140     |

| 0          | 1          | end           | 4.120     |

| 1          | 0          | start         | 0.550     |

| 1          | 0          | end           | 1.550     |

| 1          | 1          | start         | 0.430     |

| 1          | 1          | end           | 1.420     |

| 2          | 0          | start         | 4.100     |

| 2          | 0          | end           | 4.512     |

| 2          | 1          | start         | 2.500     |

| 2          | 1          | end           | 5.000     |

+------------+------------+---------------+-----------+

Output:

+------------+-----------------+

| machine_id | processing_time |

+------------+-----------------+

| 0          | 0.894           |

| 1          | 0.995           |

| 2          | 1.456           |

+------------+-----------------

 

--now checking for testcase 1

 

| machine_id | process_id | activity_type | timestamp |

| ---------- | ---------- | ------------- | --------- |

| 0          | 1          | start         | 18.891    |

| 1          | 0          | end           | 81.874    |

| 0          | 0          | start         | 37.019    |

| 0          | 1          | end           | 38.098    |

| 1          | 0          | start         | 25.135    |

| 1          | 1          | start         | 23.355    |

| 0          | 0          | end           | 40.222    |

| 1          | 1          | end           | 90.302    |

 

Expected

| machine_id | processing_time |

| ---------- | --------------- |

| 1          | 61.843          |

| 0          | 11.205          |

 

machine_id        processing_time

0                 19.207

1                 56.739

 

--FAILED for testcase 1

================================

----solution 1 with join

select a1.machine_id, round(avg(a2.timestamp-a1.timestamp), 3) as processing_time

from Activity a1

join Activity a2

on a1.machine_id=a2.machine_id and a1.process_id=a2.process_id

and a1.activity_type='start' and a2.activity_type='end'

group by a1.machine_id

--correct

 

--query

select *

from Activity a1

join Activity a2

on a1.machine_id=a2.machine_id and a1.process_id=a2.process_id

and a1.activity_type='start' and a2.activity_type='end'

 



----solution 2 with subquery

select

a.machine_id,

round(

      (select avg(a1.timestamp) from Activity a1 where a1.activity_type = 'end' and a1.machine_id = a.machine_id) -

      (select avg(a1.timestamp) from Activity a1 where a1.activity_type = 'start' and a1.machine_id = a.machine_id)

,3) as processing_time

from Activity a

group by a.machine_id

 

 

--------------------------------------

1280. Students and Examinations

Table: Students

+---------------+---------+

| Column Name   | Type    |

| student_id    | int     |

| student_name  | varchar |

+---------------+---------+

student_id is the primary key (column with unique values) for this table.

Each row of this table contains the ID and the name of one student in the school

Table: Subjects

+--------------+---------+

| Column Name  | Type    |

+--------------+---------+

| subject_name | varchar |

+--------------+---------+

subject_name is the primary key (column with unique values) for this table.

Each row of this table contains the name of one subject in the school.

Table: Examinations

+--------------+---------+

| Column Name  | Type    |

+--------------+---------+

| student_id   | int     |

| subject_name | varchar |

+--------------+---------+

There is no primary key (column with unique values) for this table. It may contain duplicates.

Each student from the Students table takes every course from the Subjects table.

Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.

The result format is in the following example.

Example 1:

Input:

Students table:

+------------+--------------+

| student_id | student_name |

+------------+--------------+

| 1          | Alice        |

| 2          | Bob          |

| 13         | John         |

| 6          | Alex         |

+------------+--------------+

Subjects table:

+--------------+

| subject_name |

+--------------+

| Math         |

| Physics      |

| Programming  |

+--------------+

Examinations table:

+------------+--------------+

| student_id | subject_name |

+------------+--------------+

| 1          | Math         |

| 1          | Physics      |

| 1          | Programming  |

| 2          | Programming  |

| 1          | Physics      |

| 1          | Math         |

| 13         | Math         |

| 13         | Programming  |

| 13         | Physics      |

| 2          | Math         |

| 1          | Math         |

+------------+--------------+

 

 

 

Output:

+------------+--------------+--------------+----------------+

| student_id | student_name | subject_name | attended_exams |

+------------+--------------+--------------+----------------+

| 1          | Alice        | Math         | 3              |

| 1          | Alice        | Physics      | 2              |

| 1          | Alice        | Programming  | 1              |

| 2          | Bob          | Math         | 1              |

| 2          | Bob          | Physics      | 0              |

| 2          | Bob          | Programming  | 1              |

| 6          | Alex         | Math         | 0              |

| 6          | Alex         | Physics      | 0              |

| 6          | Alex         | Programming  | 0              |

| 13         | John         | Math         | 1              |

| 13         | John         | Physics      | 1              |

| 13         | John         | Programming  | 1              |

+------------+--------------+--------------+----------------+

Explanation:

The result table should contain all students and all subjects.

Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time.

Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam.

Alex did not attend any exams.

John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time.

 

# Write your MySQL query statement below

 

select

*

from

Students as stud

join

Subjects as sub

 

| student_id | student_name | subject_name |

| ---------- | ------------ | ------------ |

| 1          | Alice        | Programming  |

| 1          | Alice        | Physics      |

| 1          | Alice        | Math         |

| 2          | Bob          | Programming  |

| 2          | Bob          | Physics      |

| 2          | Bob          | Math         |

| 13         | John         | Programming  |

| 13         | John         | Physics      |

| 13         | John         | Math         |

| 6          | Alex         | Programming  |

| 6          | Alex         | Physics      |

| 6          | Alex         | Math         |

 

select

*

from

Students as stud

join

Subjects as sub

join

Examinations as exam

 

| student_id | student_name | subject_name | student_id | subject_name |

| ---------- | ------------ | ------------ | ---------- | ------------ |

| 6          | Alex         | Math         | 1          | Math         |

| 6          | Alex         | Physics      | 1          | Math         |

| 6          | Alex         | Programming  | 1          | Math         |

| 13         | John         | Math         | 1          | Math         |

| 13         | John         | Physics      | 1          | Math         |

| 13         | John         | Programming  | 1          | Math         |

| 2          | Bob          | Math         | 1          | Math         |

| 2          | Bob          | Physics      | 1          | Math         |

| 2          | Bob          | Programming  | 1          | Math         |

| 1          | Alice        | Math         | 1          | Math         |

| 1          | Alice        | Physics      | 1          | Math         |

| 1          | Alice        | Programming  | 1          | Math  ...

 

 

select

*

from

Students as stud

join

Subjects as sub

join

Examinations as exam

on  stud.student_id = exam.student_id

 

| student_id | student_name | subject_name | student_id | subject_name |

| ---------- | ------------ | ------------ | ---------- | ------------ |

| 1          | Alice        | Math         | 1          | Math         |

| 1          | Alice        | Physics      | 1          | Math         |

| 1          | Alice        | Programming  | 1          | Math         |

| 1          | Alice        | Math         | 1          | Physics      |

| 1          | Alice        | Physics      | 1          | Physics      |

| 1          | Alice        | Programming  | 1          | Physics      |

| 1          | Alice        | Math         | 1          | Programming  |

| 1          | Alice        | Physics      | 1          | Programming  |

| 1          | Alice        | Programming  | 1          | Programming  |

| 2          | Bob          | Math         | 2          | Programming  |

| 2          | Bob          | Physics      | 2          | Programming  |

| 2          | Bob          | Programming  | 2          | Progra...

 

 

select

*

from

Students as stud

join

Examinations as exam

on stud.student_id = exam.student_id

join

Subjects as sub

| student_id | student_name | student_id | subject_name | subject_name |

| ---------- | ------------ | ---------- | ------------ | ------------ |

| 1          | Alice        | 1          | Math         | Math         |

| 1          | Alice        | 1          | Math         | Physics      |

| 1          | Alice        | 1          | Math         | Programming  |

| 1          | Alice        | 1          | Physics      | Math         |

| 1          | Alice        | 1          | Physics      | Physics      |

| 1          | Alice        | 1          | Physics      | Programming  |

| 1          | Alice        | 1          | Programming  | Math         |

| 1          | Alice        | 1          | Programming  | Physics      |

| 1          | Alice        | 1          | Programming  | Programming  |

| 2          | Bob          | 2          | Programming  | Math         |

| 2          | Bob          | 2          | Programming  | Physics      |

| 2          | Bob          | 2          | Programming  | Progra...

 

select

*

from

Students as stud

join

Subjects as sub

left outer join

Examinations as exam

on stud.student_id = exam.student_id

and sub.subject_name = exam.subject_name

 

| student_id | student_name | subject_name | student_id | subject_name |

| ---------- | ------------ | ------------ | ---------- | ------------ |

| 1          | Alice        | Programming  | 1          | Programming  |

| 1          | Alice        | Physics      | 1          | Physics      |

| 1          | Alice        | Physics      | 1          | Physics      |

| 1          | Alice        | Math         | 1          | Math         |

| 1          | Alice        | Math         | 1          | Math         |

| 1          | Alice        | Math         | 1          | Math         |

| 2          | Bob          | Programming  | 2          | Programming  |

| 2          | Bob          | Physics      | null       | null         |

| 2          | Bob          | Math         | 2          | Math         |

| 13         | John         | Programming  | 13         | Programming  |

| 13         | John         | Physics      | 13         | Physics      |

| 13         | John         | Math         | 13         | Math  ...

 

select

*,count(exam.subject_name) as attended_exams

from

Students as stud

join

Subjects as sub

left outer join

Examinations as exam

on stud.student_id = exam.student_id

and sub.subject_name = exam.subject_name

group by exam.subject_name,stud.student_id

 

--here we have to keep in mind for all Student and all subject data have to be collected so

--Students stud cross join with Subjects sub to get all possible but then result is only left outer join with Examinations as exam

--on condition that

--stud.student_id = exam.student_id

--and sub.subject_name = exam.subject_name

-- later for exam.subject_name we have to group by with both exam.subject_name

 

| student_id | student_name | subject_name | student_id | subject_name | attended_exams |

| ---------- | ------------ | ------------ | ---------- | ------------ | -------------- |

| 1          | Alice        | Programming  | 1          | Programming  | 1              |

| 1          | Alice        | Physics      | 1          | Physics      | 2              |

| 1          | Alice        | Math         | 1          | Math         | 3              |

| 2          | Bob          | Programming  | 2          | Programming  | 1              |

| 2          | Bob          | Physics      | null       | null         | 0              |

| 2          | Bob          | Math         | 2          | Math         | 1              |

| 13         | John         | Programming  | 13         | Programming  | 1              |

| 13         | John         | Physics      | 13         | Physics      | 1              |

| 13         | John         | Math         | 13         | Math         | 1              |

| 6          | Alex  ...

 

select

stud.student_id, stud.student_name, sub.subject_name, count(exam.subject_name) as attended_exams

from

Students as stud

join

Subjects as sub

left outer join

Examinations as exam

on stud.student_id = exam.student_id

and sub.subject_name = exam.subject_name

group by exam.subject_name,stud.student_id

 

--output

 

| student_id | student_name | subject_name | attended_exams |

| ---------- | ------------ | ------------ | -------------- |

| 1          | Alice        | Math         | 3              |

| 1          | Alice        | Physics      | 2              |

| 1          | Alice        | Programming  | 1              |

| 2          | Bob          | Math         | 1              |

| 2          | Bob          | Physics      | 0              |

| 2          | Bob          | Programming  | 1              |

| 6          | Alex         | Programming  | 0              |

| 13         | John         | Math         | 1              |

| 13         | John         | Physics      | 1              |

| 13         | John         | Programming  | 1              |

 

expected

| student_id | student_name | subject_name | attended_exams |

| ---------- | ------------ | ------------ | -------------- |

| 1          | Alice        | Math         | 3              |

| 1          | Alice        | Physics      | 2              |

| 1          | Alice        | Programming  | 1              |

| 2          | Bob          | Math         | 1              |

| 2          | Bob          | Physics      | 0              |

| 2          | Bob          | Programming  | 1              |

| 6          | Alex         | Math         | 0              |

| 6          | Alex         | Physics      | 0              |

| 6          | Alex         | Programming  | 0              |

| 13         | John         | Math         | 1              |

| 13         | John         | Physics      | 1              |

| 13         | John         | Programming  | 1              |

 

--FAIL

--here 1 thing to note is that we are counting subject_name in exam and grouping it by subject_name in sub and stud.student_id

-- sub.subject_name,stud.student_id

 

select

stud.student_id, stud.student_name, sub.subject_name

,count(exam.subject_name) as attended_exams

from

Students as stud

join

Subjects as sub

left outer join

Examinations as exam

on stud.student_id = exam.student_id

and sub.subject_name = exam.subject_name

where stud.student_name  = 'Alex'

group by sub.subject_name,stud.student_id

order by stud.student_id , sub.subject_name

 

| student_id | student_name | subject_name | attended_exams |

| ---------- | ------------ | ------------ | -------------- |

| 6          | Alex         | Math         | 0              |

| 6          | Alex         | Physics      | 0              |

| 6          | Alex         | Programming  | 0              |

 

 

select

stud.student_id, stud.student_name, sub.subject_name

,count(exam.subject_name) as attended_exams

from

Students as stud

join

Subjects as sub

left outer join

Examinations as exam

on stud.student_id = exam.student_id

and sub.subject_name = exam.subject_name

group by sub.subject_name,stud.student_id

order by stud.student_id , sub.subject_name

--output

| student_id | student_name | subject_name | attended_exams |

| ---------- | ------------ | ------------ | -------------- |

| 1          | Alice        | Math         | 3              |

| 1          | Alice        | Physics      | 2              |

| 1          | Alice        | Programming  | 1              |

| 2          | Bob          | Math         | 1              |

| 2          | Bob          | Physics      | 0              |

| 2          | Bob          | Programming  | 1              |

| 6          | Alex         | Math         | 0              |

| 6          | Alex         | Physics      | 0              |

| 6          | Alex         | Programming  | 0              |

| 13         | John         | Math         | 1              |

| 13         | John         | Physics      | 1              |

| 13         | John         | Programming  | 1              |

--expected

| student_id | student_name | subject_name | attended_exams |

| ---------- | ------------ | ------------ | -------------- |

| 1          | Alice        | Math         | 3              |

| 1          | Alice        | Physics      | 2              |

| 1          | Alice        | Programming  | 1              |

| 2          | Bob          | Math         | 1              |

| 2          | Bob          | Physics      | 0              |

| 2          | Bob          | Programming  | 1              |

| 6          | Alex         | Math         | 0              |

| 6          | Alex         | Physics      | 0              |

| 6          | Alex         | Programming  | 0              |

| 13         | John         | Math         | 1              |

| 13         | John         | Physics      | 1              |

| 13         | John         | Programming  | 1              |

 

----------

select count(distinct name)

from

CITY

where Population > 100000

group by

------------------------
 570. Managers with at Least 5 Direct Reports
Medium
Topics
Companies
Hint
SQL Schema
Pandas Schema
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+

--solution

--find manager with atleast 5 
--filter 1 name where manager_id = id and count(manager_Id) >=5


select managerId, count(managerId) as cnt
from Employee 
group by managerId   
having count(managerId) >1

--output
| managerId |cnt|
| --------- | - |
| 101       | 5 |


-- filter 1 name where id  = managerId
-- fitler 2 managerId where count(manager_Id) >=5
-- output name from filter 1 and 2

select managerId , count(managerId) as cnt
from Employee
group by managerId
having count(managerId) >=5


select name 
from Employee a 
inner join 
(
select managerId , count(managerId) as cnt
from Employee 
group by managerId
having count(managerId) >=5
) as b
on a.id =b.managerId

--output
| name |
| ---- |
| John |
--Correct

--another method
SELECT name 
FROM Employee 
WHERE id IN (
    SELECT managerId 
    FROM Employee 
    GROUP BY managerId 
    HAVING COUNT(*) >= 5)
	--and
SELECT a.name 
FROM Employee a 
JOIN Employee b ON a.id = b.managerId 
GROUP BY b.managerId 
HAVING COUNT(*) >= 5


--------------Confirmation Rate
Signups table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
+---------+---------------------+
Confirmations table:
+---------+---------------------+-----------+
| user_id | time_stamp          | action    |
+---------+---------------------+-----------+
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |
+---------+---------------------+-----------+


--two table join on user_id
select * 
from Signups s
inner join Confirmations c
on s.user_id = c.user_id  

--output
| user_id | time_stamp          | user_id | time_stamp          | action    |
| ------- | ------------------- | ------- | ------------------- | --------- |
| 3       | 2020-03-21 10:16:13 | 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2020-03-21 10:16:13 | 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2020-01-04 13:57:59 | 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2020-01-04 13:57:59 | 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2020-01-04 13:57:59 | 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2020-07-29 23:09:44 | 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2020-07-29 23:09:44 | 2       | 2021-02-28 23:59:59 | timeout   |

--inner join do not contain user_id 6 who did not requested confirmation messages

select *
from Signups s
left join Confirmations c
on s.user_id  = c.user_id

--output
| user_id | time_stamp          | user_id | time_stamp          | action    |
| ------- | ------------------- | ------- | ------------------- | --------- |
| 3       | 2020-03-21 10:16:13 | 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2020-03-21 10:16:13 | 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2020-01-04 13:57:59 | 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2020-01-04 13:57:59 | 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2020-01-04 13:57:59 | 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2020-07-29 23:09:44 | 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2020-07-29 23:09:44 | 2       | 2021-02-28 23:59:59 | timeout   |
| 6       | 2020-12-09 10:39:37 | null    | null                | null      |

--left join signups and Confirmations 
--confirmation rate = number of 'confirmed' messages / total number of requested confirmation messages
--total_req = count(action) group by user_id
--no_of_confirmed = count(case when action='confirmed') group by user_id
--confirmation_rate = round((no_of_confirmed / total_req),2)
--output user_id ,conirmation_rate

--failed to consider divide by zero for the case where action is null .. user sign up but do not request confirmation


select s.user_id, count(action) as total_req
from Signups s
left join Confirmations c
on s.user_id  = c.user_id
group by s.user_id 
order by s.user_id asc

--Error if we use select * 
--'Signups.time_stamp' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause

select s.user_id,
sum(case
	when action='confirmed' then 1 else 0 end) as no_of_confirmed
from Signups s
left join Confirmations c
on s.user_id  = c.user_id
group by s.user_id 
order by s.user_id asc

--trying to combine 2 


select 
s.user_id,
count(action) as total_req,
sum(case when action='confirmed' then 1 else 0 end) as no_of_confirmed
from Signups s
left join Confirmations c
on s.user_id  = c.user_id
group by s.user_id 
order by s.user_id asc

--output
| user_id | total_req | no_of_confirmed |
| ------- | --------- | --------------- |
| 2       | 2         | 1               |
| 3       | 2         | 0               |
| 6       | 0         | 0               |
| 7       | 3         | 3               |

--calculate confirmation_rate = round((no_of_confirmed / total_req),2)

select s.user_id, round((no_of_confirmed / total_req),2) as confirmation_rate
from
(
	select 
	s.user_id,
	count(action) as total_req,
	sum(case when action='confirmed' then 1 else 0 end) as no_of_confirmed
	from Signups s
	left join Confirmations c
	on s.user_id  = c.user_id
	group by s.user_id 
	order by s.user_id asc
) as derv

--error
--The ORDER BY clause is invalid in views, inline functions, derived tables, subqueries, and common table expressions, unless TOP, OFFSET or FOR XML is also specified. (1033) (SQLExecDirectW)


select s.user_id, round((no_of_confirmed / total_req),2) as confirmation_rate
from
(
	select 
	s.user_id,
	count(action) as total_req,
	sum(case when action='confirmed' then 1 else 0 end) as no_of_confirmed
	from Signups s
	left join Confirmations c
	on s.user_id  = c.user_id
	group by s.user_id 
) as derv

--error
--The multi-part identifier "s.user_id" could not be bound.


select derv.user_id, round((no_of_confirmed / total_req),2) as confirmation_rate
from
(
	select 
	s.user_id,
	count(action) as total_req,
	sum(case when action='confirmed' then 1 else 0 end) as no_of_confirmed
	from Signups s
	left join Confirmations c
	on s.user_id  = c.user_id
	group by s.user_id 
) as derv

--error
--Divide by zero error encountered. (8134) (SQLFetch)

select derv.user_id, 
case when total_req = 0 then 0 else round((no_of_confirmed / total_req),2) end	as confirmation_rate
from
(
	select 
	s.user_id,
	count(action) as total_req,
	sum(case when action='confirmed' then 1 else 0 end) as no_of_confirmed
	from Signups s
	left join Confirmations c
	on s.user_id  = c.user_id
	group by s.user_id 
) as derv
order by  confirmation_rate asc

--1/2 = 0.5 in MySql
--1/2 = 0	in MS SQL Server


--output

| user_id | confirmation_rate |
| ------- | ----------------- |
| 3       | 0                 |
| 6       | 0                 |
| 2       | 0.5               |
| 7       | 1                 |

--PASS

--Another method
--average and using if clause we specified that if action is confirmed we count it as 1 and else if null or timeout we will count it as 0.
--# Write your MySQL query statement below
select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from Signups as s left join Confirmations as c on s.user_id= c.user_id group by user_id;



---
--filter odd-number ID % 2 !=0 
--filter and description != 'boring'


---------------------
1251. Average Selling Price
Easy
TopicsCompanies
SQL SchemaPandas Schema
Table: Prices
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of the product_id in the period from start_date to end_date.
For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.


 
Table: UnitsSold
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the date, units, and product_id of each product sold. 


 
Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.
Return the result table in any order.
The result format is in the following example.
 
Example 1:
Input: 
Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date   | price  |
+------------+------------+------------+--------+
| 1          | 2019-02-17 | 2019-02-28 | 5      |
| 1          | 2019-03-01 | 2019-03-22 | 20     |
| 2          | 2019-02-01 | 2019-02-20 | 15     |
| 2          | 2019-02-21 | 2019-03-31 | 30     |
+------------+------------+------------+--------+
UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+
Output: 
+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+
Explanation: 
Average selling price = Total Price of Product / Number of products sold.
Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96


---combine Prices and UnitsSold
--average group by product_id
select *
from Prices p
inner join UnitsSold u 
on p.product_id = u.product_id
group by p.units



--output
| product_id | start_date | end_date   | price | product_id | purchase_date | units |
| ---------- | ---------- | ---------- | ----- | ---------- | ------------- | ----- |
| 1          | 2019-03-01 | 2019-03-22 | 20    | 1          | 2019-02-25    | 100   |
| 1          | 2019-02-17 | 2019-02-28 | 5     | 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01 | 2019-03-22 | 20    | 1          | 2019-03-01    | 15    |
| 1          | 2019-02-17 | 2019-02-28 | 5     | 1          | 2019-03-01    | 15    |
| 2          | 2019-02-21 | 2019-03-31 | 30    | 2          | 2019-02-10    | 200   |
| 2          | 2019-02-01 | 2019-02-20 | 15    | 2          | 2019-02-10    | 200   |
| 2          | 2019-02-21 | 2019-03-31 | 30    | 2          | 2019-03-22    | 30    |
| 2          | 2019-02-01 | 2019-02-20 | 15    | 2          | 2019-03-22    | 30    |


select *
from Prices p
inner join UnitsSold u 
on p.product_id = u.product_id
group by u.units

--output
| product_id | start_date | end_date   | price | product_id | purchase_date | units |
| ---------- | ---------- | ---------- | ----- | ---------- | ------------- | ----- |
| 1          | 2019-03-01 | 2019-03-22 | 20    | 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01 | 2019-03-22 | 20    | 1          | 2019-03-01    | 15    |
| 2          | 2019-02-21 | 2019-03-31 | 30    | 2          | 2019-02-10    | 200   |
| 2          | 2019-02-21 | 2019-03-31 | 30    | 2          | 2019-03-22    | 30    |

--join Prices  and UnitsSold tables on p.product_id =u.product_id  and purchase_date in between start_date and end_date
--calcute total price of product and number of product 
--calcute add price of product and number of product group by product_id
--calcute avg Total Price of Product / Number of products sold and round it to 2

select
* 
from Prices p
inner join UnitsSold u 
on p.product_id = u.product_id
where purchase_date between start_date and end_date

--output
| product_id | start_date | end_date   | price | product_id | purchase_date | units |
| ---------- | ---------- | ---------- | ----- | ---------- | ------------- | ----- |
| 1          | 2019-02-17 | 2019-02-28 | 5     | 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01 | 2019-03-22 | 20    | 1          | 2019-03-01    | 15    |
| 2          | 2019-02-01 | 2019-02-20 | 15    | 2          | 2019-02-10    | 200   |
| 2          | 2019-02-21 | 2019-03-31 | 30    | 2          | 2019-03-22    | 30    |


select
* , (price * units ) as price_total
from Prices p
inner join UnitsSold u 
on p.product_id = u.product_id
where purchase_date between start_date and end_date
--output
| product_id | start_date | end_date   | price | product_id | purchase_date | units | price_total |
| ---------- | ---------- | ---------- | ----- | ---------- | ------------- | ----- | ----------- |
| 1          | 2019-02-17 | 2019-02-28 | 5     | 1          | 2019-02-25    | 100   | 500         |
| 1          | 2019-03-01 | 2019-03-22 | 20    | 1          | 2019-03-01    | 15    | 300         |
| 2          | 2019-02-01 | 2019-02-20 | 15    | 2          | 2019-02-10    | 200   | 3000        |
| 2          | 2019-02-21 | 2019-03-31 | 30    | 2          | 2019-03-22    | 30    | 900         |


select derv1.product_id , sum(derv1.price_total) as total_price ,sum(derv1.units) as num
from
(
select
* , (price * units ) as price_total
from Prices p
inner join UnitsSold u 
on p.product_id = u.product_id
where purchase_date between start_date and end_date
) as derv1
group by derv1.product_id

--error
--Duplicate column name 'product_id'

select derv1.product_id , sum(derv1.price_total) as total_price ,sum(derv1.units) as num
from
(
	select
	p.product_id , units, (price * units ) as price_total
	from Prices p
	inner join UnitsSold u 
	on p.product_id = u.product_id
	where purchase_date between start_date and end_date
)as derv1
group by derv1.product_id

--output
| product_id | total_price | num |
| ---------- | ----------- | --- |
| 1          | 800         | 115 |
| 2          | 3900        | 230 |


select
	p.product_id , sum(price * units )  as Total_Price, sum(units) as Num_products
	from Prices p
	inner join UnitsSold u 
	on p.product_id = u.product_id
	where purchase_date between start_date and end_date
group by p.product_id

--output
| product_id | Total_Price | Num_products |
| ---------- | ----------- | ------------ |
| 1          | 800         | 115          |
| 2          | 3900        | 230          |


select product_id , round((Total_Price/Num_products),2) as average_price
from
(
	select
	p.product_id , sum(price * units )  as Total_Price, sum(units) as Num_products
	from Prices p
	inner join UnitsSold u 
	on p.product_id = u.product_id
	where purchase_date between start_date and end_date
	group by p.product_id
) as derv

--output
| product_id | average_price |
| ---------- | ------------- |
| 1          | 6.96          |
| 2          | 16.96         |
--accepted
--Wrong Answer
--15 / 17 testcases passed
--did not consider product not sold


select product_id , 
case when Num_products is null  then 0 else round((Total_Price/Num_products),2) end as average_price
from
(
	select
	p.product_id , sum(price * units )  as Total_Price, sum(units) as Num_products
	from Prices p
	left join UnitsSold u 
	on p.product_id = u.product_id
	where (purchase_date between start_date and end_date) or purchase_date is null
	group by p.product_id
) as derv

--PASS

--method 2
# Write your MySQL query statement below
SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND
u.purchase_date BETWEEN start_date AND end_date
group by product_id

------------------------------------------------------------------------------------
1075. Project Employees I
Easy
TopicsCompanies
SQL SchemaPandas Schema
Table: Project
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.


 
Table: Employee
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table. It is guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee.


 
Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.
Return the result table in any order.
The query result format is in the following example.
 
Example 1:
Input: 
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
Output: 
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
Explanation: The average experience years for the first project is (3 + 2 + 1) / 3 = 2.00 and for the second project is (3 + 2) / 2 = 2.50

--left join Project with Employee avg(experience_years) group by project_id  
--output project_id  and average_years 

select p.project_id,round(avg(experience_years),2) as average_years
from Project p
left join Employee e
on p.employee_id  = e.employee_id 
group by p.project_id

--PASS

----------------------------------------------------------------------------------
----left join Register and Users order by contest_id 
--count(contest_id) / (select count(user_name) from Users) group by contest_id 
--output contest_id  and percentage 
--order by percentage desc and contest_id asc 
select contest_id , round((count(contest_id)/(select count(user_name) from Users)) * 100  , 2) as percentage
from
Register r left join Users u
on r.user_id =u.user_id
group by contest_id 
order by percentage desc , contest_id asc  

--Wrong Answer
--13 / 14 testcases passed

| user_id | user_name |
| ------- | --------- |
| 6       | null      |
| 2       | Bob       |
| 7       | Alex      |

| contest_id | user_id |
| ---------- | ------- |
| 215        | 6       |
| 209        | 2       |
| 208        | 2       |
| 210        | 6       |
| 208        | 6       |
| 209        | 7       |
| 209        | 6       |
| 215        | 7       |
| 208        | 7       |
| 210        | 2       |
| 207        | 2       |
| 210        | 7       |

--output
| contest_id | percentage |
| ---------- | ---------- |
| 208        | 150        |3/2
| 209        | 150        |3/2
| 210        | 150        |3/2
| 215        | 100        |3/3
| 207        | 50         |1/2

--Expected
| contest_id | percentage |
| ---------- | ---------- |
| 208        | 100        |3/3
| 209        | 100        |3/3
| 210        | 100        |3/3
| 215        | 66.67      |2/3
| 207        | 33.33      |1/3




select contest_id , round((count(contest_id)/(select count(user_id) from Users)) * 100  , 2) as percentage
from
Register r left join Users u
on r.user_id =u.user_id
group by contest_id 
order by percentage desc , contest_id asc  


--PASS
--user_name can be null

------------------------------------------------------------------------------------------------------------

1211. Queries Quality and Percentage
Easy
TopicsCompanies
SQL SchemaPandas Schema
Table: Queries
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The position column has a value from 1 to 500.
The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.


 
We define query quality as:
The average of the ratio between query rating and its position.
We also define poor query percentage as:
The percentage of all queries with rating less than 3.
Write a solution to find each query_name, the quality and poor_query_percentage.
Both quality and poor_query_percentage should be rounded to 2 decimal places.
Return the result table in any order.
The result format is in the following example. 


--ratio rating/position --avg(ratio) group by query_name 
--poor_query_percentage  = sum(case  when rating <3 then 1 else 0 end)/(count of query_name ) *100


select *,rating/position  
from Queries

--output
| query_name | result           | position | rating | rating/position |
| ---------- | ---------------- | -------- | ------ | --------------- |
| Dog        | Golden Retriever | 1        | 5      | 5               |
| Dog        | German Shepherd  | 2        | 5      | 2.5             |
| Dog        | Mule             | 200      | 1      | 0.005           |
| Cat        | Shirazi          | 5        | 2      | 0.4             |
| Cat        | Siamese          | 3        | 3      | 1               |
| Cat        | Sphynx           | 7        | 4      | 0.5714          |

select *,round(avg(rating/position), 2) as quality ,
sum(case  when rating <3 then 1 else 0 end)/(select count(query_name) from Queries ) *100 as poor_query_percentage 
from Queries
group by query_name

-------------------

--select count(query_name) from Queries
--6
select
query_name,
round(avg(cast(rating as decimal) / position), 2) as quality,
round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
from
queries
group by
query_name;

--Wrong Answer
--12 / 13 testcases passed

select
query_name,
round(avg(cast(rating as decimal) / position), 2) as quality,
round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
from queries
where query_name is not null
group by query_name;

--PASS

1193. Monthly Transactions I
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
 

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
Output: 
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+

-- get year from (trans_date ) and month from (trans_date) combime year-month --month
-- count(id) group by year-month and country --trans_count
-- count(id) group by year-month and country --filter state = 'approved' --approved_count 
-- sum(amount) group by year-month and country --trans_total_amount 
-- sum(amount) group by year-month and country --filter state = 'approved' approved_total_amount 

select * , 
CONCAT(year(trans_date),'-', month(trans_date)) as mon,
count(id) as trans_count
from Transactions
group by mon, country       

--error
--[42S22] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Invalid column name 'mon'. (207) (SQLExecDirectW)

select * , 
CONCAT(year(trans_date),'-', month(trans_date)) as mon,
count(id) as trans_count
from Transactions
group by country 


--error
--[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Column 'Transactions.id' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause. (8120) (SQLExecDirectW)

select 
CONCAT(year(trans_date),'-', month(trans_date)) as mon,
count(id) as trans_count
from Transactions
group by country

--error
--[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Column 'Transactions.trans_date' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause. (8120) (SQLExecDirectW)


--year(trans_date) and month(trans_date) as month
--count(id) as trans_count,count(id) as approved_count --filter state = 'approved'
--sum(amount) as trans_total_amount  , count(amount) as approved_total_amount --filter state = 'approved'
--group by month , country 


--R1 f

with x as
(select * , rank() over (partition by product_id order by year asc) as r_no
from Sales)
select
product_id, year as first_year , quantity, price
from x where r_no = 1;

# Write your MySQL query statement below
select product_id, year as first_year, quantity, price
from
(select * , rank() over (partition by product_id order by year asc) as r_no
from Sales) as derv_table
where r_no = 1

GATE
SAS DLD EMFT -june -sept
NAS Control electronics -july -oct
Communication Analog Maths -aug -nov

IT
IBM data science -june
AWS SAA C03 2 months -june july
leetcode hackerrank kaggle - SQL and PYTHON

june july aug
sept oct nov
dec jan

6-12
6-7 exercise touch a grass
7-9 GATE
9-10 FOOD
10-12 IT

13-23


Find the largest single number. If there is no single number, report null.
The result format is in the following example.
 Example 1:
Input: 
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |

with x as
(
      select num,count(num) over (partition by num ) as cnt
      from MyNumbers
      order by num desc
)
,
y as
(
      select
      case when cnt = 1 then  num else Null end as result
      from x
)
select
distinct result as num from y
order by result desc
limit 1

--easy solution


select 
    max(num) as num 
from 
   (select
        num
    from 
        mynumbers
    group by 
        num
    having 
        count(num) = 1) as a;


Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input:
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+
Output:
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation:
The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.

# all product -product distinct count from Product
# count product by each customer_id
# return customer id where count of all product = count product by each customer_id

with x as
(
select *,count(distinct product_key) as cnt
from Customer
group by customer_id
)
select distinct customer_id
from x
where cnt in (
 select count(distinct product_key) as Total_cnt from Product
 )

SELECT  customer_id FROM Customer GROUP BY customer_id
HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product)
