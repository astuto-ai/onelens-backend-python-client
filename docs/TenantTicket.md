# TenantTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Datetime of ticket creation | 
**updated_at** | **datetime** | Datetime of ticket updation | 
**monitor_id** | **str** |  | [optional] 
**ticket_category** | [**TicketCategory**](TicketCategory.md) | Category of the ticket | 
**state** | [**TicketState**](TicketState.md) | State of the ticket | 
**entity_id** | **str** | The id of the resource experiencing policy violation. | 
**entity_type** | **str** | The type of the resource experiencing policy violation. | 
**entity_attributes** | **object** |  | [optional] 
**monthly_unblended_cost** | **str** |  | [optional] 
**assignment** | [**TicketAssignment**](TicketAssignment.md) | Assignment state of the ticket | 
**assigned_to** | **str** |  | [optional] 
**last_run_id** | **str** | Id of the last policy violation/anomaly run | 
**last_run_at** | **datetime** | Datetime of the last policy violation/anomaly run | 
**first_run_at** | **datetime** | Datetime of the first policy violation/anomaly run | 
**id** | **str** | The unique identifier of the ticket | 
**status** | [**Status**](Status.md) |  | 
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


