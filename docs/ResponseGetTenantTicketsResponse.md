# ResponseGetTenantTicketsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTenantTicketsResponse**](GetTenantTicketsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_tenant_tickets_response import ResponseGetTenantTicketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTenantTicketsResponse from a JSON string
response_get_tenant_tickets_response_instance = ResponseGetTenantTicketsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTenantTicketsResponse.to_json())

# convert the object into a dict
response_get_tenant_tickets_response_dict = response_get_tenant_tickets_response_instance.to_dict()
# create an instance of ResponseGetTenantTicketsResponse from a dict
response_get_tenant_tickets_response_form_dict = response_get_tenant_tickets_response.from_dict(response_get_tenant_tickets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


