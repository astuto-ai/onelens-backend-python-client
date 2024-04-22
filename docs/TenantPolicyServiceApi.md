# TenantPolicyServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**add_tenant_policy_exclusions**](TenantPolicyServiceApi.md#add_tenant_policy_exclusions) | Add tenant policy exclusions.
[**disable_tenant_policy**](TenantPolicyServiceApi.md#disable_tenant_policy) | disable a policy for a tenant in the tenant DB.
[**enable_all_policies**](TenantPolicyServiceApi.md#enable_all_policies) | enables all policies for a tenant.
[**enable_tenant_policy**](TenantPolicyServiceApi.md#enable_tenant_policy) | enables a policy for a tenant in the tenant DB.
[**get_tenant_policies**](TenantPolicyServiceApi.md#get_tenant_policies) | Retrieves all tenant policies, optionally filtered by the parameters in the request.
[**get_tenant_policy_settings**](TenantPolicyServiceApi.md#get_tenant_policy_settings) | Retrieves all tenant policy settings, optionally filtered by the parameters in the request.
[**override_tenant_policy_config**](TenantPolicyServiceApi.md#override_tenant_policy_config) | Override the tenant policy config with the provided config.
[**override_tenant_policy_exclusions**](TenantPolicyServiceApi.md#override_tenant_policy_exclusions) | Override tenant policy exclusions.


# **add_tenant_policy_exclusions**
> AddTenantPolicyExclusionsResponse add_tenant_policy_exclusions(add_tenant_policy_exclusions_request)

Add tenant policy exclusions.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.add_tenant_policy_exclusions_request import AddTenantPolicyExclusionsRequest
from onelens_backend_client.models.add_tenant_policy_exclusions_response import AddTenantPolicyExclusionsResponse
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
    api_instance = onelens_backend_client.TenantPolicyServiceApi(api_client)
    add_tenant_policy_exclusions_request = onelens_backend_client.AddTenantPolicyExclusionsRequest() # AddTenantPolicyExclusionsRequest | 

    try:
        # Add tenant policy exclusions.
        api_response = api_instance.add_tenant_policy_exclusions(add_tenant_policy_exclusions_request)
        print("The response of TenantPolicyServiceApi->add_tenant_policy_exclusions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPolicyServiceApi->add_tenant_policy_exclusions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_tenant_policy_exclusions_request** | [**AddTenantPolicyExclusionsRequest**](AddTenantPolicyExclusionsRequest.md)|  | 

### Return type

[**AddTenantPolicyExclusionsResponse**](AddTenantPolicyExclusionsResponse.md)

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
> object disable_tenant_policy(disable_tenant_policy_request)

disable a policy for a tenant in the tenant DB.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.disable_tenant_policy_request import DisableTenantPolicyRequest
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
    api_instance = onelens_backend_client.TenantPolicyServiceApi(api_client)
    disable_tenant_policy_request = onelens_backend_client.DisableTenantPolicyRequest() # DisableTenantPolicyRequest | 

    try:
        # disable a policy for a tenant in the tenant DB.
        api_response = api_instance.disable_tenant_policy(disable_tenant_policy_request)
        print("The response of TenantPolicyServiceApi->disable_tenant_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPolicyServiceApi->disable_tenant_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_tenant_policy_request** | [**DisableTenantPolicyRequest**](DisableTenantPolicyRequest.md)|  | 

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

# **enable_all_policies**
> object enable_all_policies(enable_all_policies_request)

enables all policies for a tenant.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.enable_all_policies_request import EnableAllPoliciesRequest
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
    api_instance = onelens_backend_client.TenantPolicyServiceApi(api_client)
    enable_all_policies_request = onelens_backend_client.EnableAllPoliciesRequest() # EnableAllPoliciesRequest | 

    try:
        # enables all policies for a tenant.
        api_response = api_instance.enable_all_policies(enable_all_policies_request)
        print("The response of TenantPolicyServiceApi->enable_all_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPolicyServiceApi->enable_all_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_all_policies_request** | [**EnableAllPoliciesRequest**](EnableAllPoliciesRequest.md)|  | 

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

# **enable_tenant_policy**
> object enable_tenant_policy(enable_tenant_policy_request)

enables a policy for a tenant in the tenant DB.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.enable_tenant_policy_request import EnableTenantPolicyRequest
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
    api_instance = onelens_backend_client.TenantPolicyServiceApi(api_client)
    enable_tenant_policy_request = onelens_backend_client.EnableTenantPolicyRequest() # EnableTenantPolicyRequest | 

    try:
        # enables a policy for a tenant in the tenant DB.
        api_response = api_instance.enable_tenant_policy(enable_tenant_policy_request)
        print("The response of TenantPolicyServiceApi->enable_tenant_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPolicyServiceApi->enable_tenant_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_tenant_policy_request** | [**EnableTenantPolicyRequest**](EnableTenantPolicyRequest.md)|  | 

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

# **get_tenant_policies**
> GetTenantPoliciesResponse get_tenant_policies(get_tenant_policies_request)

Retrieves all tenant policies, optionally filtered by the parameters in the request.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_policies_request import GetTenantPoliciesRequest
from onelens_backend_client.models.get_tenant_policies_response import GetTenantPoliciesResponse
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
    api_instance = onelens_backend_client.TenantPolicyServiceApi(api_client)
    get_tenant_policies_request = onelens_backend_client.GetTenantPoliciesRequest() # GetTenantPoliciesRequest | 

    try:
        # Retrieves all tenant policies, optionally filtered by the parameters in the request.
        api_response = api_instance.get_tenant_policies(get_tenant_policies_request)
        print("The response of TenantPolicyServiceApi->get_tenant_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPolicyServiceApi->get_tenant_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_policies_request** | [**GetTenantPoliciesRequest**](GetTenantPoliciesRequest.md)|  | 

### Return type

[**GetTenantPoliciesResponse**](GetTenantPoliciesResponse.md)

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

# **get_tenant_policy_settings**
> GetTenantPolicySettingsResponse get_tenant_policy_settings(get_tenant_policy_settings_request)

Retrieves all tenant policy settings, optionally filtered by the parameters in the request.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_policy_settings_request import GetTenantPolicySettingsRequest
from onelens_backend_client.models.get_tenant_policy_settings_response import GetTenantPolicySettingsResponse
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
    api_instance = onelens_backend_client.TenantPolicyServiceApi(api_client)
    get_tenant_policy_settings_request = onelens_backend_client.GetTenantPolicySettingsRequest() # GetTenantPolicySettingsRequest | 

    try:
        # Retrieves all tenant policy settings, optionally filtered by the parameters in the request.
        api_response = api_instance.get_tenant_policy_settings(get_tenant_policy_settings_request)
        print("The response of TenantPolicyServiceApi->get_tenant_policy_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPolicyServiceApi->get_tenant_policy_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_policy_settings_request** | [**GetTenantPolicySettingsRequest**](GetTenantPolicySettingsRequest.md)|  | 

### Return type

[**GetTenantPolicySettingsResponse**](GetTenantPolicySettingsResponse.md)

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
> OverrideTenantPolicyConfigResponse override_tenant_policy_config(override_tenant_policy_config_request)

Override the tenant policy config with the provided config.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.override_tenant_policy_config_request import OverrideTenantPolicyConfigRequest
from onelens_backend_client.models.override_tenant_policy_config_response import OverrideTenantPolicyConfigResponse
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
    api_instance = onelens_backend_client.TenantPolicyServiceApi(api_client)
    override_tenant_policy_config_request = onelens_backend_client.OverrideTenantPolicyConfigRequest() # OverrideTenantPolicyConfigRequest | 

    try:
        # Override the tenant policy config with the provided config.
        api_response = api_instance.override_tenant_policy_config(override_tenant_policy_config_request)
        print("The response of TenantPolicyServiceApi->override_tenant_policy_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPolicyServiceApi->override_tenant_policy_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_tenant_policy_config_request** | [**OverrideTenantPolicyConfigRequest**](OverrideTenantPolicyConfigRequest.md)|  | 

### Return type

[**OverrideTenantPolicyConfigResponse**](OverrideTenantPolicyConfigResponse.md)

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
> OverrideTenantPolicyExclusionsResponse override_tenant_policy_exclusions(override_tenant_policy_exclusions_request)

Override tenant policy exclusions.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.override_tenant_policy_exclusions_request import OverrideTenantPolicyExclusionsRequest
from onelens_backend_client.models.override_tenant_policy_exclusions_response import OverrideTenantPolicyExclusionsResponse
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
    api_instance = onelens_backend_client.TenantPolicyServiceApi(api_client)
    override_tenant_policy_exclusions_request = onelens_backend_client.OverrideTenantPolicyExclusionsRequest() # OverrideTenantPolicyExclusionsRequest | 

    try:
        # Override tenant policy exclusions.
        api_response = api_instance.override_tenant_policy_exclusions(override_tenant_policy_exclusions_request)
        print("The response of TenantPolicyServiceApi->override_tenant_policy_exclusions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantPolicyServiceApi->override_tenant_policy_exclusions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_tenant_policy_exclusions_request** | [**OverrideTenantPolicyExclusionsRequest**](OverrideTenantPolicyExclusionsRequest.md)|  | 

### Return type

[**OverrideTenantPolicyExclusionsResponse**](OverrideTenantPolicyExclusionsResponse.md)

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

