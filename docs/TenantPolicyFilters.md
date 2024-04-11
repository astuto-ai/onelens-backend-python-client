# TenantPolicyFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_query** | **str** |  | [optional] 
**parent_ptp_ids** | **List[str]** | Filter by parent policy template pack id. | [optional] [default to []]
**categories** | [**List[PolicyCategory]**](PolicyCategory.md) | Filter by type. | [optional] [default to []]
**providers** | [**List[Provider]**](Provider.md) | Filter by provider. | [optional] [default to []]
**services** | [**List[CreatePolicyTemplateRequestServicesInner]**](CreatePolicyTemplateRequestServicesInner.md) | Filter by services. | [optional] [default to []]
**execution_types** | [**List[PolicyExecutionType]**](PolicyExecutionType.md) | Filter by execution type. | [optional] [default to []]

## Example

```python
from onelens_backend_client.models.tenant_policy_filters import TenantPolicyFilters

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPolicyFilters from a JSON string
tenant_policy_filters_instance = TenantPolicyFilters.from_json(json)
# print the JSON string representation of the object
print(TenantPolicyFilters.to_json())

# convert the object into a dict
tenant_policy_filters_dict = tenant_policy_filters_instance.to_dict()
# create an instance of TenantPolicyFilters from a dict
tenant_policy_filters_form_dict = tenant_policy_filters.from_dict(tenant_policy_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


