# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_tenant_by_id import GetTenantById

class TestGetTenantById(unittest.TestCase):
    """GetTenantById unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTenantById:
        """Test GetTenantById
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTenantById`
        """
        model = GetTenantById()
        if include_optional:
            return GetTenantById(
                request = onelens_backend_client.models.get_tenant_by_id_request.GetTenantByIDRequest(
                    id = '', )
            )
        else:
            return GetTenantById(
                request = onelens_backend_client.models.get_tenant_by_id_request.GetTenantByIDRequest(
                    id = '', ),
        )
        """

    def testGetTenantById(self):
        """Test GetTenantById"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
