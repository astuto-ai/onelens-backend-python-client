# NaviraFullLogResponse

Model representing a Navira log response object , containing the log's unique identifier, the query prompt, and the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique integer identifier for the record. | 
**request** | **object** | The query data represented as a JSON object. | 
**created_at** | **datetime** |  | [optional] 
**response** | **object** | The response represented as a JSON object. | 

## Example

```python
from onelens_backend_client.models.navira_full_log_response import NaviraFullLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NaviraFullLogResponse from a JSON string
navira_full_log_response_instance = NaviraFullLogResponse.from_json(json)
# print the JSON string representation of the object
print(NaviraFullLogResponse.to_json())

# convert the object into a dict
navira_full_log_response_dict = navira_full_log_response_instance.to_dict()
# create an instance of NaviraFullLogResponse from a dict
navira_full_log_response_form_dict = navira_full_log_response.from_dict(navira_full_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


