# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.tenant_policy import TenantPolicy

class TestTenantPolicy(unittest.TestCase):
    """TenantPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantPolicy:
        """Test TenantPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantPolicy`
        """
        model = TenantPolicy()
        if include_optional:
            return TenantPolicy(
                parent_ptp_id = '',
                title = '',
                alias = '',
                description = '',
                services = [
                    null
                    ],
                execution_type = 'DETECTIVE',
                details = onelens_backend_client.models.policy_template_details.PolicyTemplateDetails(
                    inputs = null, 
                    config_schema = onelens_backend_client.models.config_schema.config_schema(), 
                    output_violation_schema = onelens_backend_client.models.output_violation_schema.output_violation_schema(), 
                    rule_type = 'SQL', 
                    rule_definition = '', 
                    default_policy_config = onelens_backend_client.models.default_policy_config.default_policy_config(), ),
                policy_template_id = '',
                category = 'COST_SAVING',
                provider = 'AWS',
                id = ''
            )
        else:
            return TenantPolicy(
                parent_ptp_id = '',
                title = '',
                alias = '',
                services = [
                    null
                    ],
                execution_type = 'DETECTIVE',
                details = onelens_backend_client.models.policy_template_details.PolicyTemplateDetails(
                    inputs = null, 
                    config_schema = onelens_backend_client.models.config_schema.config_schema(), 
                    output_violation_schema = onelens_backend_client.models.output_violation_schema.output_violation_schema(), 
                    rule_type = 'SQL', 
                    rule_definition = '', 
                    default_policy_config = onelens_backend_client.models.default_policy_config.default_policy_config(), ),
                policy_template_id = '',
                category = 'COST_SAVING',
                provider = 'AWS',
                id = '',
        )
        """

    def testTenantPolicy(self):
        """Test TenantPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
