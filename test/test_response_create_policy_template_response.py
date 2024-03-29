# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.response_create_policy_template_response import ResponseCreatePolicyTemplateResponse

class TestResponseCreatePolicyTemplateResponse(unittest.TestCase):
    """ResponseCreatePolicyTemplateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseCreatePolicyTemplateResponse:
        """Test ResponseCreatePolicyTemplateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseCreatePolicyTemplateResponse`
        """
        model = ResponseCreatePolicyTemplateResponse()
        if include_optional:
            return ResponseCreatePolicyTemplateResponse(
                data = onelens_backend_client.models.create_policy_template_response.CreatePolicyTemplateResponse(
                    parent_ptp_id = '', 
                    title = '', 
                    alias = '', 
                    description = '', 
                    services = [
                        null
                        ], 
                    execution_type = null, 
                    details = null, 
                    id = '', 
                    state = null, 
                    category = null, 
                    provider = null, ),
                message = ''
            )
        else:
            return ResponseCreatePolicyTemplateResponse(
                data = onelens_backend_client.models.create_policy_template_response.CreatePolicyTemplateResponse(
                    parent_ptp_id = '', 
                    title = '', 
                    alias = '', 
                    description = '', 
                    services = [
                        null
                        ], 
                    execution_type = null, 
                    details = null, 
                    id = '', 
                    state = null, 
                    category = null, 
                    provider = null, ),
        )
        """

    def testResponseCreatePolicyTemplateResponse(self):
        """Test ResponseCreatePolicyTemplateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
