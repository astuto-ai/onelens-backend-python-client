# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.join import Join

class TestJoin(unittest.TestCase):
    """Join unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Join:
        """Test Join
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Join`
        """
        model = Join()
        if include_optional:
            return Join(
                current_table_column = '',
                join_table = '',
                join_table_column = ''
            )
        else:
            return Join(
                current_table_column = '',
                join_table = '',
                join_table_column = '',
        )
        """

    def testJoin(self):
        """Test Join"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
