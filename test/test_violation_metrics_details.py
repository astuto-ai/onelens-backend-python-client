# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.violation_metrics_details import (
    ViolationMetricsDetails,
)


class TestViolationMetricsDetails(unittest.TestCase):
    """ViolationMetricsDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ViolationMetricsDetails:
        """Test ViolationMetricsDetails
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ViolationMetricsDetails`
        """
        model = ViolationMetricsDetails()
        if include_optional:
            return ViolationMetricsDetails(
                chart_title = '',
                chart_type = '',
                table_name = '',
                metric_name = '',
                aggregation_type = 'p99_maximum',
                look_back_period = onelens_backend_client.models.metrics_look_back_period.MetricsLookBackPeriod(
                    value_from = '', 
                    value = null, ),
                threshold = onelens_backend_client.models.metrics_threshold.MetricsThreshold(
                    value_from = '', 
                    value = null, ),
                query = onelens_backend_client.models.metrics_query.MetricsQuery(
                    name = '', 
                    metric_name = '', 
                    measures = [
                        'p99_maximum'
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
                    timezone = 'Asia/Kolkata', )
            )
        else:
            return ViolationMetricsDetails(
                chart_title = '',
                chart_type = '',
                table_name = '',
                metric_name = '',
                aggregation_type = 'p99_maximum',
                look_back_period = onelens_backend_client.models.metrics_look_back_period.MetricsLookBackPeriod(
                    value_from = '', 
                    value = null, ),
                query = onelens_backend_client.models.metrics_query.MetricsQuery(
                    name = '', 
                    metric_name = '', 
                    measures = [
                        'p99_maximum'
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
                    timezone = 'Asia/Kolkata', ),
        )
        """

    def testViolationMetricsDetails(self):
        """Test ViolationMetricsDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
