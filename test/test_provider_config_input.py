# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.provider_config_input import ProviderConfigInput

class TestProviderConfigInput(unittest.TestCase):
    """ProviderConfigInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProviderConfigInput:
        """Test ProviderConfigInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProviderConfigInput`
        """
        model = ProviderConfigInput()
        if include_optional:
            return ProviderConfigInput(
                regions = onelens_backend_client.models.regions.regions(),
                role_name = '',
                cur_bucket_config = onelens_backend_client.models.cur_bucket_config.CurBucketConfig(
                    name = '', 
                    role = '', 
                    path = '', 
                    version = 'v1', 
                    status = 'INITIALISED', )
            )
        else:
            return ProviderConfigInput(
        )
        """

    def testProviderConfigInput(self):
        """Test ProviderConfigInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()