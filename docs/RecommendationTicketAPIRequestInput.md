# RecommendationTicketAPIRequestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_unit_id** | **str** | Recommendation Unit ID | 
**action_type_id** | **int** | Action Type ID | 
**sequence** | **int** | Sequence | 
**priority** | **int** | Priority | 
**effort** | [**Effort**](Effort.md) | Effort | 
**instance_type** | **str** |  | [optional] 
**instance_family** | **str** |  | [optional] 
**price_per_unit** | [**PricePerUnit**](PricePerUnit.md) |  | 
**currency** | **str** | Currency | 
**unit** | **str** | Unit | 
**new_cost** | [**NewCost**](NewCost.md) |  | 
**current_cost** | [**CurrentCost**](CurrentCost.md) |  | 
**potential_saving** | [**PotentialSaving**](PotentialSaving.md) |  | 
**description** | **str** | Description | 
**begin_range** | [**BeginRange**](BeginRange.md) |  | 
**end_range** | [**EndRange**](EndRange.md) |  | 
**attributes** | **object** | Attributes | 
**ticket_id** | **str** | The unique identifier of the ticket | 
**id** | **str** | The unique identifier of the ticket | [optional] 

## Example

```python
from onelens_backend_client.models.recommendation_ticket_api_request_input import RecommendationTicketAPIRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationTicketAPIRequestInput from a JSON string
recommendation_ticket_api_request_input_instance = RecommendationTicketAPIRequestInput.from_json(json)
# print the JSON string representation of the object
print(RecommendationTicketAPIRequestInput.to_json())

# convert the object into a dict
recommendation_ticket_api_request_input_dict = recommendation_ticket_api_request_input_instance.to_dict()
# create an instance of RecommendationTicketAPIRequestInput from a dict
recommendation_ticket_api_request_input_form_dict = recommendation_ticket_api_request_input.from_dict(recommendation_ticket_api_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


