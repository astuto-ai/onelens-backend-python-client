# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.tenant_ticket_creation_api_request import TenantTicketCreationAPIRequest

class TestTenantTicketCreationAPIRequest(unittest.TestCase):
    """TenantTicketCreationAPIRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantTicketCreationAPIRequest:
        """Test TenantTicketCreationAPIRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantTicketCreationAPIRequest`
        """
        model = TenantTicketCreationAPIRequest()
        if include_optional:
            return TenantTicketCreationAPIRequest(
                new_ticket_details = [
                    onelens_backend_client.models.tenant_ticket_creation_request.TenantTicketCreationRequest(
                        monitor_id = '', 
                        ticket_category = null, 
                        system_state = null, 
                        user_state = null, 
                        details = null, )
                    ]
            )
        else:
            return TenantTicketCreationAPIRequest(
                new_ticket_details = [
                    onelens_backend_client.models.tenant_ticket_creation_request.TenantTicketCreationRequest(
                        monitor_id = '', 
                        ticket_category = null, 
                        system_state = null, 
                        user_state = null, 
                        details = null, )
                    ],
        )
        """

    def testTenantTicketCreationAPIRequest(self):
        """Test TenantTicketCreationAPIRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
