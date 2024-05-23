# GetServiceCatalogApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get**](GetServiceCatalogApi.md#get) | service catalog service handler
[**get_service_catalog**](GetServiceCatalogApi.md#get_service_catalog) | Get Service Catalog


# **get**
> ServiceCatalogResponse get(service_catalog_request)

service catalog service handler

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.service_catalog_request import ServiceCatalogRequest
from onelens_backend_client.models.service_catalog_response import ServiceCatalogResponse
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
    api_instance = onelens_backend_client.GetServiceCatalogApi(api_client)
    service_catalog_request = onelens_backend_client.ServiceCatalogRequest() # ServiceCatalogRequest | 

    try:
        # service catalog service handler
        api_response = api_instance.get(service_catalog_request)
        print("The response of GetServiceCatalogApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetServiceCatalogApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_catalog_request** | [**ServiceCatalogRequest**](ServiceCatalogRequest.md)|  | 

### Return type

[**ServiceCatalogResponse**](ServiceCatalogResponse.md)

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

# **get_service_catalog**
> object get_service_catalog(tenant_id)

Get Service Catalog

An API endpoint to get the service catalog

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
    api_instance = onelens_backend_client.GetServiceCatalogApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get Service Catalog
        api_response = api_instance.get_service_catalog(tenant_id)
        print("The response of GetServiceCatalogApi->get_service_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetServiceCatalogApi->get_service_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

**object**

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

