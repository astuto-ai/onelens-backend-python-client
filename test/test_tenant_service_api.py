# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.api.tenant_service_api import TenantServiceApi


class TestTenantServiceApi(unittest.TestCase):
    """TenantServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TenantServiceApi()

    def tearDown(self) -> None:
        pass

    def test_create_tenant(self) -> None:
        """Test case for create_tenant

        Creates a new tenant.
        """
        pass

    def test_disable_tenant(self) -> None:
        """Test case for disable_tenant

        Disables a tenant.
        """
        pass

    def test_get_tenant_by_id(self) -> None:
        """Test case for get_tenant_by_id

        Retrieves a tenant by its unique identifier.
        """
        pass

    def test_get_tenants(self) -> None:
        """Test case for get_tenants

        Retrieves all Tenants with filters.
        """
        pass

    def test_update_tenant(self) -> None:
        """Test case for update_tenant

        Updates an existing tenant.
        """
        pass


if __name__ == '__main__':
    unittest.main()
