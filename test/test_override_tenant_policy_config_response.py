# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.override_tenant_policy_config_response import OverrideTenantPolicyConfigResponse

class TestOverrideTenantPolicyConfigResponse(unittest.TestCase):
    """OverrideTenantPolicyConfigResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OverrideTenantPolicyConfigResponse:
        """Test OverrideTenantPolicyConfigResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OverrideTenantPolicyConfigResponse`
        """
        model = OverrideTenantPolicyConfigResponse()
        if include_optional:
            return OverrideTenantPolicyConfigResponse(
                id = '',
                policy_id = '',
                config_overrides = None,
                state = 'ACTIVE'
            )
        else:
            return OverrideTenantPolicyConfigResponse(
                id = '',
                policy_id = '',
                state = 'ACTIVE',
        )
        """

    def testOverrideTenantPolicyConfigResponse(self):
        """Test OverrideTenantPolicyConfigResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
