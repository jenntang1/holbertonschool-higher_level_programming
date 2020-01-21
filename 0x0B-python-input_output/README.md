# Overview #
The program codes contained in this directory is for learning and understanding Python, specifically with input/output.  

# General #
0. How to open a file?  
Use the open built-in function to open a file.  The mode is optional and these are the options: w for write, r for read, r+ for read and write and a for open to append.  In the following example, f is the file object returned when filename is opened.  

```python
>>> f = open(filename, mode)
```

1. How to write text in a file?  
Use the write built-in function to write to a file or use open with the w mode.  In the following example, f is the file object to write into.  

```python
>>> f.write('Hello World\n')
>>> f = open(filename, 'w')
```

2. How to read the full content of a file?  
Use the read built-in function to read an entire file.  In the following example, f is the file object to read from.  

```python
>>> f.read()
```

3. How to read a file line by line?  
Use the readline built-in function to read line-by-line from a file.  In the following example, f is the file object to read from.  

```python
>>> f.readline()
```

4. How to move the cursor in a file?  
Use the seek built-in function to change the position of the cursor in an already opened file.  The offset component tells how many position to move the cursor to.  The from\_what component is the reference position and probably where the cursor is currently at.  This component is an integer value in which 0 indicates the beginning of the file, 1 indicates the current position of the file and 2 indicates the end of the file.  If nothing is specified, 0 is assumed.  

5. How to make sure a file is closed after using it?  
Use the close built-in function to close a file.  In the following example, f is the file object to close.  

```python
>>> f.close()
```

6. What is and how to use the with statement?  

7. What is JSON?  
JSON stands for JaveScript Object Notation and it's a module that converts Python data hierarchies to string representations.  This process deconstructs and it's called serialization.  If reconstructing (string representations to data hierarchies) then, it's called deserialization.  

9. How to convert a Python data structure to a JSON string?  
The dumps function in the json module is used to convert and view the code in JSON.  The following encodes to JSON in which x is the data to encode into a text file called f:

```python
json.dump(x, f)
```

10. How to convert a JSON string to a Python data structure?  
The following decodes from JSON:

```python
x = json.load(f)
```

# Resources #
0. The Python Tutorial - 7.2. Reading and Writing Files  
https://docs.python.org/3.4/tutorial/inputoutput.html#reading-and-writing-files  

1. The Python Tutorial - 8.7. Predefined Clean-up Actions  
https://docs.python.org/3.4/tutorial/errors.html#predefined-clean-up-actions  

2. The Python Tutorial - 19.2 json - JSON encoder and decoder  
https://docs.python.org/3.4/library/json.html  

3. CHAPTER -1. WHAT’S NEW IN “DIVE INTO PYTHON 3”  
http://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf  

4. Learn to Program 8 : Reading / Writing Files  
https://www.youtube.com/watch?v=EukxMIsNeqU  

5. Automate the Boring Stuff with Python By Al Sweigart  
https://automatetheboringstuff.com  

# Contributor #
Jennifer Tang  
