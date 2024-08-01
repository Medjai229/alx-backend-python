#!/usr/bin/env python3
"""
9-element_length.py

A simple utility module that provides an element_length function.

This module is used to calculate the length of each element in a given list.

Author: Malik Hussein
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element
    from the input list and its length.

    Args:
        lst: An iterable of sequences (e.g., strings, lists, tuples).

    Returns:
        A list of tuples, where each tuple contains a sequence from
        the input list and its length.

    Example:
        >>> element_length(["hello", "world", [1, 2, 3], (4, 5)])
        [('hello', 5), ('world', 5), ([1, 2, 3], 3), ((4, 5), 2)]
    """
    return [(i, len(i)) for i in lst]
