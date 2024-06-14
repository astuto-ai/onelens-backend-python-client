# GetPolicyTicketStatsGroupBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Field name to be fetched | 
**field_value** | **float** |  | [optional] 
**field_details** | [**List[GetPolicyTicketStatsSubGroupBy]**](GetPolicyTicketStatsSubGroupBy.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_policy_ticket_stats_group_by import GetPolicyTicketStatsGroupBy

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketStatsGroupBy from a JSON string
get_policy_ticket_stats_group_by_instance = GetPolicyTicketStatsGroupBy.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketStatsGroupBy.to_json())

# convert the object into a dict
get_policy_ticket_stats_group_by_dict = get_policy_ticket_stats_group_by_instance.to_dict()
# create an instance of GetPolicyTicketStatsGroupBy from a dict
get_policy_ticket_stats_group_by_form_dict = get_policy_ticket_stats_group_by.from_dict(get_policy_ticket_stats_group_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


