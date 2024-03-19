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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.cloud_id import CloudId
from onelens_backend_client.models.parent_id1 import ParentId1
from onelens_backend_client.models.provider_config import ProviderConfig
from typing import Optional, Set
from typing_extensions import Self

class UpdateTenantProviderRequest(BaseModel):
    """
    UpdateTenantProviderRequest
    """ # noqa: E501
    cloud_id: Optional[CloudId] = None
    parent_id: Optional[ParentId1] = None
    provider_config: Optional[ProviderConfig] = None
    __properties: ClassVar[List[str]] = ["cloud_id", "parent_id", "provider_config"]

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
        """Create an instance of UpdateTenantProviderRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cloud_id
        if self.cloud_id:
            _dict['cloud_id'] = self.cloud_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent_id
        if self.parent_id:
            _dict['parent_id'] = self.parent_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of provider_config
        if self.provider_config:
            _dict['provider_config'] = self.provider_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateTenantProviderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloud_id": CloudId.from_dict(obj["cloud_id"]) if obj.get("cloud_id") is not None else None,
            "parent_id": ParentId1.from_dict(obj["parent_id"]) if obj.get("parent_id") is not None else None,
            "provider_config": ProviderConfig.from_dict(obj["provider_config"]) if obj.get("provider_config") is not None else None
        })
        return _obj


