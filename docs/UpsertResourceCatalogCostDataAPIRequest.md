# UpsertResourceCatalogCostDataAPIRequest

Upsert Resource Catalog Cost Data API Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_catalog_cost_data** | [**List[ResourceCatalogCostDataMixin]**](ResourceCatalogCostDataMixin.md) | The resource cost data. | 

## Example

```python
from onelens_backend_client.models.upsert_resource_catalog_cost_data_api_request import UpsertResourceCatalogCostDataAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertResourceCatalogCostDataAPIRequest from a JSON string
upsert_resource_catalog_cost_data_api_request_instance = UpsertResourceCatalogCostDataAPIRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertResourceCatalogCostDataAPIRequest.to_json())

# convert the object into a dict
upsert_resource_catalog_cost_data_api_request_dict = upsert_resource_catalog_cost_data_api_request_instance.to_dict()
# create an instance of UpsertResourceCatalogCostDataAPIRequest from a dict
upsert_resource_catalog_cost_data_api_request_form_dict = upsert_resource_catalog_cost_data_api_request.from_dict(upsert_resource_catalog_cost_data_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


