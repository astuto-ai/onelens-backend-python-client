# TenantConnectionServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_connection**](TenantConnectionServiceApi.md#create_tenant_connection) | Creates a new tenant connection.
[**get_tenant_connection**](TenantConnectionServiceApi.md#get_tenant_connection) | Retrieves a tenant connection by tenant_id and connection_type.
[**migrate**](TenantConnectionServiceApi.md#migrate) | Migrate


# **create_tenant_connection**
> GetTenantConnectionResponse create_tenant_connection(create_tenant_connection_request)

Creates a new tenant connection.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_connection_request import CreateTenantConnectionRequest
from onelens_backend_client.models.get_tenant_connection_response import GetTenantConnectionResponse
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
    api_instance = onelens_backend_client.TenantConnectionServiceApi(api_client)
    create_tenant_connection_request = onelens_backend_client.CreateTenantConnectionRequest() # CreateTenantConnectionRequest | 

    try:
        # Creates a new tenant connection.
        api_response = api_instance.create_tenant_connection(create_tenant_connection_request)
        print("The response of TenantConnectionServiceApi->create_tenant_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantConnectionServiceApi->create_tenant_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_connection_request** | [**CreateTenantConnectionRequest**](CreateTenantConnectionRequest.md)|  | 

### Return type

[**GetTenantConnectionResponse**](GetTenantConnectionResponse.md)

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

# **get_tenant_connection**
> GetTenantConnectionResponse get_tenant_connection(get_tenant_connection_request)

Retrieves a tenant connection by tenant_id and connection_type.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_connection_request import GetTenantConnectionRequest
from onelens_backend_client.models.get_tenant_connection_response import GetTenantConnectionResponse
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
    api_instance = onelens_backend_client.TenantConnectionServiceApi(api_client)
    get_tenant_connection_request = onelens_backend_client.GetTenantConnectionRequest() # GetTenantConnectionRequest | 

    try:
        # Retrieves a tenant connection by tenant_id and connection_type.
        api_response = api_instance.get_tenant_connection(get_tenant_connection_request)
        print("The response of TenantConnectionServiceApi->get_tenant_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantConnectionServiceApi->get_tenant_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_connection_request** | [**GetTenantConnectionRequest**](GetTenantConnectionRequest.md)|  | 

### Return type

[**GetTenantConnectionResponse**](GetTenantConnectionResponse.md)

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

# **migrate**
> object migrate(body)

Migrate

### Example


```python
import onelens_backend_client
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
    api_instance = onelens_backend_client.TenantConnectionServiceApi(api_client)
    body = None # object | 

    try:
        # Migrate
        api_response = api_instance.migrate(body)
        print("The response of TenantConnectionServiceApi->migrate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantConnectionServiceApi->migrate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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

