# SavedViewServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_saved_view**](SavedViewServiceApi.md#create_saved_view) | Create a saved view.
[**delete_saved_view**](SavedViewServiceApi.md#delete_saved_view) | Delete a saved view.
[**get_saved_views**](SavedViewServiceApi.md#get_saved_views) | Get saved views.
[**toggle_default_to_saved_view**](SavedViewServiceApi.md#toggle_default_to_saved_view) | Mark a saved view as default.
[**update_saved_view**](SavedViewServiceApi.md#update_saved_view) | Update a saved view.


# **create_saved_view**
> CreateSavedViewResponse create_saved_view(create_saved_view_request)

Create a saved view.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_saved_view_request import CreateSavedViewRequest
from onelens_backend_client.models.create_saved_view_response import CreateSavedViewResponse
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
    api_instance = onelens_backend_client.SavedViewServiceApi(api_client)
    create_saved_view_request = onelens_backend_client.CreateSavedViewRequest() # CreateSavedViewRequest | 

    try:
        # Create a saved view.
        api_response = api_instance.create_saved_view(create_saved_view_request)
        print("The response of SavedViewServiceApi->create_saved_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedViewServiceApi->create_saved_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_saved_view_request** | [**CreateSavedViewRequest**](CreateSavedViewRequest.md)|  | 

### Return type

[**CreateSavedViewResponse**](CreateSavedViewResponse.md)

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

# **delete_saved_view**
> object delete_saved_view(delete_saved_view_request)

Delete a saved view.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.delete_saved_view_request import DeleteSavedViewRequest
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
    api_instance = onelens_backend_client.SavedViewServiceApi(api_client)
    delete_saved_view_request = onelens_backend_client.DeleteSavedViewRequest() # DeleteSavedViewRequest | 

    try:
        # Delete a saved view.
        api_response = api_instance.delete_saved_view(delete_saved_view_request)
        print("The response of SavedViewServiceApi->delete_saved_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedViewServiceApi->delete_saved_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_saved_view_request** | [**DeleteSavedViewRequest**](DeleteSavedViewRequest.md)|  | 

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

# **get_saved_views**
> GetSavedViewsResponse get_saved_views(get_saved_views_request)

Get saved views.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_saved_views_request import GetSavedViewsRequest
from onelens_backend_client.models.get_saved_views_response import GetSavedViewsResponse
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
    api_instance = onelens_backend_client.SavedViewServiceApi(api_client)
    get_saved_views_request = onelens_backend_client.GetSavedViewsRequest() # GetSavedViewsRequest | 

    try:
        # Get saved views.
        api_response = api_instance.get_saved_views(get_saved_views_request)
        print("The response of SavedViewServiceApi->get_saved_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedViewServiceApi->get_saved_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_saved_views_request** | [**GetSavedViewsRequest**](GetSavedViewsRequest.md)|  | 

### Return type

[**GetSavedViewsResponse**](GetSavedViewsResponse.md)

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

# **toggle_default_to_saved_view**
> object toggle_default_to_saved_view(mark_view_as_default_request)

Mark a saved view as default.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.mark_view_as_default_request import MarkViewAsDefaultRequest
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
    api_instance = onelens_backend_client.SavedViewServiceApi(api_client)
    mark_view_as_default_request = onelens_backend_client.MarkViewAsDefaultRequest() # MarkViewAsDefaultRequest | 

    try:
        # Mark a saved view as default.
        api_response = api_instance.toggle_default_to_saved_view(mark_view_as_default_request)
        print("The response of SavedViewServiceApi->toggle_default_to_saved_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedViewServiceApi->toggle_default_to_saved_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_view_as_default_request** | [**MarkViewAsDefaultRequest**](MarkViewAsDefaultRequest.md)|  | 

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

# **update_saved_view**
> UpdateSavedViewResponse update_saved_view(update_saved_view_request)

Update a saved view.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_saved_view_request import UpdateSavedViewRequest
from onelens_backend_client.models.update_saved_view_response import UpdateSavedViewResponse
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
    api_instance = onelens_backend_client.SavedViewServiceApi(api_client)
    update_saved_view_request = onelens_backend_client.UpdateSavedViewRequest() # UpdateSavedViewRequest | 

    try:
        # Update a saved view.
        api_response = api_instance.update_saved_view(update_saved_view_request)
        print("The response of SavedViewServiceApi->update_saved_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedViewServiceApi->update_saved_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_saved_view_request** | [**UpdateSavedViewRequest**](UpdateSavedViewRequest.md)|  | 

### Return type

[**UpdateSavedViewResponse**](UpdateSavedViewResponse.md)

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

