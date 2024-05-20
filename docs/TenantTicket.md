# TenantTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Datetime of ticket creation | 
**updated_at** | **datetime** | Datetime of ticket updation | 
**ticket_category** | [**TicketCategory**](TicketCategory.md) | Category of the ticket | 
**state** | [**TicketState**](TicketState.md) | State of the ticket | 
**assignment** | [**TicketAssignment**](TicketAssignment.md) | Assignment state of the ticket | 
**id** | **str** | The unique identifier of the ticket | 
**status** | [**Status**](Status.md) |  | 
**monitor_id** | **str** |  | [optional] 
**heirarchy_node_id** | **str** |  | [optional] 
**assigned_to** | **str** |  | [optional] 
**details** | [**Details1**](Details1.md) |  | 

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


