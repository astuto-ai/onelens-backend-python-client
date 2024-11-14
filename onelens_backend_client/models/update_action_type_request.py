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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.service import Service
from typing import Set
from typing_extensions import Self


class UpdateActionTypeRequest(BaseModel):
    """
    UpdateActionTypeRequest
    """  # noqa: E501

    service: Service
    title: StrictStr = Field(description="Title")
    subtitle: Optional[StrictStr] = None
    description: StrictStr = Field(description="Description")
    alias: Optional[StrictStr]
    id: StrictInt = Field(description="Action Type ID")
    __properties: ClassVar[List[str]] = [
        "service",
        "title",
        "subtitle",
        "description",
        "alias",
        "id",
    ]

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
        """Create an instance of UpdateActionTypeRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of service
        if self.service:
            _dict["service"] = self.service.to_dict()
        # set to None if subtitle (nullable) is None
        # and model_fields_set contains the field
        if self.subtitle is None and "subtitle" in self.model_fields_set:
            _dict["subtitle"] = None

        # set to None if alias (nullable) is None
        # and model_fields_set contains the field
        if self.alias is None and "alias" in self.model_fields_set:
            _dict["alias"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateActionTypeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "service": Service.from_dict(obj["service"])
                if obj.get("service") is not None
                else None,
                "title": obj.get("title"),
                "subtitle": obj.get("subtitle"),
                "description": obj.get("description"),
                "alias": obj.get("alias"),
                "id": obj.get("id"),
            }
        )
        return _obj
