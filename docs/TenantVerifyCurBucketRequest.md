# TenantVerifyCurBucketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cur_bucket_config** | [**CurBucketConfig**](CurBucketConfig.md) | cur bucket config | 
**cloud_id** | **str** | cloud id | 
**tenant_id** | **str** | Tenant ID | 

## Example

```python
from onelens_backend_client.models.tenant_verify_cur_bucket_request import TenantVerifyCurBucketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantVerifyCurBucketRequest from a JSON string
tenant_verify_cur_bucket_request_instance = TenantVerifyCurBucketRequest.from_json(json)
# print the JSON string representation of the object
print(TenantVerifyCurBucketRequest.to_json())

# convert the object into a dict
tenant_verify_cur_bucket_request_dict = tenant_verify_cur_bucket_request_instance.to_dict()
# create an instance of TenantVerifyCurBucketRequest from a dict
tenant_verify_cur_bucket_request_form_dict = tenant_verify_cur_bucket_request.from_dict(tenant_verify_cur_bucket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


