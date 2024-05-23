# ServiceCatalog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**product_code** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**resource_types** | [**Dict[str, ResourceTypes]**](ResourceTypes.md) |  | 
**features** | [**Features**](Features.md) |  | 

## Example

```python
from onelens_backend_client.models.service_catalog import ServiceCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCatalog from a JSON string
service_catalog_instance = ServiceCatalog.from_json(json)
# print the JSON string representation of the object
print(ServiceCatalog.to_json())

# convert the object into a dict
service_catalog_dict = service_catalog_instance.to_dict()
# create an instance of ServiceCatalog from a dict
service_catalog_form_dict = service_catalog.from_dict(service_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


