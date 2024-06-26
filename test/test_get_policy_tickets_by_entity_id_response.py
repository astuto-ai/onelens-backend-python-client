# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_policy_tickets_by_entity_id_response import GetPolicyTicketsByEntityIdResponse

class TestGetPolicyTicketsByEntityIdResponse(unittest.TestCase):
    """GetPolicyTicketsByEntityIdResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPolicyTicketsByEntityIdResponse:
        """Test GetPolicyTicketsByEntityIdResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPolicyTicketsByEntityIdResponse`
        """
        model = GetPolicyTicketsByEntityIdResponse()
        if include_optional:
            return GetPolicyTicketsByEntityIdResponse(
                pagination = onelens_backend_client.models.pagination_fields.PaginationFields(
                    total_items = 56, 
                    total_pages = 56, 
                    current_page = 56, 
                    page_size = 56, ),
                entity_tickets = [
                    onelens_backend_client.models.get_single_policy_ticket_by_entity_id_response.GetSinglePolicyTicketByEntityIdResponse(
                        ticket_id = '', 
                        ticket_status = null, 
                        ticket_state = null, 
                        violation_attributes = onelens_backend_client.models.violation_attributes.Violation Attributes(), 
                        entity_id = '', 
                        entity_name = '', 
                        region = '', 
                        service = '', 
                        service_display_name = '', 
                        account_id = '', 
                        recommendation_unit_title = '', 
                        policy_id = '', 
                        policy_title = '', 
                        policy_labels = [
                            ''
                            ], 
                        policy_violated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        potential_savings = 1.337, )
                    ]
            )
        else:
            return GetPolicyTicketsByEntityIdResponse(
                pagination = onelens_backend_client.models.pagination_fields.PaginationFields(
                    total_items = 56, 
                    total_pages = 56, 
                    current_page = 56, 
                    page_size = 56, ),
                entity_tickets = [
                    onelens_backend_client.models.get_single_policy_ticket_by_entity_id_response.GetSinglePolicyTicketByEntityIdResponse(
                        ticket_id = '', 
                        ticket_status = null, 
                        ticket_state = null, 
                        violation_attributes = onelens_backend_client.models.violation_attributes.Violation Attributes(), 
                        entity_id = '', 
                        entity_name = '', 
                        region = '', 
                        service = '', 
                        service_display_name = '', 
                        account_id = '', 
                        recommendation_unit_title = '', 
                        policy_id = '', 
                        policy_title = '', 
                        policy_labels = [
                            ''
                            ], 
                        policy_violated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        potential_savings = 1.337, )
                    ],
        )
        """

    def testGetPolicyTicketsByEntityIdResponse(self):
        """Test GetPolicyTicketsByEntityIdResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
