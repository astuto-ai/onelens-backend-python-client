# AddTenantPolicyExclusionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the tenant policy setting. | 
**policy_id** | **str** | The id of the tenant policy. | 
**config_overrides** | **object** |  | [optional] 
**state** | [**TenantPolicyState**](TenantPolicyState.md) | The state of the policy template. | 
**version** | **int** | The version of the tenant policy. | 
**exclusions** | [**TenantPolicyExclusions**](TenantPolicyExclusions.md) | The exclusions for the tenant policy. | 
**last_run_at** | **datetime** |  | [optional] 

## Example

```python
from onelens_backend_client.models.add_tenant_policy_exclusions_response import AddTenantPolicyExclusionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddTenantPolicyExclusionsResponse from a JSON string
add_tenant_policy_exclusions_response_instance = AddTenantPolicyExclusionsResponse.from_json(json)
# print the JSON string representation of the object
print(AddTenantPolicyExclusionsResponse.to_json())

# convert the object into a dict
add_tenant_policy_exclusions_response_dict = add_tenant_policy_exclusions_response_instance.to_dict()
# create an instance of AddTenantPolicyExclusionsResponse from a dict
add_tenant_policy_exclusions_response_form_dict = add_tenant_policy_exclusions_response.from_dict(add_tenant_policy_exclusions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


