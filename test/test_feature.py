# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.feature import Feature


class TestFeature(unittest.TestCase):
    """Feature unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Feature:
        """Test Feature
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Feature`
        """
        model = Feature()
        if include_optional:
            return Feature(
                id = '',
                name = '',
                description = '',
                scope = 'POLICY',
                feature_store = onelens_backend_client.models.feature_store.FeatureStore(
                    enabled_for = [
                        ''
                        ], 
                    config = onelens_backend_client.models.feature_config.FeatureConfig(
                        enable_metrics_for_days = 56, 
                        threshold_percentage = 56, ), )
            )
        else:
            return Feature(
                id = '',
                name = '',
                description = '',
                scope = 'POLICY',
        )
        """

    def testFeature(self):
        """Test Feature"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
