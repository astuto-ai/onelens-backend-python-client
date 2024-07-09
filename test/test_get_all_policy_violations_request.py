# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_all_policy_violations_request import GetAllPolicyViolationsRequest

class TestGetAllPolicyViolationsRequest(unittest.TestCase):
    """GetAllPolicyViolationsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllPolicyViolationsRequest:
        """Test GetAllPolicyViolationsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllPolicyViolationsRequest`
        """
        model = GetAllPolicyViolationsRequest()
        if include_optional:
            return GetAllPolicyViolationsRequest(
                pagination = onelens_backend_client.models.pagination_params.PaginationParams(
                    page = 56, 
                    page_size = 56, ),
                filters = [
                    {field=policy_id, operator=equals, value=4467d3a5-d806-4389-8b87-ada5b6f9ff30}
                    ],
                tenant_id = ''
            )
        else:
            return GetAllPolicyViolationsRequest(
                filters = [
                    {field=policy_id, operator=equals, value=4467d3a5-d806-4389-8b87-ada5b6f9ff30}
                    ],
                tenant_id = '',
        )
        """

    def testGetAllPolicyViolationsRequest(self):
        """Test GetAllPolicyViolationsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()