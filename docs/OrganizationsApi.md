# OrganizationsApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_organization**](OrganizationsApi.md#create_organization) | Create Organization
[**disable_organization**](OrganizationsApi.md#disable_organization) | Disable Organization
[**enable_organization**](OrganizationsApi.md#enable_organization) | Enable Organization
[**get_organization**](OrganizationsApi.md#get_organization) | Get Organization
[**get_organizations**](OrganizationsApi.md#get_organizations) | Get Organizations
[**update_organization**](OrganizationsApi.md#update_organization) | Update Organization


# **create_organization**
> CreateOrganizationResponse create_organization(create_organization_request)

Create Organization

An API endpoint that retrieves organization with organization IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_organization_request import CreateOrganizationRequest
from onelens_backend_client.models.create_organization_response import CreateOrganizationResponse
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
    api_instance = onelens_backend_client.OrganizationsApi(api_client)
    create_organization_request = onelens_backend_client.CreateOrganizationRequest() # CreateOrganizationRequest | 

    try:
        # Create Organization
        api_response = api_instance.create_organization(create_organization_request)
        print("The response of OrganizationsApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_request** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)|  | 

### Return type

[**CreateOrganizationResponse**](CreateOrganizationResponse.md)

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

# **disable_organization**
> object disable_organization(organization_id)

Disable Organization

An API endpoint that retrieves organization with organization IDs.

### Example


```python
import onelens_backend_client
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
    api_instance = onelens_backend_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Disable Organization
        api_response = api_instance.disable_organization(organization_id)
        print("The response of OrganizationsApi->disable_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->disable_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

**object**

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

# **enable_organization**
> object enable_organization(organization_id)

Enable Organization

An API endpoint to update organisation status to enable.

### Example


```python
import onelens_backend_client
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
    api_instance = onelens_backend_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Enable Organization
        api_response = api_instance.enable_organization(organization_id)
        print("The response of OrganizationsApi->enable_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->enable_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

**object**

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

# **get_organization**
> GetOrganizationByIDResponse get_organization(organization_id)

Get Organization

An API endpoint that retrieves organization with organization IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_organization_by_id_response import GetOrganizationByIDResponse
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
    api_instance = onelens_backend_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get Organization
        api_response = api_instance.get_organization(organization_id)
        print("The response of OrganizationsApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**GetOrganizationByIDResponse**](GetOrganizationByIDResponse.md)

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

# **get_organizations**
> GetOrganizationsResponse get_organizations(get_organizations_request)

Get Organizations

An API endpoint that retrieves organization with filters.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_organizations_request import GetOrganizationsRequest
from onelens_backend_client.models.get_organizations_response import GetOrganizationsResponse
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
    api_instance = onelens_backend_client.OrganizationsApi(api_client)
    get_organizations_request = onelens_backend_client.GetOrganizationsRequest() # GetOrganizationsRequest | 

    try:
        # Get Organizations
        api_response = api_instance.get_organizations(get_organizations_request)
        print("The response of OrganizationsApi->get_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_organizations_request** | [**GetOrganizationsRequest**](GetOrganizationsRequest.md)|  | 

### Return type

[**GetOrganizationsResponse**](GetOrganizationsResponse.md)

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

# **update_organization**
> UpdateOrganizationResponse update_organization(organization_id, update_organization_request)

Update Organization

An API endpoint that retrieves organization with organization IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_organization_request import UpdateOrganizationRequest
from onelens_backend_client.models.update_organization_response import UpdateOrganizationResponse
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
    api_instance = onelens_backend_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    update_organization_request = onelens_backend_client.UpdateOrganizationRequest() # UpdateOrganizationRequest | 

    try:
        # Update Organization
        api_response = api_instance.update_organization(organization_id, update_organization_request)
        print("The response of OrganizationsApi->update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **update_organization_request** | [**UpdateOrganizationRequest**](UpdateOrganizationRequest.md)|  | 

### Return type

[**UpdateOrganizationResponse**](UpdateOrganizationResponse.md)

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

