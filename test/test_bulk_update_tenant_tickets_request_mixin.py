# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.bulk_update_tenant_tickets_request_mixin import (
    BulkUpdateTenantTicketsRequestMixin,
)


class TestBulkUpdateTenantTicketsRequestMixin(unittest.TestCase):
    """BulkUpdateTenantTicketsRequestMixin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkUpdateTenantTicketsRequestMixin:
        """Test BulkUpdateTenantTicketsRequestMixin
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `BulkUpdateTenantTicketsRequestMixin`
        """
        model = BulkUpdateTenantTicketsRequestMixin()
        if include_optional:
            return BulkUpdateTenantTicketsRequestMixin(
                ticket_ids = [
                    ''
                    ],
                status = 'TO_DO',
                assignment = '',
                assigned_to = '',
                comment = ''
            )
        else:
            return BulkUpdateTenantTicketsRequestMixin(
        )
        """

    def testBulkUpdateTenantTicketsRequestMixin(self):
        """Test BulkUpdateTenantTicketsRequestMixin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
