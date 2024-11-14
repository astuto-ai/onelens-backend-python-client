# GetAllFeaturesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[Feature]**](Feature.md) |  | 

## Example

```python
from onelens_backend_client.models.get_all_features_response import GetAllFeaturesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllFeaturesResponse from a JSON string
get_all_features_response_instance = GetAllFeaturesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllFeaturesResponse.to_json())

# convert the object into a dict
get_all_features_response_dict = get_all_features_response_instance.to_dict()
# create an instance of GetAllFeaturesResponse from a dict
get_all_features_response_form_dict = get_all_features_response.from_dict(get_all_features_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


