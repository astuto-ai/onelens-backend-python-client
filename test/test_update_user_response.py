# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.update_user_response import UpdateUserResponse

class TestUpdateUserResponse(unittest.TestCase):
    """UpdateUserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateUserResponse:
        """Test UpdateUserResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateUserResponse`
        """
        model = UpdateUserResponse()
        if include_optional:
            return UpdateUserResponse(
                auth0_id = '0',
                id = ''
            )
        else:
            return UpdateUserResponse(
                auth0_id = '0',
                id = '',
        )
        """

    def testUpdateUserResponse(self):
        """Test UpdateUserResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
