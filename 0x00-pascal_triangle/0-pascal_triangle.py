#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1, ], ]
    if n == 2:
        return [[1, ], [1, 1]]
    pascal = [[1, ], [1, 1]]
    for i in range(3, n + 1):
        row = [1, ]
        for x in range(len(pascal[-1]) - 1):
            row.append(pascal[-1][x] + pascal[-1][x + 1])
        row.append(1)
        pascal.append(row)
    return pascal
