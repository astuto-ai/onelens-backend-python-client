# StorageLensConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.storage_lens_config import StorageLensConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StorageLensConfig from a JSON string
storage_lens_config_instance = StorageLensConfig.from_json(json)
# print the JSON string representation of the object
print(StorageLensConfig.to_json())

# convert the object into a dict
storage_lens_config_dict = storage_lens_config_instance.to_dict()
# create an instance of StorageLensConfig from a dict
storage_lens_config_form_dict = storage_lens_config.from_dict(storage_lens_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


