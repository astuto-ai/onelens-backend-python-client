# GetTenantPolicyWithSummaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the tenant policy. | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_tenant_policy_with_summary_request import GetTenantPolicyWithSummaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPolicyWithSummaryRequest from a JSON string
get_tenant_policy_with_summary_request_instance = GetTenantPolicyWithSummaryRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantPolicyWithSummaryRequest.to_json())

# convert the object into a dict
get_tenant_policy_with_summary_request_dict = get_tenant_policy_with_summary_request_instance.to_dict()
# create an instance of GetTenantPolicyWithSummaryRequest from a dict
get_tenant_policy_with_summary_request_form_dict = get_tenant_policy_with_summary_request.from_dict(get_tenant_policy_with_summary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


