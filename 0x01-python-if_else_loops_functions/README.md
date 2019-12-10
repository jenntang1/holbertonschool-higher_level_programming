# Overview #
The program codes contained in this directory is for learning and developing proficiency with Python, specifically with if/else, loops and functions.  

# General #  
0. Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))?  
\#pythoniscool because it offers more structure, support and error checking than low-level programming language.  

1. Why indentation is so important in Python?  
Python implements a coding block style.  A block is a group of statements where indentation (whitespace) is used to distinguish it.  

2. How to use the if, if ... else statements?  
In Python, if/elif(else if)/else statements ends with **:**.  There could be an unlimited elif statements and else statements are optional.  
![pythonifelifelse](https://i.imgur.com/sTFfg0i.png)

3. How to use comments?  
A single line comment starts with **#** and is useful to explain variables, function declarations and expressions.
![pythoncomment1](https://i.imgur.com/Lc9ZJhn.png)

    A multi-line comment starts and ends with **"""** or **'''**.  The comment goes in-between.  
![pythoncomment2](https://i.imgur.com/WZob11l.png)  

4. How to affect values to variables?  
A variable holds a value regardless of data type.  
![pythonvars](https://i.imgur.com/lBk0651.png)

5. How to use the while and for loops?  
The general idea of loop statements is that they will continue to execute as long as the stated condition is true.  The following are flow diagrams and examples to better visualize the implementation of while and for loop statements in Python.
![pythonwhile](https://i.imgur.com/VCGIKtA.png)
![pythonfor](https://i.imgur.com/G5CGauQ.png)

6. How is Python’s for different from C‘s?  
The following are the key differences.  

| #   | C                                            | Python                                      |
| --- | -------------------------------------------- | ------------------------------------------- |
| 1.  | a compiled language directly to machine code | a interpreted language compiled to bytecode |
| 2.  | executed by CPU                              | interpreted by a C program                  |
| 3.  | variables and data types are declared        | no declaraction needed                      |
| 4.  | pointers are available                       | variables are pointers                      |
| 5.  | limited built-in functions                   | more built-in functions                     |
| 6.  | faster program execution                     | slower program execution                    |

7. How to use the break and continues statements?  


8. How to use else clauses on loops?

9. What does the pass statement do, and when to use it?

10. How to use range?  

11. What is a function and how do you use functions?  

12. What does return a function that does not use any return statement?  

13. Scope of variables?  
The part of a program code where a variable is accesible is the scope.  A variable defined at the top and visible throughout the program code is a global variable.  A variable defined inside a function and only used within it is a local variable.  
![pythonscopevars](https://i.imgur.com/PX9ZBb9.png)  

14. What’s a traceback?  

15. What are the arithmetic operators and how to use them?  


# Quiz #  
0. What do these lines print?  Holberton  
```python
if True:
    print("Holberton")
else:
	print("School")
```

1. What do these lines print?  Holberton  
```python
if 12 == 48/4:
    print("Holberton")
else:
	print("School")
```

2. What do these lines print?  School
```python
if 12 == 48/4 and False:
    print("Holberton")
else:
	print("School")
```

3. What do these lines print?  Holberton  
```python
if 12 == 48/3 or 12 is 12:
    print("Holberton")
else:
	print("School")
```

4. What do these lines print?  Holberton  
```python
a = 12
if a > 2:
    if a % 2 == 0:
		print("Holberton")
	else:
		print("C is fun")
else:
	print("School")
```

5. What do these lines print?  C is fun  
```python
a = 12
if a < 2:
    print("Holberton")
elif a % 2 == 0:
	print("C is fun")
else:
	print("School")
```

6. What do these lines print?  0 1 2 3  
```python
for i in range(4):
    print(i, end=" ")
```

7. What do these lines print?  2 3  
```python
for i in range(2, 4):
    print(i, end=" ")
```

8. What do these lines print?  2 4 6 8  
```python
for i in range(2, 10, 2):
    print(i, end=" ")
```

# Tasks #  
0. Positive anything is better than negative nothing   
This program will assign a random signed number to the variable number each time it is executed. Complete https://github.com/holbertonschool/0x01.py/blob/master/0-positive\_or\_negative\_py in order to print whether the number stored in the variable number is positive or negative.  

1. The last digit  
This program will assign a random signed number to the variable number each time it is executed. Complete https://github.com/holbertonschool/0x01.py/blob/master/1-last\_digit\_py in order to print the last digit of the number stored in the variable number.  

2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game   
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.  

3. When I was having that alphabet soup, I never thought that it would pay off  
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.  

4. Hexadecimal printing  
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example).  

5. 00...99  
Write a program that prints numbers from 0 to 99.  

6. Inventing is a combination of brains and materials. The more brains you use, the less material you need  
Write a program that prints all possible different combinations of two digits.  

7. islower  
Write a function that checks for lowercase character.  

8. To uppercase  
Write a function that prints a string in uppercase followed by a new line.  

9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important  
Write a function that prints the last digit of a number.  

10. a + b  
Write a function that adds two integers and returns the result.  

11. a ^ b  
Write a function that computes a to the power of b and return the value.  

12. Fizz Buzz  
Write a function that prints the numbers from 1 to 100 separated by a space.  

13. Insert in sorted linked list  
Write a function in C that inserts a number into a sorted singly linked list.  

# Resources #  
0. The Python Tutorial  
    https://docs.python.org/3/tutorial/index.html  

1. How To Code in Python 3  
    https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3  

2. Learn to Program  
    https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt  

3. PEP 8 -- Style Guide for Python Code  
    https://www.python.org/dev/peps/pep-0008/  

4. Python Indentation Myths  
    https://files.meetup.com/1544869/Python%20Indentation%20Myths.pdf

5. Python IndentationError: expected an indented block    
https://www.youtube.com/watch?v=1QXOd2ZQs-Q  

6. Statement, Indentation and Comment in Python  
    https://www.geeksforgeeks.org/statement-indentation-and-comment-in-python/  

7. A beginner's guide to Python's namespaces, scope resolution, and the LEGB rule  
    https://nbviewer.jupyter.org/github/rasbt/python_reference/blob/master/tutorials/scope_resolution_legb_rule.ipynb  

8. Object-Oriented Programming in Python  
    https://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html  

9. Tutorialspoint  
    https://www.tutorialspoint.com/index.htm  

10. man python3  

# Contributor(s) #  
Jennifer Tang  
