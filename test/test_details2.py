# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.details2 import Details2

class TestDetails2(unittest.TestCase):
    """Details2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Details2:
        """Test Details2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Details2`
        """
        model = Details2()
        if include_optional:
            return Details2(
                policy_id = '',
                entity_id = '',
                entity_type = '',
                policy_template_id = '',
                policy_config = '',
                policy_config_version = '',
                violation_attributes = ''
            )
        else:
            return Details2(
                policy_id = '',
                entity_id = '',
                entity_type = '',
                policy_template_id = '',
                policy_config = '',
                policy_config_version = '',
                violation_attributes = '',
        )
        """

    def testDetails2(self):
        """Test Details2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
