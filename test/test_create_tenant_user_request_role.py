# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_tenant_user_request_role import CreateTenantUserRequestRole

class TestCreateTenantUserRequestRole(unittest.TestCase):
    """CreateTenantUserRequestRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTenantUserRequestRole:
        """Test CreateTenantUserRequestRole
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTenantUserRequestRole`
        """
        model = CreateTenantUserRequestRole()
        if include_optional:
            return CreateTenantUserRequestRole(
            )
        else:
            return CreateTenantUserRequestRole(
        )
        """

    def testCreateTenantUserRequestRole(self):
        """Test CreateTenantUserRequestRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
