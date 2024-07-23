# TenantEmbedAppsLinksServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_embed_apps_links**](TenantEmbedAppsLinksServiceApi.md#create_tenant_embed_apps_links) | Creates tenant embed apps links.
[**delete_tenant_embed_apps_links**](TenantEmbedAppsLinksServiceApi.md#delete_tenant_embed_apps_links) | Deletes tenant embed apps links.
[**get_all_tenant_embed_apps_links**](TenantEmbedAppsLinksServiceApi.md#get_all_tenant_embed_apps_links) | Retrieves tenant embed apps links.
[**get_tenant_embed_apps_link_by_id**](TenantEmbedAppsLinksServiceApi.md#get_tenant_embed_apps_link_by_id) | Retrieves tenant embed apps links.
[**update_tenant_embed_apps_links**](TenantEmbedAppsLinksServiceApi.md#update_tenant_embed_apps_links) | Updates tenant embed apps links.


# **create_tenant_embed_apps_links**
> CreateTenantEmbedAppsLinksResponse create_tenant_embed_apps_links(create_tenant_embed_apps_links_request)

Creates tenant embed apps links.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_embed_apps_links_request import CreateTenantEmbedAppsLinksRequest
from onelens_backend_client.models.create_tenant_embed_apps_links_response import CreateTenantEmbedAppsLinksResponse
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
    api_instance = onelens_backend_client.TenantEmbedAppsLinksServiceApi(api_client)
    create_tenant_embed_apps_links_request = onelens_backend_client.CreateTenantEmbedAppsLinksRequest() # CreateTenantEmbedAppsLinksRequest | 

    try:
        # Creates tenant embed apps links.
        api_response = api_instance.create_tenant_embed_apps_links(create_tenant_embed_apps_links_request)
        print("The response of TenantEmbedAppsLinksServiceApi->create_tenant_embed_apps_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantEmbedAppsLinksServiceApi->create_tenant_embed_apps_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_embed_apps_links_request** | [**CreateTenantEmbedAppsLinksRequest**](CreateTenantEmbedAppsLinksRequest.md)|  | 

### Return type

[**CreateTenantEmbedAppsLinksResponse**](CreateTenantEmbedAppsLinksResponse.md)

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

# **delete_tenant_embed_apps_links**
> object delete_tenant_embed_apps_links(get_tenant_embed_apps_links_request)

Deletes tenant embed apps links.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_embed_apps_links_request import GetTenantEmbedAppsLinksRequest
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
    api_instance = onelens_backend_client.TenantEmbedAppsLinksServiceApi(api_client)
    get_tenant_embed_apps_links_request = onelens_backend_client.GetTenantEmbedAppsLinksRequest() # GetTenantEmbedAppsLinksRequest | 

    try:
        # Deletes tenant embed apps links.
        api_response = api_instance.delete_tenant_embed_apps_links(get_tenant_embed_apps_links_request)
        print("The response of TenantEmbedAppsLinksServiceApi->delete_tenant_embed_apps_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantEmbedAppsLinksServiceApi->delete_tenant_embed_apps_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_embed_apps_links_request** | [**GetTenantEmbedAppsLinksRequest**](GetTenantEmbedAppsLinksRequest.md)|  | 

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

# **get_all_tenant_embed_apps_links**
> object get_all_tenant_embed_apps_links(get_all_tenant_embed_apps_links_request)

Retrieves tenant embed apps links.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_tenant_embed_apps_links_request import GetAllTenantEmbedAppsLinksRequest
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
    api_instance = onelens_backend_client.TenantEmbedAppsLinksServiceApi(api_client)
    get_all_tenant_embed_apps_links_request = onelens_backend_client.GetAllTenantEmbedAppsLinksRequest() # GetAllTenantEmbedAppsLinksRequest | 

    try:
        # Retrieves tenant embed apps links.
        api_response = api_instance.get_all_tenant_embed_apps_links(get_all_tenant_embed_apps_links_request)
        print("The response of TenantEmbedAppsLinksServiceApi->get_all_tenant_embed_apps_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantEmbedAppsLinksServiceApi->get_all_tenant_embed_apps_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_all_tenant_embed_apps_links_request** | [**GetAllTenantEmbedAppsLinksRequest**](GetAllTenantEmbedAppsLinksRequest.md)|  | 

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

# **get_tenant_embed_apps_link_by_id**
> GetTenantEmbedAppsLinksResponse get_tenant_embed_apps_link_by_id(get_tenant_embed_apps_links_request)

Retrieves tenant embed apps links.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_embed_apps_links_request import GetTenantEmbedAppsLinksRequest
from onelens_backend_client.models.get_tenant_embed_apps_links_response import GetTenantEmbedAppsLinksResponse
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
    api_instance = onelens_backend_client.TenantEmbedAppsLinksServiceApi(api_client)
    get_tenant_embed_apps_links_request = onelens_backend_client.GetTenantEmbedAppsLinksRequest() # GetTenantEmbedAppsLinksRequest | 

    try:
        # Retrieves tenant embed apps links.
        api_response = api_instance.get_tenant_embed_apps_link_by_id(get_tenant_embed_apps_links_request)
        print("The response of TenantEmbedAppsLinksServiceApi->get_tenant_embed_apps_link_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantEmbedAppsLinksServiceApi->get_tenant_embed_apps_link_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_embed_apps_links_request** | [**GetTenantEmbedAppsLinksRequest**](GetTenantEmbedAppsLinksRequest.md)|  | 

### Return type

[**GetTenantEmbedAppsLinksResponse**](GetTenantEmbedAppsLinksResponse.md)

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

# **update_tenant_embed_apps_links**
> UpdateTenantEmbedAppsLinksResponse update_tenant_embed_apps_links(request)

Updates tenant embed apps links.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_tenant_embed_apps_links_response import UpdateTenantEmbedAppsLinksResponse
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
    api_instance = onelens_backend_client.TenantEmbedAppsLinksServiceApi(api_client)
    request = 'request_example' # str | 

    try:
        # Updates tenant embed apps links.
        api_response = api_instance.update_tenant_embed_apps_links(request)
        print("The response of TenantEmbedAppsLinksServiceApi->update_tenant_embed_apps_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantEmbedAppsLinksServiceApi->update_tenant_embed_apps_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **str**|  | 

### Return type

[**UpdateTenantEmbedAppsLinksResponse**](UpdateTenantEmbedAppsLinksResponse.md)

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

