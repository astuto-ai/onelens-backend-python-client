# ResponseGetTenantPolicyByIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTenantPolicyByIdResponse**](GetTenantPolicyByIdResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_tenant_policy_by_id_response import ResponseGetTenantPolicyByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTenantPolicyByIdResponse from a JSON string
response_get_tenant_policy_by_id_response_instance = ResponseGetTenantPolicyByIdResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTenantPolicyByIdResponse.to_json())

# convert the object into a dict
response_get_tenant_policy_by_id_response_dict = response_get_tenant_policy_by_id_response_instance.to_dict()
# create an instance of ResponseGetTenantPolicyByIdResponse from a dict
response_get_tenant_policy_by_id_response_form_dict = response_get_tenant_policy_by_id_response.from_dict(response_get_tenant_policy_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


