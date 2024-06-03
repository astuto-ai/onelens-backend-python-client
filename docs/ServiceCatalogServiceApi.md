# ServiceCatalogServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get**](ServiceCatalogServiceApi.md#get) | service catalog service handler
[**get_by_id**](ServiceCatalogServiceApi.md#get_by_id) | service catalog get by id service handler


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
    api_instance = onelens_backend_client.ServiceCatalogServiceApi(api_client)
    service_catalog_request = onelens_backend_client.ServiceCatalogRequest() # ServiceCatalogRequest | 

    try:
        # service catalog service handler
        api_response = api_instance.get(service_catalog_request)
        print("The response of ServiceCatalogServiceApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCatalogServiceApi->get: %s\n" % e)
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

# **get_by_id**
> ServiceCatalog get_by_id(service_catalog_request_find)

service catalog get by id service handler

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.service_catalog import ServiceCatalog
from onelens_backend_client.models.service_catalog_request_find import ServiceCatalogRequestFind
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
    api_instance = onelens_backend_client.ServiceCatalogServiceApi(api_client)
    service_catalog_request_find = onelens_backend_client.ServiceCatalogRequestFind() # ServiceCatalogRequestFind | 

    try:
        # service catalog get by id service handler
        api_response = api_instance.get_by_id(service_catalog_request_find)
        print("The response of ServiceCatalogServiceApi->get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCatalogServiceApi->get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_catalog_request_find** | [**ServiceCatalogRequestFind**](ServiceCatalogRequestFind.md)|  | 

### Return type

[**ServiceCatalog**](ServiceCatalog.md)

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

