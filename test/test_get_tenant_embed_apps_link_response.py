# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_tenant_embed_apps_link_response import GetTenantEmbedAppsLinkResponse

class TestGetTenantEmbedAppsLinkResponse(unittest.TestCase):
    """GetTenantEmbedAppsLinkResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTenantEmbedAppsLinkResponse:
        """Test GetTenantEmbedAppsLinkResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTenantEmbedAppsLinkResponse`
        """
        model = GetTenantEmbedAppsLinkResponse()
        if include_optional:
            return GetTenantEmbedAppsLinkResponse(
                created_by = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by = '',
                tab_name = '',
                link = '',
                system_created = True,
                state = 'ACTIVE',
                id = ''
            )
        else:
            return GetTenantEmbedAppsLinkResponse(
                created_by = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tab_name = '',
                link = '',
                state = 'ACTIVE',
                id = '',
        )
        """

    def testGetTenantEmbedAppsLinkResponse(self):
        """Test GetTenantEmbedAppsLinkResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
