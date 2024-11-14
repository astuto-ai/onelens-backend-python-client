# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.api.policy_template_service_api import (
    PolicyTemplateServiceApi,
)


class TestPolicyTemplateServiceApi(unittest.TestCase):
    """PolicyTemplateServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PolicyTemplateServiceApi()

    def tearDown(self) -> None:
        pass

    def test_activate_policy_template(self) -> None:
        """Test case for activate_policy_template

        Deprecate a policy template.
        """
        pass

    def test_create_policy_template(self) -> None:
        """Test case for create_policy_template

        Creates a new policy template.
        """
        pass

    def test_deactivate_policy_template(self) -> None:
        """Test case for deactivate_policy_template

        Deprecate a policy template.
        """
        pass

    def test_deprecate_policy_template(self) -> None:
        """Test case for deprecate_policy_template

        Deprecate a policy template.
        """
        pass

    def test_get_policy_template_by_id(self) -> None:
        """Test case for get_policy_template_by_id

        Retrieves a policy template by its unique identifier.
        """
        pass

    def test_get_policy_templates(self) -> None:
        """Test case for get_policy_templates

        Retrieves all policy templates, optionally filtered by the parameters in the request.
        """
        pass

    def test_update_policy_template(self) -> None:
        """Test case for update_policy_template

        Updates an existing policy template.
        """
        pass


if __name__ == "__main__":
    unittest.main()
