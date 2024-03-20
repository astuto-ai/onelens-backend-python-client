# TenantServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant**](TenantServiceApi.md#create_tenant) | Creates a new tenant.
[**disable_tenant**](TenantServiceApi.md#disable_tenant) | Disables a tenant.
[**get_tenant_by_id**](TenantServiceApi.md#get_tenant_by_id) | Retrieves a tenant by its unique identifier.
[**get_tenants**](TenantServiceApi.md#get_tenants) | Retrieves all Tenants with filters.
[**update_tenant**](TenantServiceApi.md#update_tenant) | Updates an existing tenant.


# **create_tenant**
> CreateTenantResponse create_tenant(create_tenant_request)

Creates a new tenant.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_request import CreateTenantRequest
from onelens_backend_client.models.create_tenant_response import CreateTenantResponse
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
    api_instance = onelens_backend_client.TenantServiceApi(api_client)
    create_tenant_request = onelens_backend_client.CreateTenantRequest() # CreateTenantRequest | 

    try:
        # Creates a new tenant.
        api_response = api_instance.create_tenant(create_tenant_request)
        print("The response of TenantServiceApi->create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantServiceApi->create_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_request** | [**CreateTenantRequest**](CreateTenantRequest.md)|  | 

### Return type

[**CreateTenantResponse**](CreateTenantResponse.md)

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

# **disable_tenant**
> object disable_tenant(disable_tenant_request)

Disables a tenant.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.disable_tenant_request import DisableTenantRequest
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
    api_instance = onelens_backend_client.TenantServiceApi(api_client)
    disable_tenant_request = onelens_backend_client.DisableTenantRequest() # DisableTenantRequest | 

    try:
        # Disables a tenant.
        api_response = api_instance.disable_tenant(disable_tenant_request)
        print("The response of TenantServiceApi->disable_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantServiceApi->disable_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_tenant_request** | [**DisableTenantRequest**](DisableTenantRequest.md)|  | 

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

# **get_tenant_by_id**
> GetTenantByIDResponse get_tenant_by_id(get_tenant_by_id_request)

Retrieves a tenant by its unique identifier.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_by_id_response import GetTenantByIDResponse
from onelens_backend_client.models.get_tenant_by_id_request import GetTenantByIdRequest
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
    api_instance = onelens_backend_client.TenantServiceApi(api_client)
    get_tenant_by_id_request = onelens_backend_client.GetTenantByIdRequest() # GetTenantByIdRequest | 

    try:
        # Retrieves a tenant by its unique identifier.
        api_response = api_instance.get_tenant_by_id(get_tenant_by_id_request)
        print("The response of TenantServiceApi->get_tenant_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantServiceApi->get_tenant_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_by_id_request** | [**GetTenantByIdRequest**](GetTenantByIdRequest.md)|  | 

### Return type

[**GetTenantByIDResponse**](GetTenantByIDResponse.md)

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

# **get_tenants**
> GetTenantsResponse get_tenants(get_tenants_request)

Retrieves all Tenants with filters.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenants_request import GetTenantsRequest
from onelens_backend_client.models.get_tenants_response import GetTenantsResponse
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
    api_instance = onelens_backend_client.TenantServiceApi(api_client)
    get_tenants_request = onelens_backend_client.GetTenantsRequest() # GetTenantsRequest | 

    try:
        # Retrieves all Tenants with filters.
        api_response = api_instance.get_tenants(get_tenants_request)
        print("The response of TenantServiceApi->get_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantServiceApi->get_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenants_request** | [**GetTenantsRequest**](GetTenantsRequest.md)|  | 

### Return type

[**GetTenantsResponse**](GetTenantsResponse.md)

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

# **update_tenant**
> UpdateTenantResponse update_tenant(update_tenant_request)

Updates an existing tenant.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_tenant_request import UpdateTenantRequest
from onelens_backend_client.models.update_tenant_response import UpdateTenantResponse
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
    api_instance = onelens_backend_client.TenantServiceApi(api_client)
    update_tenant_request = onelens_backend_client.UpdateTenantRequest() # UpdateTenantRequest | 

    try:
        # Updates an existing tenant.
        api_response = api_instance.update_tenant(update_tenant_request)
        print("The response of TenantServiceApi->update_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantServiceApi->update_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tenant_request** | [**UpdateTenantRequest**](UpdateTenantRequest.md)|  | 

### Return type

[**UpdateTenantResponse**](UpdateTenantResponse.md)

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

