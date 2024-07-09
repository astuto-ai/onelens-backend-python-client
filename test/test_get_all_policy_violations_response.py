# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_all_policy_violations_response import GetAllPolicyViolationsResponse

class TestGetAllPolicyViolationsResponse(unittest.TestCase):
    """GetAllPolicyViolationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllPolicyViolationsResponse:
        """Test GetAllPolicyViolationsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllPolicyViolationsResponse`
        """
        model = GetAllPolicyViolationsResponse()
        if include_optional:
            return GetAllPolicyViolationsResponse(
                pagination = onelens_backend_client.models.pagination_fields.PaginationFields(
                    total_items = 56, 
                    total_pages = 56, 
                    current_page = 56, 
                    page_size = 56, ),
                policy_violations = [
                    onelens_backend_client.models.get_single_policy_violations_response.GetSinglePolicyViolationsResponse(
                        policy_id = '', 
                        policy_title = '', 
                        policy_labels = [
                            ''
                            ], 
                        policy_services = [
                            ''
                            ], 
                        potential_savings = 1.337, 
                        resources = 56, )
                    ]
            )
        else:
            return GetAllPolicyViolationsResponse(
                pagination = onelens_backend_client.models.pagination_fields.PaginationFields(
                    total_items = 56, 
                    total_pages = 56, 
                    current_page = 56, 
                    page_size = 56, ),
                policy_violations = [
                    onelens_backend_client.models.get_single_policy_violations_response.GetSinglePolicyViolationsResponse(
                        policy_id = '', 
                        policy_title = '', 
                        policy_labels = [
                            ''
                            ], 
                        policy_services = [
                            ''
                            ], 
                        potential_savings = 1.337, 
                        resources = 56, )
                    ],
        )
        """

    def testGetAllPolicyViolationsResponse(self):
        """Test GetAllPolicyViolationsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()