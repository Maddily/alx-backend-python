#!/usr/bin/env python3
"""
This module contains a function to calculate
the length of elements in an iterable.

The function `element_length` takes an iterable of sequences
as input and returns a list of tuples.
Each tuple contains a sequence from the input iterable
and its corresponding length.

Example:
    lst = ['apple', 'banana', 'cherry']
    result = element_length(lst)
    print(result)
    # Output: [('apple', 5), ('banana', 6), ('cherry', 6)]
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in an iterable.

    Args:
        lst: An iterable of sequences.

    Returns:
        A list of tuples, where each tuple contains a sequence
        from the input iterable and its corresponding length.
    """

    return [(i, len(i)) for i in lst]
