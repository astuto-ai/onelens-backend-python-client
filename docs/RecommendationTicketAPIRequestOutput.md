# RecommendationTicketAPIRequestOutput


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
**source_attributes** | **object** | Source Attributes | 
**ticket_id** | **str** | The unique identifier of the ticket | 
**id** | **str** | The unique identifier of the ticket | [optional] 

## Example

```python
from onelens_backend_client.models.recommendation_ticket_api_request_output import RecommendationTicketAPIRequestOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationTicketAPIRequestOutput from a JSON string
recommendation_ticket_api_request_output_instance = RecommendationTicketAPIRequestOutput.from_json(json)
# print the JSON string representation of the object
print(RecommendationTicketAPIRequestOutput.to_json())

# convert the object into a dict
recommendation_ticket_api_request_output_dict = recommendation_ticket_api_request_output_instance.to_dict()
# create an instance of RecommendationTicketAPIRequestOutput from a dict
recommendation_ticket_api_request_output_form_dict = recommendation_ticket_api_request_output.from_dict(recommendation_ticket_api_request_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


