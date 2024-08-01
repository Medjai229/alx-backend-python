#!/usr/bin/env python3
"""
1-concat.py

A simple string module that provides a concat function.

This module is used to concatenate two strings together.

Author: Malik Hussein
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two input strings.

    Args:
        str1 (str): The first string to be concatenated.
        str2 (str): The second string to be concatenated.

    Returns:
        str: The concatenated string.

    Example:
        >>> concat("Hello, ", "World!")
        'Hello, World!'
    """
    return str1 + str2
