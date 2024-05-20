# CreateTenantTicketRequestMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_category** | [**TicketCategory**](TicketCategory.md) | Category of the ticket | 
**state** | [**TicketState**](TicketState.md) | State of the ticket | 
**assignment** | [**TicketAssignment**](TicketAssignment.md) | Assignment state of the ticket | 
**monitor_id** | **str** |  | 
**status** | [**Status**](Status.md) |  | 
**heirarchy_node_id** | **str** |  | [optional] 
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


