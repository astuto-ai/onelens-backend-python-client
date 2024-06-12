# Auth0Api

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_user**](Auth0Api.md#create_user) | Create User


# **create_user**
> ResponseCreateAuth0UserResponse create_user(create_auth0_user_request)

Create User

API endpoint that creates a new auth0 user and also stores the required data in onelens.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_auth0_user_request import CreateAuth0UserRequest
from onelens_backend_client.models.response_create_auth0_user_response import ResponseCreateAuth0UserResponse
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
    api_instance = onelens_backend_client.Auth0Api(api_client)
    create_auth0_user_request = onelens_backend_client.CreateAuth0UserRequest() # CreateAuth0UserRequest | 

    try:
        # Create User
        api_response = api_instance.create_user(create_auth0_user_request)
        print("The response of Auth0Api->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth0Api->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_auth0_user_request** | [**CreateAuth0UserRequest**](CreateAuth0UserRequest.md)|  | 

### Return type

[**ResponseCreateAuth0UserResponse**](ResponseCreateAuth0UserResponse.md)

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

