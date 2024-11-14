# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.response_get_policy_ticket_stats_response import (
    ResponseGetPolicyTicketStatsResponse,
)


class TestResponseGetPolicyTicketStatsResponse(unittest.TestCase):
    """ResponseGetPolicyTicketStatsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseGetPolicyTicketStatsResponse:
        """Test ResponseGetPolicyTicketStatsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ResponseGetPolicyTicketStatsResponse`
        """
        model = ResponseGetPolicyTicketStatsResponse()
        if include_optional:
            return ResponseGetPolicyTicketStatsResponse(
                data = onelens_backend_client.models.get_policy_ticket_stats_response.GetPolicyTicketStatsResponse(
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
                        ], ),
                message = ''
            )
        else:
            return ResponseGetPolicyTicketStatsResponse(
                data = onelens_backend_client.models.get_policy_ticket_stats_response.GetPolicyTicketStatsResponse(
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
                        ], ),
        )
        """

    def testResponseGetPolicyTicketStatsResponse(self):
        """Test ResponseGetPolicyTicketStatsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
