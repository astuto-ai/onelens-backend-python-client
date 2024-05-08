# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.update_organization_response import UpdateOrganizationResponse

class TestUpdateOrganizationResponse(unittest.TestCase):
    """UpdateOrganizationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateOrganizationResponse:
        """Test UpdateOrganizationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateOrganizationResponse`
        """
        model = UpdateOrganizationResponse()
        if include_optional:
            return UpdateOrganizationResponse(
                name = '',
                id = '',
                short_id = 56,
                status = 'ACTIVE',
                total_tenants = 56,
                country = '',
                industry = [
                    ''
                    ],
                monthly_cloud_spend = 56,
                cloud_service_providers = [
                    ''
                    ],
                website = '',
                changelogs = [
                    None
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                updated_by = ''
            )
        else:
            return UpdateOrganizationResponse(
                name = '',
                id = '',
                short_id = 56,
                status = 'ACTIVE',
                total_tenants = 56,
                country = '',
                industry = [
                    ''
                    ],
                monthly_cloud_spend = 56,
                cloud_service_providers = [
                    ''
                    ],
                website = '',
                changelogs = [
                    None
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                updated_by = '',
        )
        """

    def testUpdateOrganizationResponse(self):
        """Test UpdateOrganizationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
