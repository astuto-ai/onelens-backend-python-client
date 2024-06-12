# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.create_auth0_user_request import CreateAuth0UserRequest

class TestCreateAuth0UserRequest(unittest.TestCase):
    """CreateAuth0UserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAuth0UserRequest:
        """Test CreateAuth0UserRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAuth0UserRequest`
        """
        model = CreateAuth0UserRequest()
        if include_optional:
            return CreateAuth0UserRequest(
                email = '',
                password = '',
                email_verified = True,
                app_metadata = onelens_backend_client.models.auth0_create_user_app_metadata.Auth0CreateUserAppMetadata(
                    role = null, ),
                connection = 'Username-Password-Authentication'
            )
        else:
            return CreateAuth0UserRequest(
                email = '',
                password = '',
                app_metadata = onelens_backend_client.models.auth0_create_user_app_metadata.Auth0CreateUserAppMetadata(
                    role = null, ),
                connection = 'Username-Password-Authentication',
        )
        """

    def testCreateAuth0UserRequest(self):
        """Test CreateAuth0UserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
