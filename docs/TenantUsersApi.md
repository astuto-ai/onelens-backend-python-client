# openapi_client.TenantUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_user_v1_users_tenant_post**](TenantUsersApi.md#create_tenant_user_v1_users_tenant_post) | **POST** /v1/users/tenant/ | Create Tenant User


# **create_tenant_user_v1_users_tenant_post**
> CreateTenatUserResponse create_tenant_user_v1_users_tenant_post(create_tenant_user_request)

Create Tenant User

### Example


```python
import openapi_client
from openapi_client.models.create_tenant_user_request import CreateTenantUserRequest
from openapi_client.models.create_tenat_user_response import CreateTenatUserResponse
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
    create_tenant_user_request = openapi_client.CreateTenantUserRequest() # CreateTenantUserRequest | 

    try:
        # Create Tenant User
        api_response = api_instance.create_tenant_user_v1_users_tenant_post(create_tenant_user_request)
        print("The response of TenantUsersApi->create_tenant_user_v1_users_tenant_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantUsersApi->create_tenant_user_v1_users_tenant_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_user_request** | [**CreateTenantUserRequest**](CreateTenantUserRequest.md)|  | 

### Return type

[**CreateTenatUserResponse**](CreateTenatUserResponse.md)

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

