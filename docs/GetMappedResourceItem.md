# GetMappedResourceItem

get mapped resource item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_id** | **str** | The id of the resource catalog. | 
**cloud_id** | **str** | Resource cloud identifier | 
**region** | **str** | Resource region | 
**service** | **str** | Resource service class | 
**service_display_name** | **str** | Service name in UI | 
**resource_type** | **str** | Resource type | 
**resource_id** | **str** |  | [optional] 
**resource_url_template** | **str** | Resource url template | 
**crn** | **str** | Cloud resource identifier | 
**title** | **str** | Resource name | 
**provider** | **str** | Resource provider | 
**status** | **str** | Resource status | 
**tags** | **object** |  | [optional] 
**additional_info** | **object** | Additional info of the resource. | 
**run_id** | **str** | The run id. | 
**last_updated_at** | **datetime** | The last updated at. | 
**account_name** | **str** |  | [optional] 
**tagged_resource** | **bool** |  | [optional] 
**resource_created_at** | **datetime** |  | [optional] 
**resource_updated_at** | **datetime** |  | [optional] 
**conflict_status** | [**ValidateNodeFilterConflictStatus**](ValidateNodeFilterConflictStatus.md) | conflict status | 
**mapped_to** | [**List[HierarchyNodeEntityWithDetails]**](HierarchyNodeEntityWithDetails.md) | The list of node ids to which the resource is mapped. | 

## Example

```python
from onelens_backend_client.models.get_mapped_resource_item import GetMappedResourceItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMappedResourceItem from a JSON string
get_mapped_resource_item_instance = GetMappedResourceItem.from_json(json)
# print the JSON string representation of the object
print(GetMappedResourceItem.to_json())

# convert the object into a dict
get_mapped_resource_item_dict = get_mapped_resource_item_instance.to_dict()
# create an instance of GetMappedResourceItem from a dict
get_mapped_resource_item_form_dict = get_mapped_resource_item.from_dict(get_mapped_resource_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


