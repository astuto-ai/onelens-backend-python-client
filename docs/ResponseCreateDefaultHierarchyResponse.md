# ResponseCreateDefaultHierarchyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | create default hierarchy response | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_create_default_hierarchy_response import ResponseCreateDefaultHierarchyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreateDefaultHierarchyResponse from a JSON string
response_create_default_hierarchy_response_instance = ResponseCreateDefaultHierarchyResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCreateDefaultHierarchyResponse.to_json())

# convert the object into a dict
response_create_default_hierarchy_response_dict = response_create_default_hierarchy_response_instance.to_dict()
# create an instance of ResponseCreateDefaultHierarchyResponse from a dict
response_create_default_hierarchy_response_form_dict = response_create_default_hierarchy_response.from_dict(response_create_default_hierarchy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


