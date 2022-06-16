#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle of (n)"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        new_row = [0] * (i+1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_row):
                current = pascal_triangle[i - 1][j]
                next = pascal_triangle[i - 1][j - 1]
                new_row[j] = current + next

        pascal_triangle[i] = new_row

    return pascal_triangle
