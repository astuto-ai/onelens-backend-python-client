# LeafNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[HierarchyNodeEntityDTOInput]**](HierarchyNodeEntityDTOInput.md) | List of leaf nodes. | 

## Example

```python
from onelens_backend_client.models.leaf_nodes import LeafNodes

# TODO update the JSON string below
json = "{}"
# create an instance of LeafNodes from a JSON string
leaf_nodes_instance = LeafNodes.from_json(json)
# print the JSON string representation of the object
print(LeafNodes.to_json())

# convert the object into a dict
leaf_nodes_dict = leaf_nodes_instance.to_dict()
# create an instance of LeafNodes from a dict
leaf_nodes_form_dict = leaf_nodes.from_dict(leaf_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


