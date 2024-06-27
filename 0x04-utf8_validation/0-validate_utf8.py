#!/usr/bin/python3

""" Script to validate UTF-8 compliance
"""


def validUTF8(data):
    """ True if UTF-8 Flase if not
    """
    check = 0
    for byte in data:
        if check == 0:
            if (byte >> 5) == 0b110:
                check = 1
            elif (byte >> 4) == 0b1110:
                check = 2
            elif (byte >> 3) == 0b11110:
                check = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            check -= 1
    return check == 0
