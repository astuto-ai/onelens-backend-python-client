# ServiceCatalogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.service_catalog_request import ServiceCatalogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCatalogRequest from a JSON string
service_catalog_request_instance = ServiceCatalogRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceCatalogRequest.to_json())

# convert the object into a dict
service_catalog_request_dict = service_catalog_request_instance.to_dict()
# create an instance of ServiceCatalogRequest from a dict
service_catalog_request_form_dict = service_catalog_request.from_dict(service_catalog_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


