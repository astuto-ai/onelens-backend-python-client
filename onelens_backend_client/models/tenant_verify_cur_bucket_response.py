# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.provider_config_output import ProviderConfigOutput
from onelens_backend_client.models.tenant_provider_state import TenantProviderState
from typing import Optional, Set
from typing_extensions import Self

class TenantVerifyCurBucketResponse(BaseModel):
    """
    TenantVerifyCurBucketResponse
    """ # noqa: E501
    cloud_provider: StrictStr = Field(description="Cloud provider")
    cloud_id: StrictStr = Field(description="Cloud ID")
    parent_id: Optional[StrictStr] = None
    provider_config: Optional[ProviderConfigOutput]
    id: StrictStr = Field(description="Unique ID for the Tenant Provider")
    is_parent_account: StrictBool = Field(description="billing account")
    tenant_id: StrictStr = Field(description="Tenant ID")
    is_billing_account: StrictBool = Field(description="is billing account")
    is_verified: StrictBool = Field(description="is verified")
    state: TenantProviderState = Field(description="state")
    __properties: ClassVar[List[str]] = ["cloud_provider", "cloud_id", "parent_id", "provider_config", "id", "is_parent_account", "tenant_id", "is_billing_account", "is_verified", "state"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TenantVerifyCurBucketResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of provider_config
        if self.provider_config:
            _dict['provider_config'] = self.provider_config.to_dict()
        # set to None if parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_id is None and "parent_id" in self.model_fields_set:
            _dict['parent_id'] = None

        # set to None if provider_config (nullable) is None
        # and model_fields_set contains the field
        if self.provider_config is None and "provider_config" in self.model_fields_set:
            _dict['provider_config'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantVerifyCurBucketResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloud_provider": obj.get("cloud_provider"),
            "cloud_id": obj.get("cloud_id"),
            "parent_id": obj.get("parent_id"),
            "provider_config": ProviderConfigOutput.from_dict(obj["provider_config"]) if obj.get("provider_config") is not None else None,
            "id": obj.get("id"),
            "is_parent_account": obj.get("is_parent_account"),
            "tenant_id": obj.get("tenant_id"),
            "is_billing_account": obj.get("is_billing_account"),
            "is_verified": obj.get("is_verified"),
            "state": obj.get("state")
        })
        return _obj


