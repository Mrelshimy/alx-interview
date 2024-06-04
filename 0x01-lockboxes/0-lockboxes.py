#!/usr/bin/python3
"""Locboxes Module"""


def canUnlockAll(boxes):
    """function to solve lockboxes issue"""
    if boxes[0] == []:
        return False
    openBoxes = [0]
    for key in boxes[0]:
        if key >= len(boxes):
            continue
        else:
            openBoxes.append(key)
    for key in openBoxes:
        for newKey in boxes[key]:
            if newKey in openBoxes or newKey >= len(boxes):
                continue
            else:
                openBoxes.append(newKey)
    return True if len(boxes) == len(openBoxes) else False
