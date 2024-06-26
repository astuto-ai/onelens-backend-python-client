# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.data_retriever_response import DataRetrieverResponse

class TestDataRetrieverResponse(unittest.TestCase):
    """DataRetrieverResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataRetrieverResponse:
        """Test DataRetrieverResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataRetrieverResponse`
        """
        model = DataRetrieverResponse()
        if include_optional:
            return DataRetrieverResponse(
                query = onelens_backend_client.models.data_retriever_query.DataRetrieverQuery(
                    measures = [
                        ''
                        ], 
                    dimensions = [
                        ''
                        ], 
                    filters = [
                        onelens_backend_client.models.query_filters.QueryFilters(
                            dimension = '', 
                            operator = '', 
                            values = [
                                ''
                                ], )
                        ], 
                    time_dimensions = [
                        onelens_backend_client.models.time_dimension.TimeDimension(
                            dimension = '', 
                            date_range = [
                                ''
                                ], 
                            compare_date_range = [
                                null
                                ], 
                            granularity = '', )
                        ], 
                    segments = [
                        ''
                        ], 
                    limit = 56, 
                    total = True, 
                    offset = 56, 
                    order = [
                        'asc'
                        ], 
                    timezone = '', 
                    renew_query = True, 
                    ungrouped = True, ),
                data = [
                    None
                    ],
                annotation = None,
                last_refresh_time = '',
                data_source = '',
                db_type = '',
                ext_db_type = '',
                external = True,
                slow_query = True,
                total = 56
            )
        else:
            return DataRetrieverResponse(
                query = onelens_backend_client.models.data_retriever_query.DataRetrieverQuery(
                    measures = [
                        ''
                        ], 
                    dimensions = [
                        ''
                        ], 
                    filters = [
                        onelens_backend_client.models.query_filters.QueryFilters(
                            dimension = '', 
                            operator = '', 
                            values = [
                                ''
                                ], )
                        ], 
                    time_dimensions = [
                        onelens_backend_client.models.time_dimension.TimeDimension(
                            dimension = '', 
                            date_range = [
                                ''
                                ], 
                            compare_date_range = [
                                null
                                ], 
                            granularity = '', )
                        ], 
                    segments = [
                        ''
                        ], 
                    limit = 56, 
                    total = True, 
                    offset = 56, 
                    order = [
                        'asc'
                        ], 
                    timezone = '', 
                    renew_query = True, 
                    ungrouped = True, ),
        )
        """

    def testDataRetrieverResponse(self):
        """Test DataRetrieverResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
