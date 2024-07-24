# TenantEmbedAppsAndLinksApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_embed_apps_links**](TenantEmbedAppsAndLinksApi.md#create_tenant_embed_apps_links) | Create Tenant Embed Apps Links
[**delete_tenant_embed_apps_links**](TenantEmbedAppsAndLinksApi.md#delete_tenant_embed_apps_links) | Delete Tenant Embed Apps Links
[**get_all_tenant_embed_apps_links**](TenantEmbedAppsAndLinksApi.md#get_all_tenant_embed_apps_links) | Get All Tenant Embed Apps Links
[**get_tenant_embed_apps_link_by_id**](TenantEmbedAppsAndLinksApi.md#get_tenant_embed_apps_link_by_id) | Get Tenant Embed Apps Link By Id
[**update_tenant_embed_apps_links**](TenantEmbedAppsAndLinksApi.md#update_tenant_embed_apps_links) | Update Tenant Embed Apps Links


# **create_tenant_embed_apps_links**
> ResponseCreateTenantEmbedAppsLinksResponse create_tenant_embed_apps_links(create_tenant_embed_apps_links_request)

Create Tenant Embed Apps Links

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_embed_apps_links_request import CreateTenantEmbedAppsLinksRequest
from onelens_backend_client.models.response_create_tenant_embed_apps_links_response import ResponseCreateTenantEmbedAppsLinksResponse
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
    api_instance = onelens_backend_client.TenantEmbedAppsAndLinksApi(api_client)
    create_tenant_embed_apps_links_request = onelens_backend_client.CreateTenantEmbedAppsLinksRequest() # CreateTenantEmbedAppsLinksRequest | 

    try:
        # Create Tenant Embed Apps Links
        api_response = api_instance.create_tenant_embed_apps_links(create_tenant_embed_apps_links_request)
        print("The response of TenantEmbedAppsAndLinksApi->create_tenant_embed_apps_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantEmbedAppsAndLinksApi->create_tenant_embed_apps_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_embed_apps_links_request** | [**CreateTenantEmbedAppsLinksRequest**](CreateTenantEmbedAppsLinksRequest.md)|  | 

### Return type

[**ResponseCreateTenantEmbedAppsLinksResponse**](ResponseCreateTenantEmbedAppsLinksResponse.md)

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
> ResponseDeleteTenantEmbedAppsLinksResponse delete_tenant_embed_apps_links(link_id)

Delete Tenant Embed Apps Links

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_delete_tenant_embed_apps_links_response import ResponseDeleteTenantEmbedAppsLinksResponse
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
    api_instance = onelens_backend_client.TenantEmbedAppsAndLinksApi(api_client)
    link_id = 'link_id_example' # str | 

    try:
        # Delete Tenant Embed Apps Links
        api_response = api_instance.delete_tenant_embed_apps_links(link_id)
        print("The response of TenantEmbedAppsAndLinksApi->delete_tenant_embed_apps_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantEmbedAppsAndLinksApi->delete_tenant_embed_apps_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **str**|  | 

### Return type

[**ResponseDeleteTenantEmbedAppsLinksResponse**](ResponseDeleteTenantEmbedAppsLinksResponse.md)

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

# **get_all_tenant_embed_apps_links**
> ResponseGetTenantEmbedAppsLinksResponse get_all_tenant_embed_apps_links(get_all_tenant_embed_apps_links_request)

Get All Tenant Embed Apps Links

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_tenant_embed_apps_links_request import GetAllTenantEmbedAppsLinksRequest
from onelens_backend_client.models.response_get_tenant_embed_apps_links_response import ResponseGetTenantEmbedAppsLinksResponse
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
    api_instance = onelens_backend_client.TenantEmbedAppsAndLinksApi(api_client)
    get_all_tenant_embed_apps_links_request = onelens_backend_client.GetAllTenantEmbedAppsLinksRequest() # GetAllTenantEmbedAppsLinksRequest | 

    try:
        # Get All Tenant Embed Apps Links
        api_response = api_instance.get_all_tenant_embed_apps_links(get_all_tenant_embed_apps_links_request)
        print("The response of TenantEmbedAppsAndLinksApi->get_all_tenant_embed_apps_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantEmbedAppsAndLinksApi->get_all_tenant_embed_apps_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_all_tenant_embed_apps_links_request** | [**GetAllTenantEmbedAppsLinksRequest**](GetAllTenantEmbedAppsLinksRequest.md)|  | 

### Return type

[**ResponseGetTenantEmbedAppsLinksResponse**](ResponseGetTenantEmbedAppsLinksResponse.md)

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
> ResponseGetTenantEmbedAppsLinksResponse get_tenant_embed_apps_link_by_id(link_id)

Get Tenant Embed Apps Link By Id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_embed_apps_links_response import ResponseGetTenantEmbedAppsLinksResponse
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
    api_instance = onelens_backend_client.TenantEmbedAppsAndLinksApi(api_client)
    link_id = 'link_id_example' # str | 

    try:
        # Get Tenant Embed Apps Link By Id
        api_response = api_instance.get_tenant_embed_apps_link_by_id(link_id)
        print("The response of TenantEmbedAppsAndLinksApi->get_tenant_embed_apps_link_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantEmbedAppsAndLinksApi->get_tenant_embed_apps_link_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **str**|  | 

### Return type

[**ResponseGetTenantEmbedAppsLinksResponse**](ResponseGetTenantEmbedAppsLinksResponse.md)

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

# **update_tenant_embed_apps_links**
> ResponseUpdateTenantEmbedAppsLinksResponse update_tenant_embed_apps_links(link_id, update_tenant_embed_apps_links_request)

Update Tenant Embed Apps Links

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_embed_apps_links_response import ResponseUpdateTenantEmbedAppsLinksResponse
from onelens_backend_client.models.update_tenant_embed_apps_links_request import UpdateTenantEmbedAppsLinksRequest
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
    api_instance = onelens_backend_client.TenantEmbedAppsAndLinksApi(api_client)
    link_id = 'link_id_example' # str | 
    update_tenant_embed_apps_links_request = onelens_backend_client.UpdateTenantEmbedAppsLinksRequest() # UpdateTenantEmbedAppsLinksRequest | 

    try:
        # Update Tenant Embed Apps Links
        api_response = api_instance.update_tenant_embed_apps_links(link_id, update_tenant_embed_apps_links_request)
        print("The response of TenantEmbedAppsAndLinksApi->update_tenant_embed_apps_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantEmbedAppsAndLinksApi->update_tenant_embed_apps_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **str**|  | 
 **update_tenant_embed_apps_links_request** | [**UpdateTenantEmbedAppsLinksRequest**](UpdateTenantEmbedAppsLinksRequest.md)|  | 

### Return type

[**ResponseUpdateTenantEmbedAppsLinksResponse**](ResponseUpdateTenantEmbedAppsLinksResponse.md)

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

