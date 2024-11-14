# GetResourceCatalogCountStatsRequest

Get Resource Catalog Stats Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**navira_log_id** | **str** |  | [optional] 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_resource_catalog_count_stats_request import GetResourceCatalogCountStatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceCatalogCountStatsRequest from a JSON string
get_resource_catalog_count_stats_request_instance = GetResourceCatalogCountStatsRequest.from_json(json)
# print the JSON string representation of the object
print(GetResourceCatalogCountStatsRequest.to_json())

# convert the object into a dict
get_resource_catalog_count_stats_request_dict = get_resource_catalog_count_stats_request_instance.to_dict()
# create an instance of GetResourceCatalogCountStatsRequest from a dict
get_resource_catalog_count_stats_request_form_dict = get_resource_catalog_count_stats_request.from_dict(get_resource_catalog_count_stats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


