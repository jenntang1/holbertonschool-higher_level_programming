# Overview #
The program codes contained in this directory is to learn and understand computer networking data obtained with Python.  

## General ##
0. How to fetch internet resources with the Python package urllib?  
```python
import urllib.request
with urllib.request.urlopen('https://www.python.org/') as response:
   html = response.read()
```

1. How to decode urllib body response?  
```python
import urllib.parse  
urllib.parse.unquote('https://www.python.org/")  
```

2. How to use the Python package requests #requestsiswaysimplerthanurllib?  
```python
import requests  
```

3. How to make HTTP GET request?  
```python
requests.get('https://www.python.org/')  
```

4. How to make HTTP POST/PUT/etc. request?  
```python
requests.post('https://www.python.org/', data = myobj)  
requests.put(('https://www.python.org/', params={key: value})  
```

5. How to fetch JSON resources?  
```python
response.json()  
```

## Resources ##
0. HOWTO Fetch Internet Resources Using The urllib Package  
https://docs.python.org/3/howto/urllib2.html  

1. Requests: HTTP for Humans  
https://requests.readthedocs.io/en/master/  

2. Python get
https://docs.python.org/3.4/library/stdtypes.html#dict.get  

## Contributor ##
Jennifer Tang  
