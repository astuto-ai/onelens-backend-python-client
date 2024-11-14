# ResponseValidateHierarchyNodeFieldsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | validate hierarchy node fields response | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_validate_hierarchy_node_fields_response import ResponseValidateHierarchyNodeFieldsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseValidateHierarchyNodeFieldsResponse from a JSON string
response_validate_hierarchy_node_fields_response_instance = ResponseValidateHierarchyNodeFieldsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseValidateHierarchyNodeFieldsResponse.to_json())

# convert the object into a dict
response_validate_hierarchy_node_fields_response_dict = response_validate_hierarchy_node_fields_response_instance.to_dict()
# create an instance of ResponseValidateHierarchyNodeFieldsResponse from a dict
response_validate_hierarchy_node_fields_response_form_dict = response_validate_hierarchy_node_fields_response.from_dict(response_validate_hierarchy_node_fields_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


