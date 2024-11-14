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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from onelens_backend_client.models.details1 import Details1
from onelens_backend_client.models.status import Status
from onelens_backend_client.models.ticket_assignment import TicketAssignment
from onelens_backend_client.models.ticket_category import TicketCategory
from onelens_backend_client.models.ticket_state import TicketState
from typing import Set
from typing_extensions import Self


class TenantTicketWithTicketAlias(BaseModel):
    """
    TenantTicketWithTicketAlias
    """  # noqa: E501

    created_at: datetime = Field(description="Datetime of ticket creation")
    updated_at: datetime = Field(description="Datetime of ticket updation")
    monitor_id: Optional[StrictStr] = None
    ticket_category: TicketCategory = Field(description="Category of the ticket")
    state: TicketState = Field(description="State of the ticket")
    entity_id: StrictStr = Field(
        description="The id of the resource experiencing policy violation."
    )
    entity_type: StrictStr = Field(
        description="The type of the resource experiencing policy violation."
    )
    entity_attributes: Optional[Dict[str, Any]] = None
    monthly_unblended_cost: Optional[Union[StrictFloat, StrictInt]] = None
    assignment: TicketAssignment = Field(description="Assignment state of the ticket")
    assigned_to: Optional[StrictStr] = None
    last_run_id: StrictStr = Field(
        description="Id of the last policy violation/anomaly run"
    )
    last_run_at: datetime = Field(
        description="Datetime of the last policy violation/anomaly run"
    )
    first_run_at: datetime = Field(
        description="Datetime of the first policy violation/anomaly run"
    )
    id: StrictStr = Field(description="The unique identifier of the ticket")
    status: Status
    details: Details1
    ticket_alias: Optional[StrictStr] = None
    trigger_id: StrictStr = Field(
        description="The unique identifier of the trigger that created the ticket"
    )
    __properties: ClassVar[List[str]] = [
        "created_at",
        "updated_at",
        "monitor_id",
        "ticket_category",
        "state",
        "entity_id",
        "entity_type",
        "entity_attributes",
        "monthly_unblended_cost",
        "assignment",
        "assigned_to",
        "last_run_id",
        "last_run_at",
        "first_run_at",
        "id",
        "status",
        "details",
        "ticket_alias",
        "trigger_id",
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
        """Create an instance of TenantTicketWithTicketAlias from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict["details"] = self.details.to_dict()
        # set to None if monitor_id (nullable) is None
        # and model_fields_set contains the field
        if self.monitor_id is None and "monitor_id" in self.model_fields_set:
            _dict["monitor_id"] = None

        # set to None if entity_attributes (nullable) is None
        # and model_fields_set contains the field
        if (
            self.entity_attributes is None
            and "entity_attributes" in self.model_fields_set
        ):
            _dict["entity_attributes"] = None

        # set to None if monthly_unblended_cost (nullable) is None
        # and model_fields_set contains the field
        if (
            self.monthly_unblended_cost is None
            and "monthly_unblended_cost" in self.model_fields_set
        ):
            _dict["monthly_unblended_cost"] = None

        # set to None if assigned_to (nullable) is None
        # and model_fields_set contains the field
        if self.assigned_to is None and "assigned_to" in self.model_fields_set:
            _dict["assigned_to"] = None

        # set to None if ticket_alias (nullable) is None
        # and model_fields_set contains the field
        if self.ticket_alias is None and "ticket_alias" in self.model_fields_set:
            _dict["ticket_alias"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantTicketWithTicketAlias from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "monitor_id": obj.get("monitor_id"),
                "ticket_category": obj.get("ticket_category"),
                "state": obj.get("state"),
                "entity_id": obj.get("entity_id"),
                "entity_type": obj.get("entity_type"),
                "entity_attributes": obj.get("entity_attributes"),
                "monthly_unblended_cost": obj.get("monthly_unblended_cost"),
                "assignment": obj.get("assignment"),
                "assigned_to": obj.get("assigned_to"),
                "last_run_id": obj.get("last_run_id"),
                "last_run_at": obj.get("last_run_at"),
                "first_run_at": obj.get("first_run_at"),
                "id": obj.get("id"),
                "status": Status.from_dict(obj["status"])
                if obj.get("status") is not None
                else None,
                "details": Details1.from_dict(obj["details"])
                if obj.get("details") is not None
                else None,
                "ticket_alias": obj.get("ticket_alias"),
                "trigger_id": obj.get("trigger_id"),
            }
        )
        return _obj
