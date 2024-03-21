# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_policy_templates_request import GetPolicyTemplatesRequest

class TestGetPolicyTemplatesRequest(unittest.TestCase):
    """GetPolicyTemplatesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPolicyTemplatesRequest:
        """Test GetPolicyTemplatesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPolicyTemplatesRequest`
        """
        model = GetPolicyTemplatesRequest()
        if include_optional:
            return GetPolicyTemplatesRequest(
                pagination = onelens_backend_client.models.pagination_params.PaginationParams(
                    page = 56, 
                    page_size = 56, ),
                filters = onelens_backend_client.models.policy_template_filters.PolicyTemplateFilters(
                    search_query = '', 
                    parent_ptp_ids = [
                        ''
                        ], 
                    states = [
                        'DRAFT'
                        ], 
                    categories = [
                        'COST_SAVING'
                        ], 
                    providers = [
                        'AWS'
                        ], 
                    services = [
                        null
                        ], 
                    execution_types = [
                        'DETECTIVE'
                        ], )
            )
        else:
            return GetPolicyTemplatesRequest(
        )
        """

    def testGetPolicyTemplatesRequest(self):
        """Test GetPolicyTemplatesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
