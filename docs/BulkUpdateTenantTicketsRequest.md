# BulkUpdateTenantTicketsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_ids** | **List[str]** | List of ticket ids | [optional] [default to []]
**status** | [**PolicyTicketStatus**](PolicyTicketStatus.md) |  | [optional] 
**assignment** | **str** |  | [optional] 
**assigned_to** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.bulk_update_tenant_tickets_request import BulkUpdateTenantTicketsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateTenantTicketsRequest from a JSON string
bulk_update_tenant_tickets_request_instance = BulkUpdateTenantTicketsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateTenantTicketsRequest.to_json())

# convert the object into a dict
bulk_update_tenant_tickets_request_dict = bulk_update_tenant_tickets_request_instance.to_dict()
# create an instance of BulkUpdateTenantTicketsRequest from a dict
bulk_update_tenant_tickets_request_form_dict = bulk_update_tenant_tickets_request.from_dict(bulk_update_tenant_tickets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


