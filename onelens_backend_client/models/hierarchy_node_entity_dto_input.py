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

from datetime import datetime
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from onelens_backend_client.models.hierarchy_node_attribution_details import (
    HierarchyNodeAttributionDetails,
)
from onelens_backend_client.models.hierarchy_node_resource_filters import (
    HierarchyNodeResourceFilters,
)
from onelens_backend_client.models.hierarchy_node_state import HierarchyNodeState
from typing import Set
from typing_extensions import Self


class HierarchyNodeEntityDTOInput(BaseModel):
    """
    Hierarchy Node Entity in the JSON data
    """  # noqa: E501

    id: Optional[StrictStr] = None
    name: Annotated[str, Field(strict=True, max_length=30)]
    category: Annotated[str, Field(strict=True, max_length=20)]
    resource_filters: Optional[List[HierarchyNodeResourceFilters]] = None
    resource_filter_expression: Optional[
        Annotated[str, Field(strict=True, max_length=200)]
    ] = None
    is_shared: Optional[StrictBool] = Field(
        default=False, description="is this node a shared node or not."
    )
    attribution_details: Optional[HierarchyNodeAttributionDetails] = None
    state: HierarchyNodeState = Field(description="The state of the hierarchy node.")
    sql_filter: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[StrictStr] = None
    updated_by: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "category",
        "resource_filters",
        "resource_filter_expression",
        "is_shared",
        "attribution_details",
        "state",
        "sql_filter",
        "description",
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
    ]

    @field_validator("category")
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(
            [
                "ROOT",
                "BUSINESS_UNIT",
                "DEPARTMENT",
                "DIVISION",
                "PRODUCT",
                "TEAM",
                "APPLICATION",
                "CUSTOM",
                "SERVICE",
                "ENVIRONMENT",
                "RESIDUAL",
                "CLOUD_ID",
                "REGION",
                "PROJECT",
                "OTHER",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('ROOT', 'BUSINESS_UNIT', 'DEPARTMENT', 'DIVISION', 'PRODUCT', 'TEAM', 'APPLICATION', 'CUSTOM', 'SERVICE', 'ENVIRONMENT', 'RESIDUAL', 'CLOUD_ID', 'REGION', 'PROJECT', 'OTHER')"
            )
        return value

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
        """Create an instance of HierarchyNodeEntityDTOInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in resource_filters (list)
        _items = []
        if self.resource_filters:
            for _item in self.resource_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict["resource_filters"] = _items
        # override the default output from pydantic by calling `to_dict()` of attribution_details
        if self.attribution_details:
            _dict["attribution_details"] = self.attribution_details.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict["id"] = None

        # set to None if resource_filter_expression (nullable) is None
        # and model_fields_set contains the field
        if (
            self.resource_filter_expression is None
            and "resource_filter_expression" in self.model_fields_set
        ):
            _dict["resource_filter_expression"] = None

        # set to None if attribution_details (nullable) is None
        # and model_fields_set contains the field
        if (
            self.attribution_details is None
            and "attribution_details" in self.model_fields_set
        ):
            _dict["attribution_details"] = None

        # set to None if sql_filter (nullable) is None
        # and model_fields_set contains the field
        if self.sql_filter is None and "sql_filter" in self.model_fields_set:
            _dict["sql_filter"] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict["description"] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict["created_at"] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict["updated_at"] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict["created_by"] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict["updated_by"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HierarchyNodeEntityDTOInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "category": obj.get("category"),
                "resource_filters": [
                    HierarchyNodeResourceFilters.from_dict(_item)
                    for _item in obj["resource_filters"]
                ]
                if obj.get("resource_filters") is not None
                else None,
                "resource_filter_expression": obj.get("resource_filter_expression"),
                "is_shared": obj.get("is_shared")
                if obj.get("is_shared") is not None
                else False,
                "attribution_details": HierarchyNodeAttributionDetails.from_dict(
                    obj["attribution_details"]
                )
                if obj.get("attribution_details") is not None
                else None,
                "state": obj.get("state"),
                "sql_filter": obj.get("sql_filter"),
                "description": obj.get("description"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "created_by": obj.get("created_by"),
                "updated_by": obj.get("updated_by"),
            }
        )
        return _obj
