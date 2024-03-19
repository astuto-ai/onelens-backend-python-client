# onelens_backend_client.UserTenantMappingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_tenant_mapping_v1_users_tenant_mapping_post**](UserTenantMappingApi.md#create_user_tenant_mapping_v1_users_tenant_mapping_post) | **POST** /v1/users/tenant_mapping | Create User Tenant Mapping


# **create_user_tenant_mapping_v1_users_tenant_mapping_post**
> ResponseCreateUserTenantMappingResponse create_user_tenant_mapping_v1_users_tenant_mapping_post(create_user_tenant_mapping_request)

Create User Tenant Mapping

An API endpoint that creates a new user tenant mapping.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_user_tenant_mapping_request import CreateUserTenantMappingRequest
from onelens_backend_client.models.response_create_user_tenant_mapping_response import ResponseCreateUserTenantMappingResponse
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
    api_instance = onelens_backend_client.UserTenantMappingApi(api_client)
    create_user_tenant_mapping_request = onelens_backend_client.CreateUserTenantMappingRequest() # CreateUserTenantMappingRequest | 

    try:
        # Create User Tenant Mapping
        api_response = api_instance.create_user_tenant_mapping_v1_users_tenant_mapping_post(create_user_tenant_mapping_request)
        print("The response of UserTenantMappingApi->create_user_tenant_mapping_v1_users_tenant_mapping_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTenantMappingApi->create_user_tenant_mapping_v1_users_tenant_mapping_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_tenant_mapping_request** | [**CreateUserTenantMappingRequest**](CreateUserTenantMappingRequest.md)|  | 

### Return type

[**ResponseCreateUserTenantMappingResponse**](ResponseCreateUserTenantMappingResponse.md)

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

