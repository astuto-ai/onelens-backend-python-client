# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.create_policy_template_request import CreatePolicyTemplateRequest

class TestCreatePolicyTemplateRequest(unittest.TestCase):
    """CreatePolicyTemplateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePolicyTemplateRequest:
        """Test CreatePolicyTemplateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePolicyTemplateRequest`
        """
        model = CreatePolicyTemplateRequest()
        if include_optional:
            return CreatePolicyTemplateRequest(
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
                    default_policy_config = onelens_backend_client.models.default_policy_config.default_policy_config(), )
            )
        else:
            return CreatePolicyTemplateRequest(
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
        )
        """

    def testCreatePolicyTemplateRequest(self):
        """Test CreatePolicyTemplateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
