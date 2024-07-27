#!/usr/bin/env python3
"""
This module contains unit tests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock
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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test case to verify the public repos URL.

        This test case mocks the organization API response and checks if the
        public_repos_url property of the GithubOrgClient instance matches the
        expected URL.

        Args:
            mock_org: A mock object representing the organization API response.

        Returns:
            None
        """

        expected_url = "https://api.github.com/orgs/test/repos"
        mock_org.return_value = {"repos_url": expected_url}

        client = GithubOrgClient('test')
        url = client._public_repos_url

        self.assertEqual(url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test case for the public_repos method of the GithubOrgClient class.

        This test verifies that the public_repos method returns the correct
        list of public repository names for a given GitHub organization.

        Args:
            mock_get_json: A MagicMock object representing
            the mock of the get_json method.

        Returns:
            None
        """

        mock_get_json.return_value = [
            {
                "name": "todo-app"
            },
            {
                "name": "calculator"
            }
        ]

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            url = "https://api.github.com/orgs/test/repos"
            mock_public_repos_url.return_value = url

            client = GithubOrgClient('test')
            self.assertEqual(client.public_repos(), ['todo-app', 'calculator'])
            mock_public_repos_url.assert_called_once()

        mock_get_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
