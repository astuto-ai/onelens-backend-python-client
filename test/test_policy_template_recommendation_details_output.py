# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.policy_template_recommendation_details_output import (
    PolicyTemplateRecommendationDetailsOutput,
)


class TestPolicyTemplateRecommendationDetailsOutput(unittest.TestCase):
    """PolicyTemplateRecommendationDetailsOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PolicyTemplateRecommendationDetailsOutput:
        """Test PolicyTemplateRecommendationDetailsOutput
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PolicyTemplateRecommendationDetailsOutput`
        """
        model = PolicyTemplateRecommendationDetailsOutput()
        if include_optional:
            return PolicyTemplateRecommendationDetailsOutput(
                applicable_recommendation_units = [
                    onelens_backend_client.models.policy_template_recommendation_units.PolicyTemplateRecommendationUnits(
                        recommendation_unit_id = '', 
                        params = null, )
                    ]
            )
        else:
            return PolicyTemplateRecommendationDetailsOutput(
        )
        """

    def testPolicyTemplateRecommendationDetailsOutput(self):
        """Test PolicyTemplateRecommendationDetailsOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
