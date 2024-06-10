#!/usr/bin/env python3
"""
This module contains an asynchronous function
that creates multiple tasks to wait for random delays
and returns a list of the delays.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create multiple tasks to wait for random delays
    and return a list of the delays.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of the delays for each task.
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)

    return delays
