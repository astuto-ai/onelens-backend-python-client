# TenantUserServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_user**](TenantUserServiceApi.md#create_tenant_user) | Creates a new user.
[**create_tenant_user_from_ol_user_id**](TenantUserServiceApi.md#create_tenant_user_from_ol_user_id) | Creates a new user from onelens user id (ol_user_id).
[**disable_tenant_user**](TenantUserServiceApi.md#disable_tenant_user) | Disables an existing tenant user.
[**enable_tenant_user**](TenantUserServiceApi.md#enable_tenant_user) | Enables an existing tenant user.
[**get_tenant_user_by_ol_user_id**](TenantUserServiceApi.md#get_tenant_user_by_ol_user_id) | Retrieves a tenant user by its unique onelens user id (ol_user_id).
[**get_tenant_users**](TenantUserServiceApi.md#get_tenant_users) | Retrieves all tenant users.
[**update_tenant_user**](TenantUserServiceApi.md#update_tenant_user) | Updates an existing tenant user.
[**update_tenant_user_details**](TenantUserServiceApi.md#update_tenant_user_details) | Updates tenant user details.


# **create_tenant_user**
> CreateTenantUserResponse create_tenant_user(request)

Creates a new user.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_user_response import CreateTenantUserResponse
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
    api_instance = onelens_backend_client.TenantUserServiceApi(api_client)
    request = 'request_example' # str | 

    try:
        # Creates a new user.
        api_response = api_instance.create_tenant_user(request)
        print("The response of TenantUserServiceApi->create_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserServiceApi->create_tenant_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **str**|  | 

### Return type

[**CreateTenantUserResponse**](CreateTenantUserResponse.md)

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

# **create_tenant_user_from_ol_user_id**
> CreateTenantUserResponse create_tenant_user_from_ol_user_id(request)

Creates a new user from onelens user id (ol_user_id).

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_user_response import CreateTenantUserResponse
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
    api_instance = onelens_backend_client.TenantUserServiceApi(api_client)
    request = 'request_example' # str | 

    try:
        # Creates a new user from onelens user id (ol_user_id).
        api_response = api_instance.create_tenant_user_from_ol_user_id(request)
        print("The response of TenantUserServiceApi->create_tenant_user_from_ol_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserServiceApi->create_tenant_user_from_ol_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **str**|  | 

### Return type

[**CreateTenantUserResponse**](CreateTenantUserResponse.md)

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

# **disable_tenant_user**
> DisableTenantUserResponse disable_tenant_user(disable_tenant_user_request)

Disables an existing tenant user.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.disable_tenant_user_request import DisableTenantUserRequest
from onelens_backend_client.models.disable_tenant_user_response import DisableTenantUserResponse
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
    api_instance = onelens_backend_client.TenantUserServiceApi(api_client)
    disable_tenant_user_request = onelens_backend_client.DisableTenantUserRequest() # DisableTenantUserRequest | 

    try:
        # Disables an existing tenant user.
        api_response = api_instance.disable_tenant_user(disable_tenant_user_request)
        print("The response of TenantUserServiceApi->disable_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserServiceApi->disable_tenant_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_tenant_user_request** | [**DisableTenantUserRequest**](DisableTenantUserRequest.md)|  | 

### Return type

[**DisableTenantUserResponse**](DisableTenantUserResponse.md)

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

# **enable_tenant_user**
> EnableTenantUserResponse enable_tenant_user(enable_tenant_user_request)

Enables an existing tenant user.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.enable_tenant_user_request import EnableTenantUserRequest
from onelens_backend_client.models.enable_tenant_user_response import EnableTenantUserResponse
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
    api_instance = onelens_backend_client.TenantUserServiceApi(api_client)
    enable_tenant_user_request = onelens_backend_client.EnableTenantUserRequest() # EnableTenantUserRequest | 

    try:
        # Enables an existing tenant user.
        api_response = api_instance.enable_tenant_user(enable_tenant_user_request)
        print("The response of TenantUserServiceApi->enable_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserServiceApi->enable_tenant_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_tenant_user_request** | [**EnableTenantUserRequest**](EnableTenantUserRequest.md)|  | 

### Return type

[**EnableTenantUserResponse**](EnableTenantUserResponse.md)

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

# **get_tenant_user_by_ol_user_id**
> GetTenantUserByIDResponse get_tenant_user_by_ol_user_id(get_tenant_user_by_id_request)

Retrieves a tenant user by its unique onelens user id (ol_user_id).

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_user_by_id_request import GetTenantUserByIDRequest
from onelens_backend_client.models.get_tenant_user_by_id_response import GetTenantUserByIDResponse
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
    api_instance = onelens_backend_client.TenantUserServiceApi(api_client)
    get_tenant_user_by_id_request = onelens_backend_client.GetTenantUserByIDRequest() # GetTenantUserByIDRequest | 

    try:
        # Retrieves a tenant user by its unique onelens user id (ol_user_id).
        api_response = api_instance.get_tenant_user_by_ol_user_id(get_tenant_user_by_id_request)
        print("The response of TenantUserServiceApi->get_tenant_user_by_ol_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserServiceApi->get_tenant_user_by_ol_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_user_by_id_request** | [**GetTenantUserByIDRequest**](GetTenantUserByIDRequest.md)|  | 

### Return type

[**GetTenantUserByIDResponse**](GetTenantUserByIDResponse.md)

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

# **get_tenant_users**
> GetTenantUsersWithFilterResponse get_tenant_users(get_tenant_users_with_filter_request)

Retrieves all tenant users.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_users_with_filter_request import GetTenantUsersWithFilterRequest
from onelens_backend_client.models.get_tenant_users_with_filter_response import GetTenantUsersWithFilterResponse
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
    api_instance = onelens_backend_client.TenantUserServiceApi(api_client)
    get_tenant_users_with_filter_request = onelens_backend_client.GetTenantUsersWithFilterRequest() # GetTenantUsersWithFilterRequest | 

    try:
        # Retrieves all tenant users.
        api_response = api_instance.get_tenant_users(get_tenant_users_with_filter_request)
        print("The response of TenantUserServiceApi->get_tenant_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserServiceApi->get_tenant_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_users_with_filter_request** | [**GetTenantUsersWithFilterRequest**](GetTenantUsersWithFilterRequest.md)|  | 

### Return type

[**GetTenantUsersWithFilterResponse**](GetTenantUsersWithFilterResponse.md)

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

# **update_tenant_user**
> UpdateTenantUserResponse update_tenant_user(update_tenant_user_request)

Updates an existing tenant user.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_tenant_user_request import UpdateTenantUserRequest
from onelens_backend_client.models.update_tenant_user_response import UpdateTenantUserResponse
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
    api_instance = onelens_backend_client.TenantUserServiceApi(api_client)
    update_tenant_user_request = onelens_backend_client.UpdateTenantUserRequest() # UpdateTenantUserRequest | 

    try:
        # Updates an existing tenant user.
        api_response = api_instance.update_tenant_user(update_tenant_user_request)
        print("The response of TenantUserServiceApi->update_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserServiceApi->update_tenant_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tenant_user_request** | [**UpdateTenantUserRequest**](UpdateTenantUserRequest.md)|  | 

### Return type

[**UpdateTenantUserResponse**](UpdateTenantUserResponse.md)

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

# **update_tenant_user_details**
> UpdateTenantUserDetailsResponse update_tenant_user_details(update_tenant_user_details_request)

Updates tenant user details.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_tenant_user_details_request import UpdateTenantUserDetailsRequest
from onelens_backend_client.models.update_tenant_user_details_response import UpdateTenantUserDetailsResponse
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
    api_instance = onelens_backend_client.TenantUserServiceApi(api_client)
    update_tenant_user_details_request = onelens_backend_client.UpdateTenantUserDetailsRequest() # UpdateTenantUserDetailsRequest | 

    try:
        # Updates tenant user details.
        api_response = api_instance.update_tenant_user_details(update_tenant_user_details_request)
        print("The response of TenantUserServiceApi->update_tenant_user_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUserServiceApi->update_tenant_user_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tenant_user_details_request** | [**UpdateTenantUserDetailsRequest**](UpdateTenantUserDetailsRequest.md)|  | 

### Return type

[**UpdateTenantUserDetailsResponse**](UpdateTenantUserDetailsResponse.md)

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

