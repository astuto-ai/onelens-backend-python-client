# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.response_add_tenant_policy_exclusions_response import (
    ResponseAddTenantPolicyExclusionsResponse,
)


class TestResponseAddTenantPolicyExclusionsResponse(unittest.TestCase):
    """ResponseAddTenantPolicyExclusionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> ResponseAddTenantPolicyExclusionsResponse:
        """Test ResponseAddTenantPolicyExclusionsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ResponseAddTenantPolicyExclusionsResponse`
        """
        model = ResponseAddTenantPolicyExclusionsResponse()
        if include_optional:
            return ResponseAddTenantPolicyExclusionsResponse(
                data = onelens_backend_client.models.add_tenant_policy_exclusions_response.AddTenantPolicyExclusionsResponse(
                    id = '', 
                    policy_id = '', 
                    config_overrides = onelens_backend_client.models.config_overrides.config_overrides(), 
                    state = null, 
                    version = 56, 
                    exclusions = null, ),
                message = ''
            )
        else:
            return ResponseAddTenantPolicyExclusionsResponse(
                data = onelens_backend_client.models.add_tenant_policy_exclusions_response.AddTenantPolicyExclusionsResponse(
                    id = '', 
                    policy_id = '', 
                    config_overrides = onelens_backend_client.models.config_overrides.config_overrides(), 
                    state = null, 
                    version = 56, 
                    exclusions = null, ),
        )
        """

    def testResponseAddTenantPolicyExclusionsResponse(self):
        """Test ResponseAddTenantPolicyExclusionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
