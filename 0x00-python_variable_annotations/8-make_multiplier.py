#!/usr/bin/env python3
"""
This module contains a function that returns a multiplier function.

The make_multiplier function takes a multiplier as input and returns a
function that multiplies a given number by the multiplier.

Example:
    multiplier = make_multiplier(2.22)
    result = multiplier(2.22)
    print(result)  # Output: 4.928400000000001
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given number by the multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: The multiplier function.
    """

    return lambda number: multiplier * number
