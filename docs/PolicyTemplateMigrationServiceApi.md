# PolicyTemplateMigrationServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_pull_request**](PolicyTemplateMigrationServiceApi.md#create_pull_request) | Create a pull request for the policy template
[**sync_policies_from_repo**](PolicyTemplateMigrationServiceApi.md#sync_policies_from_repo) | Sync policy from repo


# **create_pull_request**
> CreatePolicyTemplateMigrationResponse create_pull_request(create_policy_template_migration_request)

Create a pull request for the policy template

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_policy_template_migration_request import CreatePolicyTemplateMigrationRequest
from onelens_backend_client.models.create_policy_template_migration_response import CreatePolicyTemplateMigrationResponse
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
    api_instance = onelens_backend_client.PolicyTemplateMigrationServiceApi(api_client)
    create_policy_template_migration_request = onelens_backend_client.CreatePolicyTemplateMigrationRequest() # CreatePolicyTemplateMigrationRequest | 

    try:
        # Create a pull request for the policy template
        api_response = api_instance.create_pull_request(create_policy_template_migration_request)
        print("The response of PolicyTemplateMigrationServiceApi->create_pull_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplateMigrationServiceApi->create_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_policy_template_migration_request** | [**CreatePolicyTemplateMigrationRequest**](CreatePolicyTemplateMigrationRequest.md)|  | 

### Return type

[**CreatePolicyTemplateMigrationResponse**](CreatePolicyTemplateMigrationResponse.md)

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

# **sync_policies_from_repo**
> SyncPolicyTemplateMigrationResponse sync_policies_from_repo(sync_policy_template_migration_request)

Sync policy from repo

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.sync_policy_template_migration_request import SyncPolicyTemplateMigrationRequest
from onelens_backend_client.models.sync_policy_template_migration_response import SyncPolicyTemplateMigrationResponse
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
    api_instance = onelens_backend_client.PolicyTemplateMigrationServiceApi(api_client)
    sync_policy_template_migration_request = onelens_backend_client.SyncPolicyTemplateMigrationRequest() # SyncPolicyTemplateMigrationRequest | 

    try:
        # Sync policy from repo
        api_response = api_instance.sync_policies_from_repo(sync_policy_template_migration_request)
        print("The response of PolicyTemplateMigrationServiceApi->sync_policies_from_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplateMigrationServiceApi->sync_policies_from_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_policy_template_migration_request** | [**SyncPolicyTemplateMigrationRequest**](SyncPolicyTemplateMigrationRequest.md)|  | 

### Return type

[**SyncPolicyTemplateMigrationResponse**](SyncPolicyTemplateMigrationResponse.md)

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

