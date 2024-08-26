# ResponseNaviraLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NaviraLogResponse**](NaviraLogResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_navira_log_response import ResponseNaviraLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseNaviraLogResponse from a JSON string
response_navira_log_response_instance = ResponseNaviraLogResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseNaviraLogResponse.to_json())

# convert the object into a dict
response_navira_log_response_dict = response_navira_log_response_instance.to_dict()
# create an instance of ResponseNaviraLogResponse from a dict
response_navira_log_response_form_dict = response_navira_log_response.from_dict(response_navira_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


