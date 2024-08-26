# CreateActionTypePullResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pr_link** | **str** | The action type pull request link. | 

## Example

```python
from onelens_backend_client.models.create_action_type_pull_response import CreateActionTypePullResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateActionTypePullResponse from a JSON string
create_action_type_pull_response_instance = CreateActionTypePullResponse.from_json(json)
# print the JSON string representation of the object
print(CreateActionTypePullResponse.to_json())

# convert the object into a dict
create_action_type_pull_response_dict = create_action_type_pull_response_instance.to_dict()
# create an instance of CreateActionTypePullResponse from a dict
create_action_type_pull_response_form_dict = create_action_type_pull_response.from_dict(create_action_type_pull_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


