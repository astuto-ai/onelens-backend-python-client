# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_all_navira_full_log_response import GetAllNaviraFullLogResponse

class TestGetAllNaviraFullLogResponse(unittest.TestCase):
    """GetAllNaviraFullLogResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllNaviraFullLogResponse:
        """Test GetAllNaviraFullLogResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllNaviraFullLogResponse`
        """
        model = GetAllNaviraFullLogResponse()
        if include_optional:
            return GetAllNaviraFullLogResponse(
                pagination = onelens_backend_client.models.pagination_fields.PaginationFields(
                    total_items = 56, 
                    total_pages = 56, 
                    current_page = 56, 
                    page_size = 56, ),
                navira_logs = [
                    onelens_backend_client.models.navira_full_log_response.NaviraFullLogResponse(
                        id = '', 
                        request = onelens_backend_client.models.request.Request(), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        response = onelens_backend_client.models.response.Response(), )
                    ]
            )
        else:
            return GetAllNaviraFullLogResponse(
                pagination = onelens_backend_client.models.pagination_fields.PaginationFields(
                    total_items = 56, 
                    total_pages = 56, 
                    current_page = 56, 
                    page_size = 56, ),
                navira_logs = [
                    onelens_backend_client.models.navira_full_log_response.NaviraFullLogResponse(
                        id = '', 
                        request = onelens_backend_client.models.request.Request(), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        response = onelens_backend_client.models.response.Response(), )
                    ],
        )
        """

    def testGetAllNaviraFullLogResponse(self):
        """Test GetAllNaviraFullLogResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
