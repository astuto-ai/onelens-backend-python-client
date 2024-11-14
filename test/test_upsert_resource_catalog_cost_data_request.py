# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.models.upsert_resource_catalog_cost_data_request import (
    UpsertResourceCatalogCostDataRequest,
)


class TestUpsertResourceCatalogCostDataRequest(unittest.TestCase):
    """UpsertResourceCatalogCostDataRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpsertResourceCatalogCostDataRequest:
        """Test UpsertResourceCatalogCostDataRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UpsertResourceCatalogCostDataRequest`
        """
        model = UpsertResourceCatalogCostDataRequest()
        if include_optional:
            return UpsertResourceCatalogCostDataRequest(
                resource_catalog_cost_data = [
                    onelens_backend_client.models.resource_catalog_cost_data_mixin.ResourceCatalogCostDataMixin(
                        id = '', 
                        resource_id = '', 
                        start_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        granularity = null, 
                        unblended_cost = 1.337, 
                        blended_cost = 1.337, 
                        net_unblended_cost = 1.337, )
                    ],
                tenant_id = ''
            )
        else:
            return UpsertResourceCatalogCostDataRequest(
                resource_catalog_cost_data = [
                    onelens_backend_client.models.resource_catalog_cost_data_mixin.ResourceCatalogCostDataMixin(
                        id = '', 
                        resource_id = '', 
                        start_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_datetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        granularity = null, 
                        unblended_cost = 1.337, 
                        blended_cost = 1.337, 
                        net_unblended_cost = 1.337, )
                    ],
                tenant_id = '',
        )
        """

    def testUpsertResourceCatalogCostDataRequest(self):
        """Test UpsertResourceCatalogCostDataRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
