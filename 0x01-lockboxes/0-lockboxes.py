#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Define a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    keys = [0]
    for k in keys:
        for key in boxes[k]:
            if key not in keys:
                if key < len(boxes):
                    keys.append(key)

    if len(keys) == len(boxes):
        return True
    return False
