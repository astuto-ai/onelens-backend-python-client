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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.onelens_domain_utilities_repositories_dynamic_filters_filter_criteria import OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria
from onelens_backend_client.models.pagination_params import PaginationParams
from onelens_backend_client.models.sort_criteria import SortCriteria
from typing import Optional, Set
from typing_extensions import Self

class GetTenantPoliciesWithSettingsRequest(BaseModel):
    """
    GetTenantPoliciesWithSettingsRequest
    """ # noqa: E501
    pagination: Optional[PaginationParams] = Field(default=None, description="Pagination parameters for the request.")
    filters: List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria] = Field(description="Filters to be applied")
    sort_criteria: Optional[SortCriteria] = None
    tenant_id: StrictStr = Field(description="The id of the tenant.")
    __properties: ClassVar[List[str]] = ["pagination", "filters", "sort_criteria", "tenant_id"]

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
        """Create an instance of GetTenantPoliciesWithSettingsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of sort_criteria
        if self.sort_criteria:
            _dict['sort_criteria'] = self.sort_criteria.to_dict()
        # set to None if sort_criteria (nullable) is None
        # and model_fields_set contains the field
        if self.sort_criteria is None and "sort_criteria" in self.model_fields_set:
            _dict['sort_criteria'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTenantPoliciesWithSettingsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pagination": PaginationParams.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None,
            "filters": [OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.from_dict(_item) for _item in obj["filters"]] if obj.get("filters") is not None else None,
            "sort_criteria": SortCriteria.from_dict(obj["sort_criteria"]) if obj.get("sort_criteria") is not None else None,
            "tenant_id": obj.get("tenant_id")
        })
        return _obj


