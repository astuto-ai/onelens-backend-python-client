# RecommendationTicketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_unit_id** | **str** | Recommendation Unit ID | 
**action_type_id** | **str** | Action Type ID | 
**risk** | **int** | Risk | 
**priority** | **int** | Priority | 
**cost_saving** | **str** | Cost Saving | 
**ticket_id** | **str** | The unique identifier of the ticket | 
**id** | **str** | The unique identifier of the ticket | [optional] 

## Example

```python
from onelens_backend_client.models.recommendation_ticket_response import RecommendationTicketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationTicketResponse from a JSON string
recommendation_ticket_response_instance = RecommendationTicketResponse.from_json(json)
# print the JSON string representation of the object
print(RecommendationTicketResponse.to_json())

# convert the object into a dict
recommendation_ticket_response_dict = recommendation_ticket_response_instance.to_dict()
# create an instance of RecommendationTicketResponse from a dict
recommendation_ticket_response_form_dict = recommendation_ticket_response.from_dict(recommendation_ticket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


