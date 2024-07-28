#!/usr/bin/env python3
"""
This module contains unit tests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}},
            "my_license", "my_license", True),
        ({"license": {"key": "other_license"}},
            "my_license", "other_license", False)
    ])
    @patch('client.access_nested_map')
    def test_has_license(self, repo, license_key, expected_nested_map_output,
                         expected, mock_access_nested_map):
        """
        Test the has_license method of the GithubOrgClient class.

        Args:
            repo (str): The name of the repository.
            license_key (str): The license key to check for.
            expected_nested_map_output (dict): The expected output
            of the mock_access_nested_map function.
            expected (bool): The expected result of the has_license method.
            mock_access_nested_map (MagicMock): The mock object
            for the access_nested_map function.

        Returns:
            None
        """

        mock_access_nested_map.return_value = expected_nested_map_output

        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected
            )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Test case class for integration testing of the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the necessary resources for the test class.
        """

        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            Mock(status_code=200, json=lambda: cls.org_payload),
            Mock(status_code=200, json=lambda: cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the resources used by the test class.
        """

        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test the public_repos method of the GithubOrgClient class.
        """

        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos('apache-2.0'), self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
