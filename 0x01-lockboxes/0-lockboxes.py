#!/usr/bin/python3
"""Locboxes Module"""


def canUnlockAll(boxes):
    """function to solve lockboxes issue"""
    openBoxes = [0]
    for key in boxes[0]:
        openBoxes.append(key if key < len(boxes) or key not in openBoxes else '')
    for key in openBoxes:
        for newKey in boxes[key]:
            if newKey in openBoxes or newKey >= len(boxes):
                continue
            else:
                openBoxes.append(newKey)
    return len(boxes) == len(openBoxes)
