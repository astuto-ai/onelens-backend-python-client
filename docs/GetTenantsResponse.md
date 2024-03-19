# GetTenantsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants_filter_data** | [**TenantsFilterData**](TenantsFilterData.md) |  | 

## Example

```python
from openapi_client.models.get_tenants_response import GetTenantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantsResponse from a JSON string
get_tenants_response_instance = GetTenantsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantsResponse.to_json())

# convert the object into a dict
get_tenants_response_dict = get_tenants_response_instance.to_dict()
# create an instance of GetTenantsResponse from a dict
get_tenants_response_form_dict = get_tenants_response.from_dict(get_tenants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


