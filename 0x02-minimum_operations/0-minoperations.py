#!/usr/bin/python3
"""  Minimum operations module """


def minOperations(n: int) -> int:
  """ Min operations function """

    if n <= 0 or not isinstance(n, int):
        return 0
    ops = 2
    printed = [1, 2]
    copied = [1]
    while printed[-1] <= n:
        if (n - printed[-1]) % printed[-1]:
            ops += 2
            printed.append(printed[-1] * 2)
        else:
            ops += 1
            printed.append(printed[-1] + copied[-1])
        copied.append(printed[-1] - printed[-2])
    return ops
