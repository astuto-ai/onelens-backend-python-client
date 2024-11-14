# FeatureStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_for** | **List[str]** |  | [optional] 
**config** | [**FeatureConfig**](FeatureConfig.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.feature_store import FeatureStore

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureStore from a JSON string
feature_store_instance = FeatureStore.from_json(json)
# print the JSON string representation of the object
print(FeatureStore.to_json())

# convert the object into a dict
feature_store_dict = feature_store_instance.to_dict()
# create an instance of FeatureStore from a dict
feature_store_form_dict = feature_store.from_dict(feature_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


