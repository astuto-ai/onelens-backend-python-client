# TenantsApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant**](TenantsApi.md#create_tenant) | Create Tenant
[**disable_tenant**](TenantsApi.md#disable_tenant) | Disable Tenant
[**get_tenant**](TenantsApi.md#get_tenant) | Get Tenant
[**get_tenants**](TenantsApi.md#get_tenants) | Get Tenants
[**update_tenant**](TenantsApi.md#update_tenant) | Update Tenant


# **create_tenant**
> CreateTenantResponse create_tenant(create_tenant_request)

Create Tenant

An API endpoint that retrieves tenant with tenant IDs.

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
    api_instance = onelens_backend_client.TenantsApi(api_client)
    create_tenant_request = onelens_backend_client.CreateTenantRequest() # CreateTenantRequest | 

    try:
        # Create Tenant
        api_response = api_instance.create_tenant(create_tenant_request)
        print("The response of TenantsApi->create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->create_tenant: %s\n" % e)
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
> ResponseDisableTenantResponse disable_tenant(tenant_id)

Disable Tenant

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_disable_tenant_response import ResponseDisableTenantResponse
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
    api_instance = onelens_backend_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Disable Tenant
        api_response = api_instance.disable_tenant(tenant_id)
        print("The response of TenantsApi->disable_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->disable_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ResponseDisableTenantResponse**](ResponseDisableTenantResponse.md)

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

# **get_tenant**
> ResponseGetTenantByIDResponse get_tenant(tenant_id)

Get Tenant

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_by_id_response import ResponseGetTenantByIDResponse
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
    api_instance = onelens_backend_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get Tenant
        api_response = api_instance.get_tenant(tenant_id)
        print("The response of TenantsApi->get_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ResponseGetTenantByIDResponse**](ResponseGetTenantByIDResponse.md)

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

# **get_tenants**
> ResponseGetTenantsResponse get_tenants(get_tenants_request)

Get Tenants

An API endpoint that retrieves tenant with filters.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenants_request import GetTenantsRequest
from onelens_backend_client.models.response_get_tenants_response import ResponseGetTenantsResponse
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
    api_instance = onelens_backend_client.TenantsApi(api_client)
    get_tenants_request = onelens_backend_client.GetTenantsRequest() # GetTenantsRequest | 

    try:
        # Get Tenants
        api_response = api_instance.get_tenants(get_tenants_request)
        print("The response of TenantsApi->get_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenants_request** | [**GetTenantsRequest**](GetTenantsRequest.md)|  | 

### Return type

[**ResponseGetTenantsResponse**](ResponseGetTenantsResponse.md)

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
> ResponseUpdateTenantResponse update_tenant(tenant_id, update_tenant_request)

Update Tenant

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_response import ResponseUpdateTenantResponse
from onelens_backend_client.models.update_tenant_request import UpdateTenantRequest
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
    api_instance = onelens_backend_client.TenantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    update_tenant_request = onelens_backend_client.UpdateTenantRequest() # UpdateTenantRequest | 

    try:
        # Update Tenant
        api_response = api_instance.update_tenant(tenant_id, update_tenant_request)
        print("The response of TenantsApi->update_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->update_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **update_tenant_request** | [**UpdateTenantRequest**](UpdateTenantRequest.md)|  | 

### Return type

[**ResponseUpdateTenantResponse**](ResponseUpdateTenantResponse.md)

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

