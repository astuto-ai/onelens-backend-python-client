# UpdateTenantTicketAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status1**](Status1.md) |  | [optional] 
**assignment** | [**TicketAssignment**](TicketAssignment.md) |  | [optional] 
**details** | [**Details2**](Details2.md) |  | [optional] 
**entity_attributes** | **object** |  | [optional] 
**monthly_unblended_cost** | [**MonthlyUnblendedCost1**](MonthlyUnblendedCost1.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.update_tenant_ticket_api_request import UpdateTenantTicketAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantTicketAPIRequest from a JSON string
update_tenant_ticket_api_request_instance = UpdateTenantTicketAPIRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantTicketAPIRequest.to_json())

# convert the object into a dict
update_tenant_ticket_api_request_dict = update_tenant_ticket_api_request_instance.to_dict()
# create an instance of UpdateTenantTicketAPIRequest from a dict
update_tenant_ticket_api_request_form_dict = update_tenant_ticket_api_request.from_dict(update_tenant_ticket_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


