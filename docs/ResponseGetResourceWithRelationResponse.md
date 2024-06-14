# ResponseGetResourceWithRelationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetResourceWithRelationResponse**](GetResourceWithRelationResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_resource_with_relation_response import ResponseGetResourceWithRelationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetResourceWithRelationResponse from a JSON string
response_get_resource_with_relation_response_instance = ResponseGetResourceWithRelationResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetResourceWithRelationResponse.to_json())

# convert the object into a dict
response_get_resource_with_relation_response_dict = response_get_resource_with_relation_response_instance.to_dict()
# create an instance of ResponseGetResourceWithRelationResponse from a dict
response_get_resource_with_relation_response_form_dict = response_get_resource_with_relation_response.from_dict(response_get_resource_with_relation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


