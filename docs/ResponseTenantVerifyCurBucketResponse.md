# ResponseTenantVerifyCurBucketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TenantVerifyCurBucketResponse**](TenantVerifyCurBucketResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_tenant_verify_cur_bucket_response import ResponseTenantVerifyCurBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseTenantVerifyCurBucketResponse from a JSON string
response_tenant_verify_cur_bucket_response_instance = ResponseTenantVerifyCurBucketResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseTenantVerifyCurBucketResponse.to_json())

# convert the object into a dict
response_tenant_verify_cur_bucket_response_dict = response_tenant_verify_cur_bucket_response_instance.to_dict()
# create an instance of ResponseTenantVerifyCurBucketResponse from a dict
response_tenant_verify_cur_bucket_response_form_dict = response_tenant_verify_cur_bucket_response.from_dict(response_tenant_verify_cur_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


