# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.delete_hierarchy_node_request import (
    DeleteHierarchyNodeRequest,
)


class TestDeleteHierarchyNodeRequest(unittest.TestCase):
    """DeleteHierarchyNodeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteHierarchyNodeRequest:
        """Test DeleteHierarchyNodeRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DeleteHierarchyNodeRequest`
        """
        model = DeleteHierarchyNodeRequest()
        if include_optional:
            return DeleteHierarchyNodeRequest(
                id = '',
                tenant_id = ''
            )
        else:
            return DeleteHierarchyNodeRequest(
                id = '',
                tenant_id = '',
        )
        """

    def testDeleteHierarchyNodeRequest(self):
        """Test DeleteHierarchyNodeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
