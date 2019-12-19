# Overview #
The program codes contained in this directory is to learn and develop proficiency in Python, specifically with data structures: lists and tuples.

# General #
0. Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))?  
Because of lists and tuples.  

1. What are lists and how to use them?  
Lists are arrays that could store any data types.  They could be indexed and sliced.  They are mutable - can be altered.  

2. What are the differences and similarities between strings and lists?  
Strings are made up of characters only but lists could be any data type.  They could both be manipulated through various ways, e.g., index and slice.  

3. What are the most common methods of lists and how to use them?  
![pythonlistmethods](https://i.imgur.com/Eu1la2t.png)

4. How to use lists as stacks and queues?  
When using list as a stack, an element is LIFO - last in, first out.  When using list as a queue, an element is FIFO - first in, first out.  

5. What are list comprehensions and how to use them?  
List comprehension is another way to create a list using square brackets.  

6. What are tuples and how to use them?  
A tuple contains values separated by commas.  They could be integers or characters.  They are immutable - can't be altered, therefore, a new variable needs to be created to store it.  

7. When to use tuples versus lists?  
Lists runs faster than tuples because they are smaller in size.  

8. What is a sequence?  
Sequence types are lists, tuples, strings and range.  

9. What is tuple packing?  
A tuple packing is when a value is placed into a new variable on the left hand side (the usual).  

10. What is sequence unpacking?  
A sequence unpacking is when a value is pulled back into a variable on the right hand side.  

11. What is the del statement and how to use it?  
A del statement removes an element from a list but doesn't return a value like pop does.  It could also be used to remove a variable.  

# Quiz #
0. What do these lines print?  1  
```python
>>> a = [1, 2, 3, 4]
>>> a[0]
```

1. What do these lines print?  4  
```python
>>> a = [1, 2, 3, 4]
>>> a[-1]
```

2. What do these lines print?  2  
```python
>>> a = [1, 2, 3, 4]
>>> a[-3]
```

3. What do these lines print?  4  
```python
>>> a = [1, 2, 3, 4]
>>> len(a)
```

4. What do these lines print?  5  
```python
>>> a = [1, 2, 3, 4]
>>> a.append(5)
>>> len(a)
```

5. What do these lines print?  [2, 3]  
```python
>>> a = [1, 2, 3, 4]
>>> a[1:3]
```

6. What do these lines print?  [1, 2, 10, 4]  
```python
>>> a = [1, 2, 3, 4]
>>> a[2] = 10
>>> a
```

7. What do these lines print?  [1, 2, 3, 4]  
```python
>>> a = [1, 2, 3, 4]
>>> b = a
>>> b
```

8. What do these lines print?  [1, 2, 10, 4]  
```python
 = [1, 2, 3, 4]
 >>> b = a
 >>> a[2] = 10
 >>> a
```

9. What do these lines print?  [1, 2, 10, 4]  
```python
>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> b
```

# Tasks #
0. Print a list of integers  
Write a function that prints all integers of a list.  

1. Secure access to an element in a list   
Write a function that retrieves an element from a list like in C.  

2. Replace element  
Write a function that replaces an element of a list at a specific position (like in C).  

3. Print a list of integers... in reverse!  
Write a function that prints all integers of a list, in reverse order.  

4. Replace in a copy  
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).  

5. Can you C me now?  
Write a function that removes all characters c and C from a string.  

6. Lists of lists = Matrix  
Write a function that prints a matrix of integers.  

7. Tuples addition   
Write a function that adds 2 tuples.  

8. More returns!  
Write a function that returns a tuple with the length of a string and its first character.  

9. Find the max  
Write a function that finds the biggest integer of a list.  

10. Only by 2  
Write a function that finds all multiples of 2 in a list.  

11. Delete at   
Write a function that deletes the item at a specific position in a list.  

12. Switch   
Complete the source code in order to switch value of a and b.  

13. Linked list palindrome   
Write a function in C that checks if a singly linked list is a palindrome.  

# Resources #
0. The Python Tutorial  
https://docs.python.org/3.4/tutorial/introduction.html#lists  

1. Learn to Program 6 : Lists  
https://www.youtube.com/watch?v=A1HUzrvS-Pw  

2. Python List Methods  
https://www.programiz.com/python-programming/methods/list  

3. Python List vs. Tuples  
https://www.programiz.com/python-programming/list-vs-tuples  

4. Python TUPLE - Pack, Unpack, Compare, Slicing, Delete, Key  
https://www.guru99.com/python-tuples-tutorial-comparing-deleting-slicing-keys-unpacking.html#1  

# Contributor(s) #
Jennifer Tang  
