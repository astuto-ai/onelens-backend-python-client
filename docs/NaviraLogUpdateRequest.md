# NaviraLogUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**request** | **object** |  | [optional] 
**status** | [**GenerationStatus**](GenerationStatus.md) |  | [optional] 
**response** | **object** |  | [optional] 
**extradata** | **object** |  | [optional] 
**feedback** | [**FeedbackModel**](FeedbackModel.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.navira_log_update_request import NaviraLogUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NaviraLogUpdateRequest from a JSON string
navira_log_update_request_instance = NaviraLogUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(NaviraLogUpdateRequest.to_json())

# convert the object into a dict
navira_log_update_request_dict = navira_log_update_request_instance.to_dict()
# create an instance of NaviraLogUpdateRequest from a dict
navira_log_update_request_form_dict = navira_log_update_request.from_dict(navira_log_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


