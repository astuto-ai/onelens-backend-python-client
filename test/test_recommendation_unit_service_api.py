# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.api.recommendation_unit_service_api import RecommendationUnitServiceApi


class TestRecommendationUnitServiceApi(unittest.TestCase):
    """RecommendationUnitServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RecommendationUnitServiceApi()

    def tearDown(self) -> None:
        pass

    def test_create_recommendation_unit(self) -> None:
        """Test case for create_recommendation_unit

        Create recommendation unit
        """
        pass

    def test_get_recommendation_unit_by_id(self) -> None:
        """Test case for get_recommendation_unit_by_id

        Retrieves Recommendation unit ID.
        """
        pass

    def test_get_recommendation_units(self) -> None:
        """Test case for get_recommendation_units

        Retrieves all recommendation units with filters
        """
        pass

    def test_update_recommendation_unit(self) -> None:
        """Test case for update_recommendation_unit

        Update recommendation unit
        """
        pass


if __name__ == '__main__':
    unittest.main()
