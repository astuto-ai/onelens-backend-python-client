# ResponseCreateTenantTicketsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_create_tenant_tickets_response import ResponseCreateTenantTicketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreateTenantTicketsResponse from a JSON string
response_create_tenant_tickets_response_instance = ResponseCreateTenantTicketsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCreateTenantTicketsResponse.to_json())

# convert the object into a dict
response_create_tenant_tickets_response_dict = response_create_tenant_tickets_response_instance.to_dict()
# create an instance of ResponseCreateTenantTicketsResponse from a dict
response_create_tenant_tickets_response_form_dict = response_create_tenant_tickets_response.from_dict(response_create_tenant_tickets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


