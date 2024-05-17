# UpdateTenantTicketUserStateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_state** | [**TicketUserState**](TicketUserState.md) | User state of the ticket | 
**ticket_id** | **str** | The unique identifier of the ticket | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.update_tenant_ticket_user_state_request import UpdateTenantTicketUserStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantTicketUserStateRequest from a JSON string
update_tenant_ticket_user_state_request_instance = UpdateTenantTicketUserStateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantTicketUserStateRequest.to_json())

# convert the object into a dict
update_tenant_ticket_user_state_request_dict = update_tenant_ticket_user_state_request_instance.to_dict()
# create an instance of UpdateTenantTicketUserStateRequest from a dict
update_tenant_ticket_user_state_request_form_dict = update_tenant_ticket_user_state_request.from_dict(update_tenant_ticket_user_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


