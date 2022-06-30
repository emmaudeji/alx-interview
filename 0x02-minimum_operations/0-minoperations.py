#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result 
in exactly n * H characters in the file

returns 0 If n is impossible to achieve,.
"""


def minOperations(n):
    """
    returns fewest number of operations needed
    to result in exactly n * H characters
    """
    op = 0
    char = 1
    cp_op = 0
    while (char < n):
        if((n % char) == 0):
            op += 2
            cp_op = char
            char *= 2
        else:
            op += 1
            char += cp_op
    return 
