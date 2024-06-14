# GetTenantPoliciesWithSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**policies_data** | [**List[TenantPolicyWithSetting]**](TenantPolicyWithSetting.md) | The list of policies with settings. | 

## Example

```python
from onelens_backend_client.models.get_tenant_policies_with_settings_response import GetTenantPoliciesWithSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPoliciesWithSettingsResponse from a JSON string
get_tenant_policies_with_settings_response_instance = GetTenantPoliciesWithSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantPoliciesWithSettingsResponse.to_json())

# convert the object into a dict
get_tenant_policies_with_settings_response_dict = get_tenant_policies_with_settings_response_instance.to_dict()
# create an instance of GetTenantPoliciesWithSettingsResponse from a dict
get_tenant_policies_with_settings_response_form_dict = get_tenant_policies_with_settings_response.from_dict(get_tenant_policies_with_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


