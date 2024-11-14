# RegisterAllFeaturesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[TenantFeature]**](TenantFeature.md) |  | 

## Example

```python
from onelens_backend_client.models.register_all_features_response import RegisterAllFeaturesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterAllFeaturesResponse from a JSON string
register_all_features_response_instance = RegisterAllFeaturesResponse.from_json(json)
# print the JSON string representation of the object
print(RegisterAllFeaturesResponse.to_json())

# convert the object into a dict
register_all_features_response_dict = register_all_features_response_instance.to_dict()
# create an instance of RegisterAllFeaturesResponse from a dict
register_all_features_response_form_dict = register_all_features_response.from_dict(register_all_features_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


