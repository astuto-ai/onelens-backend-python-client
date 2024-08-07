# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_action_type_response import GetActionTypeResponse

class TestGetActionTypeResponse(unittest.TestCase):
    """GetActionTypeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetActionTypeResponse:
        """Test GetActionTypeResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetActionTypeResponse`
        """
        model = GetActionTypeResponse()
        if include_optional:
            return GetActionTypeResponse(
                action_types = [
                    onelens_backend_client.models.action_type.ActionType(
                        service = null, 
                        title = '', 
                        subtitle = '', 
                        description = '', 
                        id = 56, )
                    ],
                pagination = onelens_backend_client.models.pagination_fields.PaginationFields(
                    total_items = 56, 
                    total_pages = 56, 
                    current_page = 56, 
                    page_size = 56, )
            )
        else:
            return GetActionTypeResponse(
                action_types = [
                    onelens_backend_client.models.action_type.ActionType(
                        service = null, 
                        title = '', 
                        subtitle = '', 
                        description = '', 
                        id = 56, )
                    ],
                pagination = onelens_backend_client.models.pagination_fields.PaginationFields(
                    total_items = 56, 
                    total_pages = 56, 
                    current_page = 56, 
                    page_size = 56, ),
        )
        """

    def testGetActionTypeResponse(self):
        """Test GetActionTypeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
