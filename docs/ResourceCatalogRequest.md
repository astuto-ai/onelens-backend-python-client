# ResourceCatalogRequest

Resource Catalog Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_id** | **str** | The id of the resource catalog. | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.resource_catalog_request import ResourceCatalogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCatalogRequest from a JSON string
resource_catalog_request_instance = ResourceCatalogRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceCatalogRequest.to_json())

# convert the object into a dict
resource_catalog_request_dict = resource_catalog_request_instance.to_dict()
# create an instance of ResourceCatalogRequest from a dict
resource_catalog_request_form_dict = resource_catalog_request.from_dict(resource_catalog_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


