# GetResourceCatalogStatsResponse

Get Resource Catalog Stats Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_value** | **int** | Fetched metric value | 

## Example

```python
from onelens_backend_client.models.get_resource_catalog_stats_response import GetResourceCatalogStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceCatalogStatsResponse from a JSON string
get_resource_catalog_stats_response_instance = GetResourceCatalogStatsResponse.from_json(json)
# print the JSON string representation of the object
print(GetResourceCatalogStatsResponse.to_json())

# convert the object into a dict
get_resource_catalog_stats_response_dict = get_resource_catalog_stats_response_instance.to_dict()
# create an instance of GetResourceCatalogStatsResponse from a dict
get_resource_catalog_stats_response_form_dict = get_resource_catalog_stats_response.from_dict(get_resource_catalog_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


