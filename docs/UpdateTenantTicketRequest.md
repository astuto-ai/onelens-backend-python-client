# UpdateTenantTicketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status1**](Status1.md) |  | [optional] 
**assignment** | [**TicketAssignment**](TicketAssignment.md) |  | [optional] 
**details** | [**Details2**](Details2.md) |  | [optional] 
**resource_attributes** | **object** |  | [optional] 
**ticket_id** | **str** | The unique identifier of the ticket | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.update_tenant_ticket_request import UpdateTenantTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantTicketRequest from a JSON string
update_tenant_ticket_request_instance = UpdateTenantTicketRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantTicketRequest.to_json())

# convert the object into a dict
update_tenant_ticket_request_dict = update_tenant_ticket_request_instance.to_dict()
# create an instance of UpdateTenantTicketRequest from a dict
update_tenant_ticket_request_form_dict = update_tenant_ticket_request.from_dict(update_tenant_ticket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


