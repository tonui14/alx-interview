#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): each index represents a box and values are keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is unlocked
    keys = set(boxes[0])

    while True:
        new_key_found = False

        for i in range(n):
            if not opened[i] and i in keys:
                opened[i] = True
                keys.update(boxes[i])
                new_key_found = True

        if not new_key_found:
            break

    return all(opened)
