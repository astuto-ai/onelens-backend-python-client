# TenantVerifyServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**verify_tenant**](TenantVerifyServiceApi.md#verify_tenant) | Verify Tenant
[**verify_tenant_cur_bucket**](TenantVerifyServiceApi.md#verify_tenant_cur_bucket) | Verify Tenant Cur Bucket


# **verify_tenant**
> TenantVerifyResponse verify_tenant(tenant_verify_request_with_user)

Verify Tenant

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.tenant_verify_request_with_user import TenantVerifyRequestWithUser
from onelens_backend_client.models.tenant_verify_response import TenantVerifyResponse
from onelens_backend_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = onelens_backend_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with onelens_backend_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelens_backend_client.TenantVerifyServiceApi(api_client)
    tenant_verify_request_with_user = onelens_backend_client.TenantVerifyRequestWithUser() # TenantVerifyRequestWithUser | 

    try:
        # Verify Tenant
        api_response = api_instance.verify_tenant(tenant_verify_request_with_user)
        print("The response of TenantVerifyServiceApi->verify_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantVerifyServiceApi->verify_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_verify_request_with_user** | [**TenantVerifyRequestWithUser**](TenantVerifyRequestWithUser.md)|  | 

### Return type

[**TenantVerifyResponse**](TenantVerifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_tenant_cur_bucket**
> object verify_tenant_cur_bucket(tenant_verify_cur_bucket_request)

Verify Tenant Cur Bucket

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.tenant_verify_cur_bucket_request import TenantVerifyCurBucketRequest
from onelens_backend_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = onelens_backend_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with onelens_backend_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelens_backend_client.TenantVerifyServiceApi(api_client)
    tenant_verify_cur_bucket_request = onelens_backend_client.TenantVerifyCurBucketRequest() # TenantVerifyCurBucketRequest | 

    try:
        # Verify Tenant Cur Bucket
        api_response = api_instance.verify_tenant_cur_bucket(tenant_verify_cur_bucket_request)
        print("The response of TenantVerifyServiceApi->verify_tenant_cur_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantVerifyServiceApi->verify_tenant_cur_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_verify_cur_bucket_request** | [**TenantVerifyCurBucketRequest**](TenantVerifyCurBucketRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

