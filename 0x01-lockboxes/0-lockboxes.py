#!/usr/bin/python3
""" You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes. """


def canUnlockAll(boxes):
    """ check if all boxes are unlocked """
    box_count = [0] * len(boxes)
    box_count[0] = 1
    index = 0
    for box in boxes:
        for key in box:
            if key < len(boxes) and index != key:
                box_count[key] = 1
        index += 1
    if 0 in box_count:
        return False
    else:
        return True
