# RegisterAllFeaturesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 

## Example

```python
from onelens_backend_client.models.register_all_features_request import RegisterAllFeaturesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterAllFeaturesRequest from a JSON string
register_all_features_request_instance = RegisterAllFeaturesRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterAllFeaturesRequest.to_json())

# convert the object into a dict
register_all_features_request_dict = register_all_features_request_instance.to_dict()
# create an instance of RegisterAllFeaturesRequest from a dict
register_all_features_request_form_dict = register_all_features_request.from_dict(register_all_features_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


