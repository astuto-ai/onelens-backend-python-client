# UpdateTenantTicketRequestMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** | The unique identifier of the ticket | 
**status** | [**Status**](Status.md) |  | 
**details** | [**Details1**](Details1.md) |  | 
**cost_impact** | **float** |  | [optional] 
**last_run_id** | **str** |  | [optional] 
**last_run_at** | **datetime** |  | [optional] 

## Example

```python
from onelens_backend_client.models.update_tenant_ticket_request_mixin import UpdateTenantTicketRequestMixin

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantTicketRequestMixin from a JSON string
update_tenant_ticket_request_mixin_instance = UpdateTenantTicketRequestMixin.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantTicketRequestMixin.to_json())

# convert the object into a dict
update_tenant_ticket_request_mixin_dict = update_tenant_ticket_request_mixin_instance.to_dict()
# create an instance of UpdateTenantTicketRequestMixin from a dict
update_tenant_ticket_request_mixin_form_dict = update_tenant_ticket_request_mixin.from_dict(update_tenant_ticket_request_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


