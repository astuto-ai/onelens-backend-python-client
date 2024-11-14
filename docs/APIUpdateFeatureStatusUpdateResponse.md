# APIUpdateFeatureStatusUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | [**TenantFeature**](TenantFeature.md) |  | 

## Example

```python
from onelens_backend_client.models.api_update_feature_status_update_response import APIUpdateFeatureStatusUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIUpdateFeatureStatusUpdateResponse from a JSON string
api_update_feature_status_update_response_instance = APIUpdateFeatureStatusUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(APIUpdateFeatureStatusUpdateResponse.to_json())

# convert the object into a dict
api_update_feature_status_update_response_dict = api_update_feature_status_update_response_instance.to_dict()
# create an instance of APIUpdateFeatureStatusUpdateResponse from a dict
api_update_feature_status_update_response_form_dict = api_update_feature_status_update_response.from_dict(api_update_feature_status_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


