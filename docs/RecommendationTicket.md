# RecommendationTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Recommendation Ticket | 
**ticket_id** | **str** | The unique identifier of the ticket | 
**recommendation_unit_id** | **str** | Recommendation Unit ID | 
**action_type_id** | **int** | Action Type ID | 
**priority** | **int** | Priority | 
**sequence** | **int** | Sequence | 
**effort** | [**Effort**](Effort.md) | Effort | 
**price_per_unit** | **str** | Price Per Unit | 
**currency** | **str** | Currency | 
**unit** | **str** | Unit | 
**new_cost** | **str** | New Cost | 
**current_cost** | **str** | Current Cost | 
**potential_saving** | **str** | Potential Saving | 
**description** | **str** | Description | 
**begin_range** | **str** | Begin Range | 
**end_range** | **str** | End Range | 
**attributes** | **object** | Attributes | 
**source_attributes** | **object** |  | [optional] 
**created_at** | **datetime** | Datetime of ticket creation | 

## Example

```python
from onelens_backend_client.models.recommendation_ticket import RecommendationTicket

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationTicket from a JSON string
recommendation_ticket_instance = RecommendationTicket.from_json(json)
# print the JSON string representation of the object
print(RecommendationTicket.to_json())

# convert the object into a dict
recommendation_ticket_dict = recommendation_ticket_instance.to_dict()
# create an instance of RecommendationTicket from a dict
recommendation_ticket_form_dict = recommendation_ticket.from_dict(recommendation_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


