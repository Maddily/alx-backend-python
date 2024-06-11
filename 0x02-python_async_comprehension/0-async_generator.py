#!/usr/bin/env python3
"""
This module contains an async generator function
that yields random floating-point numbers.

The async_generator function generates 10 random
floating-point numbers between 0 and 10.
Each number is yielded after a 1-second delay using asyncio.sleep.
"""

import random
from typing import AsyncGenerator
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator function that yields
    random floating-point numbers.

    Yields:
        float: A random floating-point number between 0 and 10.

    Raises:
        None

    Returns:
        None
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
