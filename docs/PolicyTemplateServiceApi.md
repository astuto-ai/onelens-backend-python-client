# onelens_backend_client.PolicyTemplateServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | ------------- | -------------
[**activate_policy_template**](PolicyTemplateServiceApi.md#activate_policy_template) | Deprecate a policy template.
[**create_policy_template**](PolicyTemplateServiceApi.md#create_policy_template) | Creates a new policy template.
[**deactivate_policy_template**](PolicyTemplateServiceApi.md#deactivate_policy_template) | Deprecate a policy template.
[**deprecate_policy_template**](PolicyTemplateServiceApi.md#deprecate_policy_template) | Deprecate a policy template.
[**get_policy_template_by_id**](PolicyTemplateServiceApi.md#get_policy_template_by_id) | Retrieves a policy template by its unique identifier.
[**get_policy_templates**](PolicyTemplateServiceApi.md#get_policy_templates) | Retrieves all policy templates, optionally filtered by the parameters in the request.
[**update_policy_template**](PolicyTemplateServiceApi.md#update_policy_template) | Updates an existing policy template.


# **activate_policy_template**
> object activate_policy_template(activate_policy_template_request)

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
    api_instance = onelens_backend_client.PolicyTemplateServiceApi(api_client)
    activate_policy_template_request = onelens_backend_client.ActivatePolicyTemplateRequest() # ActivatePolicyTemplateRequest | 

    try:
        # Deprecate a policy template.
        api_response = api_instance.activate_policy_template(activate_policy_template_request)
        print("The response of PolicyTemplateServiceApi->activate_policy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplateServiceApi->activate_policy_template: %s\n" % e)
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

# **create_policy_template**
> CreatePolicyTemplateResponse create_policy_template(create_policy_template_request)

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
    api_instance = onelens_backend_client.PolicyTemplateServiceApi(api_client)
    create_policy_template_request = onelens_backend_client.CreatePolicyTemplateRequest() # CreatePolicyTemplateRequest | 

    try:
        # Creates a new policy template.
        api_response = api_instance.create_policy_template(create_policy_template_request)
        print("The response of PolicyTemplateServiceApi->create_policy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplateServiceApi->create_policy_template: %s\n" % e)
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

# **deactivate_policy_template**
> object deactivate_policy_template(deactivate_policy_template_request)

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
    api_instance = onelens_backend_client.PolicyTemplateServiceApi(api_client)
    deactivate_policy_template_request = onelens_backend_client.DeactivatePolicyTemplateRequest() # DeactivatePolicyTemplateRequest | 

    try:
        # Deprecate a policy template.
        api_response = api_instance.deactivate_policy_template(deactivate_policy_template_request)
        print("The response of PolicyTemplateServiceApi->deactivate_policy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplateServiceApi->deactivate_policy_template: %s\n" % e)
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

# **deprecate_policy_template**
> object deprecate_policy_template(deprecate_policy_template_request)

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
    api_instance = onelens_backend_client.PolicyTemplateServiceApi(api_client)
    deprecate_policy_template_request = onelens_backend_client.DeprecatePolicyTemplateRequest() # DeprecatePolicyTemplateRequest | 

    try:
        # Deprecate a policy template.
        api_response = api_instance.deprecate_policy_template(deprecate_policy_template_request)
        print("The response of PolicyTemplateServiceApi->deprecate_policy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplateServiceApi->deprecate_policy_template: %s\n" % e)
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

# **get_policy_template_by_id**
> GetPolicyTemplateByIDResponse get_policy_template_by_id(get_policy_template_by_id_request)

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
    api_instance = onelens_backend_client.PolicyTemplateServiceApi(api_client)
    get_policy_template_by_id_request = onelens_backend_client.GetPolicyTemplateByIdRequest() # GetPolicyTemplateByIdRequest | 

    try:
        # Retrieves a policy template by its unique identifier.
        api_response = api_instance.get_policy_template_by_id(get_policy_template_by_id_request)
        print("The response of PolicyTemplateServiceApi->get_policy_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplateServiceApi->get_policy_template_by_id: %s\n" % e)
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

# **get_policy_templates**
> GetPolicyTemplatesResponse get_policy_templates(get_policy_templates_request)

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
    api_instance = onelens_backend_client.PolicyTemplateServiceApi(api_client)
    get_policy_templates_request = onelens_backend_client.GetPolicyTemplatesRequest() # GetPolicyTemplatesRequest | 

    try:
        # Retrieves all policy templates, optionally filtered by the parameters in the request.
        api_response = api_instance.get_policy_templates(get_policy_templates_request)
        print("The response of PolicyTemplateServiceApi->get_policy_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplateServiceApi->get_policy_templates: %s\n" % e)
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

# **update_policy_template**
> UpdatePolicyTemplateResponse update_policy_template(update_policy_template_request)

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
    api_instance = onelens_backend_client.PolicyTemplateServiceApi(api_client)
    update_policy_template_request = onelens_backend_client.UpdatePolicyTemplateRequest() # UpdatePolicyTemplateRequest | 

    try:
        # Updates an existing policy template.
        api_response = api_instance.update_policy_template(update_policy_template_request)
        print("The response of PolicyTemplateServiceApi->update_policy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplateServiceApi->update_policy_template: %s\n" % e)
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

