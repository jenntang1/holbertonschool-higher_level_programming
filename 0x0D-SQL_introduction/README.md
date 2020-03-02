# Overview #
The program codes contained in this directory is to help learn and understand building databases.  

## General ##
0. What’s a database?  
A database is a systematic collection of data.  

1. What’s a relational database?  
A relational database is the most popularily used DBMS.  It's a database where its collection of data is organized by tables, records and columns.  It's table can contain only one object representation.  

2. What does SQL stand for?  
SQL stands for Structured Query Language.  

3. What’s MySQL?  
MySQL is an open-source relational DBMS.  

4. How to create a database in MySQL?  
```sql
CREATE DATABASE database name;
```

5. What does DDL and DML stand for?  
DDL stands for Data Definition Language or Data Description Language.  DML stands for Data Manipulation Language.  

6. How to CREATE or ALTER a table?  
```sql
CREATE TABLE students (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT)
name VARCHAR(20),
age VARCHAR(2),
gender VARCHAR(6);
```

```sql
ALTER TABLE students ADD email VARCHAR(50);
```

7. How to SELECT data from a table?  
```sql
SELECT * FROM students;
```

8. How to INSERT, UPDATE or DELETE data?  
```sql
INSERT INT 'students' ('id','name','age','gender') VALUES (NULL, "Jane", "5","female");
```

```sql
UPDATE 'students' SET age="6" WHERE name="Jane";
```

```sql
DELETE FROM 'students' WHERE name="Jane";
```

9. What are subqueries?  
Subqueries are also called inner query or inner select.  They are nested inside a larger query.  It can be nested inside a SELECT, INSERT, UPDATE or DELETE statement.  It's usually added within the WHERE clause.  

10. How to use MySQL functions?  
MySQL has many built-in functions that are categorized into string, aggregate, control flow, comparison, data and time.  There are more that doesn't fit into these categories.  

The following illustrates the use of the UCASE function that takes a string in lowercase and converts it into uppercase.  
```sql
SELECT 'id','title', UCASE('title') FROM 'movies';
```

## Resources ##
0. What is Database & SQL?  
https://www.youtube.com/watch?v=FR4QIeZaPeM  

1. A Basic MySQL Tutorial  
https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial  

2. Basic SQL statements: DDL and DML  
https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php  

3. Basic queries: SQL and RA  
https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php  

4. SQL technique: functions  
https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php  

5. SQL technique: subqueries  
https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php  

6. What makes the big difference between a backtick and an apostrophe?  
https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458  

7. MySQL
https://en.wikipedia.org/wiki/MySQL  

8. MySQL Functions  
https://www.mysqltutorial.org/mysql-functions.aspx  

9. MySQL Functions: String, Numeric, User-Defined, Stored  
https://www.guru99.com/functions.html  

## Contributor ##
Jennifer Tang  
