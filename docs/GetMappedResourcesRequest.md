# GetMappedResourcesRequest

get mapped resources request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**node_id** | **str** | The id of the node. | 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_mapped_resources_request import GetMappedResourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMappedResourcesRequest from a JSON string
get_mapped_resources_request_instance = GetMappedResourcesRequest.from_json(json)
# print the JSON string representation of the object
print(GetMappedResourcesRequest.to_json())

# convert the object into a dict
get_mapped_resources_request_dict = get_mapped_resources_request_instance.to_dict()
# create an instance of GetMappedResourcesRequest from a dict
get_mapped_resources_request_form_dict = get_mapped_resources_request.from_dict(get_mapped_resources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


