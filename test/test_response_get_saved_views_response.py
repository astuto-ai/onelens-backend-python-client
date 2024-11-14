# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.response_get_saved_views_response import (
    ResponseGetSavedViewsResponse,
)


class TestResponseGetSavedViewsResponse(unittest.TestCase):
    """ResponseGetSavedViewsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseGetSavedViewsResponse:
        """Test ResponseGetSavedViewsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ResponseGetSavedViewsResponse`
        """
        model = ResponseGetSavedViewsResponse()
        if include_optional:
            return ResponseGetSavedViewsResponse(
                data = onelens_backend_client.models.get_saved_views_response.GetSavedViewsResponse(
                    saved_views = [
                        onelens_backend_client.models.saved_view_item.SavedViewItem(
                            id = '', 
                            name = '012', 
                            page = '012', 
                            payload = null, 
                            is_default = True, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ),
                message = ''
            )
        else:
            return ResponseGetSavedViewsResponse(
                data = onelens_backend_client.models.get_saved_views_response.GetSavedViewsResponse(
                    saved_views = [
                        onelens_backend_client.models.saved_view_item.SavedViewItem(
                            id = '', 
                            name = '012', 
                            page = '012', 
                            payload = null, 
                            is_default = True, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ),
        )
        """

    def testResponseGetSavedViewsResponse(self):
        """Test ResponseGetSavedViewsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
