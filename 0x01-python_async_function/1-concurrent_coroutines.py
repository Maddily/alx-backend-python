#!/usr/bin/env python3
"""
This module contains a function that executes multiple coroutines concurrently.

The function `wait_n` takes in two parameters:
- `n`: an integer representing the number of coroutines
to execute concurrently.
- `max_delay`: an integer representing the maximum delay for each coroutine.

The function returns a list of floats
representing the delays of each coroutine.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines concurrently.

    Args:
        n: An integer representing the number of coroutines
            to execute concurrently.
        max_delay: An integer representing
            the maximum delay for each coroutine.

    Returns:
        A list of floats representing the delays of each coroutine.
    """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)

    return delays
