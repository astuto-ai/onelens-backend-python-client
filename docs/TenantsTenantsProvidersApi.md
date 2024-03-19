# openapi_client.TenantsTenantsProvidersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_provider_v1_tenants_tenant_id_providers_post**](TenantsTenantsProvidersApi.md#create_tenant_provider_v1_tenants_tenant_id_providers_post) | **POST** /v1/tenants/{tenant_id}/providers | Create Tenant Provider
[**disable_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_disable_put**](TenantsTenantsProvidersApi.md#disable_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_disable_put) | **PUT** /v1/tenants/{tenant_id}/providers/{tenant_provider_id}/disable | Disable Tenant Provider
[**get_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_get**](TenantsTenantsProvidersApi.md#get_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_get) | **GET** /v1/tenants/{tenant_id}/providers/{tenant_provider_id} | Get Tenant Provider
[**get_tenant_providers_v1_tenants_providers_fetch_post**](TenantsTenantsProvidersApi.md#get_tenant_providers_v1_tenants_providers_fetch_post) | **POST** /v1/tenants/providers/fetch | Get Tenant Providers
[**update_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_put**](TenantsTenantsProvidersApi.md#update_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_put) | **PUT** /v1/tenants/{tenant_id}/providers/{tenant_provider_id} | Update Tenant Provider


# **create_tenant_provider_v1_tenants_tenant_id_providers_post**
> CreateTenantProviderResponse create_tenant_provider_v1_tenants_tenant_id_providers_post(tenant_id, create_tenant_provider_request)

Create Tenant Provider

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import openapi_client
from openapi_client.models.create_tenant_provider_request import CreateTenantProviderRequest
from openapi_client.models.create_tenant_provider_response import CreateTenantProviderResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsTenantsProvidersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    create_tenant_provider_request = openapi_client.CreateTenantProviderRequest() # CreateTenantProviderRequest | 

    try:
        # Create Tenant Provider
        api_response = api_instance.create_tenant_provider_v1_tenants_tenant_id_providers_post(tenant_id, create_tenant_provider_request)
        print("The response of TenantsTenantsProvidersApi->create_tenant_provider_v1_tenants_tenant_id_providers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->create_tenant_provider_v1_tenants_tenant_id_providers_post: %s\n" % e)
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

# **disable_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_disable_put**
> ResponseDisableTenantProviderResponse disable_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_disable_put(tenant_id, tenant_provider_id)

Disable Tenant Provider

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import openapi_client
from openapi_client.models.response_disable_tenant_provider_response import ResponseDisableTenantProviderResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsTenantsProvidersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_provider_id = 'tenant_provider_id_example' # str | 

    try:
        # Disable Tenant Provider
        api_response = api_instance.disable_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_disable_put(tenant_id, tenant_provider_id)
        print("The response of TenantsTenantsProvidersApi->disable_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_disable_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->disable_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_disable_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_provider_id** | **str**|  | 

### Return type

[**ResponseDisableTenantProviderResponse**](ResponseDisableTenantProviderResponse.md)

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

# **get_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_get**
> ResponseGetTenantProviderByIDResponse get_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_get(tenant_id, tenant_provider_id)

Get Tenant Provider

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import openapi_client
from openapi_client.models.response_get_tenant_provider_by_id_response import ResponseGetTenantProviderByIDResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsTenantsProvidersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_provider_id = 'tenant_provider_id_example' # str | 

    try:
        # Get Tenant Provider
        api_response = api_instance.get_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_get(tenant_id, tenant_provider_id)
        print("The response of TenantsTenantsProvidersApi->get_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->get_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_get: %s\n" % e)
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

# **get_tenant_providers_v1_tenants_providers_fetch_post**
> ResponseGetTenantProvidersResponse get_tenant_providers_v1_tenants_providers_fetch_post(get_tenant_providers_request)

Get Tenant Providers

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import openapi_client
from openapi_client.models.get_tenant_providers_request import GetTenantProvidersRequest
from openapi_client.models.response_get_tenant_providers_response import ResponseGetTenantProvidersResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsTenantsProvidersApi(api_client)
    get_tenant_providers_request = openapi_client.GetTenantProvidersRequest() # GetTenantProvidersRequest | 

    try:
        # Get Tenant Providers
        api_response = api_instance.get_tenant_providers_v1_tenants_providers_fetch_post(get_tenant_providers_request)
        print("The response of TenantsTenantsProvidersApi->get_tenant_providers_v1_tenants_providers_fetch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->get_tenant_providers_v1_tenants_providers_fetch_post: %s\n" % e)
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

# **update_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_put**
> ResponseUpdateTenantProviderResponse update_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_put(tenant_id, tenant_provider_id, update_tenant_provider_request)

Update Tenant Provider

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import openapi_client
from openapi_client.models.response_update_tenant_provider_response import ResponseUpdateTenantProviderResponse
from openapi_client.models.update_tenant_provider_request import UpdateTenantProviderRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantsTenantsProvidersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_provider_id = 'tenant_provider_id_example' # str | 
    update_tenant_provider_request = openapi_client.UpdateTenantProviderRequest() # UpdateTenantProviderRequest | 

    try:
        # Update Tenant Provider
        api_response = api_instance.update_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_put(tenant_id, tenant_provider_id, update_tenant_provider_request)
        print("The response of TenantsTenantsProvidersApi->update_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantsProvidersApi->update_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_put: %s\n" % e)
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

