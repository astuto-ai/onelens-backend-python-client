# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.get_policy_tickets_export_to_response_type import (
    GetPolicyTicketsExportToResponseType,
)


class TestGetPolicyTicketsExportToResponseType(unittest.TestCase):
    """GetPolicyTicketsExportToResponseType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPolicyTicketsExportToResponseType:
        """Test GetPolicyTicketsExportToResponseType
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetPolicyTicketsExportToResponseType`
        """
        model = GetPolicyTicketsExportToResponseType()
        if include_optional:
            return GetPolicyTicketsExportToResponseType(
                url = '',
                extenstion = ''
            )
        else:
            return GetPolicyTicketsExportToResponseType(
                url = '',
                extenstion = '',
        )
        """

    def testGetPolicyTicketsExportToResponseType(self):
        """Test GetPolicyTicketsExportToResponseType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
