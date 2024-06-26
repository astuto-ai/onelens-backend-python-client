# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.update_tenant_tickets_request import UpdateTenantTicketsRequest

class TestUpdateTenantTicketsRequest(unittest.TestCase):
    """UpdateTenantTicketsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateTenantTicketsRequest:
        """Test UpdateTenantTicketsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateTenantTicketsRequest`
        """
        model = UpdateTenantTicketsRequest()
        if include_optional:
            return UpdateTenantTicketsRequest(
                update_ticket_details = [
                    onelens_backend_client.models.tenant_ticket_updation_request.TenantTicketUpdationRequest(
                        ticket_id = '', 
                        system_state = null, 
                        user_state = null, )
                    ],
                tenant_id = ''
            )
        else:
            return UpdateTenantTicketsRequest(
                update_ticket_details = [
                    onelens_backend_client.models.tenant_ticket_updation_request.TenantTicketUpdationRequest(
                        ticket_id = '', 
                        system_state = null, 
                        user_state = null, )
                    ],
                tenant_id = '',
        )
        """

    def testUpdateTenantTicketsRequest(self):
        """Test UpdateTenantTicketsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
