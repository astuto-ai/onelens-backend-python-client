# NaviraConversationServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_thread**](NaviraConversationServiceApi.md#create_thread) | Create Thread
[**get_agent_types**](NaviraConversationServiceApi.md#get_agent_types) | Get Agent Types
[**get_all_threads**](NaviraConversationServiceApi.md#get_all_threads) | Get All Threads
[**get_messages**](NaviraConversationServiceApi.md#get_messages) | Get Messages
[**get_state**](NaviraConversationServiceApi.md#get_state) | Get State
[**get_thread_by_id**](NaviraConversationServiceApi.md#get_thread_by_id) | Get Thread By Id
[**send_message**](NaviraConversationServiceApi.md#send_message) | Send Message
[**update_state**](NaviraConversationServiceApi.md#update_state) | Update State


# **create_thread**
> CreateThreadResponse create_thread(create_thread_request)

Create Thread

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_thread_request import CreateThreadRequest
from onelens_backend_client.models.create_thread_response import CreateThreadResponse
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
    api_instance = onelens_backend_client.NaviraConversationServiceApi(api_client)
    create_thread_request = onelens_backend_client.CreateThreadRequest() # CreateThreadRequest | 

    try:
        # Create Thread
        api_response = api_instance.create_thread(create_thread_request)
        print("The response of NaviraConversationServiceApi->create_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraConversationServiceApi->create_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_thread_request** | [**CreateThreadRequest**](CreateThreadRequest.md)|  | 

### Return type

[**CreateThreadResponse**](CreateThreadResponse.md)

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

# **get_agent_types**
> GetAgentTypesResponse get_agent_types(body)

Get Agent Types

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_agent_types_response import GetAgentTypesResponse
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
    api_instance = onelens_backend_client.NaviraConversationServiceApi(api_client)
    body = None # object | 

    try:
        # Get Agent Types
        api_response = api_instance.get_agent_types(body)
        print("The response of NaviraConversationServiceApi->get_agent_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraConversationServiceApi->get_agent_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**GetAgentTypesResponse**](GetAgentTypesResponse.md)

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

# **get_all_threads**
> GetAllThreadsResponse get_all_threads(get_all_threads_request)

Get All Threads

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_threads_request import GetAllThreadsRequest
from onelens_backend_client.models.get_all_threads_response import GetAllThreadsResponse
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
    api_instance = onelens_backend_client.NaviraConversationServiceApi(api_client)
    get_all_threads_request = onelens_backend_client.GetAllThreadsRequest() # GetAllThreadsRequest | 

    try:
        # Get All Threads
        api_response = api_instance.get_all_threads(get_all_threads_request)
        print("The response of NaviraConversationServiceApi->get_all_threads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraConversationServiceApi->get_all_threads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_all_threads_request** | [**GetAllThreadsRequest**](GetAllThreadsRequest.md)|  | 

### Return type

[**GetAllThreadsResponse**](GetAllThreadsResponse.md)

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

# **get_messages**
> GetMessagesResponse get_messages(get_messages_request)

Get Messages

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_messages_request import GetMessagesRequest
from onelens_backend_client.models.get_messages_response import GetMessagesResponse
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
    api_instance = onelens_backend_client.NaviraConversationServiceApi(api_client)
    get_messages_request = onelens_backend_client.GetMessagesRequest() # GetMessagesRequest | 

    try:
        # Get Messages
        api_response = api_instance.get_messages(get_messages_request)
        print("The response of NaviraConversationServiceApi->get_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraConversationServiceApi->get_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_messages_request** | [**GetMessagesRequest**](GetMessagesRequest.md)|  | 

### Return type

[**GetMessagesResponse**](GetMessagesResponse.md)

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

# **get_state**
> GetStateResponse get_state(get_state_request)

Get State

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_state_request import GetStateRequest
from onelens_backend_client.models.get_state_response import GetStateResponse
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
    api_instance = onelens_backend_client.NaviraConversationServiceApi(api_client)
    get_state_request = onelens_backend_client.GetStateRequest() # GetStateRequest | 

    try:
        # Get State
        api_response = api_instance.get_state(get_state_request)
        print("The response of NaviraConversationServiceApi->get_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraConversationServiceApi->get_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_state_request** | [**GetStateRequest**](GetStateRequest.md)|  | 

### Return type

[**GetStateResponse**](GetStateResponse.md)

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

# **get_thread_by_id**
> GetThreadByIdResponse get_thread_by_id(get_thread_by_id_request)

Get Thread By Id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_thread_by_id_request import GetThreadByIdRequest
from onelens_backend_client.models.get_thread_by_id_response import GetThreadByIdResponse
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
    api_instance = onelens_backend_client.NaviraConversationServiceApi(api_client)
    get_thread_by_id_request = onelens_backend_client.GetThreadByIdRequest() # GetThreadByIdRequest | 

    try:
        # Get Thread By Id
        api_response = api_instance.get_thread_by_id(get_thread_by_id_request)
        print("The response of NaviraConversationServiceApi->get_thread_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraConversationServiceApi->get_thread_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_thread_by_id_request** | [**GetThreadByIdRequest**](GetThreadByIdRequest.md)|  | 

### Return type

[**GetThreadByIdResponse**](GetThreadByIdResponse.md)

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

# **send_message**
> SendMessageResponse send_message(send_message_request)

Send Message

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.send_message_request import SendMessageRequest
from onelens_backend_client.models.send_message_response import SendMessageResponse
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
    api_instance = onelens_backend_client.NaviraConversationServiceApi(api_client)
    send_message_request = onelens_backend_client.SendMessageRequest() # SendMessageRequest | 

    try:
        # Send Message
        api_response = api_instance.send_message(send_message_request)
        print("The response of NaviraConversationServiceApi->send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraConversationServiceApi->send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_message_request** | [**SendMessageRequest**](SendMessageRequest.md)|  | 

### Return type

[**SendMessageResponse**](SendMessageResponse.md)

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

# **update_state**
> object update_state(update_state_request)

Update State

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_state_request import UpdateStateRequest
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
    api_instance = onelens_backend_client.NaviraConversationServiceApi(api_client)
    update_state_request = onelens_backend_client.UpdateStateRequest() # UpdateStateRequest | 

    try:
        # Update State
        api_response = api_instance.update_state(update_state_request)
        print("The response of NaviraConversationServiceApi->update_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NaviraConversationServiceApi->update_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_state_request** | [**UpdateStateRequest**](UpdateStateRequest.md)|  | 

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

