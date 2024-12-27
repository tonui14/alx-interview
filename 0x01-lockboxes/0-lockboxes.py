#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked, starting from box 0.
Each box may contain keys to other boxes, and we assume that keys will be 
positive integers. The first box (box 0) is always unlocked.
The function `canUnlockAll` returns True if all boxes can be opened, otherwise False.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened, starting with box 0.

    Args:
        boxes (list of lists): A list where each list contains the keys of a particular box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # Set of unlocked boxes, starting with box 0 (the first box is unlocked)
    unlocked = {0}
    
    # Initialize a flag to track if any new boxes are unlocked
    unlocked_new_boxes = True
    
    # Keep looping until no new boxes are unlocked in one full pass
    while unlocked_new_boxes:
        unlocked_new_boxes = False
        
        # Iterate through the unlocked boxes
        for box_index in list(unlocked):  # Convert to list to prevent modification during iteration
            for key in boxes[box_index]:
                # If the key corresponds to a valid box and it isn't unlocked yet, unlock it
                if key < len(boxes) and key not in unlocked:
                    unlocked.add(key)
                    unlocked_new_boxes = True  # A new box was unlocked
    
    # If the number of unlocked boxes equals the total number of boxes, return True
    return len(unlocked) == len(boxes)

