# NaviraApisApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_all_resource_catalogs**](NaviraApisApi.md#get_all_resource_catalogs) | Get All Resource Catalogs
[**get_all_resource_catalogs_0**](NaviraApisApi.md#get_all_resource_catalogs_0) | Get All Resource Catalogs


# **get_all_resource_catalogs**
> ResponseGetAllNaviraLogResponse get_all_resource_catalogs(get_navira_log_api_request)

Get All Resource Catalogs

An API endpoint to get all resource catalogs

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_navira_log_api_request import GetNaviraLogApiRequest
from onelens_backend_client.models.response_get_all_navira_log_response import ResponseGetAllNaviraLogResponse
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
    api_instance = onelens_backend_client.NaviraApisApi(api_client)
    get_navira_log_api_request = onelens_backend_client.GetNaviraLogApiRequest() # GetNaviraLogApiRequest | 

    try:
        # Get All Resource Catalogs
        api_response = api_instance.get_all_resource_catalogs(get_navira_log_api_request)
        print("The response of NaviraApisApi->get_all_resource_catalogs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraApisApi->get_all_resource_catalogs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_navira_log_api_request** | [**GetNaviraLogApiRequest**](GetNaviraLogApiRequest.md)|  | 

### Return type

[**ResponseGetAllNaviraLogResponse**](ResponseGetAllNaviraLogResponse.md)

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

# **get_all_resource_catalogs_0**
> ResponseNaviraLogResponse get_all_resource_catalogs_0(navira_log_feedback_update_api_request)

Get All Resource Catalogs

An API endpoint to get all resource catalogs

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.navira_log_feedback_update_api_request import NaviraLogFeedbackUpdateApiRequest
from onelens_backend_client.models.response_navira_log_response import ResponseNaviraLogResponse
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
    api_instance = onelens_backend_client.NaviraApisApi(api_client)
    navira_log_feedback_update_api_request = onelens_backend_client.NaviraLogFeedbackUpdateApiRequest() # NaviraLogFeedbackUpdateApiRequest | 

    try:
        # Get All Resource Catalogs
        api_response = api_instance.get_all_resource_catalogs_0(navira_log_feedback_update_api_request)
        print("The response of NaviraApisApi->get_all_resource_catalogs_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraApisApi->get_all_resource_catalogs_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **navira_log_feedback_update_api_request** | [**NaviraLogFeedbackUpdateApiRequest**](NaviraLogFeedbackUpdateApiRequest.md)|  | 

### Return type

[**ResponseNaviraLogResponse**](ResponseNaviraLogResponse.md)

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

