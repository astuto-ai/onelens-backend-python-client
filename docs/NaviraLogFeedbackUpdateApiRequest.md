# NaviraLogFeedbackUpdateApiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedback** | [**FeedbackModel**](FeedbackModel.md) | Feedback associated with the log. | 
**navira_log_id** | **str** | The id of the navira log. | 

## Example

```python
from onelens_backend_client.models.navira_log_feedback_update_api_request import NaviraLogFeedbackUpdateApiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NaviraLogFeedbackUpdateApiRequest from a JSON string
navira_log_feedback_update_api_request_instance = NaviraLogFeedbackUpdateApiRequest.from_json(json)
# print the JSON string representation of the object
print(NaviraLogFeedbackUpdateApiRequest.to_json())

# convert the object into a dict
navira_log_feedback_update_api_request_dict = navira_log_feedback_update_api_request_instance.to_dict()
# create an instance of NaviraLogFeedbackUpdateApiRequest from a dict
navira_log_feedback_update_api_request_form_dict = navira_log_feedback_update_api_request.from_dict(navira_log_feedback_update_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


