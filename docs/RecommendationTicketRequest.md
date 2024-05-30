# RecommendationTicketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The unique identifier of the tenant | 
**recommendations** | [**List[RecommendationTicketAPIRequestInput]**](RecommendationTicketAPIRequestInput.md) | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.recommendation_ticket_request import RecommendationTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationTicketRequest from a JSON string
recommendation_ticket_request_instance = RecommendationTicketRequest.from_json(json)
# print the JSON string representation of the object
print(RecommendationTicketRequest.to_json())

# convert the object into a dict
recommendation_ticket_request_dict = recommendation_ticket_request_instance.to_dict()
# create an instance of RecommendationTicketRequest from a dict
recommendation_ticket_request_form_dict = recommendation_ticket_request.from_dict(recommendation_ticket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


