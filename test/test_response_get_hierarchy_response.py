# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.response_get_hierarchy_response import ResponseGetHierarchyResponse

class TestResponseGetHierarchyResponse(unittest.TestCase):
    """ResponseGetHierarchyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseGetHierarchyResponse:
        """Test ResponseGetHierarchyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseGetHierarchyResponse`
        """
        model = ResponseGetHierarchyResponse()
        if include_optional:
            return ResponseGetHierarchyResponse(
                data = onelens_backend_client.models.get_hierarchy_response.GetHierarchyResponse(
                    id = '', 
                    data = onelens_backend_client.models.data.Data(), 
                    version = 56, 
                    state = null, 
                    type = null, ),
                message = ''
            )
        else:
            return ResponseGetHierarchyResponse(
                data = onelens_backend_client.models.get_hierarchy_response.GetHierarchyResponse(
                    id = '', 
                    data = onelens_backend_client.models.data.Data(), 
                    version = 56, 
                    state = null, 
                    type = null, ),
        )
        """

    def testResponseGetHierarchyResponse(self):
        """Test ResponseGetHierarchyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
