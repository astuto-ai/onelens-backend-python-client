# GetRecommendationTicketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** | Ticket ID | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.get_recommendation_ticket_request import GetRecommendationTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecommendationTicketRequest from a JSON string
get_recommendation_ticket_request_instance = GetRecommendationTicketRequest.from_json(json)
# print the JSON string representation of the object
print(GetRecommendationTicketRequest.to_json())

# convert the object into a dict
get_recommendation_ticket_request_dict = get_recommendation_ticket_request_instance.to_dict()
# create an instance of GetRecommendationTicketRequest from a dict
get_recommendation_ticket_request_form_dict = get_recommendation_ticket_request.from_dict(get_recommendation_ticket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


