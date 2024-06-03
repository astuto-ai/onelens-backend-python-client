# GetRecommendationUnitByIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_unit** | [**ServiceConfig**](ServiceConfig.md) | Recommendation Unit | 

## Example

```python
from onelens_backend_client.models.get_recommendation_unit_by_id_response import GetRecommendationUnitByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecommendationUnitByIdResponse from a JSON string
get_recommendation_unit_by_id_response_instance = GetRecommendationUnitByIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetRecommendationUnitByIdResponse.to_json())

# convert the object into a dict
get_recommendation_unit_by_id_response_dict = get_recommendation_unit_by_id_response_instance.to_dict()
# create an instance of GetRecommendationUnitByIdResponse from a dict
get_recommendation_unit_by_id_response_form_dict = get_recommendation_unit_by_id_response.from_dict(get_recommendation_unit_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


