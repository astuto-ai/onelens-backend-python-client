# AddTenantPolicyExclusionsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusions** | [**TenantPolicyExclusions**](TenantPolicyExclusions.md) | The exclusions to add. | 

## Example

```python
from onelens_backend_client.models.add_tenant_policy_exclusions_api_request import AddTenantPolicyExclusionsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTenantPolicyExclusionsAPIRequest from a JSON string
add_tenant_policy_exclusions_api_request_instance = AddTenantPolicyExclusionsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(AddTenantPolicyExclusionsAPIRequest.to_json())

# convert the object into a dict
add_tenant_policy_exclusions_api_request_dict = add_tenant_policy_exclusions_api_request_instance.to_dict()
# create an instance of AddTenantPolicyExclusionsAPIRequest from a dict
add_tenant_policy_exclusions_api_request_form_dict = add_tenant_policy_exclusions_api_request.from_dict(add_tenant_policy_exclusions_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


