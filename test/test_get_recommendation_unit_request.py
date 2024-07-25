# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_recommendation_unit_request import GetRecommendationUnitRequest

class TestGetRecommendationUnitRequest(unittest.TestCase):
    """GetRecommendationUnitRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetRecommendationUnitRequest:
        """Test GetRecommendationUnitRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRecommendationUnitRequest`
        """
        model = GetRecommendationUnitRequest()
        if include_optional:
            return GetRecommendationUnitRequest(
                pagination = onelens_backend_client.models.pagination_params.PaginationParams(
                    page = 56, 
                    page_size = 56, ),
                filters = onelens_backend_client.models.recommendation_unit_filters.RecommendationUnitFilters(
                    search_query = '', 
                    ids = [
                        ''
                        ], 
                    services = [
                        ''
                        ], 
                    action_type_ids = [
                        56
                        ], 
                    priorities = [
                        56
                        ], 
                    efforts = [
                        'Easy'
                        ], )
            )
        else:
            return GetRecommendationUnitRequest(
        )
        """

    def testGetRecommendationUnitRequest(self):
        """Test GetRecommendationUnitRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
