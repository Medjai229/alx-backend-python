#!/usr/bin/env python3
"""
7-to_kv.py

A simple utility module that provides a to_kv function.

This module is used to convert a key-value pair
to a tuple with the value squared.

Author: Malik Hussein
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a key-value pair to a tuple with the value squared.

    Args:
        k (str): The key.
        v (Union[int, float]): The value.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.

    Example:
        >>> to_kv("example_key", 5)
        ('example_key', 25.0)
        >>> to_kv("another_key", 3.5)
        ('another_key', 12.25)
    """
    return (k, v**2)
