# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.sync_recommendation_unit_from_repo_response import SyncRecommendationUnitFromRepoResponse

class TestSyncRecommendationUnitFromRepoResponse(unittest.TestCase):
    """SyncRecommendationUnitFromRepoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyncRecommendationUnitFromRepoResponse:
        """Test SyncRecommendationUnitFromRepoResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyncRecommendationUnitFromRepoResponse`
        """
        model = SyncRecommendationUnitFromRepoResponse()
        if include_optional:
            return SyncRecommendationUnitFromRepoResponse(
                id = ''
            )
        else:
            return SyncRecommendationUnitFromRepoResponse(
                id = '',
        )
        """

    def testSyncRecommendationUnitFromRepoResponse(self):
        """Test SyncRecommendationUnitFromRepoResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()