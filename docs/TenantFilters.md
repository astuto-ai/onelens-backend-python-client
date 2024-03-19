# TenantFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | [**Names**](Names.md) |  | [optional] 
**tenant_states** | [**TenantStates**](TenantStates.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_filters import TenantFilters

# TODO update the JSON string below
json = "{}"
# create an instance of TenantFilters from a JSON string
tenant_filters_instance = TenantFilters.from_json(json)
# print the JSON string representation of the object
print(TenantFilters.to_json())

# convert the object into a dict
tenant_filters_dict = tenant_filters_instance.to_dict()
# create an instance of TenantFilters from a dict
tenant_filters_form_dict = tenant_filters.from_dict(tenant_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


