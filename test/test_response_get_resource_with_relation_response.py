# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.response_get_resource_with_relation_response import ResponseGetResourceWithRelationResponse

class TestResponseGetResourceWithRelationResponse(unittest.TestCase):
    """ResponseGetResourceWithRelationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseGetResourceWithRelationResponse:
        """Test ResponseGetResourceWithRelationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseGetResourceWithRelationResponse`
        """
        model = ResponseGetResourceWithRelationResponse()
        if include_optional:
            return ResponseGetResourceWithRelationResponse(
                data = onelens_backend_client.models.get_resource_with_relation_response.GetResourceWithRelationResponse(
                    resource = null, 
                    relationships = [
                        onelens_backend_client.models.resource_relationship_response.ResourceRelationshipResponse(
                            relationship_type = '', 
                            direction = '', 
                            resource = null, )
                        ], ),
                message = ''
            )
        else:
            return ResponseGetResourceWithRelationResponse(
                data = onelens_backend_client.models.get_resource_with_relation_response.GetResourceWithRelationResponse(
                    resource = null, 
                    relationships = [
                        onelens_backend_client.models.resource_relationship_response.ResourceRelationshipResponse(
                            relationship_type = '', 
                            direction = '', 
                            resource = null, )
                        ], ),
        )
        """

    def testResponseGetResourceWithRelationResponse(self):
        """Test ResponseGetResourceWithRelationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
