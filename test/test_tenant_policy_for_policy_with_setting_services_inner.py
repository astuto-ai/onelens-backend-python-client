# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.tenant_policy_for_policy_with_setting_services_inner import TenantPolicyForPolicyWithSettingServicesInner

class TestTenantPolicyForPolicyWithSettingServicesInner(unittest.TestCase):
    """TenantPolicyForPolicyWithSettingServicesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantPolicyForPolicyWithSettingServicesInner:
        """Test TenantPolicyForPolicyWithSettingServicesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantPolicyForPolicyWithSettingServicesInner`
        """
        model = TenantPolicyForPolicyWithSettingServicesInner()
        if include_optional:
            return TenantPolicyForPolicyWithSettingServicesInner(
                id = '',
                name = '',
                product_code = '',
                display_name = '',
                description = '',
                resource_types = [
                    onelens_backend_client.models.resource_type.ResourceType(
                        resource_type = '', 
                        resource_table = '', 
                        identifier_key = '', 
                        select_columns = [
                            ''
                            ], 
                        resource_url_template = '', 
                        is_tags_available = True, 
                        relationship_config = [
                            onelens_backend_client.models.relationship_config_item.RelationshipConfigItem(
                                relationship_type = '', 
                                join = onelens_backend_client.models.join.Join(
                                    current_table_column = '', 
                                    join_table = '', 
                                    join_table_column = '', ), )
                            ], )
                    ],
                features = onelens_backend_client.models.features.Features(
                    enable_in_policy = True, 
                    enable_in_anomalies = True, )
            )
        else:
            return TenantPolicyForPolicyWithSettingServicesInner(
                id = '',
                name = '',
                product_code = '',
                display_name = '',
                description = '',
        )
        """

    def testTenantPolicyForPolicyWithSettingServicesInner(self):
        """Test TenantPolicyForPolicyWithSettingServicesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
