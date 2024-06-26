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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.features import Features
from onelens_backend_client.models.resource_type import ResourceType
from typing import Optional, Set
from typing_extensions import Self

class ServiceCatalog(BaseModel):
    """
    ServiceCatalog
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    product_code: StrictStr
    display_name: StrictStr
    description: StrictStr
    resource_types: Optional[List[ResourceType]] = None
    features: Optional[Features] = None
    __properties: ClassVar[List[str]] = ["id", "name", "product_code", "display_name", "description", "resource_types", "features"]

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
        """Create an instance of ServiceCatalog from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in resource_types (list)
        _items = []
        if self.resource_types:
            for _item in self.resource_types:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resource_types'] = _items
        # override the default output from pydantic by calling `to_dict()` of features
        if self.features:
            _dict['features'] = self.features.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceCatalog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "product_code": obj.get("product_code"),
            "display_name": obj.get("display_name"),
            "description": obj.get("description"),
            "resource_types": [ResourceType.from_dict(_item) for _item in obj["resource_types"]] if obj.get("resource_types") is not None else None,
            "features": Features.from_dict(obj["features"]) if obj.get("features") is not None else None
        })
        return _obj


