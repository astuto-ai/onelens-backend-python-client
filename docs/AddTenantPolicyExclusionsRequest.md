# AddTenantPolicyExclusionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusions** | [**TenantPolicyExclusions**](TenantPolicyExclusions.md) | The exclusions to add. | 
**tenant_id** | **str** | The id of the tenant. | 
**policy_id** | **str** | The id of the tenant policy. | 

## Example

```python
from onelens_backend_client.models.add_tenant_policy_exclusions_request import AddTenantPolicyExclusionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTenantPolicyExclusionsRequest from a JSON string
add_tenant_policy_exclusions_request_instance = AddTenantPolicyExclusionsRequest.from_json(json)
# print the JSON string representation of the object
print(AddTenantPolicyExclusionsRequest.to_json())

# convert the object into a dict
add_tenant_policy_exclusions_request_dict = add_tenant_policy_exclusions_request_instance.to_dict()
# create an instance of AddTenantPolicyExclusionsRequest from a dict
add_tenant_policy_exclusions_request_form_dict = add_tenant_policy_exclusions_request.from_dict(add_tenant_policy_exclusions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


