# ResponseOverrideTenantPolicyExclusionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OverrideTenantPolicyExclusionsResponse**](OverrideTenantPolicyExclusionsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_override_tenant_policy_exclusions_response import ResponseOverrideTenantPolicyExclusionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseOverrideTenantPolicyExclusionsResponse from a JSON string
response_override_tenant_policy_exclusions_response_instance = ResponseOverrideTenantPolicyExclusionsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseOverrideTenantPolicyExclusionsResponse.to_json())

# convert the object into a dict
response_override_tenant_policy_exclusions_response_dict = response_override_tenant_policy_exclusions_response_instance.to_dict()
# create an instance of ResponseOverrideTenantPolicyExclusionsResponse from a dict
response_override_tenant_policy_exclusions_response_form_dict = response_override_tenant_policy_exclusions_response.from_dict(response_override_tenant_policy_exclusions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


