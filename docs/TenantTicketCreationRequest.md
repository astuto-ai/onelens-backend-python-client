# TenantTicketCreationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_id** | **str** | Violation monitor id | 
**ticket_category** | [**TicketCategory**](TicketCategory.md) | Category of the ticket | 
**system_state** | [**TicketSystemState**](TicketSystemState.md) | System state of the ticket | 
**user_state** | [**TicketUserState**](TicketUserState.md) | User state of the ticket | 
**details** | [**TicketDetails**](TicketDetails.md) | Details of the ticket | [optional] 

## Example

```python
from onelens_backend_client.models.tenant_ticket_creation_request import TenantTicketCreationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTicketCreationRequest from a JSON string
tenant_ticket_creation_request_instance = TenantTicketCreationRequest.from_json(json)
# print the JSON string representation of the object
print(TenantTicketCreationRequest.to_json())

# convert the object into a dict
tenant_ticket_creation_request_dict = tenant_ticket_creation_request_instance.to_dict()
# create an instance of TenantTicketCreationRequest from a dict
tenant_ticket_creation_request_form_dict = tenant_ticket_creation_request.from_dict(tenant_ticket_creation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


