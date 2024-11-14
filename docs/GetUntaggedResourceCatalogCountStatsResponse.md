# GetUntaggedResourceCatalogCountStatsResponse

Get Untagged Resource Catalog Count Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_value** | **int** | The count of untagged resource catalogs. | 

## Example

```python
from onelens_backend_client.models.get_untagged_resource_catalog_count_stats_response import GetUntaggedResourceCatalogCountStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUntaggedResourceCatalogCountStatsResponse from a JSON string
get_untagged_resource_catalog_count_stats_response_instance = GetUntaggedResourceCatalogCountStatsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUntaggedResourceCatalogCountStatsResponse.to_json())

# convert the object into a dict
get_untagged_resource_catalog_count_stats_response_dict = get_untagged_resource_catalog_count_stats_response_instance.to_dict()
# create an instance of GetUntaggedResourceCatalogCountStatsResponse from a dict
get_untagged_resource_catalog_count_stats_response_form_dict = get_untagged_resource_catalog_count_stats_response.from_dict(get_untagged_resource_catalog_count_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


