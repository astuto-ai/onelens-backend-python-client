# TenantPolicyExclusions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_ids** | **List[str]** | The resources excluded from running the policies on. | 

## Example

```python
from onelens_backend_client.models.tenant_policy_exclusions import TenantPolicyExclusions

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPolicyExclusions from a JSON string
tenant_policy_exclusions_instance = TenantPolicyExclusions.from_json(json)
# print the JSON string representation of the object
print(TenantPolicyExclusions.to_json())

# convert the object into a dict
tenant_policy_exclusions_dict = tenant_policy_exclusions_instance.to_dict()
# create an instance of TenantPolicyExclusions from a dict
tenant_policy_exclusions_form_dict = tenant_policy_exclusions.from_dict(tenant_policy_exclusions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


