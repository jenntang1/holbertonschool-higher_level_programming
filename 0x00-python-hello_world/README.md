# Overview #
The program codes contained in this directory is for learning and developing proficiency with Python.  

# General #
0. Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))?  
*The Zen of Python, by Tim Peters*  
Beautiful is better than ugly.  
Explicit is better than implicit.  
Simple is better than complex.  
Complex is better than complicated.  
Flat is better than nested.  
Sparse is better than dense.  
Readability counts.  
Special cases aren't special enough to break the rules.  
Although practicality beats purity.  
Errors should never pass silently.  
Unless explicitly silenced.  
In the face of ambiguity, refuse the temptation to guess.  
There should be one-- and preferably only one --obvious way to do it.  
Although that way may not be obvious at first unless you're Dutch.  
Now is better than never.  
Although never is often better than \*right\* now.  
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.  
Namespaces are one honking great idea -- let's do more of those!  

1. Who created Python?  
Dutch programmer, Guido van Rossum created Python as a hobby during his Christmas break.  

2. Who is Guido van Rossum?  
Rossum is a computer programmer and author who created high-level programming language, Python in 1989.  The goal was to create a "Computer Programming for Everybody."  It would be an easy and intuitive language, open source and suitable for daily tasks.  Additionally, Rossum created Mondrian while at Google.  It's a web-based system written in Python for code review/peer review.  

3. Where does the name ‘Python’ come from?  
Rossum is a big fan of the tv comedy, Monty Python.  

4. What is the Zen of Python?  
It's the 19 guidelines that influenced the creation of Python.  It will appear by running command *import this*.   

5. How to use the Python interpreter?  
The interpreter operates similarily to the Shell, i.e., reads and executes commands.  In order to open the interpreter, the user needs to be type *py* or *python -c command*.  In order to close the interpreter, the user types *Ctrl + D* or *quit()*.  

6. How to print string and variables using print?  
The following is the general syntax to printing a string in Python.  
```python
%[flags][width][.precision]type 
```

    The following are the conversions and flags for print.  
![pythonprintconversions](https://i.imgur.com/Tr4bNs4.png)  
![pythonprintflags](https://i.imgur.com/gXPTOmk.png)  

    The following are syntaxes to printing string in Python.  
```python
>>> print("The capital of {0:s} is {1:s}".format("Ontario","Toronto"))
The capital of Ontario is Toronto
>>> print("The capital of {province} is {capital}".format(province="Ontario",capital="Toronto"))
The capital of Ontario is Toronto
```

    The following are syntaxes to printing variables in Python.  
```python
>>> q = 459
>>> p = 0.098
>>> print(q, p, p * q)
459 0.098 44.982
>>> print(q, p, p * q, sep=",")
459,0.098,44.982
>>> print(q, p, p * q, sep=" :-) ")
459 :-) 0.098 :-) 44.982
```

7. How to use strings?  
Strings needs to be enclosed with either single or double quotes.  Similiar to the Shell, backspace could be used to escape special characters.  

8. What are indexing and slicing in Python?  
Strings are a sequence of one or more individual characters.  These characters could be letters, numbers, symbols or whitespaces.  Hence, indexing and slicing are the ways to access parts of a string.  

    Indexing:
![pythonstrindexing](https://i.imgur.com/SRsxNIG.png)  

    Slicing:
```python
>>> print(ss[6:11])
>>> Shark
>>> print(ss[7:])
>>> hark!
>>> print(ss[-4:-1])
>>> ark
>>> print(ss[6:11:1])
>>> Shark
```

9. What is the official Holberton Python coding style and how to check your code with pycodestyle?  
Pycodestyle (formerly known as Pep8) is the official Holberton Python coding style.  The following is the command used to check program codes with pycidestyle.  
```shell
 pycodestyle --first optparse.py
 optparse.py:69:11: E401 multiple imports on one line
 optparse.py:77:1: E302 expected 2 blank lines, found 1
 optparse.py:88:5: E301 expected 1 blank line, found 0
 optparse.py:222:34: W602 deprecated form of raising exception
 optparse.py:347:31: E211 whitespace before '('
 optparse.py:357:17: E201 whitespace after '{'
 optparse.py:472:29: E221 multiple spaces before operator
 optparse.py:544:21: W601 .has_key() is deprecated, use 'in'
```  

# Quiz #
0. Who created Python?  Guido van Rossum  

1. What does this command line print?  Holberton school  
```python
>>> print("Holberton school")
```

2. What does this command line print?  98 Battery street  
```python
>>> print("{:d} Battery street".format(98))
```

3. What does this command line print?  98 Battery street, San Francisco  
```python
>>> print("{:d} Battery street, {}".format(98, "San Francisco"))
```

4. What does this command line print?  o  
```python
>>> a = "Python is cool"
>>> print(a[4])
```

5. What does this command line print?  Python  
```python
>>> a = "Python is cool"
>>> print(a[0:6])
```

6. What does this command line print?  Python  
```python
>>> a = "Python is cool"
>>> print(a[:6])
```

7. What does this command line print?  is cool  
```python
>>> a = "Python is cool"
>>> print(a[7:])
```

8. What does this command line print?  is  
```python
>>> a = "Python is cool"
>>> print(a[7:-5])
```

9. What does this command line print?  o  
```python
>>> a = "Python is cool"
>>> print(a[-2])
```

# Tasks #
0. Run Python file  
    Write a Shell script that runs a Python script.  

1. Run inline  
    Write a Shell script that runs Python code.

2. Hello, print  
    Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.  

3. Print integer  
    Complete https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.  

4. Print float  
    Complete https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py in order to print the float stored in the variable number with a precision of 2 digits.  

5. Print string  
    Complete https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py in order to print 3 times a string stored in the variable str, followed by its first 9 characters.  

6. Play with strings  
    Complete https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py to print Welcome to Holberton School!  

7. Copy - Cut - Paste  
    Complete https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py  

8. Create a new sentence  
    Complete https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py to print object-oriented programming with Python, followed by a new line.  
	
9. Easter Egg  
    Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.  
	
10. Linked list cycle
    Write a function in C that checks if a singly linked list has a cycle in it.  

# Resources #
0. The Python Tutorial  
    https://docs.python.org/3/tutorial/index.html  

1. How To Use String Formatters in Python 3  
    https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3  

2. Learn to Program  
    https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt  

3. PEP 8 -- Style Guide for Python Code  
    https://www.python.org/dev/peps/pep-0008/  

4. The Zen of Python, Explained  
    https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/  

5. How to Index and Slice Strings in Python 3  
    https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3  

# Contributor(s) #
Jennifer Tang  
