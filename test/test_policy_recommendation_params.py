# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.policy_recommendation_params import PolicyRecommendationParams

class TestPolicyRecommendationParams(unittest.TestCase):
    """PolicyRecommendationParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicyRecommendationParams:
        """Test PolicyRecommendationParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicyRecommendationParams`
        """
        model = PolicyRecommendationParams()
        if include_optional:
            return PolicyRecommendationParams(
                current = None,
                target = None
            )
        else:
            return PolicyRecommendationParams(
        )
        """

    def testPolicyRecommendationParams(self):
        """Test PolicyRecommendationParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()