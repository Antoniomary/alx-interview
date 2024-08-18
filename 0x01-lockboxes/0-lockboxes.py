#!/usr/bin/python3
"""contains canUnlockAll function"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
       It returns a boolean.
    """
    # get number of boxes
    boxes_len = len(boxes)

    if boxes_len == 1:
        return True

    can_unlock_tracker = [False] * boxes_len
    can_unlock_tracker[0] = True
    i = 0
    while i < boxes_len:
        for key in boxes[i]:
            if key < boxes_len:
                if key == i or can_unlock_tracker[key]:
                    continue
                can_unlock_tracker[key] = True
        i += 1

    for each in can_unlock_tracker:
        if not each:
            return False

    return True
