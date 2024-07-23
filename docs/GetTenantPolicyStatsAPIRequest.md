# GetTenantPolicyStatsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | [optional] [default to []]

## Example

```python
from onelens_backend_client.models.get_tenant_policy_stats_api_request import GetTenantPolicyStatsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPolicyStatsAPIRequest from a JSON string
get_tenant_policy_stats_api_request_instance = GetTenantPolicyStatsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantPolicyStatsAPIRequest.to_json())

# convert the object into a dict
get_tenant_policy_stats_api_request_dict = get_tenant_policy_stats_api_request_instance.to_dict()
# create an instance of GetTenantPolicyStatsAPIRequest from a dict
get_tenant_policy_stats_api_request_form_dict = get_tenant_policy_stats_api_request.from_dict(get_tenant_policy_stats_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


