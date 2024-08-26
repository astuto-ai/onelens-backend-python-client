# GetAllResourceCatalogsResponse

Get All Resource Catalogs Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**resources** | [**List[ResourceCatalog]**](ResourceCatalog.md) | List of resource catalog. | 
**status** | [**GenerationStatus**](GenerationStatus.md) | The status of the query, represented as an enum value. | [optional] 
**ambiguous_values** | **List[str]** |  | [optional] 
**navira_log_id** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_all_resource_catalogs_response import GetAllResourceCatalogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllResourceCatalogsResponse from a JSON string
get_all_resource_catalogs_response_instance = GetAllResourceCatalogsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllResourceCatalogsResponse.to_json())

# convert the object into a dict
get_all_resource_catalogs_response_dict = get_all_resource_catalogs_response_instance.to_dict()
# create an instance of GetAllResourceCatalogsResponse from a dict
get_all_resource_catalogs_response_form_dict = get_all_resource_catalogs_response.from_dict(get_all_resource_catalogs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


