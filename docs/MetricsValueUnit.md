# MetricsValueUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The value of the metric. | 
**unit** | **str** | The unit of the value. | 

## Example

```python
from onelens_backend_client.models.metrics_value_unit import MetricsValueUnit

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsValueUnit from a JSON string
metrics_value_unit_instance = MetricsValueUnit.from_json(json)
# print the JSON string representation of the object
print(MetricsValueUnit.to_json())

# convert the object into a dict
metrics_value_unit_dict = metrics_value_unit_instance.to_dict()
# create an instance of MetricsValueUnit from a dict
metrics_value_unit_form_dict = metrics_value_unit.from_dict(metrics_value_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


