# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.response_create_user_tenant_mapping_response import ResponseCreateUserTenantMappingResponse

class TestResponseCreateUserTenantMappingResponse(unittest.TestCase):
    """ResponseCreateUserTenantMappingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseCreateUserTenantMappingResponse:
        """Test ResponseCreateUserTenantMappingResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseCreateUserTenantMappingResponse`
        """
        model = ResponseCreateUserTenantMappingResponse()
        if include_optional:
            return ResponseCreateUserTenantMappingResponse(
                data = onelens_backend_client.models.create_user_tenant_mapping_response.CreateUserTenantMappingResponse(
                    user_id = '', 
                    tenant_id = '', ),
                message = None
            )
        else:
            return ResponseCreateUserTenantMappingResponse(
                data = onelens_backend_client.models.create_user_tenant_mapping_response.CreateUserTenantMappingResponse(
                    user_id = '', 
                    tenant_id = '', ),
        )
        """

    def testResponseCreateUserTenantMappingResponse(self):
        """Test ResponseCreateUserTenantMappingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
