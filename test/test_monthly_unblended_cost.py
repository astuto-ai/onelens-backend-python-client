# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.monthly_unblended_cost import MonthlyUnblendedCost

class TestMonthlyUnblendedCost(unittest.TestCase):
    """MonthlyUnblendedCost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MonthlyUnblendedCost:
        """Test MonthlyUnblendedCost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MonthlyUnblendedCost`
        """
        model = MonthlyUnblendedCost()
        if include_optional:
            return MonthlyUnblendedCost(
            )
        else:
            return MonthlyUnblendedCost(
        )
        """

    def testMonthlyUnblendedCost(self):
        """Test MonthlyUnblendedCost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()