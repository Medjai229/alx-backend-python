#!/usr/bin/env python3
"""
100-safe_first_element.py

Duck typing.

This module is used to safely retrieve the first element of a given sequence.

Author: Malik Hussein
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it is not empty
    otherwise returns None.

    Args:
        lst: A sequence (e.g., list, tuple, string) of any type.

    Returns:
        The first element of the sequence if it is not empty, otherwise None.

    Examples:
        >>> safe_first_element([1, 2, 3])
        1
        >>> safe_first_element([])
        None
        >>> safe_first_element("hello")
        'h'
        >>> safe_first_element(())
        None
    """
    if lst:
        return lst[0]
    else:
        return None
