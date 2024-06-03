# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from onelens_backend_client.models.get_ticket_by_id_policy_details_response import GetTicketByIdPolicyDetailsResponse

class TestGetTicketByIdPolicyDetailsResponse(unittest.TestCase):
    """GetTicketByIdPolicyDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTicketByIdPolicyDetailsResponse:
        """Test GetTicketByIdPolicyDetailsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTicketByIdPolicyDetailsResponse`
        """
        model = GetTicketByIdPolicyDetailsResponse()
        if include_optional:
            return GetTicketByIdPolicyDetailsResponse(
                tenant_ticket = onelens_backend_client.models.tenant_ticket.TenantTicket(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    monitor_id = '', 
                    ticket_category = null, 
                    state = null, 
                    entity_id = '', 
                    entity_type = '', 
                    assignment = null, 
                    assigned_to = '', 
                    last_run_id = '', 
                    last_run_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    first_run_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    status = null, 
                    details = null, ),
                policy_details = onelens_backend_client.models.tenant_policy.TenantPolicy(
                    parent_ptp_id = '', 
                    title = '', 
                    alias = '', 
                    description = '', 
                    services = [
                        null
                        ], 
                    execution_type = null, 
                    details = null, 
                    description2 = '', 
                    resource_type = '', 
                    recommendation_details = null, 
                    policy_template_id = '', 
                    category = null, 
                    provider = null, 
                    id = '', ),
                recommendation_units = [
                    ''
                    ],
                hierarchy_details = onelens_backend_client.models.hierarchy_details.Hierarchy Details(),
                resource_details = onelens_backend_client.models.resource_details.Resource Details()
            )
        else:
            return GetTicketByIdPolicyDetailsResponse(
                tenant_ticket = onelens_backend_client.models.tenant_ticket.TenantTicket(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    monitor_id = '', 
                    ticket_category = null, 
                    state = null, 
                    entity_id = '', 
                    entity_type = '', 
                    assignment = null, 
                    assigned_to = '', 
                    last_run_id = '', 
                    last_run_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    first_run_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    status = null, 
                    details = null, ),
                policy_details = onelens_backend_client.models.tenant_policy.TenantPolicy(
                    parent_ptp_id = '', 
                    title = '', 
                    alias = '', 
                    description = '', 
                    services = [
                        null
                        ], 
                    execution_type = null, 
                    details = null, 
                    description2 = '', 
                    resource_type = '', 
                    recommendation_details = null, 
                    policy_template_id = '', 
                    category = null, 
                    provider = null, 
                    id = '', ),
                recommendation_units = [
                    ''
                    ],
                hierarchy_details = onelens_backend_client.models.hierarchy_details.Hierarchy Details(),
                resource_details = onelens_backend_client.models.resource_details.Resource Details(),
        )
        """

    def testGetTicketByIdPolicyDetailsResponse(self):
        """Test GetTicketByIdPolicyDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
