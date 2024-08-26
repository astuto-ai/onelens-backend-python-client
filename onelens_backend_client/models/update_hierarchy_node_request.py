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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from onelens_backend_client.models.hierarchy_node_attribution_details import HierarchyNodeAttributionDetails
from onelens_backend_client.models.hierarchy_node_resource_filters import HierarchyNodeResourceFilters
from typing import Optional, Set
from typing_extensions import Self

class UpdateHierarchyNodeRequest(BaseModel):
    """
    update a branch node request
    """ # noqa: E501
    name: Optional[Annotated[str, Field(strict=True, max_length=30)]] = None
    parent_id: Optional[StrictStr] = None
    category: Optional[Annotated[str, Field(strict=True, max_length=20)]] = None
    resource_filters: Optional[List[HierarchyNodeResourceFilters]] = None
    resource_filter_expression: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    is_shared: Optional[StrictBool] = None
    attribution_details: Optional[HierarchyNodeAttributionDetails] = None
    node_id: StrictStr = Field(description="The id of the node.")
    tenant_id: StrictStr = Field(description="The id of the tenant.")
    __properties: ClassVar[List[str]] = ["name", "parent_id", "category", "resource_filters", "resource_filter_expression", "is_shared", "attribution_details", "node_id", "tenant_id"]

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ROOT', 'BUSINESS_UNIT', 'DEPARTMENT', 'DIVISION', 'PRODUCT', 'TEAM', 'APPLICATION', 'CUSTOM', 'SERVICE', 'ENVIRONMENT', 'RESIDUAL', 'CLOUD_ID', 'REGION']):
            raise ValueError("must be one of enum values ('ROOT', 'BUSINESS_UNIT', 'DEPARTMENT', 'DIVISION', 'PRODUCT', 'TEAM', 'APPLICATION', 'CUSTOM', 'SERVICE', 'ENVIRONMENT', 'RESIDUAL', 'CLOUD_ID', 'REGION')")
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
        """Create an instance of UpdateHierarchyNodeRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in resource_filters (list)
        _items = []
        if self.resource_filters:
            for _item in self.resource_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resource_filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of attribution_details
        if self.attribution_details:
            _dict['attribution_details'] = self.attribution_details.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_id is None and "parent_id" in self.model_fields_set:
            _dict['parent_id'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if resource_filters (nullable) is None
        # and model_fields_set contains the field
        if self.resource_filters is None and "resource_filters" in self.model_fields_set:
            _dict['resource_filters'] = None

        # set to None if resource_filter_expression (nullable) is None
        # and model_fields_set contains the field
        if self.resource_filter_expression is None and "resource_filter_expression" in self.model_fields_set:
            _dict['resource_filter_expression'] = None

        # set to None if is_shared (nullable) is None
        # and model_fields_set contains the field
        if self.is_shared is None and "is_shared" in self.model_fields_set:
            _dict['is_shared'] = None

        # set to None if attribution_details (nullable) is None
        # and model_fields_set contains the field
        if self.attribution_details is None and "attribution_details" in self.model_fields_set:
            _dict['attribution_details'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateHierarchyNodeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "parent_id": obj.get("parent_id"),
            "category": obj.get("category"),
            "resource_filters": [HierarchyNodeResourceFilters.from_dict(_item) for _item in obj["resource_filters"]] if obj.get("resource_filters") is not None else None,
            "resource_filter_expression": obj.get("resource_filter_expression"),
            "is_shared": obj.get("is_shared"),
            "attribution_details": HierarchyNodeAttributionDetails.from_dict(obj["attribution_details"]) if obj.get("attribution_details") is not None else None,
            "node_id": obj.get("node_id"),
            "tenant_id": obj.get("tenant_id")
        })
        return _obj


