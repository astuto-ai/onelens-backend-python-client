# ProviderConfigInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regions** | **object** |  | [optional] 
**role_name** | **str** |  | [optional] 
**cur_bucket_config** | [**CurBucketConfig**](CurBucketConfig.md) |  | [optional] 
**storage_lens_config** | [**StorageLensConfig**](StorageLensConfig.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.provider_config_input import ProviderConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderConfigInput from a JSON string
provider_config_input_instance = ProviderConfigInput.from_json(json)
# print the JSON string representation of the object
print(ProviderConfigInput.to_json())

# convert the object into a dict
provider_config_input_dict = provider_config_input_instance.to_dict()
# create an instance of ProviderConfigInput from a dict
provider_config_input_form_dict = provider_config_input.from_dict(provider_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


