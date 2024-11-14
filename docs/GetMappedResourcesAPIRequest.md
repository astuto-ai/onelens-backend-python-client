# GetMappedResourcesAPIRequest

get mapped resources api request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**node_id** | **str** | The id of the node. | 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 

## Example

```python
from onelens_backend_client.models.get_mapped_resources_api_request import GetMappedResourcesAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMappedResourcesAPIRequest from a JSON string
get_mapped_resources_api_request_instance = GetMappedResourcesAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetMappedResourcesAPIRequest.to_json())

# convert the object into a dict
get_mapped_resources_api_request_dict = get_mapped_resources_api_request_instance.to_dict()
# create an instance of GetMappedResourcesAPIRequest from a dict
get_mapped_resources_api_request_form_dict = get_mapped_resources_api_request.from_dict(get_mapped_resources_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


