# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.response_create_default_hierarchy_response import ResponseCreateDefaultHierarchyResponse

class TestResponseCreateDefaultHierarchyResponse(unittest.TestCase):
    """ResponseCreateDefaultHierarchyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseCreateDefaultHierarchyResponse:
        """Test ResponseCreateDefaultHierarchyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseCreateDefaultHierarchyResponse`
        """
        model = ResponseCreateDefaultHierarchyResponse()
        if include_optional:
            return ResponseCreateDefaultHierarchyResponse(
                data = onelens_backend_client.models.create_default_hierarchy_response.CreateDefaultHierarchyResponse(),
                message = ''
            )
        else:
            return ResponseCreateDefaultHierarchyResponse(
                data = onelens_backend_client.models.create_default_hierarchy_response.CreateDefaultHierarchyResponse(),
        )
        """

    def testResponseCreateDefaultHierarchyResponse(self):
        """Test ResponseCreateDefaultHierarchyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()