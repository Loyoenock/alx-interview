#!/usr/bin/python3
'''
A function that seturns list representing Pascal's triangle of n
'''

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    n (int): The number of rows in Pascal's triangle.

    Returns:
    list of lists: A list of lists representing Pascal's triangle.
                   Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
