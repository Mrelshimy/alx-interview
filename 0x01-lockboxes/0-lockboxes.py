#!/usr/bin/python3

def canUnlockAll(boxes):
    if boxes[0] == []:
        return False
    openBoxes = [0]
    for key in boxes[0]:
        openBoxes.append(key)
    for key in openBoxes:
        for newKey in boxes[key]:
            if newKey in openBoxes:
                continue
            else:
                openBoxes.append(newKey)
    return True if len(boxes) == len(openBoxes) else False     