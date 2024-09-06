# CreateActionTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**Service**](Service.md) |  | 
**title** | **str** | Title | 
**subtitle** | **str** |  | [optional] 
**description** | **str** | Description | 
**alias** | **str** |  | 

## Example

```python
from onelens_backend_client.models.create_action_type_request import CreateActionTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateActionTypeRequest from a JSON string
create_action_type_request_instance = CreateActionTypeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateActionTypeRequest.to_json())

# convert the object into a dict
create_action_type_request_dict = create_action_type_request_instance.to_dict()
# create an instance of CreateActionTypeRequest from a dict
create_action_type_request_form_dict = create_action_type_request.from_dict(create_action_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


