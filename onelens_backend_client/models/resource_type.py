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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from onelens_backend_client.models.relationship_config_item import RelationshipConfigItem
from typing import Optional, Set
from typing_extensions import Self

class ResourceType(BaseModel):
    """
    ResourceType
    """ # noqa: E501
    resource_type: StrictStr
    resource_table: StrictStr
    select_columns: List[StrictStr]
    resource_url_template: StrictStr
    is_tags_available: StrictBool
    relationship_config: List[RelationshipConfigItem]
    __properties: ClassVar[List[str]] = ["resource_type", "resource_table", "select_columns", "resource_url_template", "is_tags_available", "relationship_config"]

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
        """Create an instance of ResourceType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in relationship_config (list)
        _items = []
        if self.relationship_config:
            for _item in self.relationship_config:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relationship_config'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResourceType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resource_type": obj.get("resource_type"),
            "resource_table": obj.get("resource_table"),
            "select_columns": obj.get("select_columns"),
            "resource_url_template": obj.get("resource_url_template"),
            "is_tags_available": obj.get("is_tags_available"),
            "relationship_config": [RelationshipConfigItem.from_dict(_item) for _item in obj["relationship_config"]] if obj.get("relationship_config") is not None else None
        })
        return _obj


