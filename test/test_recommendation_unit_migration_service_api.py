# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.api.recommendation_unit_migration_service_api import RecommendationUnitMigrationServiceApi


class TestRecommendationUnitMigrationServiceApi(unittest.TestCase):
    """RecommendationUnitMigrationServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RecommendationUnitMigrationServiceApi()

    def tearDown(self) -> None:
        pass

    def test_create_recommendation_unit_pull_request(self) -> None:
        """Test case for create_recommendation_unit_pull_request

        Create a pull request for the recommendation_unit template
        """
        pass

    def test_sync_recommendation_unit_from_repo(self) -> None:
        """Test case for sync_recommendation_unit_from_repo

        Sync recommendation_unit from repo
        """
        pass


if __name__ == '__main__':
    unittest.main()
