# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.recommendation_ticket import RecommendationTicket

class TestRecommendationTicket(unittest.TestCase):
    """RecommendationTicket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecommendationTicket:
        """Test RecommendationTicket
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecommendationTicket`
        """
        model = RecommendationTicket()
        if include_optional:
            return RecommendationTicket(
                recommendation_unit_id = '',
                action_type_id = 56,
                priority = 56,
                instance_type = '',
                instance_family = '',
                price_per_unit = '',
                currency = '',
                unit = '',
                new_cost = '',
                current_cost = '',
                potential_saving = '',
                description = '',
                begin_range = '',
                end_range = '',
                attributes = onelens_backend_client.models.attributes.Attributes(),
                ticket_id = '',
                id = ''
            )
        else:
            return RecommendationTicket(
                recommendation_unit_id = '',
                action_type_id = 56,
                priority = 56,
                price_per_unit = '',
                currency = '',
                unit = '',
                new_cost = '',
                current_cost = '',
                potential_saving = '',
                description = '',
                begin_range = '',
                end_range = '',
                attributes = onelens_backend_client.models.attributes.Attributes(),
                ticket_id = '',
        )
        """

    def testRecommendationTicket(self):
        """Test RecommendationTicket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()