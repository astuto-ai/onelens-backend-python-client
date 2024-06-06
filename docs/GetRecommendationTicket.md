# GetRecommendationTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_unit_id** | **str** | Recommendation Unit ID | 
**potential_saving** | **str** | Potential Saving | 
**priority** | **int** | Priority | 
**data** | [**List[RecommendationTicket]**](RecommendationTicket.md) | Data | 

## Example

```python
from onelens_backend_client.models.get_recommendation_ticket import GetRecommendationTicket

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecommendationTicket from a JSON string
get_recommendation_ticket_instance = GetRecommendationTicket.from_json(json)
# print the JSON string representation of the object
print(GetRecommendationTicket.to_json())

# convert the object into a dict
get_recommendation_ticket_dict = get_recommendation_ticket_instance.to_dict()
# create an instance of GetRecommendationTicket from a dict
get_recommendation_ticket_form_dict = get_recommendation_ticket.from_dict(get_recommendation_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


