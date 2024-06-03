# GetRecommendationUnitByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Recommendation Unit ID | 

## Example

```python
from onelens_backend_client.models.get_recommendation_unit_by_id_request import GetRecommendationUnitByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecommendationUnitByIdRequest from a JSON string
get_recommendation_unit_by_id_request_instance = GetRecommendationUnitByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetRecommendationUnitByIdRequest.to_json())

# convert the object into a dict
get_recommendation_unit_by_id_request_dict = get_recommendation_unit_by_id_request_instance.to_dict()
# create an instance of GetRecommendationUnitByIdRequest from a dict
get_recommendation_unit_by_id_request_form_dict = get_recommendation_unit_by_id_request.from_dict(get_recommendation_unit_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


