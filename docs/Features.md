# Features


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_in_policy** | **bool** |  | [optional] [default to False]
**enable_in_anomalies** | **bool** |  | [optional] [default to False]

## Example

```python
from onelens_backend_client.models.features import Features

# TODO update the JSON string below
json = "{}"
# create an instance of Features from a JSON string
features_instance = Features.from_json(json)
# print the JSON string representation of the object
print(Features.to_json())

# convert the object into a dict
features_dict = features_instance.to_dict()
# create an instance of Features from a dict
features_form_dict = features.from_dict(features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


