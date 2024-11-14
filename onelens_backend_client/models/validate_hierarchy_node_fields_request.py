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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.onelens_models_service_interfaces_tenant_metadata_commons_hierarchy_node_category2 import (
    OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2,
)
from typing import Set
from typing_extensions import Self


class ValidateHierarchyNodeFieldsRequest(BaseModel):
    """
    validate hierarchy node fields request
    """  # noqa: E501

    name: StrictStr = Field(description="The name of the node.")
    category: OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2 = Field(
        description="The category of the node."
    )
    parent_id: StrictStr = Field(description="The id of the parent node.")
    node_id: Optional[StrictStr] = None
    tenant_id: StrictStr = Field(description="The id of the tenant.")
    __properties: ClassVar[List[str]] = [
        "name",
        "category",
        "parent_id",
        "node_id",
        "tenant_id",
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
        """Create an instance of ValidateHierarchyNodeFieldsRequest from a JSON string"""
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
        # set to None if node_id (nullable) is None
        # and model_fields_set contains the field
        if self.node_id is None and "node_id" in self.model_fields_set:
            _dict["node_id"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidateHierarchyNodeFieldsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "category": obj.get("category"),
                "parent_id": obj.get("parent_id"),
                "node_id": obj.get("node_id"),
                "tenant_id": obj.get("tenant_id"),
            }
        )
        return _obj
