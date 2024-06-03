# ServiceCatalogRequestFind


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**id** | **str** | The id of the service catalog. | 

## Example

```python
from onelens_backend_client.models.service_catalog_request_find import ServiceCatalogRequestFind

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCatalogRequestFind from a JSON string
service_catalog_request_find_instance = ServiceCatalogRequestFind.from_json(json)
# print the JSON string representation of the object
print(ServiceCatalogRequestFind.to_json())

# convert the object into a dict
service_catalog_request_find_dict = service_catalog_request_find_instance.to_dict()
# create an instance of ServiceCatalogRequestFind from a dict
service_catalog_request_find_form_dict = service_catalog_request_find.from_dict(service_catalog_request_find_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


