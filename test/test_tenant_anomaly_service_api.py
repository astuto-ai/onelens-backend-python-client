# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.api.tenant_anomaly_service_api import TenantAnomalyServiceApi


class TestTenantAnomalyServiceApi(unittest.TestCase):
    """TenantAnomalyServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TenantAnomalyServiceApi()

    def tearDown(self) -> None:
        pass

    def test_disable_tenant_anomaly_setting(self) -> None:
        """Test case for disable_tenant_anomaly_setting

        disables an anomaly for a tenant in the tenant DB.
        """
        pass

    def test_enable_tenant_anomaly_setting(self) -> None:
        """Test case for enable_tenant_anomaly_setting

        enables an anomaly for a tenant in the tenant DB.
        """
        pass

    def test_get_tenant_anomaly_settings(self) -> None:
        """Test case for get_tenant_anomaly_settings

        Retrieves all tenant anomaly settings, optionally filtered by the parameters in the request.
        """
        pass

    def test_override_tenant_anomaly_setting_config(self) -> None:
        """Test case for override_tenant_anomaly_setting_config

        Override the tenant anomaly config with the provided config.
        """
        pass


if __name__ == '__main__':
    unittest.main()
