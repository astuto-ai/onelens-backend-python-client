# ResponseGetPolicyTicketStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetPolicyTicketStatsResponse**](GetPolicyTicketStatsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_policy_ticket_stats_response import ResponseGetPolicyTicketStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetPolicyTicketStatsResponse from a JSON string
response_get_policy_ticket_stats_response_instance = ResponseGetPolicyTicketStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetPolicyTicketStatsResponse.to_json())

# convert the object into a dict
response_get_policy_ticket_stats_response_dict = response_get_policy_ticket_stats_response_instance.to_dict()
# create an instance of ResponseGetPolicyTicketStatsResponse from a dict
response_get_policy_ticket_stats_response_form_dict = response_get_policy_ticket_stats_response.from_dict(response_get_policy_ticket_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


