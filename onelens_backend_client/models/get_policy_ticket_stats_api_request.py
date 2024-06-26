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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.onelens_domain_utilities_repositories_dynamic_filters_filter_criteria import OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria
from onelens_backend_client.models.tenant_tickets_stats_metrics import TenantTicketsStatsMetrics
from onelens_backend_client.models.tenant_tickets_stats_metrics_group_by import TenantTicketsStatsMetricsGroupBy
from onelens_backend_client.models.tenant_tickets_stats_metrics_sub_group_by import TenantTicketsStatsMetricsSubGroupBy
from typing import Optional, Set
from typing_extensions import Self

class GetPolicyTicketStatsAPIRequest(BaseModel):
    """
    GetPolicyTicketStatsAPIRequest
    """ # noqa: E501
    metric: TenantTicketsStatsMetrics = Field(description="Metric to be fetched")
    filters: List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria] = Field(description="Filters to be applied")
    group: Optional[TenantTicketsStatsMetricsGroupBy] = None
    sub_group: Optional[TenantTicketsStatsMetricsSubGroupBy] = None
    limit_items: Optional[StrictBool] = None
    item_count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["metric", "filters", "group", "sub_group", "limit_items", "item_count"]

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
        """Create an instance of GetPolicyTicketStatsAPIRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        # set to None if group (nullable) is None
        # and model_fields_set contains the field
        if self.group is None and "group" in self.model_fields_set:
            _dict['group'] = None

        # set to None if sub_group (nullable) is None
        # and model_fields_set contains the field
        if self.sub_group is None and "sub_group" in self.model_fields_set:
            _dict['sub_group'] = None

        # set to None if limit_items (nullable) is None
        # and model_fields_set contains the field
        if self.limit_items is None and "limit_items" in self.model_fields_set:
            _dict['limit_items'] = None

        # set to None if item_count (nullable) is None
        # and model_fields_set contains the field
        if self.item_count is None and "item_count" in self.model_fields_set:
            _dict['item_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetPolicyTicketStatsAPIRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metric": obj.get("metric"),
            "filters": [OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.from_dict(_item) for _item in obj["filters"]] if obj.get("filters") is not None else None,
            "group": obj.get("group"),
            "sub_group": obj.get("sub_group"),
            "limit_items": obj.get("limit_items"),
            "item_count": obj.get("item_count")
        })
        return _obj


