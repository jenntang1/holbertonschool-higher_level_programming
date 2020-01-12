# Overview #
The program codes contained in this repository is to help learn and understand Python, specifically test-driven development (TDD).  

# General #
0. What’s an interactive test?  
It's when a doctest module searches and executes text that are flagged as interactive Python sessions.  
```python
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

1. Why tests are important?  
In order to build a dynamic and nearly failproof program, testing needs to be done before implementation.  

2. How to write Docstrings to create tests?  
See 0. above.  

3. How to write documentation for each module and function?  
See 0. above.  

4. What are the basic option flags to create tests?  
doctest.DONT\_ACCEPT\_TRUE\_FOR\_1  
doctest.DONT\_ACCEPT\_BLANKLINE  
doctest.NORMALIZE\_WHITESPACE  
doctest.ELLIPSIS  
doctest.IGNORE\_EXCEPTION\_DETAIL  
doctest.SKIP  
doctest.COMPARISON\_FLAGS  
doctest.REPORT\_UDIFF  
doctest.REPORT\_CDIFF  
doctest.REPORT\_NDIFF  
doctest.REPORT\_ONLY\_FIRST\_FAILURE  
doctest.FAIL\_FAST  
doctest.REPORTING\_FLAGS  
doctest.register\_optionflag(name)  

5. How to find edge cases?  
Continuous testing!  

# Quiz #
0. Is this a standardized way to comment a function in Python?  No  
```python
/* Addition function */
def add(a, b):
    return a + b
```

1. Is this a standardized way to comment a function in Python?  No
```python
"""" Addition function """
def add(a, b):
    return a + b
```

2. Is this a standardized way to comment a function in Python?  No
```python
##########
# Addition function
##########
def add(a, b):
    return a + b
```

3. Is this a standardized way to comment a function in Python?  Yes
```python
def add(a, b):
    """ Addition function """
    return a + b
```

4. Is this module correctly commented?  Yes
```python
#!/usr/bin/python3
"""
    My calculation module
"""
import sys
...
```

5. Is this module correctly commented?  No, docstring must be before import statements.  
```python
#!/usr/bin/python3
import sys

"""
    My calculation module
"""
...
```

6. Based on this code, what should all the test cases be?  
```python
def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list
```

- empty list  
- list with one element of any type  
- list with two difference elements of the same type  
- list with twice the same elements of the same type  
- list with more than two times the same elements of the same type  
- list with multiple types such as int, str, etc.  
- not a list argument such as passing a dictionary to the method  

# Resources #
0. The Python Tutorial  
https://docs.python.org/3/library/doctest.html  

1. doctest — Testing Through Documentation  
https://pymotw.com/3/doctest/  

2. index of  
http://index-of.es/Python/  

# Contributor #
Jennifer Tang  
