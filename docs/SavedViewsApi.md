# SavedViewsApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_saved_view**](SavedViewsApi.md#create_saved_view) | Create a new saved view.
[**delete_saved_view**](SavedViewsApi.md#delete_saved_view) | Delete a saved view.
[**get_saved_views**](SavedViewsApi.md#get_saved_views) | Get saved views.
[**mark_saved_view_as_default**](SavedViewsApi.md#mark_saved_view_as_default) | Mark a saved view as default.
[**update_saved_view**](SavedViewsApi.md#update_saved_view) | Update a saved view.


# **create_saved_view**
> ResponseCreateSavedViewResponse create_saved_view(create_saved_view_api_request)

Create a new saved view.

Create a new saved view.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_saved_view_api_request import CreateSavedViewAPIRequest
from onelens_backend_client.models.response_create_saved_view_response import ResponseCreateSavedViewResponse
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
    api_instance = onelens_backend_client.SavedViewsApi(api_client)
    create_saved_view_api_request = onelens_backend_client.CreateSavedViewAPIRequest() # CreateSavedViewAPIRequest | 

    try:
        # Create a new saved view.
        api_response = api_instance.create_saved_view(create_saved_view_api_request)
        print("The response of SavedViewsApi->create_saved_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedViewsApi->create_saved_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_saved_view_api_request** | [**CreateSavedViewAPIRequest**](CreateSavedViewAPIRequest.md)|  | 

### Return type

[**ResponseCreateSavedViewResponse**](ResponseCreateSavedViewResponse.md)

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
> ResponseDeleteSavedViewResponse delete_saved_view(view_id)

Delete a saved view.

Delete a saved view.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_delete_saved_view_response import ResponseDeleteSavedViewResponse
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
    api_instance = onelens_backend_client.SavedViewsApi(api_client)
    view_id = 'view_id_example' # str | 

    try:
        # Delete a saved view.
        api_response = api_instance.delete_saved_view(view_id)
        print("The response of SavedViewsApi->delete_saved_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedViewsApi->delete_saved_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 

### Return type

[**ResponseDeleteSavedViewResponse**](ResponseDeleteSavedViewResponse.md)

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

# **get_saved_views**
> ResponseGetSavedViewsResponse get_saved_views(get_saved_views_api_request)

Get saved views.

Get saved views for the current user.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_saved_views_api_request import GetSavedViewsAPIRequest
from onelens_backend_client.models.response_get_saved_views_response import ResponseGetSavedViewsResponse
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
    api_instance = onelens_backend_client.SavedViewsApi(api_client)
    get_saved_views_api_request = onelens_backend_client.GetSavedViewsAPIRequest() # GetSavedViewsAPIRequest | 

    try:
        # Get saved views.
        api_response = api_instance.get_saved_views(get_saved_views_api_request)
        print("The response of SavedViewsApi->get_saved_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedViewsApi->get_saved_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_saved_views_api_request** | [**GetSavedViewsAPIRequest**](GetSavedViewsAPIRequest.md)|  | 

### Return type

[**ResponseGetSavedViewsResponse**](ResponseGetSavedViewsResponse.md)

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

# **mark_saved_view_as_default**
> ResponseMarkViewAsDefaultResponse mark_saved_view_as_default(view_id)

Mark a saved view as default.

Mark a saved view as default.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_mark_view_as_default_response import ResponseMarkViewAsDefaultResponse
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
    api_instance = onelens_backend_client.SavedViewsApi(api_client)
    view_id = 'view_id_example' # str | 

    try:
        # Mark a saved view as default.
        api_response = api_instance.mark_saved_view_as_default(view_id)
        print("The response of SavedViewsApi->mark_saved_view_as_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedViewsApi->mark_saved_view_as_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 

### Return type

[**ResponseMarkViewAsDefaultResponse**](ResponseMarkViewAsDefaultResponse.md)

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

# **update_saved_view**
> ResponseUpdateSavedViewResponse update_saved_view(view_id, update_saved_view_api_request)

Update a saved view.

Update a saved view.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_saved_view_response import ResponseUpdateSavedViewResponse
from onelens_backend_client.models.update_saved_view_api_request import UpdateSavedViewAPIRequest
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
    api_instance = onelens_backend_client.SavedViewsApi(api_client)
    view_id = 'view_id_example' # str | 
    update_saved_view_api_request = onelens_backend_client.UpdateSavedViewAPIRequest() # UpdateSavedViewAPIRequest | 

    try:
        # Update a saved view.
        api_response = api_instance.update_saved_view(view_id, update_saved_view_api_request)
        print("The response of SavedViewsApi->update_saved_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SavedViewsApi->update_saved_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 
 **update_saved_view_api_request** | [**UpdateSavedViewAPIRequest**](UpdateSavedViewAPIRequest.md)|  | 

### Return type

[**ResponseUpdateSavedViewResponse**](ResponseUpdateSavedViewResponse.md)

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

