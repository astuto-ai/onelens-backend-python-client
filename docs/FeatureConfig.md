# FeatureConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_metrics_for_days** | **int** |  | [optional] 
**threshold_percentage** | **int** |  | [optional] 

## Example

```python
from onelens_backend_client.models.feature_config import FeatureConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureConfig from a JSON string
feature_config_instance = FeatureConfig.from_json(json)
# print the JSON string representation of the object
print(FeatureConfig.to_json())

# convert the object into a dict
feature_config_dict = feature_config_instance.to_dict()
# create an instance of FeatureConfig from a dict
feature_config_form_dict = feature_config.from_dict(feature_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


