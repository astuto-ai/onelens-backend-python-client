# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.create_tenant_provider_request import CreateTenantProviderRequest

class TestCreateTenantProviderRequest(unittest.TestCase):
    """CreateTenantProviderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTenantProviderRequest:
        """Test CreateTenantProviderRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTenantProviderRequest`
        """
        model = CreateTenantProviderRequest()
        if include_optional:
            return CreateTenantProviderRequest(
                cloud_provider = '',
                cloud_id = '',
                parent_id = '',
                provider_config = onelens_backend_client.models.provider_config.Provider Config(),
                tenant_id = ''
            )
        else:
            return CreateTenantProviderRequest(
                cloud_provider = '',
                cloud_id = '',
                provider_config = onelens_backend_client.models.provider_config.Provider Config(),
        )
        """

    def testCreateTenantProviderRequest(self):
        """Test CreateTenantProviderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
