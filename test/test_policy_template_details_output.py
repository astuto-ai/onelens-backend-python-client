# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.policy_template_details_output import PolicyTemplateDetailsOutput

class TestPolicyTemplateDetailsOutput(unittest.TestCase):
    """PolicyTemplateDetailsOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicyTemplateDetailsOutput:
        """Test PolicyTemplateDetailsOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicyTemplateDetailsOutput`
        """
        model = PolicyTemplateDetailsOutput()
        if include_optional:
            return PolicyTemplateDetailsOutput(
                inputs = [
                    ''
                    ],
                config_schema = onelens_backend_client.models.config_schema.config_schema(),
                primary_violation_attributes_schema = onelens_backend_client.models.primary_violation_attributes_schema.primary_violation_attributes_schema(),
                secondary_violation_attributes_schema = onelens_backend_client.models.secondary_violation_attributes_schema.secondary_violation_attributes_schema(),
                rule_type = 'SQL',
                rule_definition = '',
                default_policy_config = onelens_backend_client.models.default_policy_config.default_policy_config(),
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
                    ]
            )
        else:
            return PolicyTemplateDetailsOutput(
        )
        """

    def testPolicyTemplateDetailsOutput(self):
        """Test PolicyTemplateDetailsOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
