# TenantUsersFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**UserStatus**](UserStatus.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.tenant_users_filters import TenantUsersFilters

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUsersFilters from a JSON string
tenant_users_filters_instance = TenantUsersFilters.from_json(json)
# print the JSON string representation of the object
print(TenantUsersFilters.to_json())

# convert the object into a dict
tenant_users_filters_dict = tenant_users_filters_instance.to_dict()
# create an instance of TenantUsersFilters from a dict
tenant_users_filters_form_dict = tenant_users_filters.from_dict(tenant_users_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


