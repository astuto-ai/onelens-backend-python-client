# ResourceType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | 
**resource_table** | **str** |  | 
**select_columns** | **List[str]** |  | 
**resource_url_template** | **str** |  | 
**relationship_config** | [**List[RelationshipConfigItem]**](RelationshipConfigItem.md) |  | 

## Example

```python
from onelens_backend_client.models.resource_type import ResourceType

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceType from a JSON string
resource_type_instance = ResourceType.from_json(json)
# print the JSON string representation of the object
print(ResourceType.to_json())

# convert the object into a dict
resource_type_dict = resource_type_instance.to_dict()
# create an instance of ResourceType from a dict
resource_type_form_dict = resource_type.from_dict(resource_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


