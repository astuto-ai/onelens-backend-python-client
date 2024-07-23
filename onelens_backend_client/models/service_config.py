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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from onelens_backend_client.models.effort import Effort
from onelens_backend_client.models.query_details import QueryDetails
from typing import Optional, Set
from typing_extensions import Self

class ServiceConfig(BaseModel):
    """
    ServiceConfig
    """ # noqa: E501
    service: StrictStr
    id: StrictStr
    action_type_id: StrictInt
    priority: StrictInt
    title: StrictStr
    subtitle: StrictStr = Field(alias="Subtitle")
    description: StrictStr
    effort: Effort
    query_details: QueryDetails
    __properties: ClassVar[List[str]] = ["service", "id", "action_type_id", "priority", "title", "Subtitle", "description", "effort", "query_details"]

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
        """Create an instance of ServiceConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of query_details
        if self.query_details:
            _dict['query_details'] = self.query_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "service": obj.get("service"),
            "id": obj.get("id"),
            "action_type_id": obj.get("action_type_id"),
            "priority": obj.get("priority"),
            "title": obj.get("title"),
            "Subtitle": obj.get("Subtitle"),
            "description": obj.get("description"),
            "effort": obj.get("effort"),
            "query_details": QueryDetails.from_dict(obj["query_details"]) if obj.get("query_details") is not None else None
        })
        return _obj


