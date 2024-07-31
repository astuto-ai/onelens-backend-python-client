# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.tenant_policy_for_policy_with_setting import TenantPolicyForPolicyWithSetting

class TestTenantPolicyForPolicyWithSetting(unittest.TestCase):
    """TenantPolicyForPolicyWithSetting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantPolicyForPolicyWithSetting:
        """Test TenantPolicyForPolicyWithSetting
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantPolicyForPolicyWithSetting`
        """
        model = TenantPolicyForPolicyWithSetting()
        if include_optional:
            return TenantPolicyForPolicyWithSetting(
                parent_ptp_id = '',
                title = '',
                alias = '',
                description = '',
                services = [
                    null
                    ],
                execution_type = 'DETECTIVE',
                details = onelens_backend_client.models.policy_template_details.PolicyTemplateDetails(
                    inputs = [
                        ''
                        ], 
                    config_schema = onelens_backend_client.models.config_schema.config_schema(), 
                    primary_violation_attributes_schema = onelens_backend_client.models.primary_violation_attributes_schema.primary_violation_attributes_schema(), 
                    secondary_violation_attributes_schema = onelens_backend_client.models.secondary_violation_attributes_schema.secondary_violation_attributes_schema(), 
                    rule_type = 'SQL', 
                    rule_definition = '', 
                    rule_definition_hash = '', 
                    default_policy_config = onelens_backend_client.models.default_policy_config.default_policy_config(), 
                    default_policy_config_hash = '', 
                    metrics_details = [
                        onelens_backend_client.models.metrics_chart_config.MetricsChartConfig(
                            chart_title = '', 
                            chart_type = '', 
                            table_name = '', 
                            metric_name = '', 
                            aggregation_type = null, 
                            look_back_period = null, 
                            threshold = onelens_backend_client.models.metrics_threshold.MetricsThreshold(
                                value_from = '', 
                                value = null, ), )
                        ], ),
                description2 = '',
                resource_type = '',
                recommendation_details = onelens_backend_client.models.policy_template_recommendation_details.PolicyTemplateRecommendationDetails(
                    applicable_recommendation_units = [
                        onelens_backend_client.models.policy_template_recommendation_units.PolicyTemplateRecommendationUnits(
                            recommendation_unit_id = '', 
                            params = null, )
                        ], ),
                policy_template_id = '',
                category = 'COST_SAVING',
                provider = 'AWS',
                id = '',
                state = 'ACTIVE'
            )
        else:
            return TenantPolicyForPolicyWithSetting(
                parent_ptp_id = '',
                title = '',
                alias = '',
                services = [
                    null
                    ],
                execution_type = 'DETECTIVE',
                details = onelens_backend_client.models.policy_template_details.PolicyTemplateDetails(
                    inputs = [
                        ''
                        ], 
                    config_schema = onelens_backend_client.models.config_schema.config_schema(), 
                    primary_violation_attributes_schema = onelens_backend_client.models.primary_violation_attributes_schema.primary_violation_attributes_schema(), 
                    secondary_violation_attributes_schema = onelens_backend_client.models.secondary_violation_attributes_schema.secondary_violation_attributes_schema(), 
                    rule_type = 'SQL', 
                    rule_definition = '', 
                    rule_definition_hash = '', 
                    default_policy_config = onelens_backend_client.models.default_policy_config.default_policy_config(), 
                    default_policy_config_hash = '', 
                    metrics_details = [
                        onelens_backend_client.models.metrics_chart_config.MetricsChartConfig(
                            chart_title = '', 
                            chart_type = '', 
                            table_name = '', 
                            metric_name = '', 
                            aggregation_type = null, 
                            look_back_period = null, 
                            threshold = onelens_backend_client.models.metrics_threshold.MetricsThreshold(
                                value_from = '', 
                                value = null, ), )
                        ], ),
                resource_type = '',
                recommendation_details = onelens_backend_client.models.policy_template_recommendation_details.PolicyTemplateRecommendationDetails(
                    applicable_recommendation_units = [
                        onelens_backend_client.models.policy_template_recommendation_units.PolicyTemplateRecommendationUnits(
                            recommendation_unit_id = '', 
                            params = null, )
                        ], ),
                policy_template_id = '',
                category = 'COST_SAVING',
                provider = 'AWS',
                id = '',
                state = 'ACTIVE',
        )
        """

    def testTenantPolicyForPolicyWithSetting(self):
        """Test TenantPolicyForPolicyWithSetting"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
