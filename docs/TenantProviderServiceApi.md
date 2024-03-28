# TenantProviderServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_provider**](TenantProviderServiceApi.md#create_tenant_provider) | Creates a new tenant Provider.
[**get_tenant_provider_by_id**](TenantProviderServiceApi.md#get_tenant_provider_by_id) | Retrieves a Tenant Provider by its unique identifier.
[**get_tenant_providers**](TenantProviderServiceApi.md#get_tenant_providers) | Retrieves all tenant providers.


# **create_tenant_provider**
> CreateTenantProviderResponse create_tenant_provider(create_tenant_provider_request)

Creates a new tenant Provider.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_provider_request import CreateTenantProviderRequest
from onelens_backend_client.models.create_tenant_provider_response import CreateTenantProviderResponse
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
    api_instance = onelens_backend_client.TenantProviderServiceApi(api_client)
    create_tenant_provider_request = onelens_backend_client.CreateTenantProviderRequest() # CreateTenantProviderRequest | 

    try:
        # Creates a new tenant Provider.
        api_response = api_instance.create_tenant_provider(create_tenant_provider_request)
        print("The response of TenantProviderServiceApi->create_tenant_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantProviderServiceApi->create_tenant_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_provider_request** | [**CreateTenantProviderRequest**](CreateTenantProviderRequest.md)|  | 

### Return type

[**CreateTenantProviderResponse**](CreateTenantProviderResponse.md)

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

# **get_tenant_provider_by_id**
> GetTenantProviderByIDResponse get_tenant_provider_by_id(get_tenant_provider_by_id_request)

Retrieves a Tenant Provider by its unique identifier.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_provider_by_id_request import GetTenantProviderByIDRequest
from onelens_backend_client.models.get_tenant_provider_by_id_response import GetTenantProviderByIDResponse
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
    api_instance = onelens_backend_client.TenantProviderServiceApi(api_client)
    get_tenant_provider_by_id_request = onelens_backend_client.GetTenantProviderByIDRequest() # GetTenantProviderByIDRequest | 

    try:
        # Retrieves a Tenant Provider by its unique identifier.
        api_response = api_instance.get_tenant_provider_by_id(get_tenant_provider_by_id_request)
        print("The response of TenantProviderServiceApi->get_tenant_provider_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantProviderServiceApi->get_tenant_provider_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_provider_by_id_request** | [**GetTenantProviderByIDRequest**](GetTenantProviderByIDRequest.md)|  | 

### Return type

[**GetTenantProviderByIDResponse**](GetTenantProviderByIDResponse.md)

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

# **get_tenant_providers**
> GetTenantProvidersResponse get_tenant_providers(get_tenant_providers_request)

Retrieves all tenant providers.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_providers_request import GetTenantProvidersRequest
from onelens_backend_client.models.get_tenant_providers_response import GetTenantProvidersResponse
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
    api_instance = onelens_backend_client.TenantProviderServiceApi(api_client)
    get_tenant_providers_request = onelens_backend_client.GetTenantProvidersRequest() # GetTenantProvidersRequest | 

    try:
        # Retrieves all tenant providers.
        api_response = api_instance.get_tenant_providers(get_tenant_providers_request)
        print("The response of TenantProviderServiceApi->get_tenant_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantProviderServiceApi->get_tenant_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_providers_request** | [**GetTenantProvidersRequest**](GetTenantProvidersRequest.md)|  | 

### Return type

[**GetTenantProvidersResponse**](GetTenantProvidersResponse.md)

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

