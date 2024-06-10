#!/usr/bin/env python3
"""
This module contains a function for creating an asyncio task.

Functions:
- task_wait_random(max_delay: int) -> asyncio.Task:
    Creates an asyncio task that calls
    the wait_random function with the given max_delay.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task that calls
        the wait_random function with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio task that will
            execute the wait_random function.
    """

    return asyncio.create_task(wait_random(max_delay))
