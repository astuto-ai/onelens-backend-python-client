# TenantPolicySettingsFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**states** | [**List[TenantPolicyState]**](TenantPolicyState.md) | Filter by state. Default is ACTIVE. | [optional] [default to [ACTIVE]]
**policy_ids** | **List[str]** | Filter by tenant policy id. | [optional] [default to []]

## Example

```python
from onelens_backend_client.models.tenant_policy_settings_filters import TenantPolicySettingsFilters

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPolicySettingsFilters from a JSON string
tenant_policy_settings_filters_instance = TenantPolicySettingsFilters.from_json(json)
# print the JSON string representation of the object
print(TenantPolicySettingsFilters.to_json())

# convert the object into a dict
tenant_policy_settings_filters_dict = tenant_policy_settings_filters_instance.to_dict()
# create an instance of TenantPolicySettingsFilters from a dict
tenant_policy_settings_filters_form_dict = tenant_policy_settings_filters.from_dict(tenant_policy_settings_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


