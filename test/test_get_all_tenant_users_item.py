# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_all_tenant_users_item import GetAllTenantUsersItem

class TestGetAllTenantUsersItem(unittest.TestCase):
    """GetAllTenantUsersItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllTenantUsersItem:
        """Test GetAllTenantUsersItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllTenantUsersItem`
        """
        model = GetAllTenantUsersItem()
        if include_optional:
            return GetAllTenantUsersItem(
                profile_pic_url = None,
                last_login = None,
                first_name = None,
                middle_name = None,
                last_name = None,
                email = None,
                mobile_country_code = None,
                mobile_number = None,
                persona = None,
                role = 'ADMIN',
                job_title = None,
                manager = None,
                city = None,
                state = None,
                country = None,
                display_language = None,
                preferred_currency = None,
                timezone = None,
                display_date_format = None,
                display_time_format = None,
                status = 'ACTIVE',
                sources = None,
                ol_user_id = None
            )
        else:
            return GetAllTenantUsersItem(
                first_name = None,
                last_name = None,
                ol_user_id = None,
        )
        """

    def testGetAllTenantUsersItem(self):
        """Test GetAllTenantUsersItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
