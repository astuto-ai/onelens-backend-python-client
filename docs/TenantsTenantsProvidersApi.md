# TenantsTenantsProvidersApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**disable_tenant_provider**](TenantsTenantsProvidersApi.md#disable_tenant_provider) | Disable Tenant Provider
[**enable_tenant_provider**](TenantsTenantsProvidersApi.md#enable_tenant_provider) | Enable Tenant Provider
[**get_tenant_provider**](TenantsTenantsProvidersApi.md#get_tenant_provider) | Get Tenant Provider
[**get_tenant_providers**](TenantsTenantsProvidersApi.md#get_tenant_providers) | Get Tenant Providers


# **disable_tenant_provider**
> ResponseSetTenantProviderStatusResponse disable_tenant_provider(tenant_id, tenant_provider_id)

Disable Tenant Provider

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_set_tenant_provider_status_response import ResponseSetTenantProviderStatusResponse
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
    api_instance = onelens_backend_client.TenantsTenantsProvidersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_provider_id = 'tenant_provider_id_example' # str | 

    try:
        # Disable Tenant Provider
        api_response = api_instance.disable_tenant_provider(tenant_id, tenant_provider_id)
        print("The response of TenantsTenantsProvidersApi->disable_tenant_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->disable_tenant_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_provider_id** | **str**|  | 

### Return type

[**ResponseSetTenantProviderStatusResponse**](ResponseSetTenantProviderStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_tenant_provider**
> ResponseSetTenantProviderStatusResponse enable_tenant_provider(tenant_id, tenant_provider_id)

Enable Tenant Provider

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_set_tenant_provider_status_response import ResponseSetTenantProviderStatusResponse
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
    api_instance = onelens_backend_client.TenantsTenantsProvidersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_provider_id = 'tenant_provider_id_example' # str | 

    try:
        # Enable Tenant Provider
        api_response = api_instance.enable_tenant_provider(tenant_id, tenant_provider_id)
        print("The response of TenantsTenantsProvidersApi->enable_tenant_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->enable_tenant_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_provider_id** | **str**|  | 

### Return type

[**ResponseSetTenantProviderStatusResponse**](ResponseSetTenantProviderStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_provider**
> ResponseGetTenantProviderByIDResponse get_tenant_provider(tenant_id, tenant_provider_id)

Get Tenant Provider

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_provider_by_id_response import ResponseGetTenantProviderByIDResponse
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
    api_instance = onelens_backend_client.TenantsTenantsProvidersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_provider_id = 'tenant_provider_id_example' # str | 

    try:
        # Get Tenant Provider
        api_response = api_instance.get_tenant_provider(tenant_id, tenant_provider_id)
        print("The response of TenantsTenantsProvidersApi->get_tenant_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->get_tenant_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_provider_id** | **str**|  | 

### Return type

[**ResponseGetTenantProviderByIDResponse**](ResponseGetTenantProviderByIDResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_providers**
> ResponseGetTenantProvidersResponse get_tenant_providers(get_tenant_providers_request)

Get Tenant Providers

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_providers_request import GetTenantProvidersRequest
from onelens_backend_client.models.response_get_tenant_providers_response import ResponseGetTenantProvidersResponse
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
    api_instance = onelens_backend_client.TenantsTenantsProvidersApi(api_client)
    get_tenant_providers_request = onelens_backend_client.GetTenantProvidersRequest() # GetTenantProvidersRequest | 

    try:
        # Get Tenant Providers
        api_response = api_instance.get_tenant_providers(get_tenant_providers_request)
        print("The response of TenantsTenantsProvidersApi->get_tenant_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->get_tenant_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_providers_request** | [**GetTenantProvidersRequest**](GetTenantProvidersRequest.md)|  | 

### Return type

[**ResponseGetTenantProvidersResponse**](ResponseGetTenantProvidersResponse.md)

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

