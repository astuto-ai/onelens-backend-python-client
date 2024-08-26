# CreateNaviraLogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**user_id** | **str** | User ID (UUID4) associated with the log. | 
**request** | **object** |  | [optional] 
**status** | [**GenerationStatus**](GenerationStatus.md) | The status of the log. | [optional] 
**response** | **object** |  | [optional] 
**extradata** | **object** |  | [optional] 
**feedback** | [**FeedbackModel**](FeedbackModel.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.create_navira_log_request import CreateNaviraLogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNaviraLogRequest from a JSON string
create_navira_log_request_instance = CreateNaviraLogRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNaviraLogRequest.to_json())

# convert the object into a dict
create_navira_log_request_dict = create_navira_log_request_instance.to_dict()
# create an instance of CreateNaviraLogRequest from a dict
create_navira_log_request_form_dict = create_navira_log_request.from_dict(create_navira_log_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


