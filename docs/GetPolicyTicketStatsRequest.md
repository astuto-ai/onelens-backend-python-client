# GetPolicyTicketStatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**TenantTicketsStatsMetrics**](TenantTicketsStatsMetrics.md) | Metric to be fetched | 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**group** | [**TenantTicketsStatsMetricsGroupBy**](TenantTicketsStatsMetricsGroupBy.md) |  | [optional] 
**sub_group** | [**TenantTicketsStatsMetricsSubGroupBy**](TenantTicketsStatsMetricsSubGroupBy.md) |  | [optional] 
**item_count** | **int** |  | [optional] 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.get_policy_ticket_stats_request import GetPolicyTicketStatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketStatsRequest from a JSON string
get_policy_ticket_stats_request_instance = GetPolicyTicketStatsRequest.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketStatsRequest.to_json())

# convert the object into a dict
get_policy_ticket_stats_request_dict = get_policy_ticket_stats_request_instance.to_dict()
# create an instance of GetPolicyTicketStatsRequest from a dict
get_policy_ticket_stats_request_form_dict = get_policy_ticket_stats_request.from_dict(get_policy_ticket_stats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


