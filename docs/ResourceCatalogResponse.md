# ResourceCatalogResponse

Resource Catalog Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_id** | **str** | The id of the resource catalog. | 
**cloud_id** | **str** | Resource cloud identifier | 
**region** | **str** | Resource region | 
**service** | **str** | Resource service class | 
**service_display_name** | **str** | Service name in UI | 
**resource_type** | **str** | Resource type | 
**resource_id** | **str** |  | [optional] 
**resource_url_template** | **str** | Resource url template | 
**crn** | **str** | Cloud resource identifier | 
**title** | **str** | Resource name | 
**provider** | **str** | Resource provider | 
**status** | **str** | Resource status | 
**tags** | **object** |  | [optional] 
**additional_info** | **object** | Additional info of the resource. | 
**run_id** | **str** | The run id. | 
**last_updated_at** | **datetime** | The last updated at. | 
**account_name** | **str** |  | [optional] 
**tagged_resource** | **bool** |  | [optional] 

## Example

```python
from onelens_backend_client.models.resource_catalog_response import ResourceCatalogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCatalogResponse from a JSON string
resource_catalog_response_instance = ResourceCatalogResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceCatalogResponse.to_json())

# convert the object into a dict
resource_catalog_response_dict = resource_catalog_response_instance.to_dict()
# create an instance of ResourceCatalogResponse from a dict
resource_catalog_response_form_dict = resource_catalog_response.from_dict(resource_catalog_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


