# ServiceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | 
**id** | **str** |  | 
**action_type_id** | **int** |  | 
**priority** | **int** |  | 
**title** | **str** |  | 
**subtitle** | **str** |  | 
**description** | **str** |  | 
**effort** | [**Effort**](Effort.md) |  | 
**query_details** | [**QueryDetails**](QueryDetails.md) |  | 

## Example

```python
from onelens_backend_client.models.service_config import ServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConfig from a JSON string
service_config_instance = ServiceConfig.from_json(json)
# print the JSON string representation of the object
print(ServiceConfig.to_json())

# convert the object into a dict
service_config_dict = service_config_instance.to_dict()
# create an instance of ServiceConfig from a dict
service_config_form_dict = service_config.from_dict(service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


