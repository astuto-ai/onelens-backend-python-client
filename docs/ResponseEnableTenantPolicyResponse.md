# ResponseEnableTenantPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_enable_tenant_policy_response import ResponseEnableTenantPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseEnableTenantPolicyResponse from a JSON string
response_enable_tenant_policy_response_instance = ResponseEnableTenantPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseEnableTenantPolicyResponse.to_json())

# convert the object into a dict
response_enable_tenant_policy_response_dict = response_enable_tenant_policy_response_instance.to_dict()
# create an instance of ResponseEnableTenantPolicyResponse from a dict
response_enable_tenant_policy_response_form_dict = response_enable_tenant_policy_response.from_dict(response_enable_tenant_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


