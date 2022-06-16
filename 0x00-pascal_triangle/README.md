0x00. Pascal's Triangle
=======================
How to generate Pascal triangle comprising od lists of list.

Introduction
------------
Pascal's triangle is a triangular array constructed by summing adjacent elements in preceding rows.

The first few elements of Pascals triangle are −
![image](https://user-images.githubusercontent.com/88405403/174070923-28bf2c7f-e632-47c1-9830-6780432bf196.png)

We are required to write a python script function that takes in a positive number, say n as the only argument.

The function should return an array of all the elements that must be present in the pascal's triangle in the (num)th row.
To build out this triangle, we need to take note of a few things.
- Each row starts and ends with a 1.
- Inside each row, between the 1s, each digit is the sum of the two digits immediately above it.
- We can use this pattern to build new rows starting with row 3. But we can’t use it to build the first or second rows.
- Each row is represented as an array; we need to output the entire triangle as an array of these rows (ie an array of arrays

Tasks
-----

### 0\. Pascal's Triangle

mandatory

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal's triangle of `n`:

-   Returns an empty list if `n <= 0`
-   You can assume `n` will be always an integer

```
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$

```

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x00-pascal_triangle`
-   File: `0-pascal_triangle.py`

 Done? Help Check your code

Copyright © 2022 ALX, All rights reserved.
