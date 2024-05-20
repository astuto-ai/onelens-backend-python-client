# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.tenant_ticket_filters import TenantTicketFilters

class TestTenantTicketFilters(unittest.TestCase):
    """TenantTicketFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantTicketFilters:
        """Test TenantTicketFilters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantTicketFilters`
        """
        model = TenantTicketFilters()
        if include_optional:
            return TenantTicketFilters(
                monitor_ids = [
                    ''
                    ],
                heirarchy_node_ids = [
                    ''
                    ],
                ticket_categories = [
                    'POLICY_TICKET'
                    ],
                states = [
                    'OPEN'
                    ],
                statuses = None
            )
        else:
            return TenantTicketFilters(
        )
        """

    def testTenantTicketFilters(self):
        """Test TenantTicketFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
