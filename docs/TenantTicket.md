# TenantTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Datetime of ticket creation | 
**updated_at** | **datetime** | Datetime of ticket updation | 
**monitor_id** | **str** | Violation monitor id | 
**ticket_category** | [**TicketCategory**](TicketCategory.md) | Category of the ticket | 
**system_state** | [**TicketSystemState**](TicketSystemState.md) | System state of the ticket | 
**user_state** | [**TicketUserState**](TicketUserState.md) | User state of the ticket | 
**details** | [**TicketDetails**](TicketDetails.md) | Details of the ticket | [optional] 
**id** | **str** | The unique identifier of the ticket | 

## Example

```python
from onelens_backend_client.models.tenant_ticket import TenantTicket

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTicket from a JSON string
tenant_ticket_instance = TenantTicket.from_json(json)
# print the JSON string representation of the object
print(TenantTicket.to_json())

# convert the object into a dict
tenant_ticket_dict = tenant_ticket_instance.to_dict()
# create an instance of TenantTicket from a dict
tenant_ticket_form_dict = tenant_ticket.from_dict(tenant_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


