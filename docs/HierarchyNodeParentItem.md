# HierarchyNodeParentItem

hierarchy node parent item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | [**NodeId**](NodeId.md) |  | 
**name** | **str** | The name of the node. | 
**category** | [**OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2**](OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2.md) | The category of the node. | 

## Example

```python
from onelens_backend_client.models.hierarchy_node_parent_item import HierarchyNodeParentItem

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchyNodeParentItem from a JSON string
hierarchy_node_parent_item_instance = HierarchyNodeParentItem.from_json(json)
# print the JSON string representation of the object
print(HierarchyNodeParentItem.to_json())

# convert the object into a dict
hierarchy_node_parent_item_dict = hierarchy_node_parent_item_instance.to_dict()
# create an instance of HierarchyNodeParentItem from a dict
hierarchy_node_parent_item_form_dict = hierarchy_node_parent_item.from_dict(hierarchy_node_parent_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


