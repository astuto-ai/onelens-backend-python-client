# GetFeaturesByFiltersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[TenantFeature]**](TenantFeature.md) |  | 

## Example

```python
from onelens_backend_client.models.get_features_by_filters_response import GetFeaturesByFiltersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeaturesByFiltersResponse from a JSON string
get_features_by_filters_response_instance = GetFeaturesByFiltersResponse.from_json(json)
# print the JSON string representation of the object
print(GetFeaturesByFiltersResponse.to_json())

# convert the object into a dict
get_features_by_filters_response_dict = get_features_by_filters_response_instance.to_dict()
# create an instance of GetFeaturesByFiltersResponse from a dict
get_features_by_filters_response_form_dict = get_features_by_filters_response.from_dict(get_features_by_filters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


