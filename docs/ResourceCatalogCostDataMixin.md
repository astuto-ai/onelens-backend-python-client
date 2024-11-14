# ResourceCatalogCostDataMixin

Resource Catalog Cost Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the resource catalog cost data. | 
**resource_catalog_id** | **str** | The id of the resource catalog. | 
**start_datetime** | **datetime** | The start datetime. | 
**end_datetime** | **datetime** | The end datetime. | 
**granularity** | [**OnelensModelsServiceInterfacesUtilitiesCommonsGranularityUnit**](OnelensModelsServiceInterfacesUtilitiesCommonsGranularityUnit.md) | The granularity. | 
**unblended_cost** | **float** |  | [optional] 
**blended_cost** | **float** |  | [optional] 
**net_unblended_cost** | **float** |  | [optional] 

## Example

```python
from onelens_backend_client.models.resource_catalog_cost_data_mixin import ResourceCatalogCostDataMixin

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCatalogCostDataMixin from a JSON string
resource_catalog_cost_data_mixin_instance = ResourceCatalogCostDataMixin.from_json(json)
# print the JSON string representation of the object
print(ResourceCatalogCostDataMixin.to_json())

# convert the object into a dict
resource_catalog_cost_data_mixin_dict = resource_catalog_cost_data_mixin_instance.to_dict()
# create an instance of ResourceCatalogCostDataMixin from a dict
resource_catalog_cost_data_mixin_form_dict = resource_catalog_cost_data_mixin.from_dict(resource_catalog_cost_data_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


