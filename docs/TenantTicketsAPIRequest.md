# TenantTicketsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_ids** | **List[str]** | Unique identifiers for violation monitors for which  tickets are to be fetched. | 

## Example

```python
from onelens_backend_client.models.tenant_tickets_api_request import TenantTicketsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTicketsAPIRequest from a JSON string
tenant_tickets_api_request_instance = TenantTicketsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(TenantTicketsAPIRequest.to_json())

# convert the object into a dict
tenant_tickets_api_request_dict = tenant_tickets_api_request_instance.to_dict()
# create an instance of TenantTicketsAPIRequest from a dict
tenant_tickets_api_request_form_dict = tenant_tickets_api_request.from_dict(tenant_tickets_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


