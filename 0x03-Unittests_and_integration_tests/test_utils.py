#!/usr/bin/env python3
"""
This module contains unit tests for the `access_nested_map`
function in the `utils` module.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    This class contains unit tests for the `access_nested_map` function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the `access_nested_map` function with different inputs.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path to the desired value.
            expected: The expected output.

        Returns:
            None
        """

        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, err_msg):
        """
        Verify that accessing a nested map with an invalid path
        raises a KeyError.

        Args:
            nested_map (dict): The nested map to access.
            path (list): The path to access the nested value.
            err_msg (str): The expected error message.

        Raises:
            AssertionError: If the KeyError is not raised
            or if the error message is not as expected.
        """

        with self.assertRaises(KeyError) as msg:
            access_nested_map(nested_map, path)
        self.assertEqual(str(msg.exception), err_msg)
