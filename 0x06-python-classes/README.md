# Overview #
The program codes contained in this repository is to learn and understand Python, specifically classess and objects.  

# General #
0. What is OOP?  
OOP stands for Object Oriented Programming which is when data and functions are combined inside an object.  Often times, we could write programs the procedure-oriented way which is when functions are grouped in blocks to manipulate data.  We use OOP when we write large programs.  

1. What is "first-class everything"?  
Functions, classes, modules, methods and data types all have equal status and are treated the same way.  

2. What is a class?  
A class creates a new data type by using **class**.  
![PythonClasses](https://i.imgur.com/u3SJKKV.png)

3. What is an object and an instance?  
An object is an instance of a class.  It can store data using variables that belongs to the object.  These variables are called fields and there are two types: instance variables and class variables.  

4. What is the difference between a class and an object or instance?  
An object or instance belongs to a class and uses the class' type.  

5. What is an attribute?  
An attribute is a collection of fields and methods for a class.  

6. What are and how to use public, protected and private attributes?  
Public = name  
Protected = \_name  
Private = \_\_name  

7. What is self?  
Self calls the instance.  

8. What is a method?  
A method are functions that belongs to a class.  

9. What is the special \_\_init\_\_ method and how to use it?  
It's the first function that runs in the class.  It acts as a function call to the getters and setters.  

10. What is Data Abstraction, Data Encapsaulation, and Information Hiding?  
Data Abstraction is a combination of Data Encapsaulation and Information Hiding.  
![PythonDataAbs](https://i.imgur.com/xgvfw4r.png)

11. What is a property?  
A property is an attribute used to define a getter.  

12. What is the difference between an attribute and a property in Python?  
A property is a type of attribute.  

13. What is the Pythonic way to write getters and setters in Python?  
getters = @property  
setters = @name.setter  

14. How to dynamically create arbitrary new attributes for existing instances of a class?  
https://stackoverflow.com/questions/2280334/shortest-way-of-creating-an-object-with-arbitrary-attributes-in-python  

15. How to bind attributes to object and classes?  
An object variable with the same name as the class variable hides the class variable.  

16. What is and what does contain \_\_dict\_\_ of a class and of an instance of a class?  
It retrieves all the attributes of a class.  

17. How does Python find the attributes of an object or class?  
By using \_\_dict\_\_.  

18. How to use the getattr function?  
It returns the value of the attribute.  

# Quiz #
0. In this following code, what is User?  A class  
```python
class User:
    id = 89
	name = "no name"
	__password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
			self.name = new_name
```

1. In this following code, what is id?  A public class attribute  
```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```

2. In this following code, what is \_\_password?  A private class attribute  
```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```

3. In this following code, what is is\_new?  A public instance attribute  
```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
        elf.name = new_name
```

4. What do these lines print?  True  
```python
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.is_new
```

5. What do these lines print?  89  
```python
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.id
```

6. What do these lines print?  'John'  
```python
>>> class User:
>>>     id = 89
3. In this following code, what is is\_new?  A public instance attribute  
```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```

7. What do these lines print?  'no name'  
```python
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.name
```

# Resources #
0. AB A Byte of Python  
https://swaroop-c-h.gitbook.io/byte-of-python/  

1. Python Course  
https://www.python-course.eu/python3\_object\_oriented\_programming.php  
https://www.python-course.eu/python3\_properties.php  

2. Learn to Program 9 : Object Oriented Programming  
https://www.youtube.com/watch?v=1AGyBuVCTeE&  

3. Python Classes and Objects || Python Tutorial || Learn Python Programming  
https://www.youtube.com/watch?v=apACNr7DC\_s  

4. 8. Object Oriented Programming  
https://www.youtube.com/watch?v=-DP1i2ZU9gk  

# Contributor #
Jennifer Tang  
