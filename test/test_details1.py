# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.details1 import Details1

class TestDetails1(unittest.TestCase):
    """Details1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Details1:
        """Test Details1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Details1`
        """
        model = Details1()
        if include_optional:
            return Details1(
                policy_id = '',
                entity_id = '',
                entity_type = '',
                policy_template_id = '',
                policy_config = '',
                policy_config_version = '',
                violation_attributes = ''
            )
        else:
            return Details1(
                policy_id = '',
                entity_id = '',
                entity_type = '',
                policy_template_id = '',
                policy_config = '',
                policy_config_version = '',
                violation_attributes = '',
        )
        """

    def testDetails1(self):
        """Test Details1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
