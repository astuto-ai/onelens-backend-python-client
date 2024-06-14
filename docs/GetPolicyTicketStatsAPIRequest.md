# GetPolicyTicketStatsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**TenantTicketsStatsMetrics**](TenantTicketsStatsMetrics.md) | Metric to be fetched | 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**group** | [**TenantTicketsStatsMetricsGroupBy**](TenantTicketsStatsMetricsGroupBy.md) |  | [optional] 
**sub_group** | [**TenantTicketsStatsMetricsSubGroupBy**](TenantTicketsStatsMetricsSubGroupBy.md) |  | [optional] 
**limit_items** | **bool** |  | [optional] 
**item_count** | **int** |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_policy_ticket_stats_api_request import GetPolicyTicketStatsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketStatsAPIRequest from a JSON string
get_policy_ticket_stats_api_request_instance = GetPolicyTicketStatsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketStatsAPIRequest.to_json())

# convert the object into a dict
get_policy_ticket_stats_api_request_dict = get_policy_ticket_stats_api_request_instance.to_dict()
# create an instance of GetPolicyTicketStatsAPIRequest from a dict
get_policy_ticket_stats_api_request_form_dict = get_policy_ticket_stats_api_request.from_dict(get_policy_ticket_stats_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


