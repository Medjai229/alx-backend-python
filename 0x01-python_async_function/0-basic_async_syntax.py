#!/usr/bin/env python3
"""
0-basic_async_syntax.py

Asynchronous utility functions.

This module provides a set of asynchronous utility functions for use in
asyncio-based applications.

Author: Malik Hussein
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random amount of time.

    Args:
    max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
    float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
