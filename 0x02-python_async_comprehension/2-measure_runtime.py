#!/usr/bin/env python3
"""
This module contains a function to measure
the runtime of an asynchronous comprehension.

The measure_runtime function uses the async_comprehension
function from the '1-async_comprehension' module
to create a list of random numbers asynchronously.
It then measures the total runtime of the asynchronous
comprehension and returns the result.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of an asynchronous comprehension.

    Returns:
        The total runtime of the asynchronous comprehension in seconds.
    """

    start_time = time.perf_counter()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    total_runtime = time.perf_counter() - start_time

    return total_runtime
