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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from onelens_backend_client.models.anomaly_rca_ids_mixin import AnomalyRcaIdsMixin
from onelens_backend_client.models.anomaly_source_type import AnomalySourceType
from onelens_backend_client.models.deviation import Deviation
from typing import Optional, Set
from typing_extensions import Self

class TenantAnomalyTicketDetailsMixin(BaseModel):
    """
    TenantAnomalyTicketDetailsMixin
    """ # noqa: E501
    anomalies: List[AnomalyRcaIdsMixin] = Field(description="List of anomaly ids and rca ids.")
    total_cost_impact: Union[StrictFloat, StrictInt] = Field(description="Total cost incurred due to the anomaly.")
    rca_hash: StrictStr = Field(description="The hash of the RCA associated with the anomaly.")
    deviation: Deviation
    duration: Union[StrictFloat, StrictInt] = Field(description="The duration of the anomaly.")
    duration_unit: StrictStr = Field(description="The duration unit of the anomaly.")
    source_type: AnomalySourceType = Field(description="The source type of the anomaly.")
    usage_type: StrictStr = Field(description="The usage type of the anomaly.")
    operation_type: StrictStr = Field(description="The operation type of the anomaly.")
    is_continuous: StrictBool = Field(description="Is the anomaly continuous.")
    __properties: ClassVar[List[str]] = ["anomalies", "total_cost_impact", "rca_hash", "deviation", "duration", "duration_unit", "source_type", "usage_type", "operation_type", "is_continuous"]

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
        """Create an instance of TenantAnomalyTicketDetailsMixin from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in anomalies (list)
        _items = []
        if self.anomalies:
            for _item in self.anomalies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['anomalies'] = _items
        # override the default output from pydantic by calling `to_dict()` of deviation
        if self.deviation:
            _dict['deviation'] = self.deviation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantAnomalyTicketDetailsMixin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "anomalies": [AnomalyRcaIdsMixin.from_dict(_item) for _item in obj["anomalies"]] if obj.get("anomalies") is not None else None,
            "total_cost_impact": obj.get("total_cost_impact"),
            "rca_hash": obj.get("rca_hash"),
            "deviation": Deviation.from_dict(obj["deviation"]) if obj.get("deviation") is not None else None,
            "duration": obj.get("duration"),
            "duration_unit": obj.get("duration_unit"),
            "source_type": obj.get("source_type"),
            "usage_type": obj.get("usage_type"),
            "operation_type": obj.get("operation_type"),
            "is_continuous": obj.get("is_continuous")
        })
        return _obj


