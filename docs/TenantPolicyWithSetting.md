# TenantPolicyWithSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**TenantPolicy**](TenantPolicy.md) | The policy details. | 
**setting** | [**TenantPolicySettings**](TenantPolicySettings.md) | The policy setting details. | 

## Example

```python
from onelens_backend_client.models.tenant_policy_with_setting import TenantPolicyWithSetting

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPolicyWithSetting from a JSON string
tenant_policy_with_setting_instance = TenantPolicyWithSetting.from_json(json)
# print the JSON string representation of the object
print(TenantPolicyWithSetting.to_json())

# convert the object into a dict
tenant_policy_with_setting_dict = tenant_policy_with_setting_instance.to_dict()
# create an instance of TenantPolicyWithSetting from a dict
tenant_policy_with_setting_form_dict = tenant_policy_with_setting.from_dict(tenant_policy_with_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


