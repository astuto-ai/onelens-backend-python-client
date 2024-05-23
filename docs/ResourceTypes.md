# ResourceTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | 
**resource_table** | **str** |  | 
**select_columns** | **List[str]** |  | 
**aws_url_template** | **str** |  | 
**relationship_config** | [**List[RelationshipConfigItem]**](RelationshipConfigItem.md) |  | 

## Example

```python
from onelens_backend_client.models.resource_types import ResourceTypes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTypes from a JSON string
resource_types_instance = ResourceTypes.from_json(json)
# print the JSON string representation of the object
print(ResourceTypes.to_json())

# convert the object into a dict
resource_types_dict = resource_types_instance.to_dict()
# create an instance of ResourceTypes from a dict
resource_types_form_dict = resource_types.from_dict(resource_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


