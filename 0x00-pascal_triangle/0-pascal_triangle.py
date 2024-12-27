#!/usr/bin/python3

"""
Module for generating Pascal's triangle.

This module provides a function to generate Pascal's triangle up to n rows.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        if i > 0:
            row.append(1)
        triangle.append(row)

    return triangle

