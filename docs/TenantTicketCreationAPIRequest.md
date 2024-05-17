# TenantTicketCreationAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_ticket_details** | [**List[TenantTicketCreationRequest]**](TenantTicketCreationRequest.md) | Request payload for ticket creation | 

## Example

```python
from onelens_backend_client.models.tenant_ticket_creation_api_request import TenantTicketCreationAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTicketCreationAPIRequest from a JSON string
tenant_ticket_creation_api_request_instance = TenantTicketCreationAPIRequest.from_json(json)
# print the JSON string representation of the object
print(TenantTicketCreationAPIRequest.to_json())

# convert the object into a dict
tenant_ticket_creation_api_request_dict = tenant_ticket_creation_api_request_instance.to_dict()
# create an instance of TenantTicketCreationAPIRequest from a dict
tenant_ticket_creation_api_request_form_dict = tenant_ticket_creation_api_request.from_dict(tenant_ticket_creation_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


