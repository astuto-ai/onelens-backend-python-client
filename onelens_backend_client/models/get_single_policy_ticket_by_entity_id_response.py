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
from onelens_backend_client.models.policy_ticket_status import PolicyTicketStatus
from onelens_backend_client.models.ticket_state import TicketState
from typing import Set
from typing_extensions import Self


class GetSinglePolicyTicketByEntityIdResponse(BaseModel):
    """
    GetSinglePolicyTicketByEntityIdResponse
    """  # noqa: E501

    ticket_id: StrictStr = Field(description="The unique identifier of the ticket")
    ticket_alias: StrictStr = Field(description="The unique identifier of the ticket")
    status: PolicyTicketStatus = Field(description="Status of the ticket")
    state: TicketState = Field(description="State of the ticket")
    violation_attributes: Dict[str, Any] = Field(
        description="Attributes of the violation"
    )
    entity_id: StrictStr = Field(
        description="The id of the resource experiencing policy violation."
    )
    entity_name: StrictStr = Field(description="Name of the resource")
    region: StrictStr = Field(description="Region of the resource")
    service: StrictStr = Field(description="Service of the resource")
    service_display_name: StrictStr = Field(description="Service name in UI")
    account_id: StrictStr = Field(description="Account Id managing the resource")
    recommendation_unit_title: Optional[StrictStr] = None
    policy_id: StrictStr = Field(description="The unique identifier of the policy")
    policy_title: StrictStr = Field(description="Policy name")
    policy_labels: Optional[List[StrictStr]] = Field(
        default=None, description="List of policy labels"
    )
    policy_display_alias: Optional[StrictStr] = None
    policy_violated_on: datetime = Field(description="Datetime of the policy violation")
    potential_savings: Union[StrictFloat, StrictInt] = Field(
        description="Potential savings possible for the current policy violation"
    )
    resource_id: Optional[StrictStr] = None
    account_name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "ticket_id",
        "ticket_alias",
        "status",
        "state",
        "violation_attributes",
        "entity_id",
        "entity_name",
        "region",
        "service",
        "service_display_name",
        "account_id",
        "recommendation_unit_title",
        "policy_id",
        "policy_title",
        "policy_labels",
        "policy_display_alias",
        "policy_violated_on",
        "potential_savings",
        "resource_id",
        "account_name",
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
        """Create an instance of GetSinglePolicyTicketByEntityIdResponse from a JSON string"""
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
        # set to None if recommendation_unit_title (nullable) is None
        # and model_fields_set contains the field
        if (
            self.recommendation_unit_title is None
            and "recommendation_unit_title" in self.model_fields_set
        ):
            _dict["recommendation_unit_title"] = None

        # set to None if policy_display_alias (nullable) is None
        # and model_fields_set contains the field
        if (
            self.policy_display_alias is None
            and "policy_display_alias" in self.model_fields_set
        ):
            _dict["policy_display_alias"] = None

        # set to None if resource_id (nullable) is None
        # and model_fields_set contains the field
        if self.resource_id is None and "resource_id" in self.model_fields_set:
            _dict["resource_id"] = None

        # set to None if account_name (nullable) is None
        # and model_fields_set contains the field
        if self.account_name is None and "account_name" in self.model_fields_set:
            _dict["account_name"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetSinglePolicyTicketByEntityIdResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "ticket_id": obj.get("ticket_id"),
                "ticket_alias": obj.get("ticket_alias"),
                "status": obj.get("status"),
                "state": obj.get("state"),
                "violation_attributes": obj.get("violation_attributes"),
                "entity_id": obj.get("entity_id"),
                "entity_name": obj.get("entity_name"),
                "region": obj.get("region"),
                "service": obj.get("service"),
                "service_display_name": obj.get("service_display_name"),
                "account_id": obj.get("account_id"),
                "recommendation_unit_title": obj.get("recommendation_unit_title"),
                "policy_id": obj.get("policy_id"),
                "policy_title": obj.get("policy_title"),
                "policy_labels": obj.get("policy_labels"),
                "policy_display_alias": obj.get("policy_display_alias"),
                "policy_violated_on": obj.get("policy_violated_on"),
                "potential_savings": obj.get("potential_savings"),
                "resource_id": obj.get("resource_id"),
                "account_name": obj.get("account_name"),
            }
        )
        return _obj
