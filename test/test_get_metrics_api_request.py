# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_metrics_api_request import GetMetricsAPIRequest

class TestGetMetricsAPIRequest(unittest.TestCase):
    """GetMetricsAPIRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMetricsAPIRequest:
        """Test GetMetricsAPIRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMetricsAPIRequest`
        """
        model = GetMetricsAPIRequest()
        if include_optional:
            return GetMetricsAPIRequest(
                query = onelens_backend_client.models.metrics_query.MetricsQuery(
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
                    timezone = 'Asia/Kolkata', )
            )
        else:
            return GetMetricsAPIRequest(
                query = onelens_backend_client.models.metrics_query.MetricsQuery(
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
                    timezone = 'Asia/Kolkata', ),
        )
        """

    def testGetMetricsAPIRequest(self):
        """Test GetMetricsAPIRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
