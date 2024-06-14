# TenantPoliciesApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**add_tenant_policy_exclusions**](TenantPoliciesApi.md#add_tenant_policy_exclusions) | Add Tenant Policy Exclusions
[**add_tenant_policy_exclusions_0**](TenantPoliciesApi.md#add_tenant_policy_exclusions_0) | Add Tenant Policy Exclusions
[**disable_tenant_policy**](TenantPoliciesApi.md#disable_tenant_policy) | Disable Tenant Policy
[**disable_tenant_policy_0**](TenantPoliciesApi.md#disable_tenant_policy_0) | Disable Tenant Policy
[**enable_all_policies**](TenantPoliciesApi.md#enable_all_policies) | Enable All Policies
[**enable_all_policies_0**](TenantPoliciesApi.md#enable_all_policies_0) | Enable All Policies
[**enable_tenant_policy**](TenantPoliciesApi.md#enable_tenant_policy) | Enable Tenant Policy
[**enable_tenant_policy_0**](TenantPoliciesApi.md#enable_tenant_policy_0) | Enable Tenant Policy
[**get_tenant_policies**](TenantPoliciesApi.md#get_tenant_policies) | Get Tenant Policies
[**get_tenant_policies_0**](TenantPoliciesApi.md#get_tenant_policies_0) | Get Tenant Policies
[**get_tenant_policies_with_settings**](TenantPoliciesApi.md#get_tenant_policies_with_settings) | Get Tenant Policies With Settings
[**get_tenant_policies_with_settings_0**](TenantPoliciesApi.md#get_tenant_policies_with_settings_0) | Get Tenant Policies With Settings
[**get_tenant_policy_by_id**](TenantPoliciesApi.md#get_tenant_policy_by_id) | Get Tenant Policy By Id
[**get_tenant_policy_by_id_0**](TenantPoliciesApi.md#get_tenant_policy_by_id_0) | Get Tenant Policy By Id
[**get_tenant_policy_by_id_with_recommendations**](TenantPoliciesApi.md#get_tenant_policy_by_id_with_recommendations) | Get Tenant Policy By Id With Recommendations
[**get_tenant_policy_by_id_with_recommendations_0**](TenantPoliciesApi.md#get_tenant_policy_by_id_with_recommendations_0) | Get Tenant Policy By Id With Recommendations
[**get_tenant_policy_settings**](TenantPoliciesApi.md#get_tenant_policy_settings) | Get Tenant Policy Settings
[**get_tenant_policy_settings_0**](TenantPoliciesApi.md#get_tenant_policy_settings_0) | Get Tenant Policy Settings
[**override_tenant_policy_config**](TenantPoliciesApi.md#override_tenant_policy_config) | Override Tenant Policy Config
[**override_tenant_policy_config_0**](TenantPoliciesApi.md#override_tenant_policy_config_0) | Override Tenant Policy Config
[**override_tenant_policy_exclusions**](TenantPoliciesApi.md#override_tenant_policy_exclusions) | Override Tenant Policy Exclusions
[**override_tenant_policy_exclusions_0**](TenantPoliciesApi.md#override_tenant_policy_exclusions_0) | Override Tenant Policy Exclusions


# **add_tenant_policy_exclusions**
> ResponseAddTenantPolicyExclusionsResponse add_tenant_policy_exclusions(tenant_id, tenant_policy_id, add_tenant_policy_exclusions_api_request)

Add Tenant Policy Exclusions

API to add Tenant Policy Exclusions in Tenant DB

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.add_tenant_policy_exclusions_api_request import AddTenantPolicyExclusionsAPIRequest
from onelens_backend_client.models.response_add_tenant_policy_exclusions_response import ResponseAddTenantPolicyExclusionsResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_policy_id = 'tenant_policy_id_example' # str | 
    add_tenant_policy_exclusions_api_request = onelens_backend_client.AddTenantPolicyExclusionsAPIRequest() # AddTenantPolicyExclusionsAPIRequest | 

    try:
        # Add Tenant Policy Exclusions
        api_response = api_instance.add_tenant_policy_exclusions(tenant_id, tenant_policy_id, add_tenant_policy_exclusions_api_request)
        print("The response of TenantPoliciesApi->add_tenant_policy_exclusions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->add_tenant_policy_exclusions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_policy_id** | **str**|  | 
 **add_tenant_policy_exclusions_api_request** | [**AddTenantPolicyExclusionsAPIRequest**](AddTenantPolicyExclusionsAPIRequest.md)|  | 

### Return type

[**ResponseAddTenantPolicyExclusionsResponse**](ResponseAddTenantPolicyExclusionsResponse.md)

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

# **add_tenant_policy_exclusions_0**
> ResponseAddTenantPolicyExclusionsResponse add_tenant_policy_exclusions_0(tenant_policy_id, add_tenant_policy_exclusions_api_request)

Add Tenant Policy Exclusions

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.add_tenant_policy_exclusions_api_request import AddTenantPolicyExclusionsAPIRequest
from onelens_backend_client.models.response_add_tenant_policy_exclusions_response import ResponseAddTenantPolicyExclusionsResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_policy_id = 'tenant_policy_id_example' # str | 
    add_tenant_policy_exclusions_api_request = onelens_backend_client.AddTenantPolicyExclusionsAPIRequest() # AddTenantPolicyExclusionsAPIRequest | 

    try:
        # Add Tenant Policy Exclusions
        api_response = api_instance.add_tenant_policy_exclusions_0(tenant_policy_id, add_tenant_policy_exclusions_api_request)
        print("The response of TenantPoliciesApi->add_tenant_policy_exclusions_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->add_tenant_policy_exclusions_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_policy_id** | **str**|  | 
 **add_tenant_policy_exclusions_api_request** | [**AddTenantPolicyExclusionsAPIRequest**](AddTenantPolicyExclusionsAPIRequest.md)|  | 

### Return type

[**ResponseAddTenantPolicyExclusionsResponse**](ResponseAddTenantPolicyExclusionsResponse.md)

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

# **disable_tenant_policy**
> ResponseDisableTenantPolicyResponse disable_tenant_policy(tenant_id, tenant_policy_id)

Disable Tenant Policy

API to Disable a single Tenant Policy in Tenant DB

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_disable_tenant_policy_response import ResponseDisableTenantPolicyResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_policy_id = 'tenant_policy_id_example' # str | 

    try:
        # Disable Tenant Policy
        api_response = api_instance.disable_tenant_policy(tenant_id, tenant_policy_id)
        print("The response of TenantPoliciesApi->disable_tenant_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->disable_tenant_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_policy_id** | **str**|  | 

### Return type

[**ResponseDisableTenantPolicyResponse**](ResponseDisableTenantPolicyResponse.md)

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

# **disable_tenant_policy_0**
> ResponseDisableTenantPolicyResponse disable_tenant_policy_0(tenant_policy_id)

Disable Tenant Policy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_disable_tenant_policy_response import ResponseDisableTenantPolicyResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_policy_id = 'tenant_policy_id_example' # str | 

    try:
        # Disable Tenant Policy
        api_response = api_instance.disable_tenant_policy_0(tenant_policy_id)
        print("The response of TenantPoliciesApi->disable_tenant_policy_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->disable_tenant_policy_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_policy_id** | **str**|  | 

### Return type

[**ResponseDisableTenantPolicyResponse**](ResponseDisableTenantPolicyResponse.md)

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

# **enable_all_policies**
> ResponseEnableAllPoliciesResponse enable_all_policies(tenant_id)

Enable All Policies

An API endpoint that enables all policies for a tenant.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_enable_all_policies_response import ResponseEnableAllPoliciesResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Enable All Policies
        api_response = api_instance.enable_all_policies(tenant_id)
        print("The response of TenantPoliciesApi->enable_all_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->enable_all_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ResponseEnableAllPoliciesResponse**](ResponseEnableAllPoliciesResponse.md)

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

# **enable_all_policies_0**
> ResponseEnableAllPoliciesResponse enable_all_policies_0()

Enable All Policies

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_enable_all_policies_response import ResponseEnableAllPoliciesResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)

    try:
        # Enable All Policies
        api_response = api_instance.enable_all_policies_0()
        print("The response of TenantPoliciesApi->enable_all_policies_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->enable_all_policies_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseEnableAllPoliciesResponse**](ResponseEnableAllPoliciesResponse.md)

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

# **enable_tenant_policy**
> ResponseEnableTenantPolicyResponse enable_tenant_policy(tenant_id, tenant_policy_id)

Enable Tenant Policy

API to Enable a single Tenant Policy in Tenant DB

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_enable_tenant_policy_response import ResponseEnableTenantPolicyResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_policy_id = 'tenant_policy_id_example' # str | 

    try:
        # Enable Tenant Policy
        api_response = api_instance.enable_tenant_policy(tenant_id, tenant_policy_id)
        print("The response of TenantPoliciesApi->enable_tenant_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->enable_tenant_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_policy_id** | **str**|  | 

### Return type

[**ResponseEnableTenantPolicyResponse**](ResponseEnableTenantPolicyResponse.md)

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

# **enable_tenant_policy_0**
> ResponseEnableTenantPolicyResponse enable_tenant_policy_0(tenant_policy_id)

Enable Tenant Policy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_enable_tenant_policy_response import ResponseEnableTenantPolicyResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_policy_id = 'tenant_policy_id_example' # str | 

    try:
        # Enable Tenant Policy
        api_response = api_instance.enable_tenant_policy_0(tenant_policy_id)
        print("The response of TenantPoliciesApi->enable_tenant_policy_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->enable_tenant_policy_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_policy_id** | **str**|  | 

### Return type

[**ResponseEnableTenantPolicyResponse**](ResponseEnableTenantPolicyResponse.md)

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

# **get_tenant_policies**
> ResponseGetTenantPoliciesResponse get_tenant_policies(tenant_id, get_tenant_policies_api_request)

Get Tenant Policies

API to get all Tenant Policies in Tenant DB

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_policies_api_request import GetTenantPoliciesAPIRequest
from onelens_backend_client.models.response_get_tenant_policies_response import ResponseGetTenantPoliciesResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_tenant_policies_api_request = onelens_backend_client.GetTenantPoliciesAPIRequest() # GetTenantPoliciesAPIRequest | 

    try:
        # Get Tenant Policies
        api_response = api_instance.get_tenant_policies(tenant_id, get_tenant_policies_api_request)
        print("The response of TenantPoliciesApi->get_tenant_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->get_tenant_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_tenant_policies_api_request** | [**GetTenantPoliciesAPIRequest**](GetTenantPoliciesAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantPoliciesResponse**](ResponseGetTenantPoliciesResponse.md)

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

# **get_tenant_policies_0**
> ResponseGetTenantPoliciesResponse get_tenant_policies_0(get_tenant_policies_api_request)

Get Tenant Policies

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_policies_api_request import GetTenantPoliciesAPIRequest
from onelens_backend_client.models.response_get_tenant_policies_response import ResponseGetTenantPoliciesResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    get_tenant_policies_api_request = onelens_backend_client.GetTenantPoliciesAPIRequest() # GetTenantPoliciesAPIRequest | 

    try:
        # Get Tenant Policies
        api_response = api_instance.get_tenant_policies_0(get_tenant_policies_api_request)
        print("The response of TenantPoliciesApi->get_tenant_policies_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->get_tenant_policies_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_policies_api_request** | [**GetTenantPoliciesAPIRequest**](GetTenantPoliciesAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantPoliciesResponse**](ResponseGetTenantPoliciesResponse.md)

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

# **get_tenant_policies_with_settings**
> ResponseGetTenantPoliciesWithSettingsResponse get_tenant_policies_with_settings(tenant_id, get_tenant_policies_with_settings_api_request)

Get Tenant Policies With Settings

API to get all Tenant Policies along with Settings in Tenant DB

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_policies_with_settings_api_request import GetTenantPoliciesWithSettingsAPIRequest
from onelens_backend_client.models.response_get_tenant_policies_with_settings_response import ResponseGetTenantPoliciesWithSettingsResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_tenant_policies_with_settings_api_request = onelens_backend_client.GetTenantPoliciesWithSettingsAPIRequest() # GetTenantPoliciesWithSettingsAPIRequest | 

    try:
        # Get Tenant Policies With Settings
        api_response = api_instance.get_tenant_policies_with_settings(tenant_id, get_tenant_policies_with_settings_api_request)
        print("The response of TenantPoliciesApi->get_tenant_policies_with_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->get_tenant_policies_with_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_tenant_policies_with_settings_api_request** | [**GetTenantPoliciesWithSettingsAPIRequest**](GetTenantPoliciesWithSettingsAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantPoliciesWithSettingsResponse**](ResponseGetTenantPoliciesWithSettingsResponse.md)

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

# **get_tenant_policies_with_settings_0**
> ResponseGetTenantPoliciesWithSettingsResponse get_tenant_policies_with_settings_0(get_tenant_policies_with_settings_api_request)

Get Tenant Policies With Settings

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_policies_with_settings_api_request import GetTenantPoliciesWithSettingsAPIRequest
from onelens_backend_client.models.response_get_tenant_policies_with_settings_response import ResponseGetTenantPoliciesWithSettingsResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    get_tenant_policies_with_settings_api_request = onelens_backend_client.GetTenantPoliciesWithSettingsAPIRequest() # GetTenantPoliciesWithSettingsAPIRequest | 

    try:
        # Get Tenant Policies With Settings
        api_response = api_instance.get_tenant_policies_with_settings_0(get_tenant_policies_with_settings_api_request)
        print("The response of TenantPoliciesApi->get_tenant_policies_with_settings_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->get_tenant_policies_with_settings_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_policies_with_settings_api_request** | [**GetTenantPoliciesWithSettingsAPIRequest**](GetTenantPoliciesWithSettingsAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantPoliciesWithSettingsResponse**](ResponseGetTenantPoliciesWithSettingsResponse.md)

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

# **get_tenant_policy_by_id**
> ResponseGetTenantPolicyByIdResponse get_tenant_policy_by_id(tenant_id, tenant_policy_id)

Get Tenant Policy By Id

API to get a Tenant Policy by id in Tenant DB

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_policy_by_id_response import ResponseGetTenantPolicyByIdResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_policy_id = 'tenant_policy_id_example' # str | 

    try:
        # Get Tenant Policy By Id
        api_response = api_instance.get_tenant_policy_by_id(tenant_id, tenant_policy_id)
        print("The response of TenantPoliciesApi->get_tenant_policy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->get_tenant_policy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_policy_id** | **str**|  | 

### Return type

[**ResponseGetTenantPolicyByIdResponse**](ResponseGetTenantPolicyByIdResponse.md)

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

# **get_tenant_policy_by_id_0**
> ResponseGetTenantPolicyByIdResponse get_tenant_policy_by_id_0(tenant_policy_id)

Get Tenant Policy By Id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_policy_by_id_response import ResponseGetTenantPolicyByIdResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_policy_id = 'tenant_policy_id_example' # str | 

    try:
        # Get Tenant Policy By Id
        api_response = api_instance.get_tenant_policy_by_id_0(tenant_policy_id)
        print("The response of TenantPoliciesApi->get_tenant_policy_by_id_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->get_tenant_policy_by_id_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_policy_id** | **str**|  | 

### Return type

[**ResponseGetTenantPolicyByIdResponse**](ResponseGetTenantPolicyByIdResponse.md)

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

# **get_tenant_policy_by_id_with_recommendations**
> ResponseGetTenantPolicyWithSummaryRequest get_tenant_policy_by_id_with_recommendations(tenant_id, tenant_policy_id)

Get Tenant Policy By Id With Recommendations

API to get a Tenant Policy by id in Tenant DB

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_policy_with_summary_request import ResponseGetTenantPolicyWithSummaryRequest
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_policy_id = 'tenant_policy_id_example' # str | 

    try:
        # Get Tenant Policy By Id With Recommendations
        api_response = api_instance.get_tenant_policy_by_id_with_recommendations(tenant_id, tenant_policy_id)
        print("The response of TenantPoliciesApi->get_tenant_policy_by_id_with_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->get_tenant_policy_by_id_with_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_policy_id** | **str**|  | 

### Return type

[**ResponseGetTenantPolicyWithSummaryRequest**](ResponseGetTenantPolicyWithSummaryRequest.md)

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

# **get_tenant_policy_by_id_with_recommendations_0**
> ResponseGetTenantPolicyWithSummaryRequest get_tenant_policy_by_id_with_recommendations_0(tenant_policy_id)

Get Tenant Policy By Id With Recommendations

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_tenant_policy_with_summary_request import ResponseGetTenantPolicyWithSummaryRequest
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_policy_id = 'tenant_policy_id_example' # str | 

    try:
        # Get Tenant Policy By Id With Recommendations
        api_response = api_instance.get_tenant_policy_by_id_with_recommendations_0(tenant_policy_id)
        print("The response of TenantPoliciesApi->get_tenant_policy_by_id_with_recommendations_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->get_tenant_policy_by_id_with_recommendations_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_policy_id** | **str**|  | 

### Return type

[**ResponseGetTenantPolicyWithSummaryRequest**](ResponseGetTenantPolicyWithSummaryRequest.md)

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

# **get_tenant_policy_settings**
> ResponseGetTenantPolicySettingsResponse get_tenant_policy_settings(tenant_id, get_tenant_policy_settings_api_request)

Get Tenant Policy Settings

API to get all Tenant Policy Settings in Tenant DB

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_policy_settings_api_request import GetTenantPolicySettingsAPIRequest
from onelens_backend_client.models.response_get_tenant_policy_settings_response import ResponseGetTenantPolicySettingsResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_tenant_policy_settings_api_request = onelens_backend_client.GetTenantPolicySettingsAPIRequest() # GetTenantPolicySettingsAPIRequest | 

    try:
        # Get Tenant Policy Settings
        api_response = api_instance.get_tenant_policy_settings(tenant_id, get_tenant_policy_settings_api_request)
        print("The response of TenantPoliciesApi->get_tenant_policy_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->get_tenant_policy_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_tenant_policy_settings_api_request** | [**GetTenantPolicySettingsAPIRequest**](GetTenantPolicySettingsAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantPolicySettingsResponse**](ResponseGetTenantPolicySettingsResponse.md)

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

# **get_tenant_policy_settings_0**
> ResponseGetTenantPolicySettingsResponse get_tenant_policy_settings_0(get_tenant_policy_settings_api_request)

Get Tenant Policy Settings

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_policy_settings_api_request import GetTenantPolicySettingsAPIRequest
from onelens_backend_client.models.response_get_tenant_policy_settings_response import ResponseGetTenantPolicySettingsResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    get_tenant_policy_settings_api_request = onelens_backend_client.GetTenantPolicySettingsAPIRequest() # GetTenantPolicySettingsAPIRequest | 

    try:
        # Get Tenant Policy Settings
        api_response = api_instance.get_tenant_policy_settings_0(get_tenant_policy_settings_api_request)
        print("The response of TenantPoliciesApi->get_tenant_policy_settings_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->get_tenant_policy_settings_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_policy_settings_api_request** | [**GetTenantPolicySettingsAPIRequest**](GetTenantPolicySettingsAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantPolicySettingsResponse**](ResponseGetTenantPolicySettingsResponse.md)

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

# **override_tenant_policy_config**
> ResponseGetTenantPoliciesResponse override_tenant_policy_config(tenant_id, tenant_policy_id, override_tenant_policy_config_api_request)

Override Tenant Policy Config

API to get all Tenant Policies in Tenant DB

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.override_tenant_policy_config_api_request import OverrideTenantPolicyConfigAPIRequest
from onelens_backend_client.models.response_get_tenant_policies_response import ResponseGetTenantPoliciesResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_policy_id = 'tenant_policy_id_example' # str | 
    override_tenant_policy_config_api_request = onelens_backend_client.OverrideTenantPolicyConfigAPIRequest() # OverrideTenantPolicyConfigAPIRequest | 

    try:
        # Override Tenant Policy Config
        api_response = api_instance.override_tenant_policy_config(tenant_id, tenant_policy_id, override_tenant_policy_config_api_request)
        print("The response of TenantPoliciesApi->override_tenant_policy_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->override_tenant_policy_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_policy_id** | **str**|  | 
 **override_tenant_policy_config_api_request** | [**OverrideTenantPolicyConfigAPIRequest**](OverrideTenantPolicyConfigAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantPoliciesResponse**](ResponseGetTenantPoliciesResponse.md)

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

# **override_tenant_policy_config_0**
> ResponseGetTenantPoliciesResponse override_tenant_policy_config_0(tenant_policy_id, override_tenant_policy_config_api_request)

Override Tenant Policy Config

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.override_tenant_policy_config_api_request import OverrideTenantPolicyConfigAPIRequest
from onelens_backend_client.models.response_get_tenant_policies_response import ResponseGetTenantPoliciesResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_policy_id = 'tenant_policy_id_example' # str | 
    override_tenant_policy_config_api_request = onelens_backend_client.OverrideTenantPolicyConfigAPIRequest() # OverrideTenantPolicyConfigAPIRequest | 

    try:
        # Override Tenant Policy Config
        api_response = api_instance.override_tenant_policy_config_0(tenant_policy_id, override_tenant_policy_config_api_request)
        print("The response of TenantPoliciesApi->override_tenant_policy_config_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->override_tenant_policy_config_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_policy_id** | **str**|  | 
 **override_tenant_policy_config_api_request** | [**OverrideTenantPolicyConfigAPIRequest**](OverrideTenantPolicyConfigAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantPoliciesResponse**](ResponseGetTenantPoliciesResponse.md)

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

# **override_tenant_policy_exclusions**
> ResponseOverrideTenantPolicyExclusionsResponse override_tenant_policy_exclusions(tenant_id, tenant_policy_id, override_tenant_policy_exclusions_api_request)

Override Tenant Policy Exclusions

API to override Tenant Policy Exclusions in Tenant DB

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.override_tenant_policy_exclusions_api_request import OverrideTenantPolicyExclusionsAPIRequest
from onelens_backend_client.models.response_override_tenant_policy_exclusions_response import ResponseOverrideTenantPolicyExclusionsResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_policy_id = 'tenant_policy_id_example' # str | 
    override_tenant_policy_exclusions_api_request = onelens_backend_client.OverrideTenantPolicyExclusionsAPIRequest() # OverrideTenantPolicyExclusionsAPIRequest | 

    try:
        # Override Tenant Policy Exclusions
        api_response = api_instance.override_tenant_policy_exclusions(tenant_id, tenant_policy_id, override_tenant_policy_exclusions_api_request)
        print("The response of TenantPoliciesApi->override_tenant_policy_exclusions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->override_tenant_policy_exclusions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_policy_id** | **str**|  | 
 **override_tenant_policy_exclusions_api_request** | [**OverrideTenantPolicyExclusionsAPIRequest**](OverrideTenantPolicyExclusionsAPIRequest.md)|  | 

### Return type

[**ResponseOverrideTenantPolicyExclusionsResponse**](ResponseOverrideTenantPolicyExclusionsResponse.md)

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

# **override_tenant_policy_exclusions_0**
> ResponseOverrideTenantPolicyExclusionsResponse override_tenant_policy_exclusions_0(tenant_policy_id, override_tenant_policy_exclusions_api_request)

Override Tenant Policy Exclusions

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.override_tenant_policy_exclusions_api_request import OverrideTenantPolicyExclusionsAPIRequest
from onelens_backend_client.models.response_override_tenant_policy_exclusions_response import ResponseOverrideTenantPolicyExclusionsResponse
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
    api_instance = onelens_backend_client.TenantPoliciesApi(api_client)
    tenant_policy_id = 'tenant_policy_id_example' # str | 
    override_tenant_policy_exclusions_api_request = onelens_backend_client.OverrideTenantPolicyExclusionsAPIRequest() # OverrideTenantPolicyExclusionsAPIRequest | 

    try:
        # Override Tenant Policy Exclusions
        api_response = api_instance.override_tenant_policy_exclusions_0(tenant_policy_id, override_tenant_policy_exclusions_api_request)
        print("The response of TenantPoliciesApi->override_tenant_policy_exclusions_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPoliciesApi->override_tenant_policy_exclusions_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_policy_id** | **str**|  | 
 **override_tenant_policy_exclusions_api_request** | [**OverrideTenantPolicyExclusionsAPIRequest**](OverrideTenantPolicyExclusionsAPIRequest.md)|  | 

### Return type

[**ResponseOverrideTenantPolicyExclusionsResponse**](ResponseOverrideTenantPolicyExclusionsResponse.md)

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

