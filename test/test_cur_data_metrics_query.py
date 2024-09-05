# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.cur_data_metrics_query import CURDataMetricsQuery

class TestCURDataMetricsQuery(unittest.TestCase):
    """CURDataMetricsQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CURDataMetricsQuery:
        """Test CURDataMetricsQuery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CURDataMetricsQuery`
        """
        model = CURDataMetricsQuery()
        if include_optional:
            return CURDataMetricsQuery(
                name = '',
                dimension = '',
                measures = [
                    'sum_unblended_cost'
                    ],
                filters = [
                    onelens_backend_client.models.filter_criteria.FilterCriteria(
                        field = '', 
                        operator = 'equals', 
                        values = null, )
                    ],
                time_filter = onelens_backend_client.models.time_dimension.TimeDimension(
                    range = [
                        ''
                        ], 
                    granularity = onelens_backend_client.models.granularity.Granularity(
                        unit = 'days', 
                        value = 56, ), ),
                timezone = 'Asia/Kolkata'
            )
        else:
            return CURDataMetricsQuery(
                name = '',
                measures = [
                    'sum_unblended_cost'
                    ],
                filters = [
                    onelens_backend_client.models.filter_criteria.FilterCriteria(
                        field = '', 
                        operator = 'equals', 
                        values = null, )
                    ],
                time_filter = onelens_backend_client.models.time_dimension.TimeDimension(
                    range = [
                        ''
                        ], 
                    granularity = onelens_backend_client.models.granularity.Granularity(
                        unit = 'days', 
                        value = 56, ), ),
        )
        """

    def testCURDataMetricsQuery(self):
        """Test CURDataMetricsQuery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()