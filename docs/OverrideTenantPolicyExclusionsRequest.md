# OverrideTenantPolicyExclusionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusions** | [**TenantPolicyExclusions**](TenantPolicyExclusions.md) | The exclusions to add. | 
**tenant_id** | **str** | The id of the tenant. | 
**policy_id** | **str** | The id of the tenant policy. | 

## Example

```python
from onelens_backend_client.models.override_tenant_policy_exclusions_request import OverrideTenantPolicyExclusionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideTenantPolicyExclusionsRequest from a JSON string
override_tenant_policy_exclusions_request_instance = OverrideTenantPolicyExclusionsRequest.from_json(json)
# print the JSON string representation of the object
print(OverrideTenantPolicyExclusionsRequest.to_json())

# convert the object into a dict
override_tenant_policy_exclusions_request_dict = override_tenant_policy_exclusions_request_instance.to_dict()
# create an instance of OverrideTenantPolicyExclusionsRequest from a dict
override_tenant_policy_exclusions_request_form_dict = override_tenant_policy_exclusions_request.from_dict(override_tenant_policy_exclusions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


