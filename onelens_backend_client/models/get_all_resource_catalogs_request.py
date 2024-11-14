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
from onelens_backend_client.models.onelens_domain_utilities_repositories_dynamic_filters_filter_criteria import (
    OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria,
)
from onelens_backend_client.models.pagination_params import PaginationParams
from typing import Set
from typing_extensions import Self


class GetAllResourceCatalogsRequest(BaseModel):
    """
    Get All Resource Catalogs Request with navira
    """  # noqa: E501

    pagination: Optional[PaginationParams] = Field(
        default=None, description="Pagination parameters for the request."
    )
    tenant_id: StrictStr = Field(description="The id of the tenant.")
    user_id: Optional[StrictStr] = None
    filters: List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria] = (
        Field(description="Filters to be applied")
    )
    navira_log_id: Optional[StrictStr] = None
    request: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "pagination",
        "tenant_id",
        "user_id",
        "filters",
        "navira_log_id",
        "request",
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
        """Create an instance of GetAllResourceCatalogsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict["pagination"] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict["filters"] = _items
        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict["user_id"] = None

        # set to None if navira_log_id (nullable) is None
        # and model_fields_set contains the field
        if self.navira_log_id is None and "navira_log_id" in self.model_fields_set:
            _dict["navira_log_id"] = None

        # set to None if request (nullable) is None
        # and model_fields_set contains the field
        if self.request is None and "request" in self.model_fields_set:
            _dict["request"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetAllResourceCatalogsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "pagination": PaginationParams.from_dict(obj["pagination"])
                if obj.get("pagination") is not None
                else None,
                "tenant_id": obj.get("tenant_id"),
                "user_id": obj.get("user_id"),
                "filters": [
                    OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.from_dict(
                        _item
                    )
                    for _item in obj["filters"]
                ]
                if obj.get("filters") is not None
                else None,
                "navira_log_id": obj.get("navira_log_id"),
                "request": obj.get("request"),
            }
        )
        return _obj
