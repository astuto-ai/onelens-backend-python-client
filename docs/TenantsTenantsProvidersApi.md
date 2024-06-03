# TenantsTenantsProvidersApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_provider**](TenantsTenantsProvidersApi.md#create_tenant_provider) | Create Tenant Provider
[**create_tenant_provider_0**](TenantsTenantsProvidersApi.md#create_tenant_provider_0) | Create Tenant Provider
[**disable_tenant_provider**](TenantsTenantsProvidersApi.md#disable_tenant_provider) | Disable Tenant Provider
[**disable_tenant_provider_0**](TenantsTenantsProvidersApi.md#disable_tenant_provider_0) | Disable Tenant Provider
[**enable_tenant_provider**](TenantsTenantsProvidersApi.md#enable_tenant_provider) | Enable Tenant Provider
[**enable_tenant_provider_0**](TenantsTenantsProvidersApi.md#enable_tenant_provider_0) | Enable Tenant Provider
[**get_tenant_provider**](TenantsTenantsProvidersApi.md#get_tenant_provider) | Get Tenant Provider
[**get_tenant_provider_0**](TenantsTenantsProvidersApi.md#get_tenant_provider_0) | Get Tenant Provider
[**get_tenant_providers**](TenantsTenantsProvidersApi.md#get_tenant_providers) | Get Tenant Providers
[**update_tenant_provider**](TenantsTenantsProvidersApi.md#update_tenant_provider) | Update Tenant Provider
[**update_tenant_provider_0**](TenantsTenantsProvidersApi.md#update_tenant_provider_0) | Update Tenant Provider


# **create_tenant_provider**
> CreateTenantProviderResponse create_tenant_provider(tenant_id, create_tenant_provider_request)

Create Tenant Provider

An API endpoint that retrieves tenant with tenant IDs.

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
    api_instance = onelens_backend_client.TenantsTenantsProvidersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    create_tenant_provider_request = onelens_backend_client.CreateTenantProviderRequest() # CreateTenantProviderRequest | 

    try:
        # Create Tenant Provider
        api_response = api_instance.create_tenant_provider(tenant_id, create_tenant_provider_request)
        print("The response of TenantsTenantsProvidersApi->create_tenant_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->create_tenant_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
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

# **create_tenant_provider_0**
> CreateTenantProviderResponse create_tenant_provider_0(create_tenant_provider_request)

Create Tenant Provider

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
    api_instance = onelens_backend_client.TenantsTenantsProvidersApi(api_client)
    create_tenant_provider_request = onelens_backend_client.CreateTenantProviderRequest() # CreateTenantProviderRequest | 

    try:
        # Create Tenant Provider
        api_response = api_instance.create_tenant_provider_0(create_tenant_provider_request)
        print("The response of TenantsTenantsProvidersApi->create_tenant_provider_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->create_tenant_provider_0: %s\n" % e)
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

# **disable_tenant_provider_0**
> ResponseSetTenantProviderStatusResponse disable_tenant_provider_0(tenant_provider_id)

Disable Tenant Provider

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
    tenant_provider_id = 'tenant_provider_id_example' # str | 

    try:
        # Disable Tenant Provider
        api_response = api_instance.disable_tenant_provider_0(tenant_provider_id)
        print("The response of TenantsTenantsProvidersApi->disable_tenant_provider_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->disable_tenant_provider_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **enable_tenant_provider_0**
> ResponseSetTenantProviderStatusResponse enable_tenant_provider_0(tenant_provider_id)

Enable Tenant Provider

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
    tenant_provider_id = 'tenant_provider_id_example' # str | 

    try:
        # Enable Tenant Provider
        api_response = api_instance.enable_tenant_provider_0(tenant_provider_id)
        print("The response of TenantsTenantsProvidersApi->enable_tenant_provider_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->enable_tenant_provider_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_tenant_provider_0**
> ResponseGetTenantProviderByIDResponse get_tenant_provider_0(tenant_provider_id)

Get Tenant Provider

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
    tenant_provider_id = 'tenant_provider_id_example' # str | 

    try:
        # Get Tenant Provider
        api_response = api_instance.get_tenant_provider_0(tenant_provider_id)
        print("The response of TenantsTenantsProvidersApi->get_tenant_provider_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->get_tenant_provider_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **update_tenant_provider**
> ResponseUpdateTenantProviderResponse update_tenant_provider(tenant_id, tenant_provider_id, update_tenant_provider_request)

Update Tenant Provider

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_provider_response import ResponseUpdateTenantProviderResponse
from onelens_backend_client.models.update_tenant_provider_request import UpdateTenantProviderRequest
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
    update_tenant_provider_request = onelens_backend_client.UpdateTenantProviderRequest() # UpdateTenantProviderRequest | 

    try:
        # Update Tenant Provider
        api_response = api_instance.update_tenant_provider(tenant_id, tenant_provider_id, update_tenant_provider_request)
        print("The response of TenantsTenantsProvidersApi->update_tenant_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->update_tenant_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_provider_id** | **str**|  | 
 **update_tenant_provider_request** | [**UpdateTenantProviderRequest**](UpdateTenantProviderRequest.md)|  | 

### Return type

[**ResponseUpdateTenantProviderResponse**](ResponseUpdateTenantProviderResponse.md)

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

# **update_tenant_provider_0**
> ResponseUpdateTenantProviderResponse update_tenant_provider_0(tenant_provider_id, update_tenant_provider_request)

Update Tenant Provider

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_provider_response import ResponseUpdateTenantProviderResponse
from onelens_backend_client.models.update_tenant_provider_request import UpdateTenantProviderRequest
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
    tenant_provider_id = 'tenant_provider_id_example' # str | 
    update_tenant_provider_request = onelens_backend_client.UpdateTenantProviderRequest() # UpdateTenantProviderRequest | 

    try:
        # Update Tenant Provider
        api_response = api_instance.update_tenant_provider_0(tenant_provider_id, update_tenant_provider_request)
        print("The response of TenantsTenantsProvidersApi->update_tenant_provider_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->update_tenant_provider_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_provider_id** | **str**|  | 
 **update_tenant_provider_request** | [**UpdateTenantProviderRequest**](UpdateTenantProviderRequest.md)|  | 

### Return type

[**ResponseUpdateTenantProviderResponse**](ResponseUpdateTenantProviderResponse.md)

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

