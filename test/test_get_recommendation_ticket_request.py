# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_recommendation_ticket_request import GetRecommendationTicketRequest

class TestGetRecommendationTicketRequest(unittest.TestCase):
    """GetRecommendationTicketRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetRecommendationTicketRequest:
        """Test GetRecommendationTicketRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRecommendationTicketRequest`
        """
        model = GetRecommendationTicketRequest()
        if include_optional:
            return GetRecommendationTicketRequest(
                ticket_id = '',
                tenant_id = ''
            )
        else:
            return GetRecommendationTicketRequest(
                ticket_id = '',
                tenant_id = '',
        )
        """

    def testGetRecommendationTicketRequest(self):
        """Test GetRecommendationTicketRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
