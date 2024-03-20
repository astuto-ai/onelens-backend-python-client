# GetTenants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetTenantsRequest**](GetTenantsRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.get_tenants import GetTenants

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenants from a JSON string
get_tenants_instance = GetTenants.from_json(json)
# print the JSON string representation of the object
print(GetTenants.to_json())

# convert the object into a dict
get_tenants_dict = get_tenants_instance.to_dict()
# create an instance of GetTenants from a dict
get_tenants_form_dict = get_tenants.from_dict(get_tenants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


