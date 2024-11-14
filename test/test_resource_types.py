# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.resource_types import ResourceTypes


class TestResourceTypes(unittest.TestCase):
    """ResourceTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceTypes:
        """Test ResourceTypes
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ResourceTypes`
        """
        model = ResourceTypes()
        if include_optional:
            return ResourceTypes(
                resource_type = '',
                resource_table = '',
                select_columns = [
                    ''
                    ],
                aws_url_template = '',
                relationship_config = [
                    onelens_backend_client.models.relationship_config_item.RelationshipConfigItem(
                        relationship_type = '', 
                        join = onelens_backend_client.models.join.Join(
                            current_table_column = '', 
                            join_table = '', 
                            join_table_column = '', ), )
                    ]
            )
        else:
            return ResourceTypes(
                resource_type = '',
                resource_table = '',
                select_columns = [
                    ''
                    ],
                aws_url_template = '',
                relationship_config = [
                    onelens_backend_client.models.relationship_config_item.RelationshipConfigItem(
                        relationship_type = '', 
                        join = onelens_backend_client.models.join.Join(
                            current_table_column = '', 
                            join_table = '', 
                            join_table_column = '', ), )
                    ],
        )
        """

    def testResourceTypes(self):
        """Test ResourceTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
