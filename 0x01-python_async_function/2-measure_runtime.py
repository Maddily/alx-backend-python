#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of a coroutine.

The measure_time function takes in two parameters:
- n: an integer representing the number of coroutines to run concurrently
- max_delay: an integer representing the maximum delay
    in seconds for each coroutine

The function measures the time it takes to run the coroutines
using the asyncio.run() function and returns the total runtime in seconds.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime of a coroutine.

    Args:
        n: An integer representing the number of coroutines
            to run concurrently.
        max_delay: An integer representing the maximum delay
            in seconds for each coroutine.

    Returns:
        The total runtime in seconds.
    """

    s = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    return time.perf_counter() - s
