# GetTenantPoliciesAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**TenantPolicyFilters**](TenantPolicyFilters.md) | Filters to apply to the tenant policies. | [optional] 

## Example

```python
from onelens_backend_client.models.get_tenant_policies_api_request import GetTenantPoliciesAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPoliciesAPIRequest from a JSON string
get_tenant_policies_api_request_instance = GetTenantPoliciesAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantPoliciesAPIRequest.to_json())

# convert the object into a dict
get_tenant_policies_api_request_dict = get_tenant_policies_api_request_instance.to_dict()
# create an instance of GetTenantPoliciesAPIRequest from a dict
get_tenant_policies_api_request_form_dict = get_tenant_policies_api_request.from_dict(get_tenant_policies_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


