# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.get_policy_ticket_stats_response import (
    GetPolicyTicketStatsResponse,
)


class TestGetPolicyTicketStatsResponse(unittest.TestCase):
    """GetPolicyTicketStatsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPolicyTicketStatsResponse:
        """Test GetPolicyTicketStatsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetPolicyTicketStatsResponse`
        """
        model = GetPolicyTicketStatsResponse()
        if include_optional:
            return GetPolicyTicketStatsResponse(
                value = 1.337,
                details = [
                    onelens_backend_client.models.get_policy_ticket_stats_group_by.GetPolicyTicketStatsGroupBy(
                        field_name = '', 
                        field_value = '', 
                        field_details = [
                            onelens_backend_client.models.get_policy_ticket_stats_sub_group_by.GetPolicyTicketStatsSubGroupBy(
                                field_name = '', 
                                field_value = '', )
                            ], )
                    ]
            )
        else:
            return GetPolicyTicketStatsResponse(
                value = 1.337,
        )
        """

    def testGetPolicyTicketStatsResponse(self):
        """Test GetPolicyTicketStatsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
