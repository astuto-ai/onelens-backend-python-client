# ResponseResourceCatalogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceCatalogResponse**](ResourceCatalogResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_resource_catalog_response import ResponseResourceCatalogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseResourceCatalogResponse from a JSON string
response_resource_catalog_response_instance = ResponseResourceCatalogResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseResourceCatalogResponse.to_json())

# convert the object into a dict
response_resource_catalog_response_dict = response_resource_catalog_response_instance.to_dict()
# create an instance of ResponseResourceCatalogResponse from a dict
response_resource_catalog_response_form_dict = response_resource_catalog_response.from_dict(response_resource_catalog_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


