# UpsertResourceCatalogCostDataRequest

Upsert Resource Catalog Cost Data Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_catalog_cost_data** | [**List[ResourceCatalogCostDataMixin]**](ResourceCatalogCostDataMixin.md) | The resource cost data. | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.upsert_resource_catalog_cost_data_request import UpsertResourceCatalogCostDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertResourceCatalogCostDataRequest from a JSON string
upsert_resource_catalog_cost_data_request_instance = UpsertResourceCatalogCostDataRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertResourceCatalogCostDataRequest.to_json())

# convert the object into a dict
upsert_resource_catalog_cost_data_request_dict = upsert_resource_catalog_cost_data_request_instance.to_dict()
# create an instance of UpsertResourceCatalogCostDataRequest from a dict
upsert_resource_catalog_cost_data_request_form_dict = upsert_resource_catalog_cost_data_request.from_dict(upsert_resource_catalog_cost_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


