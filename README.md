# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.5.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Root
        api_response = api_instance.root_get()
        print("The response of DefaultApi->root_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**root_get**](docs/DefaultApi.md#root_get) | **GET** / | Root
*PoliciesPolicyTemplatePacksApi* | [**create_policy_template_pack_v1_policies_policy_templates_packs_post**](docs/PoliciesPolicyTemplatePacksApi.md#create_policy_template_pack_v1_policies_policy_templates_packs_post) | **POST** /v1/policies/policy_templates_packs | Create Policy Template Pack
*PoliciesPolicyTemplatePacksApi* | [**get_policy_template_pack_v1_policies_policy_templates_packs_policy_template_pack_id_get**](docs/PoliciesPolicyTemplatePacksApi.md#get_policy_template_pack_v1_policies_policy_templates_packs_policy_template_pack_id_get) | **GET** /v1/policies/policy_templates_packs/{policy_template_pack_id} | Get Policy Template Pack
*PoliciesPolicyTemplatePacksApi* | [**get_policy_template_packs_v1_policies_policy_templates_packs_fetch_post**](docs/PoliciesPolicyTemplatePacksApi.md#get_policy_template_packs_v1_policies_policy_templates_packs_fetch_post) | **POST** /v1/policies/policy_templates_packs/fetch | Get Policy Template Packs
*PoliciesPolicyTemplatesApi* | [**activate_policy_template_v1_policies_policy_templates_policy_template_id_activate_post**](docs/PoliciesPolicyTemplatesApi.md#activate_policy_template_v1_policies_policy_templates_policy_template_id_activate_post) | **POST** /v1/policies/policy_templates/{policy_template_id}/activate | Activate Policy Template
*PoliciesPolicyTemplatesApi* | [**create_policy_template_v1_policies_policy_templates_post**](docs/PoliciesPolicyTemplatesApi.md#create_policy_template_v1_policies_policy_templates_post) | **POST** /v1/policies/policy_templates | Create Policy Template
*PoliciesPolicyTemplatesApi* | [**deactivate_policy_template_v1_policies_policy_templates_policy_template_id_deactivate_post**](docs/PoliciesPolicyTemplatesApi.md#deactivate_policy_template_v1_policies_policy_templates_policy_template_id_deactivate_post) | **POST** /v1/policies/policy_templates/{policy_template_id}/deactivate | Deactivate Policy Template
*PoliciesPolicyTemplatesApi* | [**deprecate_policy_template_v1_policies_policy_templates_policy_template_id_deprecate_post**](docs/PoliciesPolicyTemplatesApi.md#deprecate_policy_template_v1_policies_policy_templates_policy_template_id_deprecate_post) | **POST** /v1/policies/policy_templates/{policy_template_id}/deprecate | Deprecate Policy Template
*PoliciesPolicyTemplatesApi* | [**get_policy_template_v1_policies_policy_templates_policy_template_id_get**](docs/PoliciesPolicyTemplatesApi.md#get_policy_template_v1_policies_policy_templates_policy_template_id_get) | **GET** /v1/policies/policy_templates/{policy_template_id} | Get Policy Template
*PoliciesPolicyTemplatesApi* | [**get_policy_templates_v1_policies_policy_templates_fetch_post**](docs/PoliciesPolicyTemplatesApi.md#get_policy_templates_v1_policies_policy_templates_fetch_post) | **POST** /v1/policies/policy_templates/fetch | Get Policy Templates
*PoliciesPolicyTemplatesApi* | [**update_policy_template_v1_policies_policy_templates_policy_template_id_put**](docs/PoliciesPolicyTemplatesApi.md#update_policy_template_v1_policies_policy_templates_policy_template_id_put) | **PUT** /v1/policies/policy_templates/{policy_template_id} | Update Policy Template
*TenantUsersApi* | [**create_tenant_user_v1_users_tenant_post**](docs/TenantUsersApi.md#create_tenant_user_v1_users_tenant_post) | **POST** /v1/users/tenant/ | Create Tenant User
*TenantsApi* | [**create_tenant_v1_tenants_post**](docs/TenantsApi.md#create_tenant_v1_tenants_post) | **POST** /v1/tenants/ | Create Tenant
*TenantsApi* | [**disable_tenant_v1_tenants_tenant_id_disable_put**](docs/TenantsApi.md#disable_tenant_v1_tenants_tenant_id_disable_put) | **PUT** /v1/tenants/{tenant_id}/disable | Disable Tenant
*TenantsApi* | [**get_tenant_v1_tenants_tenant_id_get**](docs/TenantsApi.md#get_tenant_v1_tenants_tenant_id_get) | **GET** /v1/tenants/{tenant_id} | Get Tenant
*TenantsApi* | [**update_tenant_v1_tenants_tenant_id_put**](docs/TenantsApi.md#update_tenant_v1_tenants_tenant_id_put) | **PUT** /v1/tenants/{tenant_id} | Update Tenant
*TenantsTenantProviderVerifyApi* | [**verify_tenant_v1_tenants_tenant_id_providers_tenant_provider_id_verify_post**](docs/TenantsTenantProviderVerifyApi.md#verify_tenant_v1_tenants_tenant_id_providers_tenant_provider_id_verify_post) | **POST** /v1/tenants/{tenant_id}/providers/{tenant_provider_id}/verify | Verify Tenant
*TenantsTenantsProvidersApi* | [**create_tenant_provider_v1_tenants_tenant_id_providers_post**](docs/TenantsTenantsProvidersApi.md#create_tenant_provider_v1_tenants_tenant_id_providers_post) | **POST** /v1/tenants/{tenant_id}/providers | Create Tenant Provider
*TenantsTenantsProvidersApi* | [**disable_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_disable_put**](docs/TenantsTenantsProvidersApi.md#disable_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_disable_put) | **PUT** /v1/tenants/{tenant_id}/providers/{tenant_provider_id}/disable | Disable Tenant Provider
*TenantsTenantsProvidersApi* | [**get_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_get**](docs/TenantsTenantsProvidersApi.md#get_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_get) | **GET** /v1/tenants/{tenant_id}/providers/{tenant_provider_id} | Get Tenant Provider
*TenantsTenantsProvidersApi* | [**get_tenant_providers_v1_tenants_fetch_post**](docs/TenantsTenantsProvidersApi.md#get_tenant_providers_v1_tenants_fetch_post) | **POST** /v1/tenants/fetch | Get Tenant Providers
*TenantsTenantsProvidersApi* | [**update_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_put**](docs/TenantsTenantsProvidersApi.md#update_tenant_provider_v1_tenants_tenant_id_providers_tenant_provider_id_put) | **PUT** /v1/tenants/{tenant_id}/providers/{tenant_provider_id} | Update Tenant Provider
*UserTenantApi* | [**create_user_tenant_mapping_v1_users_tenant_mapping_post**](docs/UserTenantApi.md#create_user_tenant_mapping_v1_users_tenant_mapping_post) | **POST** /v1/users/tenant_mapping | Create User Tenant Mapping
*UsersApi* | [**create_user_v1_users_post**](docs/UsersApi.md#create_user_v1_users_post) | **POST** /v1/users/ | Create User
*UsersApi* | [**get_user_by_id_v1_users_user_id_get**](docs/UsersApi.md#get_user_by_id_v1_users_user_id_get) | **GET** /v1/users/{user_id} | Get User By Id
*UsersApi* | [**get_users_v1_users_get**](docs/UsersApi.md#get_users_v1_users_get) | **GET** /v1/users/ | Get Users
*UsersApi* | [**update_user_v1_users_put**](docs/UsersApi.md#update_user_v1_users_put) | **PUT** /v1/users/ | Update User


## Documentation For Models

 - [AttributesData](docs/AttributesData.md)
 - [AwsService](docs/AwsService.md)
 - [CloudId](docs/CloudId.md)
 - [CloudIds](docs/CloudIds.md)
 - [CloudProviders](docs/CloudProviders.md)
 - [ConfigSchema](docs/ConfigSchema.md)
 - [CreatePolicyTemplatePackRequest](docs/CreatePolicyTemplatePackRequest.md)
 - [CreatePolicyTemplatePackResponse](docs/CreatePolicyTemplatePackResponse.md)
 - [CreatePolicyTemplateRequest](docs/CreatePolicyTemplateRequest.md)
 - [CreatePolicyTemplateRequestServicesInner](docs/CreatePolicyTemplateRequestServicesInner.md)
 - [CreatePolicyTemplateResponse](docs/CreatePolicyTemplateResponse.md)
 - [CreateTenantProviderRequest](docs/CreateTenantProviderRequest.md)
 - [CreateTenantProviderResponse](docs/CreateTenantProviderResponse.md)
 - [CreateTenantRequest](docs/CreateTenantRequest.md)
 - [CreateTenantResponse](docs/CreateTenantResponse.md)
 - [CreateTenantUserRequest](docs/CreateTenantUserRequest.md)
 - [CreateTenatUserResponse](docs/CreateTenatUserResponse.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [CreateUserResponse](docs/CreateUserResponse.md)
 - [CreateUserTenantMappingRequest](docs/CreateUserTenantMappingRequest.md)
 - [CreateUserTenantMappingResponse](docs/CreateUserTenantMappingResponse.md)
 - [DefaultPolicyConfig](docs/DefaultPolicyConfig.md)
 - [Description](docs/Description.md)
 - [Domains](docs/Domains.md)
 - [GcpService](docs/GcpService.md)
 - [GetAllUsersRequest](docs/GetAllUsersRequest.md)
 - [GetAllUsersResponse](docs/GetAllUsersResponse.md)
 - [GetPolicyTemplateByIDResponse](docs/GetPolicyTemplateByIDResponse.md)
 - [GetPolicyTemplatePackByIdResponse](docs/GetPolicyTemplatePackByIdResponse.md)
 - [GetPolicyTemplatePacksRequest](docs/GetPolicyTemplatePacksRequest.md)
 - [GetPolicyTemplatePacksResponse](docs/GetPolicyTemplatePacksResponse.md)
 - [GetPolicyTemplatesRequest](docs/GetPolicyTemplatesRequest.md)
 - [GetPolicyTemplatesResponse](docs/GetPolicyTemplatesResponse.md)
 - [GetTenantByIDResponse](docs/GetTenantByIDResponse.md)
 - [GetTenantProviderByIDResponse](docs/GetTenantProviderByIDResponse.md)
 - [GetTenantProvidersRequest](docs/GetTenantProvidersRequest.md)
 - [GetTenantProvidersResponse](docs/GetTenantProvidersResponse.md)
 - [GetUserByIDResponse](docs/GetUserByIDResponse.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Inputs](docs/Inputs.md)
 - [IsParentAccount](docs/IsParentAccount.md)
 - [IsVerified](docs/IsVerified.md)
 - [Message](docs/Message.md)
 - [Name](docs/Name.md)
 - [OutputViolationSchema](docs/OutputViolationSchema.md)
 - [PaginationFields](docs/PaginationFields.md)
 - [PaginationParams](docs/PaginationParams.md)
 - [ParentId](docs/ParentId.md)
 - [ParentId1](docs/ParentId1.md)
 - [ParentIds](docs/ParentIds.md)
 - [PolicyCategory](docs/PolicyCategory.md)
 - [PolicyExecutionType](docs/PolicyExecutionType.md)
 - [PolicyTemplate](docs/PolicyTemplate.md)
 - [PolicyTemplateDetails](docs/PolicyTemplateDetails.md)
 - [PolicyTemplateDetailsRuleType](docs/PolicyTemplateDetailsRuleType.md)
 - [PolicyTemplateFilters](docs/PolicyTemplateFilters.md)
 - [PolicyTemplatePack](docs/PolicyTemplatePack.md)
 - [PolicyTemplatePackDetails](docs/PolicyTemplatePackDetails.md)
 - [PolicyTemplatePackState](docs/PolicyTemplatePackState.md)
 - [PolicyTemplateState](docs/PolicyTemplateState.md)
 - [PolicyTemplateUpdateFieldsMixin](docs/PolicyTemplateUpdateFieldsMixin.md)
 - [PolicyTemplateUpdateFieldsMixinDetails](docs/PolicyTemplateUpdateFieldsMixinDetails.md)
 - [PolicyTemplateUpdateFieldsMixinExecutionType](docs/PolicyTemplateUpdateFieldsMixinExecutionType.md)
 - [Provider](docs/Provider.md)
 - [ProviderConfig](docs/ProviderConfig.md)
 - [ResponseActivatePolicyTemplateResponse](docs/ResponseActivatePolicyTemplateResponse.md)
 - [ResponseCreatePolicyTemplatePackResponse](docs/ResponseCreatePolicyTemplatePackResponse.md)
 - [ResponseCreatePolicyTemplateResponse](docs/ResponseCreatePolicyTemplateResponse.md)
 - [ResponseCreateUserTenantMappingResponse](docs/ResponseCreateUserTenantMappingResponse.md)
 - [ResponseDeprecatePolicyTemplateResponse](docs/ResponseDeprecatePolicyTemplateResponse.md)
 - [ResponseDisableTenantProviderResponse](docs/ResponseDisableTenantProviderResponse.md)
 - [ResponseDisableTenantResponse](docs/ResponseDisableTenantResponse.md)
 - [ResponseGetPolicyTemplateByIDResponse](docs/ResponseGetPolicyTemplateByIDResponse.md)
 - [ResponseGetPolicyTemplatePackByIdResponse](docs/ResponseGetPolicyTemplatePackByIdResponse.md)
 - [ResponseGetPolicyTemplatePacksResponse](docs/ResponseGetPolicyTemplatePacksResponse.md)
 - [ResponseGetPolicyTemplatesResponse](docs/ResponseGetPolicyTemplatesResponse.md)
 - [ResponseGetTenantByIDResponse](docs/ResponseGetTenantByIDResponse.md)
 - [ResponseGetTenantProviderByIDResponse](docs/ResponseGetTenantProviderByIDResponse.md)
 - [ResponseGetTenantProvidersResponse](docs/ResponseGetTenantProvidersResponse.md)
 - [ResponseTenantVerifyResponse](docs/ResponseTenantVerifyResponse.md)
 - [ResponseUpdatePolicyTemplateResponse](docs/ResponseUpdatePolicyTemplateResponse.md)
 - [ResponseUpdateTenantProviderResponse](docs/ResponseUpdateTenantProviderResponse.md)
 - [ResponseUpdateTenantResponse](docs/ResponseUpdateTenantResponse.md)
 - [Role](docs/Role.md)
 - [RuleDefinition](docs/RuleDefinition.md)
 - [RuleType](docs/RuleType.md)
 - [SearchQuery](docs/SearchQuery.md)
 - [Services](docs/Services.md)
 - [SourceSchema](docs/SourceSchema.md)
 - [Sources](docs/Sources.md)
 - [States](docs/States.md)
 - [Status](docs/Status.md)
 - [TenantFilterData](docs/TenantFilterData.md)
 - [TenantId](docs/TenantId.md)
 - [TenantIds](docs/TenantIds.md)
 - [TenantProviderAttributes](docs/TenantProviderAttributes.md)
 - [TenantProviderFilters](docs/TenantProviderFilters.md)
 - [TenantVerifyRequest](docs/TenantVerifyRequest.md)
 - [TenantVerifyResponse](docs/TenantVerifyResponse.md)
 - [Timezone](docs/Timezone.md)
 - [Title](docs/Title.md)
 - [UpdatePolicyTemplateResponse](docs/UpdatePolicyTemplateResponse.md)
 - [UpdateTenantProviderRequest](docs/UpdateTenantProviderRequest.md)
 - [UpdateTenantProviderResponse](docs/UpdateTenantProviderResponse.md)
 - [UpdateTenantRequest](docs/UpdateTenantRequest.md)
 - [UpdateTenantResponse](docs/UpdateTenantResponse.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [UpdateUserResponse](docs/UpdateUserResponse.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




