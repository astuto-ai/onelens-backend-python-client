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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RecommendationTicket(BaseModel):
    """
    RecommendationTicket
    """ # noqa: E501
    recommendation_unit_id: StrictStr = Field(description="Recommendation Unit ID")
    action_type_id: StrictInt = Field(description="Action Type ID")
    priority: StrictInt = Field(description="Priority")
    instance_type: Optional[StrictStr] = None
    instance_family: Optional[StrictStr] = None
    price_per_unit: StrictStr = Field(description="Price Per Unit")
    currency: StrictStr = Field(description="Currency")
    unit: StrictStr = Field(description="Unit")
    new_cost: StrictStr = Field(description="New Cost")
    current_cost: StrictStr = Field(description="Current Cost")
    potential_saving: StrictStr = Field(description="Potential Saving")
    description: StrictStr = Field(description="Description")
    begin_range: StrictStr = Field(description="Begin Range")
    end_range: StrictStr = Field(description="End Range")
    attributes: Dict[str, Any] = Field(description="Attributes")
    ticket_id: StrictStr = Field(description="The unique identifier of the ticket")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the ticket")
    __properties: ClassVar[List[str]] = ["recommendation_unit_id", "action_type_id", "priority", "instance_type", "instance_family", "price_per_unit", "currency", "unit", "new_cost", "current_cost", "potential_saving", "description", "begin_range", "end_range", "attributes", "ticket_id", "id"]

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
        """Create an instance of RecommendationTicket from a JSON string"""
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
        # set to None if instance_type (nullable) is None
        # and model_fields_set contains the field
        if self.instance_type is None and "instance_type" in self.model_fields_set:
            _dict['instance_type'] = None

        # set to None if instance_family (nullable) is None
        # and model_fields_set contains the field
        if self.instance_family is None and "instance_family" in self.model_fields_set:
            _dict['instance_family'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecommendationTicket from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "recommendation_unit_id": obj.get("recommendation_unit_id"),
            "action_type_id": obj.get("action_type_id"),
            "priority": obj.get("priority"),
            "instance_type": obj.get("instance_type"),
            "instance_family": obj.get("instance_family"),
            "price_per_unit": obj.get("price_per_unit"),
            "currency": obj.get("currency"),
            "unit": obj.get("unit"),
            "new_cost": obj.get("new_cost"),
            "current_cost": obj.get("current_cost"),
            "potential_saving": obj.get("potential_saving"),
            "description": obj.get("description"),
            "begin_range": obj.get("begin_range"),
            "end_range": obj.get("end_range"),
            "attributes": obj.get("attributes"),
            "ticket_id": obj.get("ticket_id"),
            "id": obj.get("id")
        })
        return _obj

