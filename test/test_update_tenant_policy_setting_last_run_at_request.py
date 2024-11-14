# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.update_tenant_policy_setting_last_run_at_request import (
    UpdateTenantPolicySettingLastRunAtRequest,
)


class TestUpdateTenantPolicySettingLastRunAtRequest(unittest.TestCase):
    """UpdateTenantPolicySettingLastRunAtRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> UpdateTenantPolicySettingLastRunAtRequest:
        """Test UpdateTenantPolicySettingLastRunAtRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UpdateTenantPolicySettingLastRunAtRequest`
        """
        model = UpdateTenantPolicySettingLastRunAtRequest()
        if include_optional:
            return UpdateTenantPolicySettingLastRunAtRequest(
                tenant_id = '',
                updates = [
                    onelens_backend_client.models.last_run_at_update_item.LastRunAtUpdateItem(
                        policy_id = '', 
                        last_run_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return UpdateTenantPolicySettingLastRunAtRequest(
                tenant_id = '',
                updates = [
                    onelens_backend_client.models.last_run_at_update_item.LastRunAtUpdateItem(
                        policy_id = '', 
                        last_run_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testUpdateTenantPolicySettingLastRunAtRequest(self):
        """Test UpdateTenantPolicySettingLastRunAtRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
