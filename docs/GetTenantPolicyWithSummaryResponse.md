# GetTenantPolicyWithSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**TenantPolicyWithPolicyDisplayAlias**](TenantPolicyWithPolicyDisplayAlias.md) | The policy details. | 
**recommendation_units** | **List[str]** | List of recommendation units names. | 

## Example

```python
from onelens_backend_client.models.get_tenant_policy_with_summary_response import GetTenantPolicyWithSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPolicyWithSummaryResponse from a JSON string
get_tenant_policy_with_summary_response_instance = GetTenantPolicyWithSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantPolicyWithSummaryResponse.to_json())

# convert the object into a dict
get_tenant_policy_with_summary_response_dict = get_tenant_policy_with_summary_response_instance.to_dict()
# create an instance of GetTenantPolicyWithSummaryResponse from a dict
get_tenant_policy_with_summary_response_form_dict = get_tenant_policy_with_summary_response.from_dict(get_tenant_policy_with_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


