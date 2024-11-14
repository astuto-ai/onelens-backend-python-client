# APIGetFeaturesByFiltersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**TenantFeatureScope**](TenantFeatureScope.md) |  | [optional] 
**entity_id** | **List[str]** |  | [optional] 
**feature_name** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 

## Example

```python
from onelens_backend_client.models.api_get_features_by_filters_request import APIGetFeaturesByFiltersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of APIGetFeaturesByFiltersRequest from a JSON string
api_get_features_by_filters_request_instance = APIGetFeaturesByFiltersRequest.from_json(json)
# print the JSON string representation of the object
print(APIGetFeaturesByFiltersRequest.to_json())

# convert the object into a dict
api_get_features_by_filters_request_dict = api_get_features_by_filters_request_instance.to_dict()
# create an instance of APIGetFeaturesByFiltersRequest from a dict
api_get_features_by_filters_request_form_dict = api_get_features_by_filters_request.from_dict(api_get_features_by_filters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


