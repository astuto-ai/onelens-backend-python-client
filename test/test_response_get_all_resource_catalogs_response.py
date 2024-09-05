# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.response_get_all_resource_catalogs_response import ResponseGetAllResourceCatalogsResponse

class TestResponseGetAllResourceCatalogsResponse(unittest.TestCase):
    """ResponseGetAllResourceCatalogsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseGetAllResourceCatalogsResponse:
        """Test ResponseGetAllResourceCatalogsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseGetAllResourceCatalogsResponse`
        """
        model = ResponseGetAllResourceCatalogsResponse()
        if include_optional:
            return ResponseGetAllResourceCatalogsResponse(
                data = onelens_backend_client.models.get_all_resource_catalogs_response.GetAllResourceCatalogsResponse(
                    pagination = null, 
                    resources = [
                        onelens_backend_client.models.resource_catalog.ResourceCatalog(
                            ol_id = '', 
                            cloud_id = '', 
                            region = '', 
                            service = '', 
                            service_display_name = '', 
                            resource_type = '', 
                            resource_id = '', 
                            resource_url_template = '', 
                            crn = '', 
                            title = '', 
                            provider = '', 
                            status = '', 
                            tags = onelens_backend_client.models.tags.tags(), 
                            additional_info = onelens_backend_client.models.additional_info.Additional Info(), 
                            run_id = '', 
                            last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            account_name = '', 
                            tagged_resource = True, )
                        ], 
                    status = null, 
                    ambiguous_values = [
                        ''
                        ], 
                    navira_log_id = '', ),
                message = ''
            )
        else:
            return ResponseGetAllResourceCatalogsResponse(
                data = onelens_backend_client.models.get_all_resource_catalogs_response.GetAllResourceCatalogsResponse(
                    pagination = null, 
                    resources = [
                        onelens_backend_client.models.resource_catalog.ResourceCatalog(
                            ol_id = '', 
                            cloud_id = '', 
                            region = '', 
                            service = '', 
                            service_display_name = '', 
                            resource_type = '', 
                            resource_id = '', 
                            resource_url_template = '', 
                            crn = '', 
                            title = '', 
                            provider = '', 
                            status = '', 
                            tags = onelens_backend_client.models.tags.tags(), 
                            additional_info = onelens_backend_client.models.additional_info.Additional Info(), 
                            run_id = '', 
                            last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            account_name = '', 
                            tagged_resource = True, )
                        ], 
                    status = null, 
                    ambiguous_values = [
                        ''
                        ], 
                    navira_log_id = '', ),
        )
        """

    def testResponseGetAllResourceCatalogsResponse(self):
        """Test ResponseGetAllResourceCatalogsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()