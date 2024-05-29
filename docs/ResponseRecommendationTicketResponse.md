# ResponseRecommendationTicketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RecommendationTicketResponse**](RecommendationTicketResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_recommendation_ticket_response import ResponseRecommendationTicketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseRecommendationTicketResponse from a JSON string
response_recommendation_ticket_response_instance = ResponseRecommendationTicketResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseRecommendationTicketResponse.to_json())

# convert the object into a dict
response_recommendation_ticket_response_dict = response_recommendation_ticket_response_instance.to_dict()
# create an instance of ResponseRecommendationTicketResponse from a dict
response_recommendation_ticket_response_form_dict = response_recommendation_ticket_response.from_dict(response_recommendation_ticket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


