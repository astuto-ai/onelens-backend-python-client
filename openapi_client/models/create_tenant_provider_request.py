# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.parent_id import ParentId
from openapi_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class CreateTenantProviderRequest(BaseModel):
    """
    CreateTenantProviderRequest
    """ # noqa: E501
    cloud_provider: StrictStr = Field(description="Cloud provider")
    cloud_id: StrictStr = Field(description="Cloud ID")
    parent_id: Optional[ParentId] = None
    provider_config: Dict[str, Any] = Field(description="Provider config")
    tenant_id: Optional[TenantId] = None
    __properties: ClassVar[List[str]] = ["cloud_provider", "cloud_id", "parent_id", "provider_config", "tenant_id"]

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
        """Create an instance of CreateTenantProviderRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parent_id
        if self.parent_id:
            _dict['parent_id'] = self.parent_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenant_id'] = self.tenant_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateTenantProviderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloud_provider": obj.get("cloud_provider"),
            "cloud_id": obj.get("cloud_id"),
            "parent_id": ParentId.from_dict(obj["parent_id"]) if obj.get("parent_id") is not None else None,
            "provider_config": obj.get("provider_config"),
            "tenant_id": TenantId.from_dict(obj["tenant_id"]) if obj.get("tenant_id") is not None else None
        })
        return _obj


