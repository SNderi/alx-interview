#!/usr/bin/python3
""" Module for a function that determines if
all boxes can be opened.
"""


def canUnlockAll(boxes):
    """ A method that determines if all the boxes can be opened. """
    for n in range(1, len(boxes)):
        subset = set(sum((boxes[:n] + boxes[n + 1:]), []))
        if n not in subset:
            return False
    return True
