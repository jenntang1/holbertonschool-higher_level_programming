# Overview #
The program codes contained in this directory is to help learn and understand SQL.  

## General ##
0. How to create a new MySQL user?  
```sql
CREATE USER newuser@localhost IDENTIFIED BY password;
```

1. How to manage privileges for a user to a database or table?  
There are many permission types in SQL.  A user could have ALL PRIVILEGES which grants full access to database, table and every data within.  A user could have access to CREATE database or table.  A user could have access to DROP (delete) database or table only.  A user could have access to DELETE rows from a table.  A user could have access to INSERT rows into a table.  A user could have read only access, granting usage of the SELECT command.  A user could have write only access, granting usage of the UPDATE command.  A user could have the ability to manage privileges only, granting usage of the GRANT OPTION command.  

The following illustrates user access granted to both database and table.  
```sql
GRANT ALL PRIVILEGES ON * . * TO user@localhost;
```

The following illustrates user access granted for specific permission type.  
```sql
GRANT permissiontype ON databasename.tablename TO user@localhost;
```

2. What’s a PRIMARY KEY?  
A PRIMARY KEY is a unique key assigned to one record in a table.  It can't be NULL and there's only one for each table.  

3. What’s a FOREIGN KEY?  
A FOREIGN KEY is assigned to a field that could be referred to a field in another table.  Basically, it creates a link between two separate tables.  

4. How to use NOT NULL and UNIQUE constraints?  

The following illustrates the use of NOT NULL.  
```sql
CREATE TABLE Student(id INT, name TEXT NOT NULL);
```

The following illustrates the use of UNIQUE.  The name field is assigned as the UNIQUE.  
```sql
CREATE TABLE Student(id INT, name VARCHAR(30) UNIQUE);
```

5. How to retrieve data from multiple tables in one request?  
By implementing multiple joins and the distinct keyword techniques, we could retrieve data from multiple tables in one request.  

6. What are JOIN and UNION?  
JOIN allows retrieval of data from two separate tables.  UNION allows the retrieved data to be combined into a new table.  

## Resources ##
0. How To Create a New User and Grant Permissions in MySQL  
https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql  

1. MySQL Tutorial  
https://www.mysqltutorial.org/mysql-adminsitration/mysql-grant-aspx/  

2. MySQL constraints  
http://zetcode.com/databases/mysqltutorial/constraints/  

3. DB Design UML SQL  
https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php  

4. SQL Commands Cheat Sheet  
https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf  

5. A beginner's guide to 7 types of SQL JOINs  
https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html  

6. MySQL Tutorial by Derek Banas  
https://www.youtube.com/watch?v=yPu6qV5byu4  

7. SQL Style Guide  
https://www.sqlstyle.guide  

8. MySQL Documentation  
https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html  

## Contributor ##
Jennifer Tang  
