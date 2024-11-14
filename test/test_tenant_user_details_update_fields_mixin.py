# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.tenant_user_details_update_fields_mixin import (
    TenantUserDetailsUpdateFieldsMixin,
)


class TestTenantUserDetailsUpdateFieldsMixin(unittest.TestCase):
    """TenantUserDetailsUpdateFieldsMixin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantUserDetailsUpdateFieldsMixin:
        """Test TenantUserDetailsUpdateFieldsMixin
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TenantUserDetailsUpdateFieldsMixin`
        """
        model = TenantUserDetailsUpdateFieldsMixin()
        if include_optional:
            return TenantUserDetailsUpdateFieldsMixin(
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
                display_time_format = ''
            )
        else:
            return TenantUserDetailsUpdateFieldsMixin(
        )
        """

    def testTenantUserDetailsUpdateFieldsMixin(self):
        """Test TenantUserDetailsUpdateFieldsMixin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
