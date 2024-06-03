# GetPolicyTicketStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Value of the metric | 
**details** | [**List[GetPolicyTicketStatsGroupBy]**](GetPolicyTicketStatsGroupBy.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_policy_ticket_stats_response import GetPolicyTicketStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketStatsResponse from a JSON string
get_policy_ticket_stats_response_instance = GetPolicyTicketStatsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketStatsResponse.to_json())

# convert the object into a dict
get_policy_ticket_stats_response_dict = get_policy_ticket_stats_response_instance.to_dict()
# create an instance of GetPolicyTicketStatsResponse from a dict
get_policy_ticket_stats_response_form_dict = get_policy_ticket_stats_response.from_dict(get_policy_ticket_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


