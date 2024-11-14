# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.update_hierarchy_node_api_request import (
    UpdateHierarchyNodeAPIRequest,
)


class TestUpdateHierarchyNodeAPIRequest(unittest.TestCase):
    """UpdateHierarchyNodeAPIRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateHierarchyNodeAPIRequest:
        """Test UpdateHierarchyNodeAPIRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UpdateHierarchyNodeAPIRequest`
        """
        model = UpdateHierarchyNodeAPIRequest()
        if include_optional:
            return UpdateHierarchyNodeAPIRequest(
                name = '',
                parent_id = '',
                category = 'ROOT',
                resource_filters = [
                    onelens_backend_client.models.hierarchy_node_resource_filters.HierarchyNodeResourceFilters(
                        key = 56, 
                        field = '', 
                        operator = '', 
                        value = null, )
                    ],
                resource_filter_expression = '',
                is_shared = True,
                attribution_details = onelens_backend_client.models.hierarchy_node_attribution_details.HierarchyNodeAttributionDetails(
                    nodes = [
                        ''
                        ], 
                    strategy = null, )
            )
        else:
            return UpdateHierarchyNodeAPIRequest(
        )
        """

    def testUpdateHierarchyNodeAPIRequest(self):
        """Test UpdateHierarchyNodeAPIRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
