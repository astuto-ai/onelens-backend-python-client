# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.response_get_tenant_provider_by_id_response import ResponseGetTenantProviderByIDResponse

class TestResponseGetTenantProviderByIDResponse(unittest.TestCase):
    """ResponseGetTenantProviderByIDResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseGetTenantProviderByIDResponse:
        """Test ResponseGetTenantProviderByIDResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseGetTenantProviderByIDResponse`
        """
        model = ResponseGetTenantProviderByIDResponse()
        if include_optional:
            return ResponseGetTenantProviderByIDResponse(
                data = onelens_backend_client.models.get_tenant_provider_by_id_response.GetTenantProviderByIDResponse(
                    cloud_provider = '', 
                    cloud_id = '', 
                    parent_id = null, 
                    provider_config = onelens_backend_client.models.provider_config.Provider Config(), 
                    id = '', 
                    is_parent_account = True, 
                    is_verified = True, 
                    state = '', ),
                message = None
            )
        else:
            return ResponseGetTenantProviderByIDResponse(
                data = onelens_backend_client.models.get_tenant_provider_by_id_response.GetTenantProviderByIDResponse(
                    cloud_provider = '', 
                    cloud_id = '', 
                    parent_id = null, 
                    provider_config = onelens_backend_client.models.provider_config.Provider Config(), 
                    id = '', 
                    is_parent_account = True, 
                    is_verified = True, 
                    state = '', ),
        )
        """

    def testResponseGetTenantProviderByIDResponse(self):
        """Test ResponseGetTenantProviderByIDResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
