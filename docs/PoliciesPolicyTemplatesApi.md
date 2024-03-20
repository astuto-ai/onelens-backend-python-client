# PoliciesPolicyTemplatesApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**activate_policy_template_policies_policy_templates_policy_template_id_activate_post**](PoliciesPolicyTemplatesApi.md#activate_policy_template_policies_policy_templates_policy_template_id_activate_post) | Activate Policy Template
[**create_policy_template_policies_policy_templates_post**](PoliciesPolicyTemplatesApi.md#create_policy_template_policies_policy_templates_post) | Create Policy Template
[**deactivate_policy_template_policies_policy_templates_policy_template_id_deactivate_post**](PoliciesPolicyTemplatesApi.md#deactivate_policy_template_policies_policy_templates_policy_template_id_deactivate_post) | Deactivate Policy Template
[**deprecate_policy_template_policies_policy_templates_policy_template_id_deprecate_post**](PoliciesPolicyTemplatesApi.md#deprecate_policy_template_policies_policy_templates_policy_template_id_deprecate_post) | Deprecate Policy Template
[**get_policy_template_policies_policy_templates_policy_template_id_get**](PoliciesPolicyTemplatesApi.md#get_policy_template_policies_policy_templates_policy_template_id_get) | Get Policy Template
[**get_policy_templates_policies_policy_templates_fetch_post**](PoliciesPolicyTemplatesApi.md#get_policy_templates_policies_policy_templates_fetch_post) | Get Policy Templates
[**update_policy_template_policies_policy_templates_policy_template_id_put**](PoliciesPolicyTemplatesApi.md#update_policy_template_policies_policy_templates_policy_template_id_put) | Update Policy Template


# **activate_policy_template_policies_policy_templates_policy_template_id_activate_post**
> ResponseActivatePolicyTemplateResponse activate_policy_template_policies_policy_templates_policy_template_id_activate_post(policy_template_id)

Activate Policy Template

An API endpoint that activates a policy template.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_activate_policy_template_response import ResponseActivatePolicyTemplateResponse
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
    api_instance = onelens_backend_client.PoliciesPolicyTemplatesApi(api_client)
    policy_template_id = 'policy_template_id_example' # str | 

    try:
        # Activate Policy Template
        api_response = api_instance.activate_policy_template_policies_policy_templates_policy_template_id_activate_post(policy_template_id)
        print("The response of PoliciesPolicyTemplatesApi->activate_policy_template_policies_policy_templates_policy_template_id_activate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesPolicyTemplatesApi->activate_policy_template_policies_policy_templates_policy_template_id_activate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_template_id** | **str**|  | 

### Return type

[**ResponseActivatePolicyTemplateResponse**](ResponseActivatePolicyTemplateResponse.md)

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

# **create_policy_template_policies_policy_templates_post**
> ResponseCreatePolicyTemplateResponse create_policy_template_policies_policy_templates_post(create_policy_template_request)

Create Policy Template

An API endpoint that creates a new policy template.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_policy_template_request import CreatePolicyTemplateRequest
from onelens_backend_client.models.response_create_policy_template_response import ResponseCreatePolicyTemplateResponse
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
    api_instance = onelens_backend_client.PoliciesPolicyTemplatesApi(api_client)
    create_policy_template_request = onelens_backend_client.CreatePolicyTemplateRequest() # CreatePolicyTemplateRequest | 

    try:
        # Create Policy Template
        api_response = api_instance.create_policy_template_policies_policy_templates_post(create_policy_template_request)
        print("The response of PoliciesPolicyTemplatesApi->create_policy_template_policies_policy_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesPolicyTemplatesApi->create_policy_template_policies_policy_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_policy_template_request** | [**CreatePolicyTemplateRequest**](CreatePolicyTemplateRequest.md)|  | 

### Return type

[**ResponseCreatePolicyTemplateResponse**](ResponseCreatePolicyTemplateResponse.md)

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

# **deactivate_policy_template_policies_policy_templates_policy_template_id_deactivate_post**
> ResponseDeprecatePolicyTemplateResponse deactivate_policy_template_policies_policy_templates_policy_template_id_deactivate_post(policy_template_id)

Deactivate Policy Template

An API endpoint that deactivates a policy template.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_deprecate_policy_template_response import ResponseDeprecatePolicyTemplateResponse
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
    api_instance = onelens_backend_client.PoliciesPolicyTemplatesApi(api_client)
    policy_template_id = 'policy_template_id_example' # str | 

    try:
        # Deactivate Policy Template
        api_response = api_instance.deactivate_policy_template_policies_policy_templates_policy_template_id_deactivate_post(policy_template_id)
        print("The response of PoliciesPolicyTemplatesApi->deactivate_policy_template_policies_policy_templates_policy_template_id_deactivate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesPolicyTemplatesApi->deactivate_policy_template_policies_policy_templates_policy_template_id_deactivate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_template_id** | **str**|  | 

### Return type

[**ResponseDeprecatePolicyTemplateResponse**](ResponseDeprecatePolicyTemplateResponse.md)

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

# **deprecate_policy_template_policies_policy_templates_policy_template_id_deprecate_post**
> ResponseDeprecatePolicyTemplateResponse deprecate_policy_template_policies_policy_templates_policy_template_id_deprecate_post(policy_template_id)

Deprecate Policy Template

An API endpoint that deprecates a policy template.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_deprecate_policy_template_response import ResponseDeprecatePolicyTemplateResponse
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
    api_instance = onelens_backend_client.PoliciesPolicyTemplatesApi(api_client)
    policy_template_id = 'policy_template_id_example' # str | 

    try:
        # Deprecate Policy Template
        api_response = api_instance.deprecate_policy_template_policies_policy_templates_policy_template_id_deprecate_post(policy_template_id)
        print("The response of PoliciesPolicyTemplatesApi->deprecate_policy_template_policies_policy_templates_policy_template_id_deprecate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesPolicyTemplatesApi->deprecate_policy_template_policies_policy_templates_policy_template_id_deprecate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_template_id** | **str**|  | 

### Return type

[**ResponseDeprecatePolicyTemplateResponse**](ResponseDeprecatePolicyTemplateResponse.md)

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

# **get_policy_template_policies_policy_templates_policy_template_id_get**
> ResponseGetPolicyTemplateByIDResponse get_policy_template_policies_policy_templates_policy_template_id_get(policy_template_id)

Get Policy Template

An API endpoint that retrieves a policy template by id.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_policy_template_by_id_response import ResponseGetPolicyTemplateByIDResponse
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
    api_instance = onelens_backend_client.PoliciesPolicyTemplatesApi(api_client)
    policy_template_id = 'policy_template_id_example' # str | 

    try:
        # Get Policy Template
        api_response = api_instance.get_policy_template_policies_policy_templates_policy_template_id_get(policy_template_id)
        print("The response of PoliciesPolicyTemplatesApi->get_policy_template_policies_policy_templates_policy_template_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesPolicyTemplatesApi->get_policy_template_policies_policy_templates_policy_template_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_template_id** | **str**|  | 

### Return type

[**ResponseGetPolicyTemplateByIDResponse**](ResponseGetPolicyTemplateByIDResponse.md)

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

# **get_policy_templates_policies_policy_templates_fetch_post**
> ResponseGetPolicyTemplatesResponse get_policy_templates_policies_policy_templates_fetch_post(get_policy_templates_request)

Get Policy Templates

An API endpoint that retrieves all policy templates.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_templates_request import GetPolicyTemplatesRequest
from onelens_backend_client.models.response_get_policy_templates_response import ResponseGetPolicyTemplatesResponse
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
    api_instance = onelens_backend_client.PoliciesPolicyTemplatesApi(api_client)
    get_policy_templates_request = onelens_backend_client.GetPolicyTemplatesRequest() # GetPolicyTemplatesRequest | 

    try:
        # Get Policy Templates
        api_response = api_instance.get_policy_templates_policies_policy_templates_fetch_post(get_policy_templates_request)
        print("The response of PoliciesPolicyTemplatesApi->get_policy_templates_policies_policy_templates_fetch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesPolicyTemplatesApi->get_policy_templates_policies_policy_templates_fetch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_templates_request** | [**GetPolicyTemplatesRequest**](GetPolicyTemplatesRequest.md)|  | 

### Return type

[**ResponseGetPolicyTemplatesResponse**](ResponseGetPolicyTemplatesResponse.md)

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

# **update_policy_template_policies_policy_templates_policy_template_id_put**
> ResponseUpdatePolicyTemplateResponse update_policy_template_policies_policy_templates_policy_template_id_put(policy_template_id, policy_template_update_fields_mixin)

Update Policy Template

An API endpoint that updates a policy template.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.policy_template_update_fields_mixin import PolicyTemplateUpdateFieldsMixin
from onelens_backend_client.models.response_update_policy_template_response import ResponseUpdatePolicyTemplateResponse
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
    api_instance = onelens_backend_client.PoliciesPolicyTemplatesApi(api_client)
    policy_template_id = 'policy_template_id_example' # str | 
    policy_template_update_fields_mixin = onelens_backend_client.PolicyTemplateUpdateFieldsMixin() # PolicyTemplateUpdateFieldsMixin | 

    try:
        # Update Policy Template
        api_response = api_instance.update_policy_template_policies_policy_templates_policy_template_id_put(policy_template_id, policy_template_update_fields_mixin)
        print("The response of PoliciesPolicyTemplatesApi->update_policy_template_policies_policy_templates_policy_template_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesPolicyTemplatesApi->update_policy_template_policies_policy_templates_policy_template_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_template_id** | **str**|  | 
 **policy_template_update_fields_mixin** | [**PolicyTemplateUpdateFieldsMixin**](PolicyTemplateUpdateFieldsMixin.md)|  | 

### Return type

[**ResponseUpdatePolicyTemplateResponse**](ResponseUpdatePolicyTemplateResponse.md)

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

