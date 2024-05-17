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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from onelens_backend_client.models.cost_saving import CostSaving
from typing import Optional, Set
from typing_extensions import Self

class RecommendationTicketAPIRequest(BaseModel):
    """
    RecommendationTicketAPIRequest
    """ # noqa: E501
    recommendation_unit_id: StrictStr = Field(description="Recommendation Unit ID")
    action_type_id: StrictStr = Field(description="Action Type ID")
    risk: StrictInt = Field(description="Risk")
    priority: StrictInt = Field(description="Priority")
    cost_saving: CostSaving
    ticket_id: StrictStr = Field(description="The unique identifier of the ticket")
    __properties: ClassVar[List[str]] = ["recommendation_unit_id", "action_type_id", "risk", "priority", "cost_saving", "ticket_id"]

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
        """Create an instance of RecommendationTicketAPIRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cost_saving
        if self.cost_saving:
            _dict['cost_saving'] = self.cost_saving.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecommendationTicketAPIRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "recommendation_unit_id": obj.get("recommendation_unit_id"),
            "action_type_id": obj.get("action_type_id"),
            "risk": obj.get("risk"),
            "priority": obj.get("priority"),
            "cost_saving": CostSaving.from_dict(obj["cost_saving"]) if obj.get("cost_saving") is not None else None,
            "ticket_id": obj.get("ticket_id")
        })
        return _obj


