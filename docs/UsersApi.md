# onelens_backend_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_v1_users_post**](UsersApi.md#create_user_v1_users_post) | **POST** /v1/users/ | Create User
[**get_user_by_id_v1_users_user_id_get**](UsersApi.md#get_user_by_id_v1_users_user_id_get) | **GET** /v1/users/{user_id} | Get User By Id
[**get_users_v1_users_get**](UsersApi.md#get_users_v1_users_get) | **GET** /v1/users/ | Get Users
[**update_user_v1_users_put**](UsersApi.md#update_user_v1_users_put) | **PUT** /v1/users/ | Update User


# **create_user_v1_users_post**
> CreateUserResponse create_user_v1_users_post(create_user_request)

Create User

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_user_request import CreateUserRequest
from onelens_backend_client.models.create_user_response import CreateUserResponse
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
    api_instance = onelens_backend_client.UsersApi(api_client)
    create_user_request = onelens_backend_client.CreateUserRequest() # CreateUserRequest | 

    try:
        # Create User
        api_response = api_instance.create_user_v1_users_post(create_user_request)
        print("The response of UsersApi->create_user_v1_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_v1_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)|  | 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

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

# **get_user_by_id_v1_users_user_id_get**
> object get_user_by_id_v1_users_user_id_get(user_id)

Get User By Id

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
    api_instance = onelens_backend_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User By Id
        api_response = api_instance.get_user_by_id_v1_users_user_id_get(user_id)
        print("The response of UsersApi->get_user_by_id_v1_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_id_v1_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

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

# **get_users_v1_users_get**
> GetAllUsersResponse get_users_v1_users_get(get_all_users_request)

Get Users

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_users_request import GetAllUsersRequest
from onelens_backend_client.models.get_all_users_response import GetAllUsersResponse
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
    api_instance = onelens_backend_client.UsersApi(api_client)
    get_all_users_request = onelens_backend_client.GetAllUsersRequest() # GetAllUsersRequest | 

    try:
        # Get Users
        api_response = api_instance.get_users_v1_users_get(get_all_users_request)
        print("The response of UsersApi->get_users_v1_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_v1_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_all_users_request** | [**GetAllUsersRequest**](GetAllUsersRequest.md)|  | 

### Return type

[**GetAllUsersResponse**](GetAllUsersResponse.md)

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

# **update_user_v1_users_put**
> UpdateUserResponse update_user_v1_users_put(update_user_request)

Update User

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_user_request import UpdateUserRequest
from onelens_backend_client.models.update_user_response import UpdateUserResponse
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
    api_instance = onelens_backend_client.UsersApi(api_client)
    update_user_request = onelens_backend_client.UpdateUserRequest() # UpdateUserRequest | 

    try:
        # Update User
        api_response = api_instance.update_user_v1_users_put(update_user_request)
        print("The response of UsersApi->update_user_v1_users_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_v1_users_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 

### Return type

[**UpdateUserResponse**](UpdateUserResponse.md)

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

