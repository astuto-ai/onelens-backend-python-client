# ResponseAddTenantPolicyExclusionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AddTenantPolicyExclusionsResponse**](AddTenantPolicyExclusionsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_add_tenant_policy_exclusions_response import ResponseAddTenantPolicyExclusionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseAddTenantPolicyExclusionsResponse from a JSON string
response_add_tenant_policy_exclusions_response_instance = ResponseAddTenantPolicyExclusionsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseAddTenantPolicyExclusionsResponse.to_json())

# convert the object into a dict
response_add_tenant_policy_exclusions_response_dict = response_add_tenant_policy_exclusions_response_instance.to_dict()
# create an instance of ResponseAddTenantPolicyExclusionsResponse from a dict
response_add_tenant_policy_exclusions_response_form_dict = response_add_tenant_policy_exclusions_response.from_dict(response_add_tenant_policy_exclusions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


