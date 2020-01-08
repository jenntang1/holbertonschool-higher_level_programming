# Overview #
The program codes contained in this directory is to help learn and understand Python, specifically exceptions.  

# General #
0. What’s the difference between errors and exceptions?  
Errors are usually due to incorrect syntax aka parsing errors, meanwhile, exceptions are errors that occurs during execution.  

1. What are exceptions and how to use them?  
Exceptions are non-fatal and syntactically sound errors that occurs during execution.  The following is an example of an exception error.  The exception type is printed first followed by a detailed explanation on why the program couldn't execute.  
![PythonException](https://i.imgur.com/5rxMkIE.png)  

2. When do we need to use exceptions?  
Exceptions are useful when debugging program codes that are attempting to be executed.  

3. How to correctly handle an exception?  
Programmers could write programs that handles exceptions.  For example, the **try** functionn takes user input and executes it.  If it's followed by the **except** function and an exception occurs, then the **except** function is executed instead.  If an exception occurs but it doesn't match the one specified, then it's an unhandled exception that breaks execution.  There could be multiple **except** functions for different exception cases.  

It's best to first implement the **BaseException** which is the base exception class that defined all the basic attributes of an exception.  **GeneratorExit**, **SystemExit** and **KeyboardInterrupt** are builtin exceptions that are based off of the **BaseException**.  

4. What’s the purpose of catching exceptions?  
See 2. above.  

5. How to raise a builtin exception?  
The **raise** function forces an exception to occur.  The following are some ways to use it:  
![PythonRaise1](https://i.imgur.com/V4yT9TX.png)  
![PythonRaise2](https://i.imgur.com/tY2ITKO.png)  
![PythonRaise3](https://i.imgur.com/GFG20jY.png)  

6. When do we need to implement a clean-up action after an exception?  
In the **try** function, the option **finall** could be used to define a clean-up action.  It's will be the last step executed in the program, whether or not an exception occurs.  

# Resources #
0. The Python Tutorial  
https://docs.python.org/3/tutorial/errors.html  
https://docs.python.org/3/library/exceptions.html#bltin-exceptions  

1. Learn to Program 11 Static & Exception Handling  
https://www.youtube.com/watch?v=7vbgD-3s-w4  

2. **pydoc2 exceptions** and **pydoc3 builtins**  

3. Julien Danjou - The definitive guide to Python exceptions  
https://julien.danjou.info/python-exceptions-guide/  

# Contributor #
Jennifer Tang  
