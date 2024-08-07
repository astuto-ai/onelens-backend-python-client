# TenantUsersApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_user**](TenantUsersApi.md#create_tenant_user) | Create a new user in the Tenant Database.
[**disable_tenant_user**](TenantUsersApi.md#disable_tenant_user) | Disable a user in the Tenant Database.
[**enable_tenant_user**](TenantUsersApi.md#enable_tenant_user) | Enable a user in the Tenant Database.
[**get_all_tenant_users_with_filter**](TenantUsersApi.md#get_all_tenant_users_with_filter) | Get all users from the Tenant Database.
[**get_tenant_user_by_ol_user_id**](TenantUsersApi.md#get_tenant_user_by_ol_user_id) | Get a user from the Tenant Database.
[**get_tenant_user_profile**](TenantUsersApi.md#get_tenant_user_profile) | Get user profile from the Tenant Database.
[**send_email_to_user_for_password_change**](TenantUsersApi.md#send_email_to_user_for_password_change) | Send user password change email.
[**update_tenant_user**](TenantUsersApi.md#update_tenant_user) | Update a user in the Tenant Database.
[**update_tenant_user_details**](TenantUsersApi.md#update_tenant_user_details) | Update a user details in the Tenant Database.


# **create_tenant_user**
> ResponseCreateTenantUserResponse create_tenant_user(create_tenant_user_request)

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
    create_tenant_user_request = onelens_backend_client.CreateTenantUserRequest() # CreateTenantUserRequest | 

    try:
        # Create a new user in the Tenant Database.
        api_response = api_instance.create_tenant_user(create_tenant_user_request)
        print("The response of TenantUsersApi->create_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->create_tenant_user: %s\n" % e)
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
> ResponseGetTenantUserByIDResponse disable_tenant_user(ol_user_id)

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
    ol_user_id = 'ol_user_id_example' # str | 

    try:
        # Disable a user in the Tenant Database.
        api_response = api_instance.disable_tenant_user(ol_user_id)
        print("The response of TenantUsersApi->disable_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->disable_tenant_user: %s\n" % e)
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
> ResponseGetTenantUserByIDResponse enable_tenant_user(ol_user_id)

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
    ol_user_id = 'ol_user_id_example' # str | 

    try:
        # Enable a user in the Tenant Database.
        api_response = api_instance.enable_tenant_user(ol_user_id)
        print("The response of TenantUsersApi->enable_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->enable_tenant_user: %s\n" % e)
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
> ResponseGetTenantUsersWithFilterResponse get_all_tenant_users_with_filter(get_tenant_users_with_filter_api_request)

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
    get_tenant_users_with_filter_api_request = onelens_backend_client.GetTenantUsersWithFilterAPIRequest() # GetTenantUsersWithFilterAPIRequest | 

    try:
        # Get all users from the Tenant Database.
        api_response = api_instance.get_all_tenant_users_with_filter(get_tenant_users_with_filter_api_request)
        print("The response of TenantUsersApi->get_all_tenant_users_with_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->get_all_tenant_users_with_filter: %s\n" % e)
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
> ResponseGetTenantUserByIDResponse get_tenant_user_by_ol_user_id(ol_user_id)

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
    ol_user_id = 'ol_user_id_example' # str | 

    try:
        # Get a user from the Tenant Database.
        api_response = api_instance.get_tenant_user_by_ol_user_id(ol_user_id)
        print("The response of TenantUsersApi->get_tenant_user_by_ol_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->get_tenant_user_by_ol_user_id: %s\n" % e)
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

# **get_tenant_user_profile**
> ResponseGetTenantUserProfileResponse get_tenant_user_profile()

Get user profile from the Tenant Database.

Get user profile in the Tenant Database.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_user_profile_response import ResponseGetTenantUserProfileResponse
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

    try:
        # Get user profile from the Tenant Database.
        api_response = api_instance.get_tenant_user_profile()
        print("The response of TenantUsersApi->get_tenant_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->get_tenant_user_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseGetTenantUserProfileResponse**](ResponseGetTenantUserProfileResponse.md)

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

# **send_email_to_user_for_password_change**
> ResponsePasswordChangeEmailResponse send_email_to_user_for_password_change(ol_user_id)

Send user password change email.

Send user password change email.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_password_change_email_response import ResponsePasswordChangeEmailResponse
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
        # Send user password change email.
        api_response = api_instance.send_email_to_user_for_password_change(ol_user_id)
        print("The response of TenantUsersApi->send_email_to_user_for_password_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->send_email_to_user_for_password_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ol_user_id** | **str**|  | 

### Return type

[**ResponsePasswordChangeEmailResponse**](ResponsePasswordChangeEmailResponse.md)

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
> ResponseUpdateTenantUserResponse update_tenant_user(ol_user_id, tenant_user_update_fields_mixin)

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
    ol_user_id = 'ol_user_id_example' # str | 
    tenant_user_update_fields_mixin = onelens_backend_client.TenantUserUpdateFieldsMixin() # TenantUserUpdateFieldsMixin | 

    try:
        # Update a user in the Tenant Database.
        api_response = api_instance.update_tenant_user(ol_user_id, tenant_user_update_fields_mixin)
        print("The response of TenantUsersApi->update_tenant_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->update_tenant_user: %s\n" % e)
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
> ResponseUpdateTenantUserDetailsResponse update_tenant_user_details(tenant_user_details_update_fields_mixin)

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
    tenant_user_details_update_fields_mixin = onelens_backend_client.TenantUserDetailsUpdateFieldsMixin() # TenantUserDetailsUpdateFieldsMixin | 

    try:
        # Update a user details in the Tenant Database.
        api_response = api_instance.update_tenant_user_details(tenant_user_details_update_fields_mixin)
        print("The response of TenantUsersApi->update_tenant_user_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->update_tenant_user_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

