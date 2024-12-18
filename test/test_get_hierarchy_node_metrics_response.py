# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_hierarchy_node_metrics_response import GetHierarchyNodeMetricsResponse

class TestGetHierarchyNodeMetricsResponse(unittest.TestCase):
    """GetHierarchyNodeMetricsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetHierarchyNodeMetricsResponse:
        """Test GetHierarchyNodeMetricsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetHierarchyNodeMetricsResponse`
        """
        model = GetHierarchyNodeMetricsResponse()
        if include_optional:
            return GetHierarchyNodeMetricsResponse(
                metrics = {
                    'key' : onelens_backend_client.models.hierarchy_node_resource_metrics.HierarchyNodeResourceMetrics(
                        total = 56, 
                        unique = 56, 
                        conflicting = 56, )
                    }
            )
        else:
            return GetHierarchyNodeMetricsResponse(
                metrics = {
                    'key' : onelens_backend_client.models.hierarchy_node_resource_metrics.HierarchyNodeResourceMetrics(
                        total = 56, 
                        unique = 56, 
                        conflicting = 56, )
                    },
        )
        """

    def testGetHierarchyNodeMetricsResponse(self):
        """Test GetHierarchyNodeMetricsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
