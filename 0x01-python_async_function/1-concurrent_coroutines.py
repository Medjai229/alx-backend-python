#!/usr/bin/env python3
"""
1-concurrent_coroutines.py

Module for asynchronously running a list of wait_random tasks.

This module provides a function, wait_n, which runs a specified number of
wait_random tasks asynchronously and returns the results.

Author: Malik Hussein
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously runs a list of wait_random tasks and returns the results.

    Args:
    n (int): Number of coroutines to run.
    max_delay (int): Maximum time for each coroutine to run.

    Returns:
    List[float]: List of delays for each coroutine.
    """
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    res = []
    for task in asyncio.as_completed(tasks):
        res.append(await task)

    return res
