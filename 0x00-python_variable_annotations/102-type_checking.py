#!/usr/bin/env python3
"""
This module contains a function for zooming in on an array.

The zoom_array function takes in a tuple and an optional factor parameter,
and returns a list that contains each element of the input tuple repeated
a certain number of times based on the factor.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on an array.

    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: A list containing each element of the input tuple repeated
        a certain number of times based on the factor.
    """

    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
