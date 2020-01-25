# Overview #
The program codes contained in this directory is to help with learning and understanding Python, specifically classes, unittesting and JSON.  

# General #
0. What is Unit testing and how to implement it in a large project?  
In the unittest module, there are many tools used to automate testing of program codes.  Personally, I think creating a code base first and then, create unit tests every time an error is found.  

1. How to serialize and deserialize a Class?  
In the json module, the JSONEncoder would serialize a class when passed into the class and then, the class is passed into the dumps function.  The JSONDecoder works similiarily but with more options.  

2. How to write and read a JSON file?  
In the json module, the dump function writes data objects to a file and the load function reads strings from a file.

3. What is \*args and how to use it?  
\*args is a magic variable that allows user to pass an unknown number of non-keyword arguments into a function.  
![Pythonargs](https://i.imgur.com/Uxigeoa.png)

4. What is \*\*kwargs and how to use it?  
\*\*kwargs is also a magic variable that allows user to pass an unknown number of keyword arguments into a function.  Keyword arguments are also known as named arguments.  
![Pythonkargs](https://i.imgur.com/67Ho8oI.png)

5. How to handle named arguments in a function?  
Name arguments explicitly states what the arguments represent.  Often times, we can leave out arguments if a default value is stated.  Also, since the arguments have a name associated to it, its position could be rearranged when called.

# Resources #
0. Python Tips  
https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/  

1. json — JSON encoder and decoder  
https://docs.python.org/3/library/json.html  

2. 26.3. unittest — Unit testing framework  
https://docs.python.org/3.4/library/unittest.html#module-unittest  

3. PY Sheet  
https://www.pythonsheets.com/notes/python-tests.html  

# Contributor #
Jennifer Tang  
