# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.sync_recommendation_unit_from_repo_request import (
    SyncRecommendationUnitFromRepoRequest,
)


class TestSyncRecommendationUnitFromRepoRequest(unittest.TestCase):
    """SyncRecommendationUnitFromRepoRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyncRecommendationUnitFromRepoRequest:
        """Test SyncRecommendationUnitFromRepoRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SyncRecommendationUnitFromRepoRequest`
        """
        model = SyncRecommendationUnitFromRepoRequest()
        if include_optional:
            return SyncRecommendationUnitFromRepoRequest(
                id = ''
            )
        else:
            return SyncRecommendationUnitFromRepoRequest(
                id = '',
        )
        """

    def testSyncRecommendationUnitFromRepoRequest(self):
        """Test SyncRecommendationUnitFromRepoRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
