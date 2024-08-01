#!/usr/bin/env python3
"""
102-type.py

mypy.

This module is used to safely retrieve a value from a dictionary
returning a default value if the key is not found.

Author: Malik Hussein
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on a given array by repeating
    each element a specified number of times.

    Args:
        lst (Tuple): The input array to be zoomed in.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed-in array.

    Example:
        >>> zoom_array((12, 72, 91))
        [12, 12, 72, 72, 91, 91]
        >>> zoom_array((12, 72, 91), 3)
        [12, 12, 12, 72, 72, 72, 91, 91, 91]
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
