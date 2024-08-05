#!/usr/bin/env python3
"""
3-tasks.py

Asyncio task management module.

Provides task_wait_random and task_wait_n functions for
creating tasks that wait for random amounts of time.

Author: Malik Hussein
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task object that runs the
    `wait_random` function with the given `max_delay`.

    Args:
        max_delay (int): The maximum delay in seconds
        for the `wait_random` function.

    Returns:
        asyncio.Task: The asyncio Task object
        that runs the `wait_random` function.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
