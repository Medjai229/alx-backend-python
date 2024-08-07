#!/usr/bin/env python3
"""
1-async_comprehension.py

This module provides an asynchronous list comprehension
that generates a list of numbers from an asynchronous generator.

The async_comprehension function uses async comprehension to generate a list
of numbers from the async_generator function in 0-async_generator.py.

Author: Malik Hussein
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Asynchronously generates a list of numbers using async comprehension.

    Returns:
        List: A list of numbers generated asynchronously.
    """
    return [number async for number in async_generator()]
