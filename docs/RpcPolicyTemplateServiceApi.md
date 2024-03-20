# RpcPolicyTemplateServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**activate_policy_template_rpc_policy_template_service_activate_policy_template_post**](RpcPolicyTemplateServiceApi.md#activate_policy_template_rpc_policy_template_service_activate_policy_template_post) | Deprecate a policy template.
[**create_policy_template_rpc_policy_template_service_create_policy_template_post**](RpcPolicyTemplateServiceApi.md#create_policy_template_rpc_policy_template_service_create_policy_template_post) | Creates a new policy template.
[**deactivate_policy_template_rpc_policy_template_service_deactivate_policy_template_post**](RpcPolicyTemplateServiceApi.md#deactivate_policy_template_rpc_policy_template_service_deactivate_policy_template_post) | Deprecate a policy template.
[**deprecate_policy_template_rpc_policy_template_service_deprecate_policy_template_post**](RpcPolicyTemplateServiceApi.md#deprecate_policy_template_rpc_policy_template_service_deprecate_policy_template_post) | Deprecate a policy template.
[**get_policy_template_by_id_rpc_policy_template_service_get_policy_template_by_id_post**](RpcPolicyTemplateServiceApi.md#get_policy_template_by_id_rpc_policy_template_service_get_policy_template_by_id_post) | Retrieves a policy template by its unique identifier.
[**get_policy_templates_rpc_policy_template_service_get_policy_templates_post**](RpcPolicyTemplateServiceApi.md#get_policy_templates_rpc_policy_template_service_get_policy_templates_post) | Retrieves all policy templates, optionally filtered by the parameters in the request.
[**update_policy_template_rpc_policy_template_service_update_policy_template_post**](RpcPolicyTemplateServiceApi.md#update_policy_template_rpc_policy_template_service_update_policy_template_post) | Updates an existing policy template.


# **activate_policy_template_rpc_policy_template_service_activate_policy_template_post**
> object activate_policy_template_rpc_policy_template_service_activate_policy_template_post(activate_policy_template_request)

Deprecate a policy template.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.activate_policy_template_request import ActivatePolicyTemplateRequest
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
    api_instance = onelens_backend_client.RpcPolicyTemplateServiceApi(api_client)
    activate_policy_template_request = onelens_backend_client.ActivatePolicyTemplateRequest() # ActivatePolicyTemplateRequest | 

    try:
        # Deprecate a policy template.
        api_response = api_instance.activate_policy_template_rpc_policy_template_service_activate_policy_template_post(activate_policy_template_request)
        print("The response of RpcPolicyTemplateServiceApi->activate_policy_template_rpc_policy_template_service_activate_policy_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpcPolicyTemplateServiceApi->activate_policy_template_rpc_policy_template_service_activate_policy_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_policy_template_request** | [**ActivatePolicyTemplateRequest**](ActivatePolicyTemplateRequest.md)|  | 

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

# **create_policy_template_rpc_policy_template_service_create_policy_template_post**
> CreatePolicyTemplateResponse create_policy_template_rpc_policy_template_service_create_policy_template_post(create_policy_template_request)

Creates a new policy template.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_policy_template_request import CreatePolicyTemplateRequest
from onelens_backend_client.models.create_policy_template_response import CreatePolicyTemplateResponse
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
    api_instance = onelens_backend_client.RpcPolicyTemplateServiceApi(api_client)
    create_policy_template_request = onelens_backend_client.CreatePolicyTemplateRequest() # CreatePolicyTemplateRequest | 

    try:
        # Creates a new policy template.
        api_response = api_instance.create_policy_template_rpc_policy_template_service_create_policy_template_post(create_policy_template_request)
        print("The response of RpcPolicyTemplateServiceApi->create_policy_template_rpc_policy_template_service_create_policy_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpcPolicyTemplateServiceApi->create_policy_template_rpc_policy_template_service_create_policy_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_policy_template_request** | [**CreatePolicyTemplateRequest**](CreatePolicyTemplateRequest.md)|  | 

### Return type

[**CreatePolicyTemplateResponse**](CreatePolicyTemplateResponse.md)

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

# **deactivate_policy_template_rpc_policy_template_service_deactivate_policy_template_post**
> object deactivate_policy_template_rpc_policy_template_service_deactivate_policy_template_post(deactivate_policy_template_request)

Deprecate a policy template.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.deactivate_policy_template_request import DeactivatePolicyTemplateRequest
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
    api_instance = onelens_backend_client.RpcPolicyTemplateServiceApi(api_client)
    deactivate_policy_template_request = onelens_backend_client.DeactivatePolicyTemplateRequest() # DeactivatePolicyTemplateRequest | 

    try:
        # Deprecate a policy template.
        api_response = api_instance.deactivate_policy_template_rpc_policy_template_service_deactivate_policy_template_post(deactivate_policy_template_request)
        print("The response of RpcPolicyTemplateServiceApi->deactivate_policy_template_rpc_policy_template_service_deactivate_policy_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpcPolicyTemplateServiceApi->deactivate_policy_template_rpc_policy_template_service_deactivate_policy_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deactivate_policy_template_request** | [**DeactivatePolicyTemplateRequest**](DeactivatePolicyTemplateRequest.md)|  | 

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

# **deprecate_policy_template_rpc_policy_template_service_deprecate_policy_template_post**
> object deprecate_policy_template_rpc_policy_template_service_deprecate_policy_template_post(deprecate_policy_template_request)

Deprecate a policy template.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.deprecate_policy_template_request import DeprecatePolicyTemplateRequest
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
    api_instance = onelens_backend_client.RpcPolicyTemplateServiceApi(api_client)
    deprecate_policy_template_request = onelens_backend_client.DeprecatePolicyTemplateRequest() # DeprecatePolicyTemplateRequest | 

    try:
        # Deprecate a policy template.
        api_response = api_instance.deprecate_policy_template_rpc_policy_template_service_deprecate_policy_template_post(deprecate_policy_template_request)
        print("The response of RpcPolicyTemplateServiceApi->deprecate_policy_template_rpc_policy_template_service_deprecate_policy_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpcPolicyTemplateServiceApi->deprecate_policy_template_rpc_policy_template_service_deprecate_policy_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deprecate_policy_template_request** | [**DeprecatePolicyTemplateRequest**](DeprecatePolicyTemplateRequest.md)|  | 

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

# **get_policy_template_by_id_rpc_policy_template_service_get_policy_template_by_id_post**
> GetPolicyTemplateByIDResponse get_policy_template_by_id_rpc_policy_template_service_get_policy_template_by_id_post(get_policy_template_by_id_request)

Retrieves a policy template by its unique identifier.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_template_by_id_response import GetPolicyTemplateByIDResponse
from onelens_backend_client.models.get_policy_template_by_id_request import GetPolicyTemplateByIdRequest
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
    api_instance = onelens_backend_client.RpcPolicyTemplateServiceApi(api_client)
    get_policy_template_by_id_request = onelens_backend_client.GetPolicyTemplateByIdRequest() # GetPolicyTemplateByIdRequest | 

    try:
        # Retrieves a policy template by its unique identifier.
        api_response = api_instance.get_policy_template_by_id_rpc_policy_template_service_get_policy_template_by_id_post(get_policy_template_by_id_request)
        print("The response of RpcPolicyTemplateServiceApi->get_policy_template_by_id_rpc_policy_template_service_get_policy_template_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpcPolicyTemplateServiceApi->get_policy_template_by_id_rpc_policy_template_service_get_policy_template_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_template_by_id_request** | [**GetPolicyTemplateByIdRequest**](GetPolicyTemplateByIdRequest.md)|  | 

### Return type

[**GetPolicyTemplateByIDResponse**](GetPolicyTemplateByIDResponse.md)

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

# **get_policy_templates_rpc_policy_template_service_get_policy_templates_post**
> GetPolicyTemplatesResponse get_policy_templates_rpc_policy_template_service_get_policy_templates_post(get_policy_templates_request)

Retrieves all policy templates, optionally filtered by the parameters in the request.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_templates_request import GetPolicyTemplatesRequest
from onelens_backend_client.models.get_policy_templates_response import GetPolicyTemplatesResponse
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
    api_instance = onelens_backend_client.RpcPolicyTemplateServiceApi(api_client)
    get_policy_templates_request = onelens_backend_client.GetPolicyTemplatesRequest() # GetPolicyTemplatesRequest | 

    try:
        # Retrieves all policy templates, optionally filtered by the parameters in the request.
        api_response = api_instance.get_policy_templates_rpc_policy_template_service_get_policy_templates_post(get_policy_templates_request)
        print("The response of RpcPolicyTemplateServiceApi->get_policy_templates_rpc_policy_template_service_get_policy_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpcPolicyTemplateServiceApi->get_policy_templates_rpc_policy_template_service_get_policy_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_templates_request** | [**GetPolicyTemplatesRequest**](GetPolicyTemplatesRequest.md)|  | 

### Return type

[**GetPolicyTemplatesResponse**](GetPolicyTemplatesResponse.md)

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

# **update_policy_template_rpc_policy_template_service_update_policy_template_post**
> UpdatePolicyTemplateResponse update_policy_template_rpc_policy_template_service_update_policy_template_post(update_policy_template_request)

Updates an existing policy template.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_policy_template_request import UpdatePolicyTemplateRequest
from onelens_backend_client.models.update_policy_template_response import UpdatePolicyTemplateResponse
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
    api_instance = onelens_backend_client.RpcPolicyTemplateServiceApi(api_client)
    update_policy_template_request = onelens_backend_client.UpdatePolicyTemplateRequest() # UpdatePolicyTemplateRequest | 

    try:
        # Updates an existing policy template.
        api_response = api_instance.update_policy_template_rpc_policy_template_service_update_policy_template_post(update_policy_template_request)
        print("The response of RpcPolicyTemplateServiceApi->update_policy_template_rpc_policy_template_service_update_policy_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpcPolicyTemplateServiceApi->update_policy_template_rpc_policy_template_service_update_policy_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_policy_template_request** | [**UpdatePolicyTemplateRequest**](UpdatePolicyTemplateRequest.md)|  | 

### Return type

[**UpdatePolicyTemplateResponse**](UpdatePolicyTemplateResponse.md)

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

