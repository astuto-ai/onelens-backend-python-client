# RelationshipConfigItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationship_type** | **str** |  | 
**join** | [**Join**](Join.md) |  | 

## Example

```python
from onelens_backend_client.models.relationship_config_item import RelationshipConfigItem

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipConfigItem from a JSON string
relationship_config_item_instance = RelationshipConfigItem.from_json(json)
# print the JSON string representation of the object
print(RelationshipConfigItem.to_json())

# convert the object into a dict
relationship_config_item_dict = relationship_config_item_instance.to_dict()
# create an instance of RelationshipConfigItem from a dict
relationship_config_item_form_dict = relationship_config_item.from_dict(relationship_config_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


