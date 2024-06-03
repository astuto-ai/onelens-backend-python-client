# TenantsTenantTicketsApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_tenant_tickets**](TenantsTenantTicketsApi.md#create_tenant_tickets) | Create Tenant Tickets
[**create_tenant_tickets_0**](TenantsTenantTicketsApi.md#create_tenant_tickets_0) | Create Tenant Tickets
[**get_all_policy_violations**](TenantsTenantTicketsApi.md#get_all_policy_violations) | Get All Policy Violations
[**get_all_policy_violations_0**](TenantsTenantTicketsApi.md#get_all_policy_violations_0) | Get All Policy Violations
[**get_policy_ticket_stats**](TenantsTenantTicketsApi.md#get_policy_ticket_stats) | Get Policy Ticket Stats
[**get_policy_ticket_stats_0**](TenantsTenantTicketsApi.md#get_policy_ticket_stats_0) | Get Policy Ticket Stats
[**get_policy_tickets_by_entity_id**](TenantsTenantTicketsApi.md#get_policy_tickets_by_entity_id) | Get Policy Tickets By Entity Id
[**get_policy_tickets_by_entity_id_0**](TenantsTenantTicketsApi.md#get_policy_tickets_by_entity_id_0) | Get Policy Tickets By Entity Id
[**get_policy_tickets_by_policy_id**](TenantsTenantTicketsApi.md#get_policy_tickets_by_policy_id) | Get Policy Tickets By Policy Id
[**get_policy_tickets_by_policy_id_0**](TenantsTenantTicketsApi.md#get_policy_tickets_by_policy_id_0) | Get Policy Tickets By Policy Id
[**get_tenant_ticket_by_id_with_policy**](TenantsTenantTicketsApi.md#get_tenant_ticket_by_id_with_policy) | Get Tenant Ticket By Id With Policy
[**get_tenant_ticket_by_id_with_policy_0**](TenantsTenantTicketsApi.md#get_tenant_ticket_by_id_with_policy_0) | Get Tenant Ticket By Id With Policy
[**get_tenant_tickets**](TenantsTenantTicketsApi.md#get_tenant_tickets) | Get Tenant Tickets
[**get_tenant_tickets_0**](TenantsTenantTicketsApi.md#get_tenant_tickets_0) | Get Tenant Tickets
[**update_tenant_ticket**](TenantsTenantTicketsApi.md#update_tenant_ticket) | Update Tenant Ticket
[**update_tenant_ticket_0**](TenantsTenantTicketsApi.md#update_tenant_ticket_0) | Update Tenant Ticket
[**update_tenant_tickets**](TenantsTenantTicketsApi.md#update_tenant_tickets) | Update Tenant Tickets
[**update_tenant_tickets_0**](TenantsTenantTicketsApi.md#update_tenant_tickets_0) | Update Tenant Tickets


# **create_tenant_tickets**
> ResponseCreateTenantTicketsResponse create_tenant_tickets(tenant_id, create_tenant_tickets_api_request)

Create Tenant Tickets

An API endpoint to create new tickets for a tenant in bulk

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_tickets_api_request import CreateTenantTicketsAPIRequest
from onelens_backend_client.models.response_create_tenant_tickets_response import ResponseCreateTenantTicketsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    create_tenant_tickets_api_request = onelens_backend_client.CreateTenantTicketsAPIRequest() # CreateTenantTicketsAPIRequest | 

    try:
        # Create Tenant Tickets
        api_response = api_instance.create_tenant_tickets(tenant_id, create_tenant_tickets_api_request)
        print("The response of TenantsTenantTicketsApi->create_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->create_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **create_tenant_tickets_api_request** | [**CreateTenantTicketsAPIRequest**](CreateTenantTicketsAPIRequest.md)|  | 

### Return type

[**ResponseCreateTenantTicketsResponse**](ResponseCreateTenantTicketsResponse.md)

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

# **create_tenant_tickets_0**
> ResponseCreateTenantTicketsResponse create_tenant_tickets_0(create_tenant_tickets_api_request)

Create Tenant Tickets

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_tenant_tickets_api_request import CreateTenantTicketsAPIRequest
from onelens_backend_client.models.response_create_tenant_tickets_response import ResponseCreateTenantTicketsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    create_tenant_tickets_api_request = onelens_backend_client.CreateTenantTicketsAPIRequest() # CreateTenantTicketsAPIRequest | 

    try:
        # Create Tenant Tickets
        api_response = api_instance.create_tenant_tickets_0(create_tenant_tickets_api_request)
        print("The response of TenantsTenantTicketsApi->create_tenant_tickets_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->create_tenant_tickets_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_tickets_api_request** | [**CreateTenantTicketsAPIRequest**](CreateTenantTicketsAPIRequest.md)|  | 

### Return type

[**ResponseCreateTenantTicketsResponse**](ResponseCreateTenantTicketsResponse.md)

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

# **get_all_policy_violations**
> ResponseGetAllPolicyViolationsResponse get_all_policy_violations(tenant_id, get_all_policy_violations_api_request)

Get All Policy Violations

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_policy_violations_api_request import GetAllPolicyViolationsAPIRequest
from onelens_backend_client.models.response_get_all_policy_violations_response import ResponseGetAllPolicyViolationsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_all_policy_violations_api_request = onelens_backend_client.GetAllPolicyViolationsAPIRequest() # GetAllPolicyViolationsAPIRequest | 

    try:
        # Get All Policy Violations
        api_response = api_instance.get_all_policy_violations(tenant_id, get_all_policy_violations_api_request)
        print("The response of TenantsTenantTicketsApi->get_all_policy_violations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_all_policy_violations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_all_policy_violations_api_request** | [**GetAllPolicyViolationsAPIRequest**](GetAllPolicyViolationsAPIRequest.md)|  | 

### Return type

[**ResponseGetAllPolicyViolationsResponse**](ResponseGetAllPolicyViolationsResponse.md)

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

# **get_all_policy_violations_0**
> ResponseGetAllPolicyViolationsResponse get_all_policy_violations_0(get_all_policy_violations_api_request)

Get All Policy Violations

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_policy_violations_api_request import GetAllPolicyViolationsAPIRequest
from onelens_backend_client.models.response_get_all_policy_violations_response import ResponseGetAllPolicyViolationsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    get_all_policy_violations_api_request = onelens_backend_client.GetAllPolicyViolationsAPIRequest() # GetAllPolicyViolationsAPIRequest | 

    try:
        # Get All Policy Violations
        api_response = api_instance.get_all_policy_violations_0(get_all_policy_violations_api_request)
        print("The response of TenantsTenantTicketsApi->get_all_policy_violations_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_all_policy_violations_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_all_policy_violations_api_request** | [**GetAllPolicyViolationsAPIRequest**](GetAllPolicyViolationsAPIRequest.md)|  | 

### Return type

[**ResponseGetAllPolicyViolationsResponse**](ResponseGetAllPolicyViolationsResponse.md)

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

# **get_policy_ticket_stats**
> ResponseGetPolicyTicketStatsResponse get_policy_ticket_stats(tenant_id, get_policy_ticket_stats_api_request)

Get Policy Ticket Stats

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_ticket_stats_api_request import GetPolicyTicketStatsAPIRequest
from onelens_backend_client.models.response_get_policy_ticket_stats_response import ResponseGetPolicyTicketStatsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_policy_ticket_stats_api_request = onelens_backend_client.GetPolicyTicketStatsAPIRequest() # GetPolicyTicketStatsAPIRequest | 

    try:
        # Get Policy Ticket Stats
        api_response = api_instance.get_policy_ticket_stats(tenant_id, get_policy_ticket_stats_api_request)
        print("The response of TenantsTenantTicketsApi->get_policy_ticket_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_policy_ticket_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_policy_ticket_stats_api_request** | [**GetPolicyTicketStatsAPIRequest**](GetPolicyTicketStatsAPIRequest.md)|  | 

### Return type

[**ResponseGetPolicyTicketStatsResponse**](ResponseGetPolicyTicketStatsResponse.md)

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

# **get_policy_ticket_stats_0**
> ResponseGetPolicyTicketStatsResponse get_policy_ticket_stats_0(get_policy_ticket_stats_api_request)

Get Policy Ticket Stats

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_ticket_stats_api_request import GetPolicyTicketStatsAPIRequest
from onelens_backend_client.models.response_get_policy_ticket_stats_response import ResponseGetPolicyTicketStatsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    get_policy_ticket_stats_api_request = onelens_backend_client.GetPolicyTicketStatsAPIRequest() # GetPolicyTicketStatsAPIRequest | 

    try:
        # Get Policy Ticket Stats
        api_response = api_instance.get_policy_ticket_stats_0(get_policy_ticket_stats_api_request)
        print("The response of TenantsTenantTicketsApi->get_policy_ticket_stats_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_policy_ticket_stats_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_ticket_stats_api_request** | [**GetPolicyTicketStatsAPIRequest**](GetPolicyTicketStatsAPIRequest.md)|  | 

### Return type

[**ResponseGetPolicyTicketStatsResponse**](ResponseGetPolicyTicketStatsResponse.md)

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

# **get_policy_tickets_by_entity_id**
> ResponseGetPolicyTicketsByEntityIdResponse get_policy_tickets_by_entity_id(tenant_id, get_policy_tickets_by_entity_id_api_request)

Get Policy Tickets By Entity Id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_tickets_by_entity_id_api_request import GetPolicyTicketsByEntityIdAPIRequest
from onelens_backend_client.models.response_get_policy_tickets_by_entity_id_response import ResponseGetPolicyTicketsByEntityIdResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_policy_tickets_by_entity_id_api_request = onelens_backend_client.GetPolicyTicketsByEntityIdAPIRequest() # GetPolicyTicketsByEntityIdAPIRequest | 

    try:
        # Get Policy Tickets By Entity Id
        api_response = api_instance.get_policy_tickets_by_entity_id(tenant_id, get_policy_tickets_by_entity_id_api_request)
        print("The response of TenantsTenantTicketsApi->get_policy_tickets_by_entity_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_policy_tickets_by_entity_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_policy_tickets_by_entity_id_api_request** | [**GetPolicyTicketsByEntityIdAPIRequest**](GetPolicyTicketsByEntityIdAPIRequest.md)|  | 

### Return type

[**ResponseGetPolicyTicketsByEntityIdResponse**](ResponseGetPolicyTicketsByEntityIdResponse.md)

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

# **get_policy_tickets_by_entity_id_0**
> ResponseGetPolicyTicketsByEntityIdResponse get_policy_tickets_by_entity_id_0(get_policy_tickets_by_entity_id_api_request)

Get Policy Tickets By Entity Id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_tickets_by_entity_id_api_request import GetPolicyTicketsByEntityIdAPIRequest
from onelens_backend_client.models.response_get_policy_tickets_by_entity_id_response import ResponseGetPolicyTicketsByEntityIdResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    get_policy_tickets_by_entity_id_api_request = onelens_backend_client.GetPolicyTicketsByEntityIdAPIRequest() # GetPolicyTicketsByEntityIdAPIRequest | 

    try:
        # Get Policy Tickets By Entity Id
        api_response = api_instance.get_policy_tickets_by_entity_id_0(get_policy_tickets_by_entity_id_api_request)
        print("The response of TenantsTenantTicketsApi->get_policy_tickets_by_entity_id_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_policy_tickets_by_entity_id_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_tickets_by_entity_id_api_request** | [**GetPolicyTicketsByEntityIdAPIRequest**](GetPolicyTicketsByEntityIdAPIRequest.md)|  | 

### Return type

[**ResponseGetPolicyTicketsByEntityIdResponse**](ResponseGetPolicyTicketsByEntityIdResponse.md)

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

# **get_policy_tickets_by_policy_id**
> ResponseGetPolicyTicketsByPolicyIdResponse get_policy_tickets_by_policy_id(tenant_id, get_policy_tickets_by_policy_id_api_request)

Get Policy Tickets By Policy Id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_tickets_by_policy_id_api_request import GetPolicyTicketsByPolicyIdAPIRequest
from onelens_backend_client.models.response_get_policy_tickets_by_policy_id_response import ResponseGetPolicyTicketsByPolicyIdResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_policy_tickets_by_policy_id_api_request = onelens_backend_client.GetPolicyTicketsByPolicyIdAPIRequest() # GetPolicyTicketsByPolicyIdAPIRequest | 

    try:
        # Get Policy Tickets By Policy Id
        api_response = api_instance.get_policy_tickets_by_policy_id(tenant_id, get_policy_tickets_by_policy_id_api_request)
        print("The response of TenantsTenantTicketsApi->get_policy_tickets_by_policy_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_policy_tickets_by_policy_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_policy_tickets_by_policy_id_api_request** | [**GetPolicyTicketsByPolicyIdAPIRequest**](GetPolicyTicketsByPolicyIdAPIRequest.md)|  | 

### Return type

[**ResponseGetPolicyTicketsByPolicyIdResponse**](ResponseGetPolicyTicketsByPolicyIdResponse.md)

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

# **get_policy_tickets_by_policy_id_0**
> ResponseGetPolicyTicketsByPolicyIdResponse get_policy_tickets_by_policy_id_0(get_policy_tickets_by_policy_id_api_request)

Get Policy Tickets By Policy Id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_policy_tickets_by_policy_id_api_request import GetPolicyTicketsByPolicyIdAPIRequest
from onelens_backend_client.models.response_get_policy_tickets_by_policy_id_response import ResponseGetPolicyTicketsByPolicyIdResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    get_policy_tickets_by_policy_id_api_request = onelens_backend_client.GetPolicyTicketsByPolicyIdAPIRequest() # GetPolicyTicketsByPolicyIdAPIRequest | 

    try:
        # Get Policy Tickets By Policy Id
        api_response = api_instance.get_policy_tickets_by_policy_id_0(get_policy_tickets_by_policy_id_api_request)
        print("The response of TenantsTenantTicketsApi->get_policy_tickets_by_policy_id_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_policy_tickets_by_policy_id_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_policy_tickets_by_policy_id_api_request** | [**GetPolicyTicketsByPolicyIdAPIRequest**](GetPolicyTicketsByPolicyIdAPIRequest.md)|  | 

### Return type

[**ResponseGetPolicyTicketsByPolicyIdResponse**](ResponseGetPolicyTicketsByPolicyIdResponse.md)

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

# **get_tenant_ticket_by_id_with_policy**
> ResponseGetTicketByIdPolicyDetailsResponse get_tenant_ticket_by_id_with_policy(tenant_id, ticket_id)

Get Tenant Ticket By Id With Policy

An API endpoint to get the ticket with policy details

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_ticket_by_id_policy_details_response import ResponseGetTicketByIdPolicyDetailsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ticket_id = 'ticket_id_example' # str | 

    try:
        # Get Tenant Ticket By Id With Policy
        api_response = api_instance.get_tenant_ticket_by_id_with_policy(tenant_id, ticket_id)
        print("The response of TenantsTenantTicketsApi->get_tenant_ticket_by_id_with_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_tenant_ticket_by_id_with_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ticket_id** | **str**|  | 

### Return type

[**ResponseGetTicketByIdPolicyDetailsResponse**](ResponseGetTicketByIdPolicyDetailsResponse.md)

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

# **get_tenant_ticket_by_id_with_policy_0**
> ResponseGetTicketByIdPolicyDetailsResponse get_tenant_ticket_by_id_with_policy_0(ticket_id)

Get Tenant Ticket By Id With Policy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_ticket_by_id_policy_details_response import ResponseGetTicketByIdPolicyDetailsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    ticket_id = 'ticket_id_example' # str | 

    try:
        # Get Tenant Ticket By Id With Policy
        api_response = api_instance.get_tenant_ticket_by_id_with_policy_0(ticket_id)
        print("The response of TenantsTenantTicketsApi->get_tenant_ticket_by_id_with_policy_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_tenant_ticket_by_id_with_policy_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 

### Return type

[**ResponseGetTicketByIdPolicyDetailsResponse**](ResponseGetTicketByIdPolicyDetailsResponse.md)

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

# **get_tenant_tickets**
> ResponseGetTenantTicketsResponse get_tenant_tickets(tenant_id, get_tenant_tickets_api_request)

Get Tenant Tickets

An API endpoint that retrieves active tickets for a tenant

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_tickets_api_request import GetTenantTicketsAPIRequest
from onelens_backend_client.models.response_get_tenant_tickets_response import ResponseGetTenantTicketsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    get_tenant_tickets_api_request = onelens_backend_client.GetTenantTicketsAPIRequest() # GetTenantTicketsAPIRequest | 

    try:
        # Get Tenant Tickets
        api_response = api_instance.get_tenant_tickets(tenant_id, get_tenant_tickets_api_request)
        print("The response of TenantsTenantTicketsApi->get_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **get_tenant_tickets_api_request** | [**GetTenantTicketsAPIRequest**](GetTenantTicketsAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantTicketsResponse**](ResponseGetTenantTicketsResponse.md)

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

# **get_tenant_tickets_0**
> ResponseGetTenantTicketsResponse get_tenant_tickets_0(get_tenant_tickets_api_request)

Get Tenant Tickets

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_tenant_tickets_api_request import GetTenantTicketsAPIRequest
from onelens_backend_client.models.response_get_tenant_tickets_response import ResponseGetTenantTicketsResponse
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    get_tenant_tickets_api_request = onelens_backend_client.GetTenantTicketsAPIRequest() # GetTenantTicketsAPIRequest | 

    try:
        # Get Tenant Tickets
        api_response = api_instance.get_tenant_tickets_0(get_tenant_tickets_api_request)
        print("The response of TenantsTenantTicketsApi->get_tenant_tickets_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->get_tenant_tickets_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tenant_tickets_api_request** | [**GetTenantTicketsAPIRequest**](GetTenantTicketsAPIRequest.md)|  | 

### Return type

[**ResponseGetTenantTicketsResponse**](ResponseGetTenantTicketsResponse.md)

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

# **update_tenant_ticket**
> ResponseUpdateTenantTicketResponse update_tenant_ticket(tenant_id, ticket_id, update_tenant_ticket_api_request)

Update Tenant Ticket

An API endpoint to update the user state of a ticket

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_ticket_response import ResponseUpdateTenantTicketResponse
from onelens_backend_client.models.update_tenant_ticket_api_request import UpdateTenantTicketAPIRequest
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    ticket_id = 'ticket_id_example' # str | 
    update_tenant_ticket_api_request = onelens_backend_client.UpdateTenantTicketAPIRequest() # UpdateTenantTicketAPIRequest | 

    try:
        # Update Tenant Ticket
        api_response = api_instance.update_tenant_ticket(tenant_id, ticket_id, update_tenant_ticket_api_request)
        print("The response of TenantsTenantTicketsApi->update_tenant_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->update_tenant_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **ticket_id** | **str**|  | 
 **update_tenant_ticket_api_request** | [**UpdateTenantTicketAPIRequest**](UpdateTenantTicketAPIRequest.md)|  | 

### Return type

[**ResponseUpdateTenantTicketResponse**](ResponseUpdateTenantTicketResponse.md)

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

# **update_tenant_ticket_0**
> ResponseUpdateTenantTicketResponse update_tenant_ticket_0(ticket_id, update_tenant_ticket_api_request)

Update Tenant Ticket

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_ticket_response import ResponseUpdateTenantTicketResponse
from onelens_backend_client.models.update_tenant_ticket_api_request import UpdateTenantTicketAPIRequest
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    ticket_id = 'ticket_id_example' # str | 
    update_tenant_ticket_api_request = onelens_backend_client.UpdateTenantTicketAPIRequest() # UpdateTenantTicketAPIRequest | 

    try:
        # Update Tenant Ticket
        api_response = api_instance.update_tenant_ticket_0(ticket_id, update_tenant_ticket_api_request)
        print("The response of TenantsTenantTicketsApi->update_tenant_ticket_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->update_tenant_ticket_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **update_tenant_ticket_api_request** | [**UpdateTenantTicketAPIRequest**](UpdateTenantTicketAPIRequest.md)|  | 

### Return type

[**ResponseUpdateTenantTicketResponse**](ResponseUpdateTenantTicketResponse.md)

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

# **update_tenant_tickets**
> ResponseUpdateTenantTicketsResponse update_tenant_tickets(tenant_id, update_tenant_tickets_api_request)

Update Tenant Tickets

An API endpoint to update tickets for a tenant in bulk

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_tickets_response import ResponseUpdateTenantTicketsResponse
from onelens_backend_client.models.update_tenant_tickets_api_request import UpdateTenantTicketsAPIRequest
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    update_tenant_tickets_api_request = onelens_backend_client.UpdateTenantTicketsAPIRequest() # UpdateTenantTicketsAPIRequest | 

    try:
        # Update Tenant Tickets
        api_response = api_instance.update_tenant_tickets(tenant_id, update_tenant_tickets_api_request)
        print("The response of TenantsTenantTicketsApi->update_tenant_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->update_tenant_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **update_tenant_tickets_api_request** | [**UpdateTenantTicketsAPIRequest**](UpdateTenantTicketsAPIRequest.md)|  | 

### Return type

[**ResponseUpdateTenantTicketsResponse**](ResponseUpdateTenantTicketsResponse.md)

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

# **update_tenant_tickets_0**
> ResponseUpdateTenantTicketsResponse update_tenant_tickets_0(update_tenant_tickets_api_request)

Update Tenant Tickets

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_update_tenant_tickets_response import ResponseUpdateTenantTicketsResponse
from onelens_backend_client.models.update_tenant_tickets_api_request import UpdateTenantTicketsAPIRequest
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
    api_instance = onelens_backend_client.TenantsTenantTicketsApi(api_client)
    update_tenant_tickets_api_request = onelens_backend_client.UpdateTenantTicketsAPIRequest() # UpdateTenantTicketsAPIRequest | 

    try:
        # Update Tenant Tickets
        api_response = api_instance.update_tenant_tickets_0(update_tenant_tickets_api_request)
        print("The response of TenantsTenantTicketsApi->update_tenant_tickets_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsTenantTicketsApi->update_tenant_tickets_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tenant_tickets_api_request** | [**UpdateTenantTicketsAPIRequest**](UpdateTenantTicketsAPIRequest.md)|  | 

### Return type

[**ResponseUpdateTenantTicketsResponse**](ResponseUpdateTenantTicketsResponse.md)

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

