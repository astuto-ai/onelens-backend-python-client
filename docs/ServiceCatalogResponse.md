# ServiceCatalogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[ServiceCatalog]**](ServiceCatalog.md) |  | 

## Example

```python
from onelens_backend_client.models.service_catalog_response import ServiceCatalogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCatalogResponse from a JSON string
service_catalog_response_instance = ServiceCatalogResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceCatalogResponse.to_json())

# convert the object into a dict
service_catalog_response_dict = service_catalog_response_instance.to_dict()
# create an instance of ServiceCatalogResponse from a dict
service_catalog_response_form_dict = service_catalog_response.from_dict(service_catalog_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


