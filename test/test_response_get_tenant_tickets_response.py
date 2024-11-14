# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.response_get_tenant_tickets_response import (
    ResponseGetTenantTicketsResponse,
)


class TestResponseGetTenantTicketsResponse(unittest.TestCase):
    """ResponseGetTenantTicketsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseGetTenantTicketsResponse:
        """Test ResponseGetTenantTicketsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ResponseGetTenantTicketsResponse`
        """
        model = ResponseGetTenantTicketsResponse()
        if include_optional:
            return ResponseGetTenantTicketsResponse(
                data = onelens_backend_client.models.get_tenant_tickets_response.GetTenantTicketsResponse(
                    tenant_tickets = [
                        onelens_backend_client.models.tenant_ticket.TenantTicket(
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            monitor_id = '', 
                            ticket_category = null, 
                            system_state = null, 
                            user_state = null, 
                            details = null, 
                            id = '', )
                        ], ),
                message = ''
            )
        else:
            return ResponseGetTenantTicketsResponse(
                data = onelens_backend_client.models.get_tenant_tickets_response.GetTenantTicketsResponse(
                    tenant_tickets = [
                        onelens_backend_client.models.tenant_ticket.TenantTicket(
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            monitor_id = '', 
                            ticket_category = null, 
                            system_state = null, 
                            user_state = null, 
                            details = null, 
                            id = '', )
                        ], ),
        )
        """

    def testResponseGetTenantTicketsResponse(self):
        """Test ResponseGetTenantTicketsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
