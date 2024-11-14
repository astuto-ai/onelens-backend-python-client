# ResponseGetUntaggedResourceCatalogCountStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetUntaggedResourceCatalogCountStatsResponse**](GetUntaggedResourceCatalogCountStatsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_untagged_resource_catalog_count_stats_response import ResponseGetUntaggedResourceCatalogCountStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetUntaggedResourceCatalogCountStatsResponse from a JSON string
response_get_untagged_resource_catalog_count_stats_response_instance = ResponseGetUntaggedResourceCatalogCountStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetUntaggedResourceCatalogCountStatsResponse.to_json())

# convert the object into a dict
response_get_untagged_resource_catalog_count_stats_response_dict = response_get_untagged_resource_catalog_count_stats_response_instance.to_dict()
# create an instance of ResponseGetUntaggedResourceCatalogCountStatsResponse from a dict
response_get_untagged_resource_catalog_count_stats_response_form_dict = response_get_untagged_resource_catalog_count_stats_response.from_dict(response_get_untagged_resource_catalog_count_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


