# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.response_get_policy_template_pack_by_id_response import (
    ResponseGetPolicyTemplatePackByIdResponse,
)


class TestResponseGetPolicyTemplatePackByIdResponse(unittest.TestCase):
    """ResponseGetPolicyTemplatePackByIdResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> ResponseGetPolicyTemplatePackByIdResponse:
        """Test ResponseGetPolicyTemplatePackByIdResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ResponseGetPolicyTemplatePackByIdResponse`
        """
        model = ResponseGetPolicyTemplatePackByIdResponse()
        if include_optional:
            return ResponseGetPolicyTemplatePackByIdResponse(
                data = onelens_backend_client.models.get_policy_template_pack_by_id_response.GetPolicyTemplatePackByIdResponse(
                    alias = '', 
                    category = null, 
                    provider = null, 
                    details = null, 
                    id = '', 
                    state = null, ),
                message = ''
            )
        else:
            return ResponseGetPolicyTemplatePackByIdResponse(
                data = onelens_backend_client.models.get_policy_template_pack_by_id_response.GetPolicyTemplatePackByIdResponse(
                    alias = '', 
                    category = null, 
                    provider = null, 
                    details = null, 
                    id = '', 
                    state = null, ),
        )
        """

    def testResponseGetPolicyTemplatePackByIdResponse(self):
        """Test ResponseGetPolicyTemplatePackByIdResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
