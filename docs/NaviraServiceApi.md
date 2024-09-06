# NaviraServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_navira_log**](NaviraServiceApi.md#create_navira_log) | Create Navira Log
[**fetch_logs_with_filters**](NaviraServiceApi.md#fetch_logs_with_filters) | Fetch Logs With Filters
[**update_navira_log**](NaviraServiceApi.md#update_navira_log) | Update Navira Log


# **create_navira_log**
> NaviraLogResponse create_navira_log(create_navira_log_request)

Create Navira Log

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_navira_log_request import CreateNaviraLogRequest
from onelens_backend_client.models.navira_log_response import NaviraLogResponse
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
    api_instance = onelens_backend_client.NaviraServiceApi(api_client)
    create_navira_log_request = onelens_backend_client.CreateNaviraLogRequest() # CreateNaviraLogRequest | 

    try:
        # Create Navira Log
        api_response = api_instance.create_navira_log(create_navira_log_request)
        print("The response of NaviraServiceApi->create_navira_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraServiceApi->create_navira_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_navira_log_request** | [**CreateNaviraLogRequest**](CreateNaviraLogRequest.md)|  | 

### Return type

[**NaviraLogResponse**](NaviraLogResponse.md)

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

# **fetch_logs_with_filters**
> GetAllNaviraFullLogResponse fetch_logs_with_filters(request)

Fetch Logs With Filters

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_navira_full_log_response import GetAllNaviraFullLogResponse
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
    api_instance = onelens_backend_client.NaviraServiceApi(api_client)
    request = 'request_example' # str | 

    try:
        # Fetch Logs With Filters
        api_response = api_instance.fetch_logs_with_filters(request)
        print("The response of NaviraServiceApi->fetch_logs_with_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraServiceApi->fetch_logs_with_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **str**|  | 

### Return type

[**GetAllNaviraFullLogResponse**](GetAllNaviraFullLogResponse.md)

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

# **update_navira_log**
> NaviraLogResponse update_navira_log(navira_log_update_request)

Update Navira Log

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.navira_log_response import NaviraLogResponse
from onelens_backend_client.models.navira_log_update_request import NaviraLogUpdateRequest
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
    api_instance = onelens_backend_client.NaviraServiceApi(api_client)
    navira_log_update_request = onelens_backend_client.NaviraLogUpdateRequest() # NaviraLogUpdateRequest | 

    try:
        # Update Navira Log
        api_response = api_instance.update_navira_log(navira_log_update_request)
        print("The response of NaviraServiceApi->update_navira_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraServiceApi->update_navira_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **navira_log_update_request** | [**NaviraLogUpdateRequest**](NaviraLogUpdateRequest.md)|  | 

### Return type

[**NaviraLogResponse**](NaviraLogResponse.md)

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

