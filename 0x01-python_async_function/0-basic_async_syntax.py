#!/usr/bin/env python3
"""
This module contains a basic async function
that waits for a random amount of time.

Functions:
- wait_random(max_delay: int = 10) -> float: An async function
that waits for a random amount of time and returns the delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random amount of time and returns the delay.

    Args:
      max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
      float: The random delay in seconds.
    """

    random_delay = random.uniform(0, max_delay)

    await asyncio.sleep(random_delay)

    return random_delay
