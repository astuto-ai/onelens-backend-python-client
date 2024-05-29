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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.details1 import Details1
from onelens_backend_client.models.status import Status
from onelens_backend_client.models.ticket_assignment import TicketAssignment
from onelens_backend_client.models.ticket_category import TicketCategory
from onelens_backend_client.models.ticket_state import TicketState
from typing import Optional, Set
from typing_extensions import Self

class TenantTicket(BaseModel):
    """
    TenantTicket
    """ # noqa: E501
    created_at: datetime = Field(description="Datetime of ticket creation")
    updated_at: datetime = Field(description="Datetime of ticket updation")
    monitor_id: Optional[StrictStr] = None
    ticket_category: TicketCategory = Field(description="Category of the ticket")
    state: TicketState = Field(description="State of the ticket")
    entity_id: StrictStr = Field(description="The id of the resource experiencing policy violation.")
    entity_type: StrictStr = Field(description="The type of the resource experiencing policy violation.")
    assignment: TicketAssignment = Field(description="Assignment state of the ticket")
    assigned_to: Optional[StrictStr] = None
    last_run_id: StrictStr = Field(description="Id of the last policy violation/anomaly run")
    last_run_at: datetime = Field(description="Datetime of the last policy violation/anomaly run")
    first_run_at: datetime = Field(description="Datetime of the first policy violation/anomaly run")
    id: StrictStr = Field(description="The unique identifier of the ticket")
    status: Status
    details: Details1
    __properties: ClassVar[List[str]] = ["created_at", "updated_at", "monitor_id", "ticket_category", "state", "entity_id", "entity_type", "assignment", "assigned_to", "last_run_id", "last_run_at", "first_run_at", "id", "status", "details"]

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
        """Create an instance of TenantTicket from a JSON string"""
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
        # set to None if monitor_id (nullable) is None
        # and model_fields_set contains the field
        if self.monitor_id is None and "monitor_id" in self.model_fields_set:
            _dict['monitor_id'] = None

        # set to None if assigned_to (nullable) is None
        # and model_fields_set contains the field
        if self.assigned_to is None and "assigned_to" in self.model_fields_set:
            _dict['assigned_to'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantTicket from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "monitor_id": obj.get("monitor_id"),
            "ticket_category": obj.get("ticket_category"),
            "state": obj.get("state"),
            "entity_id": obj.get("entity_id"),
            "entity_type": obj.get("entity_type"),
            "assignment": obj.get("assignment"),
            "assigned_to": obj.get("assigned_to"),
            "last_run_id": obj.get("last_run_id"),
            "last_run_at": obj.get("last_run_at"),
            "first_run_at": obj.get("first_run_at"),
            "id": obj.get("id"),
            "status": Status.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "details": Details1.from_dict(obj["details"]) if obj.get("details") is not None else None
        })
        return _obj


