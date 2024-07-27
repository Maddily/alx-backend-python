#!/usr/bin/env python3
"""
This module contains unit tests for the `access_nested_map`
function in the `utils` module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for testing the `access_nested_map` function.
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


class TestGetJson(unittest.TestCase):
    """
    Test case class for testing the get_json function.
    """

    @parameterized.expand([
                ('http://example.com', {"payload": True}),
                ('http://holberton.io', {"payload": False})
            ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function with different URLs and payloads.

        Args:
            test_url (str): The URL to test.
            test_payload (dict): The expected payload for the given URL.
            mock_get (MagicMock): The mocked requests.get function.

        Returns:
            None
        """

        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        response = get_json(test_url)

        self.assertEqual(response, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test case class for the memoize decorator.
    """

    def test_memoize(self):
        """
        Test the memoize decorator on a_property method of TestClass.
        """

        class TestClass:
            """
            Test class for memoize decorator.
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42
        ) as mock_a_method:
            instance = TestClass()
            result1 = instance.a_property
            result2 = instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
