# TenantTicketUpdateUserStateAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_state** | [**TicketUserState**](TicketUserState.md) | User state of the ticket | 

## Example

```python
from onelens_backend_client.models.tenant_ticket_update_user_state_api_request import TenantTicketUpdateUserStateAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTicketUpdateUserStateAPIRequest from a JSON string
tenant_ticket_update_user_state_api_request_instance = TenantTicketUpdateUserStateAPIRequest.from_json(json)
# print the JSON string representation of the object
print(TenantTicketUpdateUserStateAPIRequest.to_json())

# convert the object into a dict
tenant_ticket_update_user_state_api_request_dict = tenant_ticket_update_user_state_api_request_instance.to_dict()
# create an instance of TenantTicketUpdateUserStateAPIRequest from a dict
tenant_ticket_update_user_state_api_request_form_dict = tenant_ticket_update_user_state_api_request.from_dict(tenant_ticket_update_user_state_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


