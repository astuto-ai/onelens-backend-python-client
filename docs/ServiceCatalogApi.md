# ServiceCatalogApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_metrics**](ServiceCatalogApi.md#get_metrics) | Get Metrics
[**get_service_catalog**](ServiceCatalogApi.md#get_service_catalog) | Get Service Catalog


# **get_metrics**
> ResponseGetMetricsResponse get_metrics(get_metrics_api_request)

Get Metrics

An API endpoint to get tenant cloud metadata like cloud id, region, service...

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_metrics_api_request import GetMetricsAPIRequest
from onelens_backend_client.models.response_get_metrics_response import ResponseGetMetricsResponse
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
    api_instance = onelens_backend_client.ServiceCatalogApi(api_client)
    get_metrics_api_request = onelens_backend_client.GetMetricsAPIRequest() # GetMetricsAPIRequest | 

    try:
        # Get Metrics
        api_response = api_instance.get_metrics(get_metrics_api_request)
        print("The response of ServiceCatalogApi->get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCatalogApi->get_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_metrics_api_request** | [**GetMetricsAPIRequest**](GetMetricsAPIRequest.md)|  | 

### Return type

[**ResponseGetMetricsResponse**](ResponseGetMetricsResponse.md)

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
> object get_service_catalog()

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
    api_instance = onelens_backend_client.ServiceCatalogApi(api_client)

    try:
        # Get Service Catalog
        api_response = api_instance.get_service_catalog()
        print("The response of ServiceCatalogApi->get_service_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceCatalogApi->get_service_catalog: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

