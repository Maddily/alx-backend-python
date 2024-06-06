#!/usr/bin/env python3
"""
This module contains a function to_kv
that takes a string and a number as input
and returns a tuple with the string and the square of the number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a number as input
    and returns a tuple with the string and
    the square of the number.

    Args:
        k (str): The string key.
        v (Union[int, float]): The number value.

    Returns:
        Tuple[str, float]: A tuple containing the string key
        and the square of the number.
    """

    return (k, v ** 2)
