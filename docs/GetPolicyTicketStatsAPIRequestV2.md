# GetPolicyTicketStatsAPIRequestV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**TenantTicketsStatsMetrics**](TenantTicketsStatsMetrics.md) | Metric to be fetched | 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**group** | [**GroupByOption**](GroupByOption.md) |  | [optional] 
**sub_group** | [**SubGroupByOption**](SubGroupByOption.md) |  | [optional] 
**limit_items** | **bool** |  | [optional] 
**item_count** | **int** |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_policy_ticket_stats_api_request_v2 import GetPolicyTicketStatsAPIRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketStatsAPIRequestV2 from a JSON string
get_policy_ticket_stats_api_request_v2_instance = GetPolicyTicketStatsAPIRequestV2.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketStatsAPIRequestV2.to_json())

# convert the object into a dict
get_policy_ticket_stats_api_request_v2_dict = get_policy_ticket_stats_api_request_v2_instance.to_dict()
# create an instance of GetPolicyTicketStatsAPIRequestV2 from a dict
get_policy_ticket_stats_api_request_v2_form_dict = get_policy_ticket_stats_api_request_v2.from_dict(get_policy_ticket_stats_api_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


