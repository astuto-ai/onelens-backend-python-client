# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.update_tenant_user_by_system_request import UpdateTenantUserBySystemRequest

class TestUpdateTenantUserBySystemRequest(unittest.TestCase):
    """UpdateTenantUserBySystemRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateTenantUserBySystemRequest:
        """Test UpdateTenantUserBySystemRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateTenantUserBySystemRequest`
        """
        model = UpdateTenantUserBySystemRequest()
        if include_optional:
            return UpdateTenantUserBySystemRequest(
                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                first_name = '',
                middle_name = '',
                last_name = '',
                mobile_country_code = '',
                mobile_number = '',
                persona = 'DevOps',
                job_title = '',
                manager = '',
                city = '',
                state = '',
                country = '',
                display_language = '',
                preferred_currency = '',
                timezone = '',
                display_date_format = '',
                display_time_format = '',
                ol_user_id = '',
                tenant_id = ''
            )
        else:
            return UpdateTenantUserBySystemRequest(
                ol_user_id = '',
                tenant_id = '',
        )
        """

    def testUpdateTenantUserBySystemRequest(self):
        """Test UpdateTenantUserBySystemRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()