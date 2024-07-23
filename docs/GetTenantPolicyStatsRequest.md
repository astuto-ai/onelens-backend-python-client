# GetTenantPolicyStatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | [optional] [default to []]
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_tenant_policy_stats_request import GetTenantPolicyStatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPolicyStatsRequest from a JSON string
get_tenant_policy_stats_request_instance = GetTenantPolicyStatsRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantPolicyStatsRequest.to_json())

# convert the object into a dict
get_tenant_policy_stats_request_dict = get_tenant_policy_stats_request_instance.to_dict()
# create an instance of GetTenantPolicyStatsRequest from a dict
get_tenant_policy_stats_request_form_dict = get_tenant_policy_stats_request.from_dict(get_tenant_policy_stats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


