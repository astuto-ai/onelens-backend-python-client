# GetStateResponse

Response model for getting the agent state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_state** | **object** | Current state of the agent | 

## Example

```python
from onelens_backend_client.models.get_state_response import GetStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStateResponse from a JSON string
get_state_response_instance = GetStateResponse.from_json(json)
# print the JSON string representation of the object
print(GetStateResponse.to_json())

# convert the object into a dict
get_state_response_dict = get_state_response_instance.to_dict()
# create an instance of GetStateResponse from a dict
get_state_response_form_dict = get_state_response.from_dict(get_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


