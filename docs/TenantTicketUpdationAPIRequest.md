# TenantTicketUpdationAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_ticket_details** | [**List[TenantTicketUpdationRequest]**](TenantTicketUpdationRequest.md) | Request payload for ticket updation | 

## Example

```python
from onelens_backend_client.models.tenant_ticket_updation_api_request import TenantTicketUpdationAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTicketUpdationAPIRequest from a JSON string
tenant_ticket_updation_api_request_instance = TenantTicketUpdationAPIRequest.from_json(json)
# print the JSON string representation of the object
print(TenantTicketUpdationAPIRequest.to_json())

# convert the object into a dict
tenant_ticket_updation_api_request_dict = tenant_ticket_updation_api_request_instance.to_dict()
# create an instance of TenantTicketUpdationAPIRequest from a dict
tenant_ticket_updation_api_request_form_dict = tenant_ticket_updation_api_request.from_dict(tenant_ticket_updation_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


