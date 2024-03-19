# openapi_client.TenantUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_user_v1_users_tenant_tenant_id_post**](TenantUsersApi.md#create_tenant_user_v1_users_tenant_tenant_id_post) | **POST** /v1/users/tenant/{tenant_id} | Create a new user in the Tenant Database.
[**update_tenant_user_v1_users_tenant_tenant_id_ol_user_id_put**](TenantUsersApi.md#update_tenant_user_v1_users_tenant_tenant_id_ol_user_id_put) | **PUT** /v1/users/tenant/{tenant_id}/{ol_user_id} | Update a user in the Tenant Database.


# **create_tenant_user_v1_users_tenant_tenant_id_post**
> ResponseCreateTenantUserResponse create_tenant_user_v1_users_tenant_tenant_id_post(tenant_id, create_tenant_user_request)

Create a new user in the Tenant Database.

Create a new user in the Tenant Database.

### Example


```python
import openapi_client
from openapi_client.models.create_tenant_user_request import CreateTenantUserRequest
from openapi_client.models.response_create_tenant_user_response import ResponseCreateTenantUserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    create_tenant_user_request = openapi_client.CreateTenantUserRequest() # CreateTenantUserRequest | 

    try:
        # Create a new user in the Tenant Database.
        api_response = api_instance.create_tenant_user_v1_users_tenant_tenant_id_post(tenant_id, create_tenant_user_request)
        print("The response of TenantUsersApi->create_tenant_user_v1_users_tenant_tenant_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->create_tenant_user_v1_users_tenant_tenant_id_post: %s\n" % e)
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

# **update_tenant_user_v1_users_tenant_tenant_id_ol_user_id_put**
> ResponseUpdateTenantUserResponse update_tenant_user_v1_users_tenant_tenant_id_ol_user_id_put(tenant_id, ol_user_id, tenant_user_update_fields_mixin)

Update a user in the Tenant Database.

Update a user in the Tenant Database.

### Example


```python
import openapi_client
from openapi_client.models.response_update_tenant_user_response import ResponseUpdateTenantUserResponse
from openapi_client.models.tenant_user_update_fields_mixin import TenantUserUpdateFieldsMixin
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TenantUsersApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ol_user_id = 'ol_user_id_example' # str | 
    tenant_user_update_fields_mixin = openapi_client.TenantUserUpdateFieldsMixin() # TenantUserUpdateFieldsMixin | 

    try:
        # Update a user in the Tenant Database.
        api_response = api_instance.update_tenant_user_v1_users_tenant_tenant_id_ol_user_id_put(tenant_id, ol_user_id, tenant_user_update_fields_mixin)
        print("The response of TenantUsersApi->update_tenant_user_v1_users_tenant_tenant_id_ol_user_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->update_tenant_user_v1_users_tenant_tenant_id_ol_user_id_put: %s\n" % e)
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

