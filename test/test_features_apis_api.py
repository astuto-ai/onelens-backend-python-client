# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.api.features_apis_api import FeaturesApisApi


class TestFeaturesApisApi(unittest.TestCase):
    """FeaturesApisApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FeaturesApisApi()

    def tearDown(self) -> None:
        pass

    def test_get_all_features(self) -> None:
        """Test case for get_all_features

        Get All Features
        """
        pass

    def test_get_features_by_scope(self) -> None:
        """Test case for get_features_by_scope

        Get Features By Scope
        """
        pass

    def test_update_feature_status_disabled(self) -> None:
        """Test case for update_feature_status_disabled

        Update Feature Status Disabled
        """
        pass

    def test_update_feature_status_enabled(self) -> None:
        """Test case for update_feature_status_enabled

        Update Feature Status Enabled
        """
        pass


if __name__ == "__main__":
    unittest.main()
