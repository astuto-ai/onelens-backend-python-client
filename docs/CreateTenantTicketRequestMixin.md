# CreateTenantTicketRequestMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_id** | **str** |  | [optional] 
**ticket_category** | [**TicketCategory**](TicketCategory.md) | Category of the ticket | 
**state** | [**TicketState**](TicketState.md) | State of the ticket | 
**entity_id** | **str** | The id of the resource experiencing policy violation. | 
**entity_type** | **str** | The type of the resource experiencing policy violation. | 
**assignment** | [**TicketAssignment**](TicketAssignment.md) | Assignment state of the ticket | 
**assigned_to** | **str** |  | [optional] 
**last_run_id** | **str** | Id of the last policy violation/anomaly run | 
**last_run_at** | **datetime** | Datetime of the last policy violation/anomaly run | 
**first_run_at** | **datetime** | Datetime of the first policy violation/anomaly run | 
**status** | [**Status**](Status.md) |  | 
**details** | [**Details**](Details.md) |  | 

## Example

```python
from onelens_backend_client.models.create_tenant_ticket_request_mixin import CreateTenantTicketRequestMixin

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantTicketRequestMixin from a JSON string
create_tenant_ticket_request_mixin_instance = CreateTenantTicketRequestMixin.from_json(json)
# print the JSON string representation of the object
print(CreateTenantTicketRequestMixin.to_json())

# convert the object into a dict
create_tenant_ticket_request_mixin_dict = create_tenant_ticket_request_mixin_instance.to_dict()
# create an instance of CreateTenantTicketRequestMixin from a dict
create_tenant_ticket_request_mixin_form_dict = create_tenant_ticket_request_mixin.from_dict(create_tenant_ticket_request_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


