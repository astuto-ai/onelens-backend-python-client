# GetResourceWithRelationResponse

Get Resource With Relations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**ResourceCatalog**](ResourceCatalog.md) | The resource details. | 
**relationships** | [**List[ResourceRelationshipResponse]**](ResourceRelationshipResponse.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_resource_with_relation_response import GetResourceWithRelationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceWithRelationResponse from a JSON string
get_resource_with_relation_response_instance = GetResourceWithRelationResponse.from_json(json)
# print the JSON string representation of the object
print(GetResourceWithRelationResponse.to_json())

# convert the object into a dict
get_resource_with_relation_response_dict = get_resource_with_relation_response_instance.to_dict()
# create an instance of GetResourceWithRelationResponse from a dict
get_resource_with_relation_response_form_dict = get_resource_with_relation_response.from_dict(get_resource_with_relation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


