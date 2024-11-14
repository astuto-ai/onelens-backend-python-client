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
from typing_extensions import Annotated
from onelens_backend_client.models.onelens_models_service_interfaces_tenant_metadata_commons_hierarchy_node_category2 import (
    OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2,
)
from typing import Set
from typing_extensions import Self


class GetHierarchyFlatFilters(BaseModel):
    """
    get hierarchy flat filters request
    """  # noqa: E501

    is_leaf: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    parent_names: Optional[List[StrictStr]] = None
    has_conflict: Optional[Annotated[List[StrictBool], Field(max_length=2)]] = None
    node_category: Optional[
        List[OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2]
    ] = None
    node_ids: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = [
        "is_leaf",
        "name",
        "parent_names",
        "has_conflict",
        "node_category",
        "node_ids",
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
        """Create an instance of GetHierarchyFlatFilters from a JSON string"""
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
        # set to None if is_leaf (nullable) is None
        # and model_fields_set contains the field
        if self.is_leaf is None and "is_leaf" in self.model_fields_set:
            _dict["is_leaf"] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict["name"] = None

        # set to None if parent_names (nullable) is None
        # and model_fields_set contains the field
        if self.parent_names is None and "parent_names" in self.model_fields_set:
            _dict["parent_names"] = None

        # set to None if has_conflict (nullable) is None
        # and model_fields_set contains the field
        if self.has_conflict is None and "has_conflict" in self.model_fields_set:
            _dict["has_conflict"] = None

        # set to None if node_category (nullable) is None
        # and model_fields_set contains the field
        if self.node_category is None and "node_category" in self.model_fields_set:
            _dict["node_category"] = None

        # set to None if node_ids (nullable) is None
        # and model_fields_set contains the field
        if self.node_ids is None and "node_ids" in self.model_fields_set:
            _dict["node_ids"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetHierarchyFlatFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "is_leaf": obj.get("is_leaf"),
                "name": obj.get("name"),
                "parent_names": obj.get("parent_names"),
                "has_conflict": obj.get("has_conflict"),
                "node_category": obj.get("node_category"),
                "node_ids": obj.get("node_ids"),
            }
        )
        return _obj
