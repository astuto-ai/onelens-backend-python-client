# GetTenantPolicySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**policy_settings** | [**List[TenantPolicySettings]**](TenantPolicySettings.md) | List of tenant policy settings. | 

## Example

```python
from onelens_backend_client.models.get_tenant_policy_settings_response import GetTenantPolicySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPolicySettingsResponse from a JSON string
get_tenant_policy_settings_response_instance = GetTenantPolicySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantPolicySettingsResponse.to_json())

# convert the object into a dict
get_tenant_policy_settings_response_dict = get_tenant_policy_settings_response_instance.to_dict()
# create an instance of GetTenantPolicySettingsResponse from a dict
get_tenant_policy_settings_response_form_dict = get_tenant_policy_settings_response.from_dict(get_tenant_policy_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


