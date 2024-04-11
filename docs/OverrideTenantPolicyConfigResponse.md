# OverrideTenantPolicyConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the tenant policy setting. | 
**policy_id** | **str** | The id of the tenant policy. | 
**config_overrides** | **object** |  | [optional] 
**state** | [**TenantPolicyState**](TenantPolicyState.md) | The state of the policy template. | 

## Example

```python
from onelens_backend_client.models.override_tenant_policy_config_response import OverrideTenantPolicyConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideTenantPolicyConfigResponse from a JSON string
override_tenant_policy_config_response_instance = OverrideTenantPolicyConfigResponse.from_json(json)
# print the JSON string representation of the object
print(OverrideTenantPolicyConfigResponse.to_json())

# convert the object into a dict
override_tenant_policy_config_response_dict = override_tenant_policy_config_response_instance.to_dict()
# create an instance of OverrideTenantPolicyConfigResponse from a dict
override_tenant_policy_config_response_form_dict = override_tenant_policy_config_response.from_dict(override_tenant_policy_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


