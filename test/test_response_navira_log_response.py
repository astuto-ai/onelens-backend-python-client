# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.response_navira_log_response import (
    ResponseNaviraLogResponse,
)


class TestResponseNaviraLogResponse(unittest.TestCase):
    """ResponseNaviraLogResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseNaviraLogResponse:
        """Test ResponseNaviraLogResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ResponseNaviraLogResponse`
        """
        model = ResponseNaviraLogResponse()
        if include_optional:
            return ResponseNaviraLogResponse(
                data = onelens_backend_client.models.navira_log_response.NaviraLogResponse(
                    id = '', 
                    request = onelens_backend_client.models.request.Request(), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                message = ''
            )
        else:
            return ResponseNaviraLogResponse(
                data = onelens_backend_client.models.navira_log_response.NaviraLogResponse(
                    id = '', 
                    request = onelens_backend_client.models.request.Request(), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testResponseNaviraLogResponse(self):
        """Test ResponseNaviraLogResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
