# ResponseGetTenantPolicyWithSummaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTenantPolicyWithSummaryRequest**](GetTenantPolicyWithSummaryRequest.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_tenant_policy_with_summary_request import ResponseGetTenantPolicyWithSummaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTenantPolicyWithSummaryRequest from a JSON string
response_get_tenant_policy_with_summary_request_instance = ResponseGetTenantPolicyWithSummaryRequest.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTenantPolicyWithSummaryRequest.to_json())

# convert the object into a dict
response_get_tenant_policy_with_summary_request_dict = response_get_tenant_policy_with_summary_request_instance.to_dict()
# create an instance of ResponseGetTenantPolicyWithSummaryRequest from a dict
response_get_tenant_policy_with_summary_request_form_dict = response_get_tenant_policy_with_summary_request.from_dict(response_get_tenant_policy_with_summary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


