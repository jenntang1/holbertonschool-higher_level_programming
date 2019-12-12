# Overview #
The program contained in this directory is for learning and developing proficiency with Python, specifically with import and modules.  

# General #
0. Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))?
Python has a lot of functionality contained in external and standard libraries.  

1. How to import functions from another file?  
Definitions such as functions and variables made could be stored in a module which essentially is a file.  These definitions could be imported into other modules (files).    

2. How to use imported functions?  
Use the import command.  

3. How to create a module?  
A module defines functions, classes and/or variables like so:  
```python
def hello_world():
	print("Hello World")
```

4. How to use the built-in function **dir()**?  
**dir()** returns a list of attributes of an object that could be a function, module, string, list or dictionary.  
```python
dir({object})
```

5. How to prevent code in your script from being executed when imported?  
Add the following if condition before the code you don't want to execute.  
```python
if __name__ == '__main__':
```

6. How to use command line arguments with your Python programs?  
Command line arguments are stored in the sys module's argv attribute as a list.  
```python
>>> import sys
>>> print(sys.argv)
	['demo.py', 'one', 'two', 'three']
```

The argparse module is another way to process command line arguments in that it extracts one or more filenames.  
```python
import argparse

parser = argparse.ArgumentParser(prog = 'top',
		    description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
	print(args)
```

# Quiz #
0. What do these lines print?  In my function  
```python
>>> def my_function():
>>>     print("In my function")
>>> 
>>> my_function()
```

1. What do these lines print?  function my\_function at …
```python
>>> def my_function():
>>>     print("In my function")
>>> 
>>> my_function
```

2. What do these lines print?  Counter: 12  
```python
>>> def my_function(counter):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function(12)
```

3. What do these lines print?  Counter: 12  
```python
>>> def my_function(counter=89):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function(12)
```

4. What do these lines print?  Counter: 89  
```python
>>> def my_function(counter=89):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function()
```

5. What do these lines print?  90  
```python
>>> def my_function(counter=89):
>>>     return counter + 1
>>> 
>>> print(my_function())
```

# Tasks #
0. Import a simple function from a simple file  
Write a program that imports the function def add(a, b): from the file add\_0.py and prints the result of the addition 1 + 2 = 3.  

1. My first toolbox! 
Write a program that imports functions from the file calculator\_1.py, does some Maths, and prints the result.

2. How to make a script dynamic!  
Write a program that prints the number of and the list of its arguments.  

3. Infinite addition  
Write a program that prints the result of the addition of all arguments.

4. Who are you?  
Write a program that prints all the names defined by the compiled module hidden\_4.pyc.  

5. Everything can be imported  
Write a program that imports the variable a from the file variable\_load\_5.py and prints its value.  

# Resources #
0. What makes the Python Cool.  
https://hackernoon.com/what-makes-the-python-cool-426e4c576685  

1. The Python Tutorial  
https://docs.python.org/3/tutorial/modules.html  

2. How to Code in Python 3  
https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3  

3. Python | dir() function  
https://www.geeksforgeeks.org/python-dir-function/  

4. Preventing Python Modules from Executing (if \_\_name\_\_ == ‘\_\_main\_\_’: Explained)  
https://medium.com/@eightlimbed/preventing-python-modules-from-executing-if-name-main-explained-78e574dc44e9  

# Contributor(s) #
Jennifer Tang
