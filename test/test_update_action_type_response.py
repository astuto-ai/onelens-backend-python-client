# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.update_action_type_response import (
    UpdateActionTypeResponse,
)


class TestUpdateActionTypeResponse(unittest.TestCase):
    """UpdateActionTypeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateActionTypeResponse:
        """Test UpdateActionTypeResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UpdateActionTypeResponse`
        """
        model = UpdateActionTypeResponse()
        if include_optional:
            return UpdateActionTypeResponse(
                service = None,
                title = '',
                subtitle = '',
                description = '',
                id = 56
            )
        else:
            return UpdateActionTypeResponse(
                service = None,
                title = '',
                description = '',
                id = 56,
        )
        """

    def testUpdateActionTypeResponse(self):
        """Test UpdateActionTypeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
