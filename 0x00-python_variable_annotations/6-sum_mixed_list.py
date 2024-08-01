#!/usr/bin/env python3
"""
6-sum_mixed_list.py

A simple math module that provides a sum_mixed_list function.

This module is used to calculate the sum of all elements
in a mixed list of integers and floats.

Author: Malik Hussein
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function calculates the sum of a mixed list
    containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
        A list containing integers and/or floats.

    Returns:
        float: The sum of all elements in the list.

    Example:
        >>> sum_mixed_list([1, 2, 3.5, 4])
        10.5
    """
    return sum(mxd_lst)
