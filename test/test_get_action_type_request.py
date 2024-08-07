# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_action_type_request import GetActionTypeRequest

class TestGetActionTypeRequest(unittest.TestCase):
    """GetActionTypeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetActionTypeRequest:
        """Test GetActionTypeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetActionTypeRequest`
        """
        model = GetActionTypeRequest()
        if include_optional:
            return GetActionTypeRequest(
                pagination = onelens_backend_client.models.pagination_params.PaginationParams(
                    page = 56, 
                    page_size = 56, ),
                filters = onelens_backend_client.models.action_type_filters.ActionTypeFilters(
                    search_query = '', 
                    ids = [
                        56
                        ], 
                    services = [
                        null
                        ], )
            )
        else:
            return GetActionTypeRequest(
        )
        """

    def testGetActionTypeRequest(self):
        """Test GetActionTypeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
