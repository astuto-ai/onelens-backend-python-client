# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.granularity_output import GranularityOutput

class TestGranularityOutput(unittest.TestCase):
    """GranularityOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GranularityOutput:
        """Test GranularityOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GranularityOutput`
        """
        model = GranularityOutput()
        if include_optional:
            return GranularityOutput(
                unit = 'minutes',
                value = 56
            )
        else:
            return GranularityOutput(
                unit = 'minutes',
                value = 56,
        )
        """

    def testGranularityOutput(self):
        """Test GranularityOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
