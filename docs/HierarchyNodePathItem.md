# HierarchyNodePathItem

hierarchy node path item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | [**NodeId**](NodeId.md) |  | 
**name** | **str** | The name of the node. | 

## Example

```python
from onelens_backend_client.models.hierarchy_node_path_item import HierarchyNodePathItem

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchyNodePathItem from a JSON string
hierarchy_node_path_item_instance = HierarchyNodePathItem.from_json(json)
# print the JSON string representation of the object
print(HierarchyNodePathItem.to_json())

# convert the object into a dict
hierarchy_node_path_item_dict = hierarchy_node_path_item_instance.to_dict()
# create an instance of HierarchyNodePathItem from a dict
hierarchy_node_path_item_form_dict = hierarchy_node_path_item.from_dict(hierarchy_node_path_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


