UTF-8 Validation
================

Resources
---------

-   [UTF-8](https://alx-intranet.hbtn.io/rltoken/oqFi6P1hNvp9aSuNv---IQ "UTF-8")
-   [Characters, Symbols, and the Unicode Miracle](https://alx-intranet.hbtn.io/rltoken/d--jVK8sBSlhkosu7pFzdw "Characters, Symbols, and the Unicode Miracle")
-   [watch](https://www.youtube.com/watch?v=MijmeoH9LT4)


Tasks
-----
```
Write a method that determines if a given data set represents a valid UTF-8 encoding.

-   Prototype: `def validUTF8(data)`
-   Return: `True` if data is a valid UTF-8 encoding, else return `False`
-   A character in UTF-8 can be 1 to 4 bytes long
-   The data set can contain multiple characters
-   The data will be represented by a list of integers
-   Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
```
Test
----
```
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$

```
Expected result
---------------
```
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```
