#!/usr/bin/env python3
"""
2-floor.py

A simple math module that provides a floor function.

This module is used to perform basic arithmetic operations.

Author: Malik Hussein
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of a given float number.

    Args:
        n (float): The input float number.

    Returns:
        int: The floor of the input number.

    Example:
        >>> floor(3.7)
        3
        >>> floor(-2.3)
        -3
    """
    return math.floor(n)
