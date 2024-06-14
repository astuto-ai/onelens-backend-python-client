# ResourceRelationshipResponse

Resource Relationship Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationship_type** | **str** | The relationship type | 
**direction** | **str** | The relationship direction | 
**resource** | [**ResourceCatalog**](ResourceCatalog.md) | The resource details. | 

## Example

```python
from onelens_backend_client.models.resource_relationship_response import ResourceRelationshipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRelationshipResponse from a JSON string
resource_relationship_response_instance = ResourceRelationshipResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceRelationshipResponse.to_json())

# convert the object into a dict
resource_relationship_response_dict = resource_relationship_response_instance.to_dict()
# create an instance of ResourceRelationshipResponse from a dict
resource_relationship_response_form_dict = resource_relationship_response.from_dict(resource_relationship_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


