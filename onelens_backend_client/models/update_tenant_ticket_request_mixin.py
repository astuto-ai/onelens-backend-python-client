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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from onelens_backend_client.models.details2 import Details2
from onelens_backend_client.models.monthly_unblended_cost1 import MonthlyUnblendedCost1
from onelens_backend_client.models.status1 import Status1
from typing import Optional, Set
from typing_extensions import Self

class UpdateTenantTicketRequestMixin(BaseModel):
    """
    UpdateTenantTicketRequestMixin
    """ # noqa: E501
    ticket_id: StrictStr = Field(description="The unique identifier of the ticket")
    status: Optional[Status1] = None
    details: Optional[Details2] = None
    entity_attributes: Optional[Dict[str, Any]] = None
    monthly_unblended_cost: Optional[MonthlyUnblendedCost1] = None
    cost_impact: Optional[Union[StrictFloat, StrictInt]] = None
    last_run_id: Optional[StrictStr] = None
    last_run_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["ticket_id", "status", "details", "entity_attributes", "monthly_unblended_cost", "cost_impact", "last_run_id", "last_run_at"]

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
        """Create an instance of UpdateTenantTicketRequestMixin from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict['details'] = self.details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of monthly_unblended_cost
        if self.monthly_unblended_cost:
            _dict['monthly_unblended_cost'] = self.monthly_unblended_cost.to_dict()
        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        # set to None if entity_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.entity_attributes is None and "entity_attributes" in self.model_fields_set:
            _dict['entity_attributes'] = None

        # set to None if monthly_unblended_cost (nullable) is None
        # and model_fields_set contains the field
        if self.monthly_unblended_cost is None and "monthly_unblended_cost" in self.model_fields_set:
            _dict['monthly_unblended_cost'] = None

        # set to None if cost_impact (nullable) is None
        # and model_fields_set contains the field
        if self.cost_impact is None and "cost_impact" in self.model_fields_set:
            _dict['cost_impact'] = None

        # set to None if last_run_id (nullable) is None
        # and model_fields_set contains the field
        if self.last_run_id is None and "last_run_id" in self.model_fields_set:
            _dict['last_run_id'] = None

        # set to None if last_run_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_run_at is None and "last_run_at" in self.model_fields_set:
            _dict['last_run_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateTenantTicketRequestMixin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ticket_id": obj.get("ticket_id"),
            "status": Status1.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "details": Details2.from_dict(obj["details"]) if obj.get("details") is not None else None,
            "entity_attributes": obj.get("entity_attributes"),
            "monthly_unblended_cost": MonthlyUnblendedCost1.from_dict(obj["monthly_unblended_cost"]) if obj.get("monthly_unblended_cost") is not None else None,
            "cost_impact": obj.get("cost_impact"),
            "last_run_id": obj.get("last_run_id"),
            "last_run_at": obj.get("last_run_at")
        })
        return _obj


