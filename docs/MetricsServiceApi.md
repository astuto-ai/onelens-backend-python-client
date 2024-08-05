# MetricsServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_metrics**](MetricsServiceApi.md#get_metrics) | get metrics
[**get_multiple_metrics**](MetricsServiceApi.md#get_multiple_metrics) | get mutiple metrics


# **get_metrics**
> GetMetricsResponse get_metrics(get_metrics_request)

get metrics

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_metrics_request import GetMetricsRequest
from onelens_backend_client.models.get_metrics_response import GetMetricsResponse
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
    api_instance = onelens_backend_client.MetricsServiceApi(api_client)
    get_metrics_request = onelens_backend_client.GetMetricsRequest() # GetMetricsRequest | 

    try:
        # get metrics
        api_response = api_instance.get_metrics(get_metrics_request)
        print("The response of MetricsServiceApi->get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsServiceApi->get_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_metrics_request** | [**GetMetricsRequest**](GetMetricsRequest.md)|  | 

### Return type

[**GetMetricsResponse**](GetMetricsResponse.md)

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

# **get_multiple_metrics**
> GetMutipleMetricsResponse get_multiple_metrics(get_mutiple_metrics_request)

get mutiple metrics

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_mutiple_metrics_request import GetMutipleMetricsRequest
from onelens_backend_client.models.get_mutiple_metrics_response import GetMutipleMetricsResponse
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
    api_instance = onelens_backend_client.MetricsServiceApi(api_client)
    get_mutiple_metrics_request = onelens_backend_client.GetMutipleMetricsRequest() # GetMutipleMetricsRequest | 

    try:
        # get mutiple metrics
        api_response = api_instance.get_multiple_metrics(get_mutiple_metrics_request)
        print("The response of MetricsServiceApi->get_multiple_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsServiceApi->get_multiple_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_mutiple_metrics_request** | [**GetMutipleMetricsRequest**](GetMutipleMetricsRequest.md)|  | 

### Return type

[**GetMutipleMetricsResponse**](GetMutipleMetricsResponse.md)

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

