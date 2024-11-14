# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.create_auth0_and_onelens_user_response import (
    CreateAuth0AndOnelensUserResponse,
)


class TestCreateAuth0AndOnelensUserResponse(unittest.TestCase):
    """CreateAuth0AndOnelensUserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAuth0AndOnelensUserResponse:
        """Test CreateAuth0AndOnelensUserResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateAuth0AndOnelensUserResponse`
        """
        model = CreateAuth0AndOnelensUserResponse()
        if include_optional:
            return CreateAuth0AndOnelensUserResponse(
                auth0_data = onelens_backend_client.models.auth0_user_all_fields.Auth0UserAllFields(
                    email = '', 
                    email_verified = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    identities = [
                        null
                        ], 
                    name = '', 
                    nickname = '', 
                    picture = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user_id = '', 
                    user_metadata = onelens_backend_client.models.user_metadata.user_metadata(), 
                    app_metadata = onelens_backend_client.models.app_metadata.App Metadata(), 
                    last_ip = '', 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    logins_count = 56, ),
                onelens_data = onelens_backend_client.models.create_user_response.CreateUserResponse(
                    auth0_id = '0', 
                    state = 'ACTIVE', 
                    details = null, 
                    id = '', )
            )
        else:
            return CreateAuth0AndOnelensUserResponse(
                auth0_data = onelens_backend_client.models.auth0_user_all_fields.Auth0UserAllFields(
                    email = '', 
                    email_verified = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    identities = [
                        null
                        ], 
                    name = '', 
                    nickname = '', 
                    picture = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user_id = '', 
                    user_metadata = onelens_backend_client.models.user_metadata.user_metadata(), 
                    app_metadata = onelens_backend_client.models.app_metadata.App Metadata(), 
                    last_ip = '', 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    logins_count = 56, ),
                onelens_data = onelens_backend_client.models.create_user_response.CreateUserResponse(
                    auth0_id = '0', 
                    state = 'ACTIVE', 
                    details = null, 
                    id = '', ),
        )
        """

    def testCreateAuth0AndOnelensUserResponse(self):
        """Test CreateAuth0AndOnelensUserResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
