# GetResourceCatalogStatsAPIRequest

Get Resource Catalog Stats API Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 

## Example

```python
from onelens_backend_client.models.get_resource_catalog_stats_api_request import GetResourceCatalogStatsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceCatalogStatsAPIRequest from a JSON string
get_resource_catalog_stats_api_request_instance = GetResourceCatalogStatsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetResourceCatalogStatsAPIRequest.to_json())

# convert the object into a dict
get_resource_catalog_stats_api_request_dict = get_resource_catalog_stats_api_request_instance.to_dict()
# create an instance of GetResourceCatalogStatsAPIRequest from a dict
get_resource_catalog_stats_api_request_form_dict = get_resource_catalog_stats_api_request.from_dict(get_resource_catalog_stats_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


