# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.response_disable_tenant_response import (
    ResponseDisableTenantResponse,
)


class TestResponseDisableTenantResponse(unittest.TestCase):
    """ResponseDisableTenantResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseDisableTenantResponse:
        """Test ResponseDisableTenantResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ResponseDisableTenantResponse`
        """
        model = ResponseDisableTenantResponse()
        if include_optional:
            return ResponseDisableTenantResponse(
                data = onelens_backend_client.models.disable_tenant_response.DisableTenantResponse(),
                message = ''
            )
        else:
            return ResponseDisableTenantResponse(
                data = onelens_backend_client.models.disable_tenant_response.DisableTenantResponse(),
        )
        """

    def testResponseDisableTenantResponse(self):
        """Test ResponseDisableTenantResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
