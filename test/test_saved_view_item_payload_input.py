# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.saved_view_item_payload_input import (
    SavedViewItemPayloadInput,
)


class TestSavedViewItemPayloadInput(unittest.TestCase):
    """SavedViewItemPayloadInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SavedViewItemPayloadInput:
        """Test SavedViewItemPayloadInput
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SavedViewItemPayloadInput`
        """
        model = SavedViewItemPayloadInput()
        if include_optional:
            return SavedViewItemPayloadInput(
                filters = None,
                sort_criteria = None,
                pagination = None,
                selected_fields = None
            )
        else:
            return SavedViewItemPayloadInput(
        )
        """

    def testSavedViewItemPayloadInput(self):
        """Test SavedViewItemPayloadInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
