# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.metrics_value_unit import MetricsValueUnit


class TestMetricsValueUnit(unittest.TestCase):
    """MetricsValueUnit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetricsValueUnit:
        """Test MetricsValueUnit
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `MetricsValueUnit`
        """
        model = MetricsValueUnit()
        if include_optional:
            return MetricsValueUnit(
                value = 56,
                unit = ''
            )
        else:
            return MetricsValueUnit(
                value = 56,
                unit = '',
        )
        """

    def testMetricsValueUnit(self):
        """Test MetricsValueUnit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
