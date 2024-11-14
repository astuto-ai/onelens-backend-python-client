# ResponseGetMappedResourcesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetMappedResourcesResponse**](GetMappedResourcesResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_mapped_resources_response import ResponseGetMappedResourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetMappedResourcesResponse from a JSON string
response_get_mapped_resources_response_instance = ResponseGetMappedResourcesResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetMappedResourcesResponse.to_json())

# convert the object into a dict
response_get_mapped_resources_response_dict = response_get_mapped_resources_response_instance.to_dict()
# create an instance of ResponseGetMappedResourcesResponse from a dict
response_get_mapped_resources_response_form_dict = response_get_mapped_resources_response.from_dict(response_get_mapped_resources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


