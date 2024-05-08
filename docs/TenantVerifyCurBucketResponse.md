# TenantVerifyCurBucketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** | Cloud provider | 
**cloud_id** | **str** | Cloud ID | 
**parent_id** | **str** |  | [optional] 
**provider_config** | [**ProviderConfigOutput**](ProviderConfigOutput.md) |  | 
**id** | **str** | Unique ID for the Tenant Provider | 
**is_parent_account** | **bool** | billing account | 
**tenant_id** | **str** | Tenant ID | 
**is_billing_account** | **bool** | is billing account | 
**is_verified** | **bool** | is verified | 
**state** | [**TenantProviderState**](TenantProviderState.md) | state | 

## Example

```python
from onelens_backend_client.models.tenant_verify_cur_bucket_response import TenantVerifyCurBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantVerifyCurBucketResponse from a JSON string
tenant_verify_cur_bucket_response_instance = TenantVerifyCurBucketResponse.from_json(json)
# print the JSON string representation of the object
print(TenantVerifyCurBucketResponse.to_json())

# convert the object into a dict
tenant_verify_cur_bucket_response_dict = tenant_verify_cur_bucket_response_instance.to_dict()
# create an instance of TenantVerifyCurBucketResponse from a dict
tenant_verify_cur_bucket_response_form_dict = tenant_verify_cur_bucket_response.from_dict(tenant_verify_cur_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


