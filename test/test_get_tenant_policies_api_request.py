# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_tenant_policies_api_request import GetTenantPoliciesAPIRequest

class TestGetTenantPoliciesAPIRequest(unittest.TestCase):
    """GetTenantPoliciesAPIRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTenantPoliciesAPIRequest:
        """Test GetTenantPoliciesAPIRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTenantPoliciesAPIRequest`
        """
        model = GetTenantPoliciesAPIRequest()
        if include_optional:
            return GetTenantPoliciesAPIRequest(
                pagination = onelens_backend_client.models.pagination_params.PaginationParams(
                    page = 56, 
                    page_size = 56, ),
                filters = onelens_backend_client.models.tenant_policy_filters.TenantPolicyFilters(
                    search_query = '', 
                    parent_ptp_ids = [
                        ''
                        ], 
                    categories = [
                        'COST_SAVING'
                        ], 
                    providers = [
                        'AWS'
                        ], 
                    services = [
                        null
                        ], 
                    execution_types = [
                        'DETECTIVE'
                        ], )
            )
        else:
            return GetTenantPoliciesAPIRequest(
        )
        """

    def testGetTenantPoliciesAPIRequest(self):
        """Test GetTenantPoliciesAPIRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
