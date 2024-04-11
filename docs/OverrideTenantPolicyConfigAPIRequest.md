# OverrideTenantPolicyConfigAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_overrides** | **object** | The config overrides for the tenant policy. | 

## Example

```python
from onelens_backend_client.models.override_tenant_policy_config_api_request import OverrideTenantPolicyConfigAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideTenantPolicyConfigAPIRequest from a JSON string
override_tenant_policy_config_api_request_instance = OverrideTenantPolicyConfigAPIRequest.from_json(json)
# print the JSON string representation of the object
print(OverrideTenantPolicyConfigAPIRequest.to_json())

# convert the object into a dict
override_tenant_policy_config_api_request_dict = override_tenant_policy_config_api_request_instance.to_dict()
# create an instance of OverrideTenantPolicyConfigAPIRequest from a dict
override_tenant_policy_config_api_request_form_dict = override_tenant_policy_config_api_request.from_dict(override_tenant_policy_config_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


