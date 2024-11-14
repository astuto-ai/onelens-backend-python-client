# GetPolicyTicketStatsRequestV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**TenantTicketsStatsMetrics**](TenantTicketsStatsMetrics.md) | Metric to be fetched | 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**group** | [**GroupByOption**](GroupByOption.md) |  | [optional] 
**sub_group** | [**SubGroupByOption**](SubGroupByOption.md) |  | [optional] 
**limit_items** | **bool** |  | [optional] 
**item_count** | **int** |  | [optional] 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.get_policy_ticket_stats_request_v2 import GetPolicyTicketStatsRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketStatsRequestV2 from a JSON string
get_policy_ticket_stats_request_v2_instance = GetPolicyTicketStatsRequestV2.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketStatsRequestV2.to_json())

# convert the object into a dict
get_policy_ticket_stats_request_v2_dict = get_policy_ticket_stats_request_v2_instance.to_dict()
# create an instance of GetPolicyTicketStatsRequestV2 from a dict
get_policy_ticket_stats_request_v2_form_dict = get_policy_ticket_stats_request_v2.from_dict(get_policy_ticket_stats_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


