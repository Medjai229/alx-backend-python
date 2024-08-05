#!/usr/bin/env python3
"""
2-measure_runtime.py

Module for measuring the runtime of the wait_n function.

This module provides a function, measure_time, which measures
the average time taken to run the wait_n function with
a given number of coroutines and maximum delay.

Author: Malik Hussein
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Calculate the average time taken to run the wait_n function
    with a given number of coroutines and maximum delay.

    Args:
        n (int): The number of coroutines to run concurrently.
        max_delay (int): The maximum delay in seconds for each coroutine.

    Returns:
        float: The average time taken to run the wait_n function, in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    return (end_time - start_time) / n
