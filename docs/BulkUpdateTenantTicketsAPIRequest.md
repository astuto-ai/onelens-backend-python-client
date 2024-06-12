# BulkUpdateTenantTicketsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_ids** | **List[str]** | List of ticket ids | [optional] [default to []]
**status** | [**PolicyTicketStatus**](PolicyTicketStatus.md) |  | [optional] 
**assignment** | **str** |  | [optional] 
**assigned_to** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.bulk_update_tenant_tickets_api_request import BulkUpdateTenantTicketsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateTenantTicketsAPIRequest from a JSON string
bulk_update_tenant_tickets_api_request_instance = BulkUpdateTenantTicketsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateTenantTicketsAPIRequest.to_json())

# convert the object into a dict
bulk_update_tenant_tickets_api_request_dict = bulk_update_tenant_tickets_api_request_instance.to_dict()
# create an instance of BulkUpdateTenantTicketsAPIRequest from a dict
bulk_update_tenant_tickets_api_request_form_dict = bulk_update_tenant_tickets_api_request.from_dict(bulk_update_tenant_tickets_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


