# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.password_change_email_request import PasswordChangeEmailRequest

class TestPasswordChangeEmailRequest(unittest.TestCase):
    """PasswordChangeEmailRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PasswordChangeEmailRequest:
        """Test PasswordChangeEmailRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PasswordChangeEmailRequest`
        """
        model = PasswordChangeEmailRequest()
        if include_optional:
            return PasswordChangeEmailRequest(
                ol_user_id = '',
                tenant_id = ''
            )
        else:
            return PasswordChangeEmailRequest(
                ol_user_id = '',
                tenant_id = '',
        )
        """

    def testPasswordChangeEmailRequest(self):
        """Test PasswordChangeEmailRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
