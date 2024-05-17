# TenantTicketUpdationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** | The unique identifier of the ticket | 
**system_state** | [**TicketSystemState**](TicketSystemState.md) | System state of the ticket | 
**user_state** | [**TicketUserState**](TicketUserState.md) | User state of the ticket | 

## Example

```python
from onelens_backend_client.models.tenant_ticket_updation_request import TenantTicketUpdationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTicketUpdationRequest from a JSON string
tenant_ticket_updation_request_instance = TenantTicketUpdationRequest.from_json(json)
# print the JSON string representation of the object
print(TenantTicketUpdationRequest.to_json())

# convert the object into a dict
tenant_ticket_updation_request_dict = tenant_ticket_updation_request_instance.to_dict()
# create an instance of TenantTicketUpdationRequest from a dict
tenant_ticket_updation_request_form_dict = tenant_ticket_updation_request.from_dict(tenant_ticket_updation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


