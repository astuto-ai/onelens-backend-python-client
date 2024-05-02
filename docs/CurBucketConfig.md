# CurBucketConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**version** | [**CurBucketVersion**](CurBucketVersion.md) |  | [optional] 
**status** | [**TenantProviderState**](TenantProviderState.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.cur_bucket_config import CurBucketConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CurBucketConfig from a JSON string
cur_bucket_config_instance = CurBucketConfig.from_json(json)
# print the JSON string representation of the object
print(CurBucketConfig.to_json())

# convert the object into a dict
cur_bucket_config_dict = cur_bucket_config_instance.to_dict()
# create an instance of CurBucketConfig from a dict
cur_bucket_config_form_dict = cur_bucket_config.from_dict(cur_bucket_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


