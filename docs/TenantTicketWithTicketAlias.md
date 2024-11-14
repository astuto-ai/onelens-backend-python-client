# TenantTicketWithTicketAlias


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
**monthly_unblended_cost** | **float** |  | [optional] 
**assignment** | [**TicketAssignment**](TicketAssignment.md) | Assignment state of the ticket | 
**assigned_to** | **str** |  | [optional] 
**last_run_id** | **str** | Id of the last policy violation/anomaly run | 
**last_run_at** | **datetime** | Datetime of the last policy violation/anomaly run | 
**first_run_at** | **datetime** | Datetime of the first policy violation/anomaly run | 
**id** | **str** | The unique identifier of the ticket | 
**status** | [**Status**](Status.md) |  | 
**details** | [**Details1**](Details1.md) |  | 
**ticket_alias** | **str** |  | [optional] 
**trigger_id** | **str** | The unique identifier of the trigger that created the ticket | 

## Example

```python
from onelens_backend_client.models.tenant_ticket_with_ticket_alias import TenantTicketWithTicketAlias

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTicketWithTicketAlias from a JSON string
tenant_ticket_with_ticket_alias_instance = TenantTicketWithTicketAlias.from_json(json)
# print the JSON string representation of the object
print(TenantTicketWithTicketAlias.to_json())

# convert the object into a dict
tenant_ticket_with_ticket_alias_dict = tenant_ticket_with_ticket_alias_instance.to_dict()
# create an instance of TenantTicketWithTicketAlias from a dict
tenant_ticket_with_ticket_alias_form_dict = tenant_ticket_with_ticket_alias.from_dict(tenant_ticket_with_ticket_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


