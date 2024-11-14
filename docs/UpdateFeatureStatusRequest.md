# UpdateFeatureStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**is_enabled** | **bool** |  | 

## Example

```python
from onelens_backend_client.models.update_feature_status_request import UpdateFeatureStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeatureStatusRequest from a JSON string
update_feature_status_request_instance = UpdateFeatureStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFeatureStatusRequest.to_json())

# convert the object into a dict
update_feature_status_request_dict = update_feature_status_request_instance.to_dict()
# create an instance of UpdateFeatureStatusRequest from a dict
update_feature_status_request_form_dict = update_feature_status_request.from_dict(update_feature_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


