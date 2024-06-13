#!/usr/bin/python3
""" Minimum operations Module"""


def minOperations(n: int) -> int:
    """ Function for Min operations """

    if n <= 1 or not isinstance(n, int):
        return 0
    ops = 2
    printed = [1, 2]
    copied = 1
    while printed[-1] < n:
        if (n - printed[-1]) % printed[-1] == 0:
            ops += 2
            printed.append(printed[-1] * 2)
        else:
            ops += 1
            printed.append(printed[-1] + copied)
        copied = (printed[-1] - printed[-2])
    return ops
