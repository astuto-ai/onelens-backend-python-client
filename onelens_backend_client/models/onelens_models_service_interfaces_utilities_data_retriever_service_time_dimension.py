# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.time_dimension_output_compare_date_range_inner import TimeDimensionOutputCompareDateRangeInner
from typing import Optional, Set
from typing_extensions import Self

class OnelensModelsServiceInterfacesUtilitiesDataRetrieverServiceTimeDimension(BaseModel):
    """
    OnelensModelsServiceInterfacesUtilitiesDataRetrieverServiceTimeDimension
    """ # noqa: E501
    dimension: Optional[StrictStr] = None
    date_range: Optional[List[StrictStr]] = Field(default=None, alias="dateRange")
    compare_date_range: Optional[List[TimeDimensionOutputCompareDateRangeInner]] = Field(default=None, alias="compareDateRange")
    granularity: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["dimension", "dateRange", "compareDateRange", "granularity"]

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
        """Create an instance of OnelensModelsServiceInterfacesUtilitiesDataRetrieverServiceTimeDimension from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in compare_date_range (list)
        _items = []
        if self.compare_date_range:
            for _item in self.compare_date_range:
                if _item:
                    _items.append(_item.to_dict())
            _dict['compareDateRange'] = _items
        # set to None if dimension (nullable) is None
        # and model_fields_set contains the field
        if self.dimension is None and "dimension" in self.model_fields_set:
            _dict['dimension'] = None

        # set to None if granularity (nullable) is None
        # and model_fields_set contains the field
        if self.granularity is None and "granularity" in self.model_fields_set:
            _dict['granularity'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OnelensModelsServiceInterfacesUtilitiesDataRetrieverServiceTimeDimension from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimension": obj.get("dimension"),
            "dateRange": obj.get("dateRange"),
            "compareDateRange": [TimeDimensionOutputCompareDateRangeInner.from_dict(_item) for _item in obj["compareDateRange"]] if obj.get("compareDateRange") is not None else None,
            "granularity": obj.get("granularity")
        })
        return _obj


