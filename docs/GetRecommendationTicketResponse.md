# GetRecommendationTicketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**List[GetRecommendationTicket]**](GetRecommendationTicket.md) | The recommendations for the ticket | 

## Example

```python
from onelens_backend_client.models.get_recommendation_ticket_response import GetRecommendationTicketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecommendationTicketResponse from a JSON string
get_recommendation_ticket_response_instance = GetRecommendationTicketResponse.from_json(json)
# print the JSON string representation of the object
print(GetRecommendationTicketResponse.to_json())

# convert the object into a dict
get_recommendation_ticket_response_dict = get_recommendation_ticket_response_instance.to_dict()
# create an instance of GetRecommendationTicketResponse from a dict
get_recommendation_ticket_response_form_dict = get_recommendation_ticket_response.from_dict(get_recommendation_ticket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


