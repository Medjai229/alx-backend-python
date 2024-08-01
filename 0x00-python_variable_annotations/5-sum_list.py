#!/usr/bin/env python3
from typing import List
"""
5-sum_list.py

A simple math module that provides a sum_list function.

This module is used to calculate the sum of all elements in a list of numbers.

Author: Malik Hussein
"""


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of all elements in a given list of numbers.

    Args:
        input_list (List[float]): A list of floating point numbers.

    Returns:
        float: The sum of all elements in the input list.

    Example:
        >>> sum_list([1.0, 2.0, 3.0, 4.0])
        10.0
    """
    return sum(input_list)
