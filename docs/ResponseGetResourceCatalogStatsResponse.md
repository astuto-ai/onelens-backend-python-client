# ResponseGetResourceCatalogStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetResourceCatalogStatsResponse**](GetResourceCatalogStatsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_resource_catalog_stats_response import ResponseGetResourceCatalogStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetResourceCatalogStatsResponse from a JSON string
response_get_resource_catalog_stats_response_instance = ResponseGetResourceCatalogStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetResourceCatalogStatsResponse.to_json())

# convert the object into a dict
response_get_resource_catalog_stats_response_dict = response_get_resource_catalog_stats_response_instance.to_dict()
# create an instance of ResponseGetResourceCatalogStatsResponse from a dict
response_get_resource_catalog_stats_response_form_dict = response_get_resource_catalog_stats_response.from_dict(response_get_resource_catalog_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


