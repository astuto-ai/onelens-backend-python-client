# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.recommendation_engine_api_request import (
    RecommendationEngineAPIRequest,
)


class TestRecommendationEngineAPIRequest(unittest.TestCase):
    """RecommendationEngineAPIRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecommendationEngineAPIRequest:
        """Test RecommendationEngineAPIRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `RecommendationEngineAPIRequest`
        """
        model = RecommendationEngineAPIRequest()
        if include_optional:
            return RecommendationEngineAPIRequest(
                recommendation_unit_id = '',
                resource_id = '',
                params = onelens_backend_client.models.recommendation_params.RecommendationParams(
                    actual = onelens_backend_client.models.actual.Actual(), 
                    target = onelens_backend_client.models.target.Target(), ),
                policy_config = onelens_backend_client.models.policy_config.Policy Config()
            )
        else:
            return RecommendationEngineAPIRequest(
                recommendation_unit_id = '',
                resource_id = '',
                params = onelens_backend_client.models.recommendation_params.RecommendationParams(
                    actual = onelens_backend_client.models.actual.Actual(), 
                    target = onelens_backend_client.models.target.Target(), ),
                policy_config = onelens_backend_client.models.policy_config.Policy Config(),
        )
        """

    def testRecommendationEngineAPIRequest(self):
        """Test RecommendationEngineAPIRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
