#!/usr/bin/env python3
"""
This module contains unit tests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case class for the GithubOrgClient class.
    """

    @parameterized.expand([
        ('google', {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ('abc', {"repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test the org method of the GithubOrgClient class.

        Args:
            org_name (str): The name of the organization.
            expected (dict): The expected response from the API.
            mock_get_json (MagicMock): The mocked get_json function.

        Returns:
            None
        """

        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        response = client.org

        self.assertEqual(response, expected)

        org_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(org_url)
