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
from onelens_backend_client.models.cur_data_aggregation_type import CURDataAggregationType
from onelens_backend_client.models.onelens_models_service_interfaces_tenant_data_cur_service_filter_criteria import OnelensModelsServiceInterfacesTenantDataCurServiceFilterCriteria
from onelens_backend_client.models.onelens_models_service_interfaces_tenant_data_cur_service_time_dimension import OnelensModelsServiceInterfacesTenantDataCurServiceTimeDimension
from typing import Optional, Set
from typing_extensions import Self

class CURDataMetricsQuery(BaseModel):
    """
    CURDataMetricsQuery
    """ # noqa: E501
    name: StrictStr
    dimension: Optional[StrictStr] = None
    measures: List[CURDataAggregationType]
    filters: List[OnelensModelsServiceInterfacesTenantDataCurServiceFilterCriteria]
    time_filter: OnelensModelsServiceInterfacesTenantDataCurServiceTimeDimension
    timezone: Optional[StrictStr] = 'Asia/Kolkata'
    __properties: ClassVar[List[str]] = ["name", "dimension", "measures", "filters", "time_filter", "timezone"]

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
        """Create an instance of CURDataMetricsQuery from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of time_filter
        if self.time_filter:
            _dict['time_filter'] = self.time_filter.to_dict()
        # set to None if dimension (nullable) is None
        # and model_fields_set contains the field
        if self.dimension is None and "dimension" in self.model_fields_set:
            _dict['dimension'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CURDataMetricsQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "dimension": obj.get("dimension"),
            "measures": obj.get("measures"),
            "filters": [OnelensModelsServiceInterfacesTenantDataCurServiceFilterCriteria.from_dict(_item) for _item in obj["filters"]] if obj.get("filters") is not None else None,
            "time_filter": OnelensModelsServiceInterfacesTenantDataCurServiceTimeDimension.from_dict(obj["time_filter"]) if obj.get("time_filter") is not None else None,
            "timezone": obj.get("timezone") if obj.get("timezone") is not None else 'Asia/Kolkata'
        })
        return _obj


