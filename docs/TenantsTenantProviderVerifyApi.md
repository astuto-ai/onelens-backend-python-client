# TenantsTenantProviderVerifyApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**verify_tenant**](TenantsTenantProviderVerifyApi.md#verify_tenant) | Verify Tenant


# **verify_tenant**
> ResponseTenantVerifyResponse verify_tenant(tenant_id, tenant_provider_id, tenant_verify_request)

Verify Tenant

An API endpoint that verified the tenant IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_tenant_verify_response import ResponseTenantVerifyResponse
from onelens_backend_client.models.tenant_verify_request import TenantVerifyRequest
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
    api_instance = onelens_backend_client.TenantsTenantProviderVerifyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_provider_id = 'tenant_provider_id_example' # str | 
    tenant_verify_request = onelens_backend_client.TenantVerifyRequest() # TenantVerifyRequest | 

    try:
        # Verify Tenant
        api_response = api_instance.verify_tenant(tenant_id, tenant_provider_id, tenant_verify_request)
        print("The response of TenantsTenantProviderVerifyApi->verify_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantProviderVerifyApi->verify_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_provider_id** | **str**|  | 
 **tenant_verify_request** | [**TenantVerifyRequest**](TenantVerifyRequest.md)|  | 

### Return type

[**ResponseTenantVerifyResponse**](ResponseTenantVerifyResponse.md)

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

