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
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Asynchronously generates and yields a sequence of random numbers.

    Yields:
        float: A random floating point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
