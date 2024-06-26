# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.override_tenant_policy_exclusions_request import OverrideTenantPolicyExclusionsRequest

class TestOverrideTenantPolicyExclusionsRequest(unittest.TestCase):
    """OverrideTenantPolicyExclusionsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OverrideTenantPolicyExclusionsRequest:
        """Test OverrideTenantPolicyExclusionsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OverrideTenantPolicyExclusionsRequest`
        """
        model = OverrideTenantPolicyExclusionsRequest()
        if include_optional:
            return OverrideTenantPolicyExclusionsRequest(
                exclusions = onelens_backend_client.models.tenant_policy_exclusions.TenantPolicyExclusions(
                    resource_ids = [
                        ''
                        ], ),
                tenant_id = '',
                policy_id = ''
            )
        else:
            return OverrideTenantPolicyExclusionsRequest(
                exclusions = onelens_backend_client.models.tenant_policy_exclusions.TenantPolicyExclusions(
                    resource_ids = [
                        ''
                        ], ),
                tenant_id = '',
                policy_id = '',
        )
        """

    def testOverrideTenantPolicyExclusionsRequest(self):
        """Test OverrideTenantPolicyExclusionsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
