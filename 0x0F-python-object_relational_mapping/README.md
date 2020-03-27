# Overview #
The program codes contained in this directory is to help with learning and understanding object-relational mapping in Python.  

## General ##
0. How to connect to a MySQL database from a Python script?  
In Python, use the connect() constructor to connect to a MySQL database.  The following is a basic Python script that illustrates this.  
```python
import mysql.connector

connection = mysql.connector.connect(
	user='username',
	password='password',
	host='ip address',
	database='database name')
```

1. How to SELECT rows in a MySQL table from a Python script?  
In Python, use the SELECT statement to select all rows/records from a MySQL table.  The following is a Python script that illustrates this.  
```python
import mysql.connector

connection = mysql.connector.connect(
	user='username',
	password='password',
	host='ip address',
	database='database name')

cursor = connection.cursor()

cursor.execute("SELECT * from table")
```

2. How to INSERT rows in a MySQL table from a Python script?  
In Python, use the INSERT statement to insert a row/record into a MySQL table.  The following is a Python script that illustrates this.  
```python
import mysql.connector

connection = mysql.connector.connect(
	user='username',
	password='password',
	host='ip address',
	database='database name')

cursor = connection.cursor()

data = "INSERT INTO table (column) VALUES ("data1", "data2")"

cursor.execute(data)
```

3. What ORM means?  
ORM stands for Object-Relational Mapper which is a library that transfers data stored in a relational database table into an object.  

4. How to map a Python Class to a MySQL table?  
SQLAlchemy maps a Python Class to a MySQL table by creating an engine.  

## Contributor ##
Jennifer Tang  
