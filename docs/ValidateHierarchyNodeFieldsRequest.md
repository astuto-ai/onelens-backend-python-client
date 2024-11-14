# ValidateHierarchyNodeFieldsRequest

validate hierarchy node fields request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the node. | 
**category** | [**OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2**](OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2.md) | The category of the node. | 
**parent_id** | **str** | The id of the parent node. | 
**node_id** | **str** |  | [optional] 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.validate_hierarchy_node_fields_request import ValidateHierarchyNodeFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateHierarchyNodeFieldsRequest from a JSON string
validate_hierarchy_node_fields_request_instance = ValidateHierarchyNodeFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateHierarchyNodeFieldsRequest.to_json())

# convert the object into a dict
validate_hierarchy_node_fields_request_dict = validate_hierarchy_node_fields_request_instance.to_dict()
# create an instance of ValidateHierarchyNodeFieldsRequest from a dict
validate_hierarchy_node_fields_request_form_dict = validate_hierarchy_node_fields_request.from_dict(validate_hierarchy_node_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


