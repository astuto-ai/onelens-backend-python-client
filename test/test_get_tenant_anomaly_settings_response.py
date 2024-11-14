# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.get_tenant_anomaly_settings_response import (
    GetTenantAnomalySettingsResponse,
)


class TestGetTenantAnomalySettingsResponse(unittest.TestCase):
    """GetTenantAnomalySettingsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTenantAnomalySettingsResponse:
        """Test GetTenantAnomalySettingsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetTenantAnomalySettingsResponse`
        """
        model = GetTenantAnomalySettingsResponse()
        if include_optional:
            return GetTenantAnomalySettingsResponse(
                pagination = onelens_backend_client.models.pagination_fields.PaginationFields(
                    total_items = 56, 
                    total_pages = 56, 
                    current_page = 56, 
                    page_size = 56, ),
                anomaly_settings = [
                    onelens_backend_client.models.tenant_anomaly_settings.TenantAnomalySettings(
                        config_overrides = onelens_backend_client.models.anomaly_logic_operation.AnomalyLogicOperation(
                            and = [
                                onelens_backend_client.models.and_item.AndItem(
                                    >= = null, 
                                    > = null, )
                                ], 
                            or = [
                                onelens_backend_client.models.or_item.OrItem(
                                    >= = null, 
                                    > = null, )
                                ], ), 
                        state = null, 
                        id = '', )
                    ]
            )
        else:
            return GetTenantAnomalySettingsResponse(
                pagination = onelens_backend_client.models.pagination_fields.PaginationFields(
                    total_items = 56, 
                    total_pages = 56, 
                    current_page = 56, 
                    page_size = 56, ),
                anomaly_settings = [
                    onelens_backend_client.models.tenant_anomaly_settings.TenantAnomalySettings(
                        config_overrides = onelens_backend_client.models.anomaly_logic_operation.AnomalyLogicOperation(
                            and = [
                                onelens_backend_client.models.and_item.AndItem(
                                    >= = null, 
                                    > = null, )
                                ], 
                            or = [
                                onelens_backend_client.models.or_item.OrItem(
                                    >= = null, 
                                    > = null, )
                                ], ), 
                        state = null, 
                        id = '', )
                    ],
        )
        """

    def testGetTenantAnomalySettingsResponse(self):
        """Test GetTenantAnomalySettingsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
