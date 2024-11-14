# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.leaf_nodes import LeafNodes


class TestLeafNodes(unittest.TestCase):
    """LeafNodes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeafNodes:
        """Test LeafNodes
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LeafNodes`
        """
        model = LeafNodes()
        if include_optional:
            return LeafNodes(
                nodes = [
                    onelens_backend_client.models.hierarchy_node_entity_dto.HierarchyNodeEntityDTO(
                        id = '', 
                        name = '', 
                        category = 'ROOT', 
                        resource_filters = [
                            onelens_backend_client.models.hierarchy_node_resource_filters.HierarchyNodeResourceFilters(
                                key = 56, 
                                field = '', 
                                operator = '', 
                                value = null, 
                                json_key = '', )
                            ], 
                        resource_filter_expression = '', 
                        is_shared = True, 
                        attribution_details = onelens_backend_client.models.hierarchy_node_attribution_details.HierarchyNodeAttributionDetails(
                            nodes = [
                                ''
                                ], 
                            strategy = null, ), 
                        state = null, 
                        sql_filter = '', 
                        description = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by = '', 
                        updated_by = '', )
                    ]
            )
        else:
            return LeafNodes(
                nodes = [
                    onelens_backend_client.models.hierarchy_node_entity_dto.HierarchyNodeEntityDTO(
                        id = '', 
                        name = '', 
                        category = 'ROOT', 
                        resource_filters = [
                            onelens_backend_client.models.hierarchy_node_resource_filters.HierarchyNodeResourceFilters(
                                key = 56, 
                                field = '', 
                                operator = '', 
                                value = null, 
                                json_key = '', )
                            ], 
                        resource_filter_expression = '', 
                        is_shared = True, 
                        attribution_details = onelens_backend_client.models.hierarchy_node_attribution_details.HierarchyNodeAttributionDetails(
                            nodes = [
                                ''
                                ], 
                            strategy = null, ), 
                        state = null, 
                        sql_filter = '', 
                        description = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by = '', 
                        updated_by = '', )
                    ],
        )
        """

    def testLeafNodes(self):
        """Test LeafNodes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
