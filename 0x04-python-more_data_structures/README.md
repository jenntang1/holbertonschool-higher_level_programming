# Overview #
The program codes in this directory are to assist in learning and developing proficiency with Python, specifically with data structures: set and dictionary.  

# General #
0. Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))?  
Because of sets and dictionaries.  

1. What are set and how to use them?  
A set is a data type of unordered collection of unique elements.  

2. What are the most common methods of set and how to use them?  
![pythonsetmethods](https://i.imgur.com/uSudrkH.png)

3. When to use sets versus lists?  
Sets are faster than lists when searching for a value, however, it's slower when iterating.  

4. How to iterate into a set?  
A simple loop could be used to iterate into a set.  A loop using enumerate could also be used for iteration.  Importing timeit from libraries could also help with iteration.  

5. What are dictionary and how to use them?  
A dictionary is a data structure used to associate a key to a value.  Similar to lists, a key is a single element.  Meanwhile, a value could be any type: list, list within a list or numbers.  

6. When to use dictionaries versus lists or sets?  
A dictionary is quite different from lists and sets, therefore, usage between the three depends on the situation.  A dictionary holds more information then both lists and sets.  

7. What is a key in a dictionary?  
A key is a string element in a dictionary that holds a value.  

8. How to iterate into a dictionary?  
Since a dictionary contains a key and its associated value, it's possible to iterate into a dictionary via the key or value or both.  

9. What is a lambda function?  
The creator of Python, Guido van Rossum tried to make the lambda, filter, map and reduce functions obsolete but without success with the exception of reduce.  Because list comprehension is a more efficient way to create small functions that are "throw-away" or "anonymous."  

10. What is map and reduce functions?  
A map function takes two arguments where the first is the name of the function and the second is its sequence.  A reduce function has been made obsolete because it's limited to associative operators.  

# Quiz #
0. What do these lines print?  89  
```python
>>> a = { 'id': 89, 'name': "John" }
>>> a['id']
```

1. What do these lines print?  89  
```python
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('id')
```
2. What do these lines print?  Nothing
```python
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age')
```

3. What do these lines print?  0  
```python
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age', 0)
```

4. What do these lines print?  [1, 2, 3, 4]  
```python
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')
```

5. What do these lines print?  4  
```python
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')[3]
```

6. What do these lines print? 'Amy'  
```python
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
>>> a.get('friends')[-1].get("name")
```

7. What do these lines print?  0 1 2  
```python
>>> for i in range(0, 3):
>>>     print(i, end=" ")
```

8. What do these lines print?  1 2 3  
```python
>>> for i in range(1, 4):
>>>     print(i, end=" ")
```

9. What do these lines print?  1 2 3 4  
```python
>>> for i in [1, 2, 3, 4]:
>>>     print(i, end=" ")
```

10. What do these lines print?  1 3 4 2  
```python
>>> for i in [1, 3, 4, 2]:
>>>     print(i, end=" ")
```

11. What do these lines print?  Hello Holberton School 98  
```python
>>> for i in ["Hello", "Holberton", "School", 98]:
>>>     print(i, end=" ")
```

# Tasks #
0. Squared simple  
Write a function that computes the square value of all integers of a matrix.  

1. Search and replace  
Write a function that replaces all occurrences of an element by another in a new list.  

2. Unique addition  
Write a function that adds all unique integers in a list (only once for each integer).  

3. Present in both  
Write a function that returns a set of common elements in two sets.  

4. Only differents  
Write a function that returns a set of all elements present in only one set.  

5. Number of keys  
Write a function that returns the number of keys in a dictionary.  

6. Print sorted dictionary  
Write a function that prints a dictionary by ordered keys.  

7. Update dictionary  
Write a function that replaces or adds key/value in a dictionary.  

8. Simple delete by key  
Write a function that deletes a key in a dictionary.  

9. Multiply by 2  
Write a function that returns a new dictionary with all values multiplied by 2.  

10. Best score  
Write a function that returns a key with the biggest integer value.  

11. Multiply by using map  
Write a function that returns a list with all values multiplied by a number without using any loops.  

12. Roman to Integer  
Create a function that converts a Roman numeral to an integer.  

# Resources #
0. The Python Tutorial  
https://docs.python.org/3.4/tutorial/datastructures.html  

1. Python Course  
https://www.python-course.eu/python3\_lambda.php  

2. Learn to Program 12 Lambda Map Filter Reduce  
https://www.youtube.com/watch?v=1GAC6KQUPeg  

3. Python Set Methods  
https://www.w3schools.com/python/python\_ref\_set.asp  

4. Iterate over a set in Python  
https://www.geeksforgeeks.org/iterate-over-a-set-in-python/  

# Contributor(s) #
Jennifer Tang
