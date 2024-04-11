# ResponseGetTenantPolicySettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTenantPolicySettingsResponse**](GetTenantPolicySettingsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_tenant_policy_settings_response import ResponseGetTenantPolicySettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTenantPolicySettingsResponse from a JSON string
response_get_tenant_policy_settings_response_instance = ResponseGetTenantPolicySettingsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTenantPolicySettingsResponse.to_json())

# convert the object into a dict
response_get_tenant_policy_settings_response_dict = response_get_tenant_policy_settings_response_instance.to_dict()
# create an instance of ResponseGetTenantPolicySettingsResponse from a dict
response_get_tenant_policy_settings_response_form_dict = response_get_tenant_policy_settings_response.from_dict(response_get_tenant_policy_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


