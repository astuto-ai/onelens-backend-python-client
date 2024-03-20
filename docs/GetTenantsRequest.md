# GetTenantsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetTenantsRequest**](GetTenantsRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.get_tenants_request import GetTenantsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantsRequest from a JSON string
get_tenants_request_instance = GetTenantsRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantsRequest.to_json())

# convert the object into a dict
get_tenants_request_dict = get_tenants_request_instance.to_dict()
# create an instance of GetTenantsRequest from a dict
get_tenants_request_form_dict = get_tenants_request.from_dict(get_tenants_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


