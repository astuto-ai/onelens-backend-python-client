# TenantUsersApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_user**](TenantUsersApi.md#create_tenant_user) | Create a new user in the Tenant Database.
[**create_tenant_user_0**](TenantUsersApi.md#create_tenant_user_0) | Create Tenant User
[**disable_tenant_user**](TenantUsersApi.md#disable_tenant_user) | Disable a user in the Tenant Database.
[**disable_tenant_user_0**](TenantUsersApi.md#disable_tenant_user_0) | Disable Tenant User
[**enable_tenant_user**](TenantUsersApi.md#enable_tenant_user) | Enable a user in the Tenant Database.
[**enable_tenant_user_0**](TenantUsersApi.md#enable_tenant_user_0) | Enable Tenant User
[**get_all_tenant_users_with_filter**](TenantUsersApi.md#get_all_tenant_users_with_filter) | Get all users from the Tenant Database.
[**get_all_tenant_users_with_filter_0**](TenantUsersApi.md#get_all_tenant_users_with_filter_0) | Get All Tenant Users With Filter
[**get_tenant_user_by_ol_user_id**](TenantUsersApi.md#get_tenant_user_by_ol_user_id) | Get a user from the Tenant Database.
[**get_tenant_user_by_ol_user_id_0**](TenantUsersApi.md#get_tenant_user_by_ol_user_id_0) | Get Tenant User By Ol User Id
[**update_tenant_user**](TenantUsersApi.md#update_tenant_user) | Update a user in the Tenant Database.
[**update_tenant_user_0**](TenantUsersApi.md#update_tenant_user_0) | Update Tenant User
[**update_tenant_user_details**](TenantUsersApi.md#update_tenant_user_details) | Update a user details in the Tenant Database.
[**update_tenant_user_details_0**](TenantUsersApi.md#update_tenant_user_details_0) | Update Tenant User Details


# **create_tenant_user**
> ResponseCreateTenantUserResponse create_tenant_user(tenant_id, create_tenant_user_request)

Create a new user in the Tenant Database.

Create a new user in the Tenant Database.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_user_request import CreateTenantUserRequest
from onelens_backend_client.models.response_create_tenant_user_response import ResponseCreateTenantUserResponse
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    create_tenant_user_request = onelens_backend_client.CreateTenantUserRequest() # CreateTenantUserRequest | 

    try:
        # Create a new user in the Tenant Database.
        api_response = api_instance.create_tenant_user(tenant_id, create_tenant_user_request)
        print("The response of TenantUsersApi->create_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->create_tenant_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **create_tenant_user_request** | [**CreateTenantUserRequest**](CreateTenantUserRequest.md)|  | 

### Return type

[**ResponseCreateTenantUserResponse**](ResponseCreateTenantUserResponse.md)

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

# **create_tenant_user_0**
> ResponseCreateTenantUserResponse create_tenant_user_0(create_tenant_user_request)

Create Tenant User

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_user_request import CreateTenantUserRequest
from onelens_backend_client.models.response_create_tenant_user_response import ResponseCreateTenantUserResponse
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    create_tenant_user_request = onelens_backend_client.CreateTenantUserRequest() # CreateTenantUserRequest | 

    try:
        # Create Tenant User
        api_response = api_instance.create_tenant_user_0(create_tenant_user_request)
        print("The response of TenantUsersApi->create_tenant_user_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->create_tenant_user_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_user_request** | [**CreateTenantUserRequest**](CreateTenantUserRequest.md)|  | 

### Return type

[**ResponseCreateTenantUserResponse**](ResponseCreateTenantUserResponse.md)

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

# **disable_tenant_user**
> ResponseGetTenantUserByIDResponse disable_tenant_user(tenant_id, ol_user_id)

Disable a user in the Tenant Database.

Update a user details in the Tenant Database.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_user_by_id_response import ResponseGetTenantUserByIDResponse
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ol_user_id = 'ol_user_id_example' # str | 

    try:
        # Disable a user in the Tenant Database.
        api_response = api_instance.disable_tenant_user(tenant_id, ol_user_id)
        print("The response of TenantUsersApi->disable_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->disable_tenant_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ol_user_id** | **str**|  | 

### Return type

[**ResponseGetTenantUserByIDResponse**](ResponseGetTenantUserByIDResponse.md)

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

# **disable_tenant_user_0**
> ResponseGetTenantUserByIDResponse disable_tenant_user_0(ol_user_id)

Disable Tenant User

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_user_by_id_response import ResponseGetTenantUserByIDResponse
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    ol_user_id = 'ol_user_id_example' # str | 

    try:
        # Disable Tenant User
        api_response = api_instance.disable_tenant_user_0(ol_user_id)
        print("The response of TenantUsersApi->disable_tenant_user_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->disable_tenant_user_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ol_user_id** | **str**|  | 

### Return type

[**ResponseGetTenantUserByIDResponse**](ResponseGetTenantUserByIDResponse.md)

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

# **enable_tenant_user**
> ResponseGetTenantUserByIDResponse enable_tenant_user(tenant_id, ol_user_id)

Enable a user in the Tenant Database.

Update a user details in the Tenant Database.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_user_by_id_response import ResponseGetTenantUserByIDResponse
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ol_user_id = 'ol_user_id_example' # str | 

    try:
        # Enable a user in the Tenant Database.
        api_response = api_instance.enable_tenant_user(tenant_id, ol_user_id)
        print("The response of TenantUsersApi->enable_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->enable_tenant_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ol_user_id** | **str**|  | 

### Return type

[**ResponseGetTenantUserByIDResponse**](ResponseGetTenantUserByIDResponse.md)

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

# **enable_tenant_user_0**
> ResponseGetTenantUserByIDResponse enable_tenant_user_0(ol_user_id)

Enable Tenant User

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_user_by_id_response import ResponseGetTenantUserByIDResponse
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    ol_user_id = 'ol_user_id_example' # str | 

    try:
        # Enable Tenant User
        api_response = api_instance.enable_tenant_user_0(ol_user_id)
        print("The response of TenantUsersApi->enable_tenant_user_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->enable_tenant_user_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ol_user_id** | **str**|  | 

### Return type

[**ResponseGetTenantUserByIDResponse**](ResponseGetTenantUserByIDResponse.md)

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

# **get_all_tenant_users_with_filter**
> ResponseGetTenantUsersWithFilterResponse get_all_tenant_users_with_filter(tenant_id, get_tenant_users_with_filter_api_request)

Get all users from the Tenant Database.

Get all users in the Tenant Database.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_users_with_filter_api_request import GetTenantUsersWithFilterAPIRequest
from onelens_backend_client.models.response_get_tenant_users_with_filter_response import ResponseGetTenantUsersWithFilterResponse
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_tenant_users_with_filter_api_request = onelens_backend_client.GetTenantUsersWithFilterAPIRequest() # GetTenantUsersWithFilterAPIRequest | 

    try:
        # Get all users from the Tenant Database.
        api_response = api_instance.get_all_tenant_users_with_filter(tenant_id, get_tenant_users_with_filter_api_request)
        print("The response of TenantUsersApi->get_all_tenant_users_with_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->get_all_tenant_users_with_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_tenant_users_with_filter_api_request** | [**GetTenantUsersWithFilterAPIRequest**](GetTenantUsersWithFilterAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantUsersWithFilterResponse**](ResponseGetTenantUsersWithFilterResponse.md)

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

# **get_all_tenant_users_with_filter_0**
> ResponseGetTenantUsersWithFilterResponse get_all_tenant_users_with_filter_0(get_tenant_users_with_filter_api_request)

Get All Tenant Users With Filter

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_users_with_filter_api_request import GetTenantUsersWithFilterAPIRequest
from onelens_backend_client.models.response_get_tenant_users_with_filter_response import ResponseGetTenantUsersWithFilterResponse
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    get_tenant_users_with_filter_api_request = onelens_backend_client.GetTenantUsersWithFilterAPIRequest() # GetTenantUsersWithFilterAPIRequest | 

    try:
        # Get All Tenant Users With Filter
        api_response = api_instance.get_all_tenant_users_with_filter_0(get_tenant_users_with_filter_api_request)
        print("The response of TenantUsersApi->get_all_tenant_users_with_filter_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->get_all_tenant_users_with_filter_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_users_with_filter_api_request** | [**GetTenantUsersWithFilterAPIRequest**](GetTenantUsersWithFilterAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantUsersWithFilterResponse**](ResponseGetTenantUsersWithFilterResponse.md)

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
> ResponseGetTenantUserByIDResponse get_tenant_user_by_ol_user_id(tenant_id, ol_user_id)

Get a user from the Tenant Database.

Get a user in the Tenant Database.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_user_by_id_response import ResponseGetTenantUserByIDResponse
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ol_user_id = 'ol_user_id_example' # str | 

    try:
        # Get a user from the Tenant Database.
        api_response = api_instance.get_tenant_user_by_ol_user_id(tenant_id, ol_user_id)
        print("The response of TenantUsersApi->get_tenant_user_by_ol_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->get_tenant_user_by_ol_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ol_user_id** | **str**|  | 

### Return type

[**ResponseGetTenantUserByIDResponse**](ResponseGetTenantUserByIDResponse.md)

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

# **get_tenant_user_by_ol_user_id_0**
> ResponseGetTenantUserByIDResponse get_tenant_user_by_ol_user_id_0(ol_user_id)

Get Tenant User By Ol User Id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_user_by_id_response import ResponseGetTenantUserByIDResponse
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    ol_user_id = 'ol_user_id_example' # str | 

    try:
        # Get Tenant User By Ol User Id
        api_response = api_instance.get_tenant_user_by_ol_user_id_0(ol_user_id)
        print("The response of TenantUsersApi->get_tenant_user_by_ol_user_id_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->get_tenant_user_by_ol_user_id_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ol_user_id** | **str**|  | 

### Return type

[**ResponseGetTenantUserByIDResponse**](ResponseGetTenantUserByIDResponse.md)

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

# **update_tenant_user**
> ResponseUpdateTenantUserResponse update_tenant_user(tenant_id, ol_user_id, tenant_user_update_fields_mixin)

Update a user in the Tenant Database.

Update a user in the Tenant Database.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_user_response import ResponseUpdateTenantUserResponse
from onelens_backend_client.models.tenant_user_update_fields_mixin import TenantUserUpdateFieldsMixin
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ol_user_id = 'ol_user_id_example' # str | 
    tenant_user_update_fields_mixin = onelens_backend_client.TenantUserUpdateFieldsMixin() # TenantUserUpdateFieldsMixin | 

    try:
        # Update a user in the Tenant Database.
        api_response = api_instance.update_tenant_user(tenant_id, ol_user_id, tenant_user_update_fields_mixin)
        print("The response of TenantUsersApi->update_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->update_tenant_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ol_user_id** | **str**|  | 
 **tenant_user_update_fields_mixin** | [**TenantUserUpdateFieldsMixin**](TenantUserUpdateFieldsMixin.md)|  | 

### Return type

[**ResponseUpdateTenantUserResponse**](ResponseUpdateTenantUserResponse.md)

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

# **update_tenant_user_0**
> ResponseUpdateTenantUserResponse update_tenant_user_0(ol_user_id, tenant_user_update_fields_mixin)

Update Tenant User

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_user_response import ResponseUpdateTenantUserResponse
from onelens_backend_client.models.tenant_user_update_fields_mixin import TenantUserUpdateFieldsMixin
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    ol_user_id = 'ol_user_id_example' # str | 
    tenant_user_update_fields_mixin = onelens_backend_client.TenantUserUpdateFieldsMixin() # TenantUserUpdateFieldsMixin | 

    try:
        # Update Tenant User
        api_response = api_instance.update_tenant_user_0(ol_user_id, tenant_user_update_fields_mixin)
        print("The response of TenantUsersApi->update_tenant_user_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->update_tenant_user_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ol_user_id** | **str**|  | 
 **tenant_user_update_fields_mixin** | [**TenantUserUpdateFieldsMixin**](TenantUserUpdateFieldsMixin.md)|  | 

### Return type

[**ResponseUpdateTenantUserResponse**](ResponseUpdateTenantUserResponse.md)

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
> ResponseUpdateTenantUserDetailsResponse update_tenant_user_details(tenant_id, ol_user_id, tenant_user_details_update_fields_mixin)

Update a user details in the Tenant Database.

Update a user details in the Tenant Database.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_user_details_response import ResponseUpdateTenantUserDetailsResponse
from onelens_backend_client.models.tenant_user_details_update_fields_mixin import TenantUserDetailsUpdateFieldsMixin
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ol_user_id = 'ol_user_id_example' # str | 
    tenant_user_details_update_fields_mixin = onelens_backend_client.TenantUserDetailsUpdateFieldsMixin() # TenantUserDetailsUpdateFieldsMixin | 

    try:
        # Update a user details in the Tenant Database.
        api_response = api_instance.update_tenant_user_details(tenant_id, ol_user_id, tenant_user_details_update_fields_mixin)
        print("The response of TenantUsersApi->update_tenant_user_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->update_tenant_user_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ol_user_id** | **str**|  | 
 **tenant_user_details_update_fields_mixin** | [**TenantUserDetailsUpdateFieldsMixin**](TenantUserDetailsUpdateFieldsMixin.md)|  | 

### Return type

[**ResponseUpdateTenantUserDetailsResponse**](ResponseUpdateTenantUserDetailsResponse.md)

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

# **update_tenant_user_details_0**
> ResponseUpdateTenantUserDetailsResponse update_tenant_user_details_0(ol_user_id, tenant_user_details_update_fields_mixin)

Update Tenant User Details

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_user_details_response import ResponseUpdateTenantUserDetailsResponse
from onelens_backend_client.models.tenant_user_details_update_fields_mixin import TenantUserDetailsUpdateFieldsMixin
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
    api_instance = onelens_backend_client.TenantUsersApi(api_client)
    ol_user_id = 'ol_user_id_example' # str | 
    tenant_user_details_update_fields_mixin = onelens_backend_client.TenantUserDetailsUpdateFieldsMixin() # TenantUserDetailsUpdateFieldsMixin | 

    try:
        # Update Tenant User Details
        api_response = api_instance.update_tenant_user_details_0(ol_user_id, tenant_user_details_update_fields_mixin)
        print("The response of TenantUsersApi->update_tenant_user_details_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->update_tenant_user_details_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ol_user_id** | **str**|  | 
 **tenant_user_details_update_fields_mixin** | [**TenantUserDetailsUpdateFieldsMixin**](TenantUserDetailsUpdateFieldsMixin.md)|  | 

### Return type

[**ResponseUpdateTenantUserDetailsResponse**](ResponseUpdateTenantUserDetailsResponse.md)

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

