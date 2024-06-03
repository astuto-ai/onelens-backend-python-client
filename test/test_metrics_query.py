# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.metrics_query import MetricsQuery

class TestMetricsQuery(unittest.TestCase):
    """MetricsQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetricsQuery:
        """Test MetricsQuery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricsQuery`
        """
        model = MetricsQuery()
        if include_optional:
            return MetricsQuery(
                name = '',
                metric_name = '',
                measures = [
                    ''
                    ],
                filters = [
                    onelens_backend_client.models.filter_criteria.FilterCriteria(
                        field = '', 
                        operator = '', 
                        values = null, )
                    ],
                time_filter = onelens_backend_client.models.time_dimension.TimeDimension(
                    range = [
                        ''
                        ], 
                    granularity = null, ),
                timezone = 'Asia/Kolkata'
            )
        else:
            return MetricsQuery(
                name = '',
                metric_name = '',
                measures = [
                    ''
                    ],
                filters = [
                    onelens_backend_client.models.filter_criteria.FilterCriteria(
                        field = '', 
                        operator = '', 
                        values = null, )
                    ],
                time_filter = onelens_backend_client.models.time_dimension.TimeDimension(
                    range = [
                        ''
                        ], 
                    granularity = null, ),
        )
        """

    def testMetricsQuery(self):
        """Test MetricsQuery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
