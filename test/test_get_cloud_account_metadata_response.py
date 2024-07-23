# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_cloud_account_metadata_response import GetCloudAccountMetadataResponse

class TestGetCloudAccountMetadataResponse(unittest.TestCase):
    """GetCloudAccountMetadataResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCloudAccountMetadataResponse:
        """Test GetCloudAccountMetadataResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCloudAccountMetadataResponse`
        """
        model = GetCloudAccountMetadataResponse()
        if include_optional:
            return GetCloudAccountMetadataResponse(
                cloud_accounts_metadata = [
                    onelens_backend_client.models.cloud_account_metadata.CloudAccountMetadata(
                        ol_id = '', 
                        account_aliases = [
                            ''
                            ], 
                        organization_available_policy_types = [
                            None
                            ], 
                        akas = [
                            ''
                            ], 
                        organization_master_account_arn = '', 
                        organization_master_account_email = '', 
                        organization_master_account_id = '', 
                        region = '', 
                        account_name = '', 
                        cloud_id = '', 
                        cloud_provider = '', 
                        arn = '', 
                        organization_id = '', 
                        organization_arn = '', 
                        run_id = '', 
                        last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return GetCloudAccountMetadataResponse(
                cloud_accounts_metadata = [
                    onelens_backend_client.models.cloud_account_metadata.CloudAccountMetadata(
                        ol_id = '', 
                        account_aliases = [
                            ''
                            ], 
                        organization_available_policy_types = [
                            None
                            ], 
                        akas = [
                            ''
                            ], 
                        organization_master_account_arn = '', 
                        organization_master_account_email = '', 
                        organization_master_account_id = '', 
                        region = '', 
                        account_name = '', 
                        cloud_id = '', 
                        cloud_provider = '', 
                        arn = '', 
                        organization_id = '', 
                        organization_arn = '', 
                        run_id = '', 
                        last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testGetCloudAccountMetadataResponse(self):
        """Test GetCloudAccountMetadataResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
