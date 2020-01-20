# Overview #
The program codes contained in this directory is for learning and understanding Python, specifically with inheritance.  

# General #
0. What is a superclass, baseclass or parentclass?  
They are all the same in terms of object oriented programming hierachy in that they are ancestral classes that other classes inherits from.  

1. What is a subclass?  
A subclass inherits from the superclass.  

2. How to list all attributes and methods of a class or instance?  
The built-in function, dir lists all attributes and methods in a class or instance.  

3. When can an instance have new attributes?  
An instance could define new attributes anytime within an instance by creating a new variable.  

4. How to inherit class from another?  
In order to inherit a class from another, define the new class with the superclass inside the parentheses.  

5. How to define a class with multiple base classes?  
```python
class SubclassName(BaseClass1, BaseClass2, BaseClass3, ...):
```

6. What is the default class every class inherit from?  
The superclass.  

7. How to override a method or attribute inherited from the base class?  
A override replaces a method or attribute from the superclass with a new one.  Simply create the new method or attribute in the subclass.  

8. Which attributes or methods are available by heritage to subclasses?  
All.  

9. What is the purpose of inheritance?  
Inheritance allows for ease of reusing programming codes.  

10. What are, when and how to use isinstance, issubclass, type and super built-in functions?  
The built-in isinstance checks an object's type and returns True or False.  
The built-in issubclass checks for class inheritance of an object's type and returns True or False.  

# Resources #
0. The Python Tutorial  
https://docs.python.org/3.4/tutorial/classes.html#inheritance  

1. Python 3 Object Oriented Programming  
https://hub.packtpub.com/inheritance-python/  

2. Learn to Program 10 : Inheritance Magic Methods  
https://www.youtube.com/watch?v=d8kCdLCi6Lk  

3. Python Course  
https://www.python-course.eu/python3\_inheritance.php  

# Contributor #
Jennifer Tang  
