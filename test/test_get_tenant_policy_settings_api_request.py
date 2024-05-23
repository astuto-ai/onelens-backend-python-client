# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_tenant_policy_settings_api_request import GetTenantPolicySettingsAPIRequest

class TestGetTenantPolicySettingsAPIRequest(unittest.TestCase):
    """GetTenantPolicySettingsAPIRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTenantPolicySettingsAPIRequest:
        """Test GetTenantPolicySettingsAPIRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTenantPolicySettingsAPIRequest`
        """
        model = GetTenantPolicySettingsAPIRequest()
        if include_optional:
            return GetTenantPolicySettingsAPIRequest(
                pagination = onelens_backend_client.models.pagination_params.PaginationParams(
                    page = 56, 
                    page_size = 56, ),
                filters = onelens_backend_client.models.tenant_policy_settings_filters.TenantPolicySettingsFilters(
                    states = [
                        'ACTIVE'
                        ], 
                    policy_ids = [
                        ''
                        ], )
            )
        else:
            return GetTenantPolicySettingsAPIRequest(
        )
        """

    def testGetTenantPolicySettingsAPIRequest(self):
        """Test GetTenantPolicySettingsAPIRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()