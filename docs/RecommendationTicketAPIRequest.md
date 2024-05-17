# RecommendationTicketAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_unit_id** | **str** | Recommendation Unit ID | 
**action_type_id** | **str** | Action Type ID | 
**risk** | **int** | Risk | 
**priority** | **int** | Priority | 
**cost_saving** | [**CostSaving**](CostSaving.md) |  | 
**ticket_id** | **str** | The unique identifier of the ticket | 

## Example

```python
from onelens_backend_client.models.recommendation_ticket_api_request import RecommendationTicketAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationTicketAPIRequest from a JSON string
recommendation_ticket_api_request_instance = RecommendationTicketAPIRequest.from_json(json)
# print the JSON string representation of the object
print(RecommendationTicketAPIRequest.to_json())

# convert the object into a dict
recommendation_ticket_api_request_dict = recommendation_ticket_api_request_instance.to_dict()
# create an instance of RecommendationTicketAPIRequest from a dict
recommendation_ticket_api_request_form_dict = recommendation_ticket_api_request.from_dict(recommendation_ticket_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


