#!/usr/bin/python3
""" Minimum operations Module"""


def minoperations(n: int) -> int:
    """ Function for Min operations """

    if n <= 1:
        return 0

    i = 2
    operations = 0

    while i <= n:
        if n % i == 0:
            n = n / i
            operations += i
        else:
            i += 1

    return operations
