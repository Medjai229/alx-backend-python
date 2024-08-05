#!/usr/bin/env python3
"""
4-tasks.py

Module for asynchronously running a list of wait_random tasks.

This module provides a function, task_wait_n, which runs a specified number of
task_wait_random tasks asynchronously and returns the results.

Author: Malik Hussein
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a list of tasks
    to complete and returns the results.

    Args:
        n (int): The number of tasks to wait for.
        max_delay (int): The maximum delay time for each task.

    Returns:
        List[float]: A list of floats representing
        the results of each completed task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
