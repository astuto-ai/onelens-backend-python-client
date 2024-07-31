# TenantPolicyForPolicyWithSettingServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**product_code** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**resource_types** | [**List[ResourceType]**](ResourceType.md) |  | [optional] [default to []]
**features** | [**Features**](Features.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.tenant_policy_for_policy_with_setting_services_inner import TenantPolicyForPolicyWithSettingServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPolicyForPolicyWithSettingServicesInner from a JSON string
tenant_policy_for_policy_with_setting_services_inner_instance = TenantPolicyForPolicyWithSettingServicesInner.from_json(json)
# print the JSON string representation of the object
print(TenantPolicyForPolicyWithSettingServicesInner.to_json())

# convert the object into a dict
tenant_policy_for_policy_with_setting_services_inner_dict = tenant_policy_for_policy_with_setting_services_inner_instance.to_dict()
# create an instance of TenantPolicyForPolicyWithSettingServicesInner from a dict
tenant_policy_for_policy_with_setting_services_inner_form_dict = tenant_policy_for_policy_with_setting_services_inner.from_dict(tenant_policy_for_policy_with_setting_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


