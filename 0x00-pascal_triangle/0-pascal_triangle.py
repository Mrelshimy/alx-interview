#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal traingle implementation function"""
    triangle = []
    if n <= 0:
        return triangle
    else:
        for i in range(n):
            row = [1]
            for j in range(i):
                row.append(1)
            triangle.append(row)
        for row in range(2, n):
            for item in range(1, row):
                triangle[row][item] = triangle[row-1][item-1]\
                      + triangle[row-1][item]
    return (triangle)
