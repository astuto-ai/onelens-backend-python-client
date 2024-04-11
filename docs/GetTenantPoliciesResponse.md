# GetTenantPoliciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**policies** | [**List[TenantPolicy]**](TenantPolicy.md) | List of tenant policies. | 

## Example

```python
from onelens_backend_client.models.get_tenant_policies_response import GetTenantPoliciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPoliciesResponse from a JSON string
get_tenant_policies_response_instance = GetTenantPoliciesResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantPoliciesResponse.to_json())

# convert the object into a dict
get_tenant_policies_response_dict = get_tenant_policies_response_instance.to_dict()
# create an instance of GetTenantPoliciesResponse from a dict
get_tenant_policies_response_form_dict = get_tenant_policies_response.from_dict(get_tenant_policies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


