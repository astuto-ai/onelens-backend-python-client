# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.disable_tenant_request import DisableTenantRequest

class TestDisableTenantRequest(unittest.TestCase):
    """DisableTenantRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisableTenantRequest:
        """Test DisableTenantRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisableTenantRequest`
        """
        model = DisableTenantRequest()
        if include_optional:
            return DisableTenantRequest(
                request = onelens_backend_client.models.disable_tenant_request.DisableTenantRequest(
                    id = '', )
            )
        else:
            return DisableTenantRequest(
                request = onelens_backend_client.models.disable_tenant_request.DisableTenantRequest(
                    id = '', ),
        )
        """

    def testDisableTenantRequest(self):
        """Test DisableTenantRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
