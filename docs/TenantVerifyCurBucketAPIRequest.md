# TenantVerifyCurBucketAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cur_bucket_config** | [**CurBucketConfig**](CurBucketConfig.md) | cur bucket config | 
**cloud_id** | **str** | cloud id | 

## Example

```python
from onelens_backend_client.models.tenant_verify_cur_bucket_api_request import TenantVerifyCurBucketAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantVerifyCurBucketAPIRequest from a JSON string
tenant_verify_cur_bucket_api_request_instance = TenantVerifyCurBucketAPIRequest.from_json(json)
# print the JSON string representation of the object
print(TenantVerifyCurBucketAPIRequest.to_json())

# convert the object into a dict
tenant_verify_cur_bucket_api_request_dict = tenant_verify_cur_bucket_api_request_instance.to_dict()
# create an instance of TenantVerifyCurBucketAPIRequest from a dict
tenant_verify_cur_bucket_api_request_form_dict = tenant_verify_cur_bucket_api_request.from_dict(tenant_verify_cur_bucket_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


