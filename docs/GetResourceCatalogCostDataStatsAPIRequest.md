# GetResourceCatalogCostDataStatsAPIRequest

Get Resource Catalog Cost Data Stats API Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**navira_log_id** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_resource_catalog_cost_data_stats_api_request import GetResourceCatalogCostDataStatsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceCatalogCostDataStatsAPIRequest from a JSON string
get_resource_catalog_cost_data_stats_api_request_instance = GetResourceCatalogCostDataStatsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetResourceCatalogCostDataStatsAPIRequest.to_json())

# convert the object into a dict
get_resource_catalog_cost_data_stats_api_request_dict = get_resource_catalog_cost_data_stats_api_request_instance.to_dict()
# create an instance of GetResourceCatalogCostDataStatsAPIRequest from a dict
get_resource_catalog_cost_data_stats_api_request_form_dict = get_resource_catalog_cost_data_stats_api_request.from_dict(get_resource_catalog_cost_data_stats_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


