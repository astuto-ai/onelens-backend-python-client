# GetTenantPoliciesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**TenantPolicyFilters**](TenantPolicyFilters.md) | Filters to apply to the tenant policies. | [optional] 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_tenant_policies_request import GetTenantPoliciesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPoliciesRequest from a JSON string
get_tenant_policies_request_instance = GetTenantPoliciesRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantPoliciesRequest.to_json())

# convert the object into a dict
get_tenant_policies_request_dict = get_tenant_policies_request_instance.to_dict()
# create an instance of GetTenantPoliciesRequest from a dict
get_tenant_policies_request_form_dict = get_tenant_policies_request.from_dict(get_tenant_policies_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


