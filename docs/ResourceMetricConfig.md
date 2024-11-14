# ResourceMetricConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | [optional] 
**metric_table_additional_columns** | **List[str]** |  | [optional] 
**resource_select_statement** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.resource_metric_config import ResourceMetricConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceMetricConfig from a JSON string
resource_metric_config_instance = ResourceMetricConfig.from_json(json)
# print the JSON string representation of the object
print(ResourceMetricConfig.to_json())

# convert the object into a dict
resource_metric_config_dict = resource_metric_config_instance.to_dict()
# create an instance of ResourceMetricConfig from a dict
resource_metric_config_form_dict = resource_metric_config.from_dict(resource_metric_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


