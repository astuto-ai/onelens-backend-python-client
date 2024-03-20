# PolicyTemplatePackServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_policy_template_pack**](PolicyTemplatePackServiceApi.md#create_policy_template_pack) | Create a new policy template pack.
[**get_policy_template_pack_by_id**](PolicyTemplatePackServiceApi.md#get_policy_template_pack_by_id) | Get a policy template pack by id.
[**get_policy_template_packs**](PolicyTemplatePackServiceApi.md#get_policy_template_packs) | Get all policy template packs.


# **create_policy_template_pack**
> CreatePolicyTemplatePackResponse create_policy_template_pack(create_policy_template_pack_request)

Create a new policy template pack.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_policy_template_pack_request import CreatePolicyTemplatePackRequest
from onelens_backend_client.models.create_policy_template_pack_response import CreatePolicyTemplatePackResponse
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
    api_instance = onelens_backend_client.PolicyTemplatePackServiceApi(api_client)
    create_policy_template_pack_request = onelens_backend_client.CreatePolicyTemplatePackRequest() # CreatePolicyTemplatePackRequest | 

    try:
        # Create a new policy template pack.
        api_response = api_instance.create_policy_template_pack(create_policy_template_pack_request)
        print("The response of PolicyTemplatePackServiceApi->create_policy_template_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplatePackServiceApi->create_policy_template_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_policy_template_pack_request** | [**CreatePolicyTemplatePackRequest**](CreatePolicyTemplatePackRequest.md)|  | 

### Return type

[**CreatePolicyTemplatePackResponse**](CreatePolicyTemplatePackResponse.md)

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

# **get_policy_template_pack_by_id**
> GetPolicyTemplatePackByIdResponse get_policy_template_pack_by_id(get_policy_template_pack_by_id_request)

Get a policy template pack by id.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_template_pack_by_id_request import GetPolicyTemplatePackByIdRequest
from onelens_backend_client.models.get_policy_template_pack_by_id_response import GetPolicyTemplatePackByIdResponse
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
    api_instance = onelens_backend_client.PolicyTemplatePackServiceApi(api_client)
    get_policy_template_pack_by_id_request = onelens_backend_client.GetPolicyTemplatePackByIdRequest() # GetPolicyTemplatePackByIdRequest | 

    try:
        # Get a policy template pack by id.
        api_response = api_instance.get_policy_template_pack_by_id(get_policy_template_pack_by_id_request)
        print("The response of PolicyTemplatePackServiceApi->get_policy_template_pack_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplatePackServiceApi->get_policy_template_pack_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_template_pack_by_id_request** | [**GetPolicyTemplatePackByIdRequest**](GetPolicyTemplatePackByIdRequest.md)|  | 

### Return type

[**GetPolicyTemplatePackByIdResponse**](GetPolicyTemplatePackByIdResponse.md)

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

# **get_policy_template_packs**
> GetPolicyTemplatePacksResponse get_policy_template_packs(get_policy_template_packs_request)

Get all policy template packs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_template_packs_request import GetPolicyTemplatePacksRequest
from onelens_backend_client.models.get_policy_template_packs_response import GetPolicyTemplatePacksResponse
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
    api_instance = onelens_backend_client.PolicyTemplatePackServiceApi(api_client)
    get_policy_template_packs_request = onelens_backend_client.GetPolicyTemplatePacksRequest() # GetPolicyTemplatePacksRequest | 

    try:
        # Get all policy template packs.
        api_response = api_instance.get_policy_template_packs(get_policy_template_packs_request)
        print("The response of PolicyTemplatePackServiceApi->get_policy_template_packs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplatePackServiceApi->get_policy_template_packs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_template_packs_request** | [**GetPolicyTemplatePacksRequest**](GetPolicyTemplatePacksRequest.md)|  | 

### Return type

[**GetPolicyTemplatePacksResponse**](GetPolicyTemplatePacksResponse.md)

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

