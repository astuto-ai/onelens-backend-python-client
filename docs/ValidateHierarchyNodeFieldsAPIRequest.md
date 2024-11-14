# ValidateHierarchyNodeFieldsAPIRequest

validate hierarchy node fields api request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the node. | 
**category** | [**OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2**](OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2.md) | The category of the node. | 
**parent_id** | **str** | The id of the parent node. | 
**node_id** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.validate_hierarchy_node_fields_api_request import ValidateHierarchyNodeFieldsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateHierarchyNodeFieldsAPIRequest from a JSON string
validate_hierarchy_node_fields_api_request_instance = ValidateHierarchyNodeFieldsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateHierarchyNodeFieldsAPIRequest.to_json())

# convert the object into a dict
validate_hierarchy_node_fields_api_request_dict = validate_hierarchy_node_fields_api_request_instance.to_dict()
# create an instance of ValidateHierarchyNodeFieldsAPIRequest from a dict
validate_hierarchy_node_fields_api_request_form_dict = validate_hierarchy_node_fields_api_request.from_dict(validate_hierarchy_node_fields_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


