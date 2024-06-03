# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_recommendation_unit_by_id_response import GetRecommendationUnitByIdResponse

class TestGetRecommendationUnitByIdResponse(unittest.TestCase):
    """GetRecommendationUnitByIdResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetRecommendationUnitByIdResponse:
        """Test GetRecommendationUnitByIdResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRecommendationUnitByIdResponse`
        """
        model = GetRecommendationUnitByIdResponse()
        if include_optional:
            return GetRecommendationUnitByIdResponse(
                recommendation_unit = onelens_backend_client.models.service_config.ServiceConfig(
                    service = '', 
                    id = '', 
                    action_type_id = 56, 
                    priority = 56, 
                    title = '', 
                    subtitle = '', 
                    description = '', 
                    effort = 'Easy', 
                    query_details = onelens_backend_client.models.query_details.QueryDetails(
                        derived_variables = [
                            onelens_backend_client.models.derived_variable.DerivedVariable(
                                key = '', 
                                value_type = '', 
                                source_key = '', )
                            ], 
                        query = '', ), )
            )
        else:
            return GetRecommendationUnitByIdResponse(
                recommendation_unit = onelens_backend_client.models.service_config.ServiceConfig(
                    service = '', 
                    id = '', 
                    action_type_id = 56, 
                    priority = 56, 
                    title = '', 
                    subtitle = '', 
                    description = '', 
                    effort = 'Easy', 
                    query_details = onelens_backend_client.models.query_details.QueryDetails(
                        derived_variables = [
                            onelens_backend_client.models.derived_variable.DerivedVariable(
                                key = '', 
                                value_type = '', 
                                source_key = '', )
                            ], 
                        query = '', ), ),
        )
        """

    def testGetRecommendationUnitByIdResponse(self):
        """Test GetRecommendationUnitByIdResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
