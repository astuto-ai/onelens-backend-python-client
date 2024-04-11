# TenantPolicySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the tenant policy setting. | 
**policy_id** | **str** | The id of the tenant policy. | 
**config_overrides** | **object** |  | [optional] 
**state** | [**TenantPolicyState**](TenantPolicyState.md) | The state of the policy template. | 

## Example

```python
from onelens_backend_client.models.tenant_policy_settings import TenantPolicySettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPolicySettings from a JSON string
tenant_policy_settings_instance = TenantPolicySettings.from_json(json)
# print the JSON string representation of the object
print(TenantPolicySettings.to_json())

# convert the object into a dict
tenant_policy_settings_dict = tenant_policy_settings_instance.to_dict()
# create an instance of TenantPolicySettings from a dict
tenant_policy_settings_form_dict = tenant_policy_settings.from_dict(tenant_policy_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


