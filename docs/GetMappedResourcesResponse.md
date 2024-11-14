# GetMappedResourcesResponse

get mapped resources response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**resources** | [**List[GetMappedResourceItem]**](GetMappedResourceItem.md) | List of mapped resources. | 

## Example

```python
from onelens_backend_client.models.get_mapped_resources_response import GetMappedResourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMappedResourcesResponse from a JSON string
get_mapped_resources_response_instance = GetMappedResourcesResponse.from_json(json)
# print the JSON string representation of the object
print(GetMappedResourcesResponse.to_json())

# convert the object into a dict
get_mapped_resources_response_dict = get_mapped_resources_response_instance.to_dict()
# create an instance of GetMappedResourcesResponse from a dict
get_mapped_resources_response_form_dict = get_mapped_resources_response.from_dict(get_mapped_resources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


