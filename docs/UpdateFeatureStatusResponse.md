# UpdateFeatureStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | [**TenantFeature**](TenantFeature.md) |  | 

## Example

```python
from onelens_backend_client.models.update_feature_status_response import UpdateFeatureStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeatureStatusResponse from a JSON string
update_feature_status_response_instance = UpdateFeatureStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateFeatureStatusResponse.to_json())

# convert the object into a dict
update_feature_status_response_dict = update_feature_status_response_instance.to_dict()
# create an instance of UpdateFeatureStatusResponse from a dict
update_feature_status_response_form_dict = update_feature_status_response.from_dict(update_feature_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


