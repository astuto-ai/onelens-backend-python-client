# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.query_details_derived_variables import (
    QueryDetailsDerivedVariables,
)


class TestQueryDetailsDerivedVariables(unittest.TestCase):
    """QueryDetailsDerivedVariables unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryDetailsDerivedVariables:
        """Test QueryDetailsDerivedVariables
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `QueryDetailsDerivedVariables`
        """
        model = QueryDetailsDerivedVariables()
        if include_optional:
            return QueryDetailsDerivedVariables(
                key = '',
                value_type = '',
                source_key = ''
            )
        else:
            return QueryDetailsDerivedVariables(
                key = '',
                value_type = '',
                source_key = '',
        )
        """

    def testQueryDetailsDerivedVariables(self):
        """Test QueryDetailsDerivedVariables"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
