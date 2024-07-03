#!/usr/bin/python3
"""Module 0-lockboxes.py"""


def canUnlockAll(boxes):
    """Function that creates a list to keep track of opened boxes

    Args:
        boxes (list): Liat of Integers
    """
    opened = [False] * len(boxes)
    # The first box is always unlocked
    opened[0] = True
    # Create a stack to keep track of the boxes to be opened
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
