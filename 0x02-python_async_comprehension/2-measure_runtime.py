#!/usr/bin/env python3
"""
2-measure_runtime.py

This module measures the runtime of the async_comprehension function.

It provides an measure_runtime function that executes the async_comprehension
function four times concurrently using asyncio.gather.
The total runtime is then calculated by subtracting start time from end time.

Author: Malik Hussein
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of the `async_comprehension` function.

    This function uses the `asyncio.gather` function to execute the
    `async_comprehension` function four times concurrently.
    It then calculates the difference between the start and end times
    to determine the total runtime.

    Returns:
        float: The runtime of the `async_comprehension` function in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
