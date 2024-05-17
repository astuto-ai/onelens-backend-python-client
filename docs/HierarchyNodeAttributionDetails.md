# HierarchyNodeAttributionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **List[int]** | List of nodes with which the node is shared | 
**strategy** | **str** | Strategy for attribution | 

## Example

```python
from onelens_backend_client.models.hierarchy_node_attribution_details import HierarchyNodeAttributionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchyNodeAttributionDetails from a JSON string
hierarchy_node_attribution_details_instance = HierarchyNodeAttributionDetails.from_json(json)
# print the JSON string representation of the object
print(HierarchyNodeAttributionDetails.to_json())

# convert the object into a dict
hierarchy_node_attribution_details_dict = hierarchy_node_attribution_details_instance.to_dict()
# create an instance of HierarchyNodeAttributionDetails from a dict
hierarchy_node_attribution_details_form_dict = hierarchy_node_attribution_details.from_dict(hierarchy_node_attribution_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


