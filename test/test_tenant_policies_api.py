# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.api.tenant_policies_api import TenantPoliciesApi


class TestTenantPoliciesApi(unittest.TestCase):
    """TenantPoliciesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TenantPoliciesApi()

    def tearDown(self) -> None:
        pass

    def test_disable_tenant_policy(self) -> None:
        """Test case for disable_tenant_policy

        Disable Tenant Policy
        """
        pass

    def test_enable_all_policies(self) -> None:
        """Test case for enable_all_policies

        Enable All Policies
        """
        pass

    def test_enable_tenant_policy(self) -> None:
        """Test case for enable_tenant_policy

        Enable Tenant Policy
        """
        pass

    def test_get_tenant_policies(self) -> None:
        """Test case for get_tenant_policies

        Get Tenant Policies
        """
        pass

    def test_get_tenant_policy_settings(self) -> None:
        """Test case for get_tenant_policy_settings

        Get Tenant Policy Settings
        """
        pass

    def test_override_tenant_policy_config(self) -> None:
        """Test case for override_tenant_policy_config

        Override Tenant Policy Config
        """
        pass


if __name__ == '__main__':
    unittest.main()