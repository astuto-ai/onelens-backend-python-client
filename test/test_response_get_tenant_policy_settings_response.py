# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.response_get_tenant_policy_settings_response import ResponseGetTenantPolicySettingsResponse

class TestResponseGetTenantPolicySettingsResponse(unittest.TestCase):
    """ResponseGetTenantPolicySettingsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseGetTenantPolicySettingsResponse:
        """Test ResponseGetTenantPolicySettingsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseGetTenantPolicySettingsResponse`
        """
        model = ResponseGetTenantPolicySettingsResponse()
        if include_optional:
            return ResponseGetTenantPolicySettingsResponse(
                data = onelens_backend_client.models.get_tenant_policy_settings_response.GetTenantPolicySettingsResponse(
                    pagination = null, 
                    policy_settings = [
                        onelens_backend_client.models.tenant_policy_settings.TenantPolicySettings(
                            id = '', 
                            policy_id = '', 
                            config_overrides = onelens_backend_client.models.config_overrides.config_overrides(), 
                            state = null, )
                        ], ),
                message = ''
            )
        else:
            return ResponseGetTenantPolicySettingsResponse(
                data = onelens_backend_client.models.get_tenant_policy_settings_response.GetTenantPolicySettingsResponse(
                    pagination = null, 
                    policy_settings = [
                        onelens_backend_client.models.tenant_policy_settings.TenantPolicySettings(
                            id = '', 
                            policy_id = '', 
                            config_overrides = onelens_backend_client.models.config_overrides.config_overrides(), 
                            state = null, )
                        ], ),
        )
        """

    def testResponseGetTenantPolicySettingsResponse(self):
        """Test ResponseGetTenantPolicySettingsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
