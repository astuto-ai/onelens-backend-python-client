# ResponseGetTenantsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTenantsResponse**](GetTenantsResponse.md) |  | 
**message** | [**Message**](Message.md) |  | 

## Example

```python
from onelens_backend_client.models.response_get_tenants_response import ResponseGetTenantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTenantsResponse from a JSON string
response_get_tenants_response_instance = ResponseGetTenantsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTenantsResponse.to_json())

# convert the object into a dict
response_get_tenants_response_dict = response_get_tenants_response_instance.to_dict()
# create an instance of ResponseGetTenantsResponse from a dict
response_get_tenants_response_form_dict = response_get_tenants_response.from_dict(response_get_tenants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


