# onelens_backend_client.PoliciesPolicyTemplatePacksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_template_pack**](PoliciesPolicyTemplatePacksApi.md#create_policy_template_pack) | **POST** /v1/policies/policy_templates_packs | Create Policy Template Pack
[**get_policy_template_pack**](PoliciesPolicyTemplatePacksApi.md#get_policy_template_pack) | **GET** /v1/policies/policy_templates_packs/{policy_template_pack_id} | Get Policy Template Pack
[**get_policy_template_packs**](PoliciesPolicyTemplatePacksApi.md#get_policy_template_packs) | **POST** /v1/policies/policy_templates_packs/fetch | Get Policy Template Packs


# **create_policy_template_pack**
> ResponseCreatePolicyTemplatePackResponse create_policy_template_pack(create_policy_template_pack_request)

Create Policy Template Pack

An API endpoint that creates a new policy template pack.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_policy_template_pack_request import CreatePolicyTemplatePackRequest
from onelens_backend_client.models.response_create_policy_template_pack_response import ResponseCreatePolicyTemplatePackResponse
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
    api_instance = onelens_backend_client.PoliciesPolicyTemplatePacksApi(api_client)
    create_policy_template_pack_request = onelens_backend_client.CreatePolicyTemplatePackRequest() # CreatePolicyTemplatePackRequest | 

    try:
        # Create Policy Template Pack
        api_response = api_instance.create_policy_template_pack(create_policy_template_pack_request)
        print("The response of PoliciesPolicyTemplatePacksApi->create_policy_template_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesPolicyTemplatePacksApi->create_policy_template_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_policy_template_pack_request** | [**CreatePolicyTemplatePackRequest**](CreatePolicyTemplatePackRequest.md)|  | 

### Return type

[**ResponseCreatePolicyTemplatePackResponse**](ResponseCreatePolicyTemplatePackResponse.md)

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

# **get_policy_template_pack**
> ResponseGetPolicyTemplatePackByIdResponse get_policy_template_pack(policy_template_pack_id)

Get Policy Template Pack

An API endpoint that retrieves a policy template pack by id.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_policy_template_pack_by_id_response import ResponseGetPolicyTemplatePackByIdResponse
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
    api_instance = onelens_backend_client.PoliciesPolicyTemplatePacksApi(api_client)
    policy_template_pack_id = 'policy_template_pack_id_example' # str | 

    try:
        # Get Policy Template Pack
        api_response = api_instance.get_policy_template_pack(policy_template_pack_id)
        print("The response of PoliciesPolicyTemplatePacksApi->get_policy_template_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesPolicyTemplatePacksApi->get_policy_template_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_template_pack_id** | **str**|  | 

### Return type

[**ResponseGetPolicyTemplatePackByIdResponse**](ResponseGetPolicyTemplatePackByIdResponse.md)

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

# **get_policy_template_packs**
> ResponseGetPolicyTemplatePacksResponse get_policy_template_packs(get_policy_template_packs_request)

Get Policy Template Packs

An API endpoint that retrieves all policy template packs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_template_packs_request import GetPolicyTemplatePacksRequest
from onelens_backend_client.models.response_get_policy_template_packs_response import ResponseGetPolicyTemplatePacksResponse
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
    api_instance = onelens_backend_client.PoliciesPolicyTemplatePacksApi(api_client)
    get_policy_template_packs_request = onelens_backend_client.GetPolicyTemplatePacksRequest() # GetPolicyTemplatePacksRequest | 

    try:
        # Get Policy Template Packs
        api_response = api_instance.get_policy_template_packs(get_policy_template_packs_request)
        print("The response of PoliciesPolicyTemplatePacksApi->get_policy_template_packs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesPolicyTemplatePacksApi->get_policy_template_packs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_template_packs_request** | [**GetPolicyTemplatePacksRequest**](GetPolicyTemplatePacksRequest.md)|  | 

### Return type

[**ResponseGetPolicyTemplatePacksResponse**](ResponseGetPolicyTemplatePacksResponse.md)

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

