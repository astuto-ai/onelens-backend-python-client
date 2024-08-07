# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetTenantEmbedAppsLinksResponse(BaseModel):
    """
    GetTenantEmbedAppsLinksResponse
    """ # noqa: E501
    ol_user_id: StrictStr = Field(description="Unique onelens identifier for the user")
    tenant_id: StrictStr = Field(description="The unique identifier of the tenant")
    tab_name: StrictStr = Field(description="Name of the tab")
    link: StrictStr = Field(description="Link of the tab")
    system_created: Optional[StrictBool] = None
    id: StrictStr = Field(description="The unique identifier of the link")
    __properties: ClassVar[List[str]] = ["ol_user_id", "tenant_id", "tab_name", "link", "system_created", "id"]

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
        """Create an instance of GetTenantEmbedAppsLinksResponse from a JSON string"""
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
        # set to None if system_created (nullable) is None
        # and model_fields_set contains the field
        if self.system_created is None and "system_created" in self.model_fields_set:
            _dict['system_created'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTenantEmbedAppsLinksResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ol_user_id": obj.get("ol_user_id"),
            "tenant_id": obj.get("tenant_id"),
            "tab_name": obj.get("tab_name"),
            "link": obj.get("link"),
            "system_created": obj.get("system_created"),
            "id": obj.get("id")
        })
        return _obj


