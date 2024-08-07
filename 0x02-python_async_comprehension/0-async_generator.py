#!/usr/bin/env python3
"""
0-async_generator.py

This module provides an asynchronous generator
that yields a sequence of random numbers.

The async_generator function generates and yields a sequence of 10 random
floating point numbers between 0 and 10, with a 1s delay between each number.

Author: Malik Hussein
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronously generates and yields a sequence of random numbers.

    Yields:
        float: A random floating point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
