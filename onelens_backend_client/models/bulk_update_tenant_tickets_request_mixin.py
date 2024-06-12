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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.policy_ticket_status import PolicyTicketStatus
from typing import Optional, Set
from typing_extensions import Self

class BulkUpdateTenantTicketsRequestMixin(BaseModel):
    """
    BulkUpdateTenantTicketsRequestMixin
    """ # noqa: E501
    ticket_ids: Optional[List[StrictStr]] = Field(default=None, description="List of ticket ids")
    status: Optional[PolicyTicketStatus] = None
    assignment: Optional[StrictStr] = None
    assigned_to: Optional[StrictStr] = None
    comment: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["ticket_ids", "status", "assignment", "assigned_to", "comment"]

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
        """Create an instance of BulkUpdateTenantTicketsRequestMixin from a JSON string"""
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
        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if assigned_to (nullable) is None
        # and model_fields_set contains the field
        if self.assigned_to is None and "assigned_to" in self.model_fields_set:
            _dict['assigned_to'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BulkUpdateTenantTicketsRequestMixin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ticket_ids": obj.get("ticket_ids"),
            "status": obj.get("status"),
            "assignment": obj.get("assignment"),
            "assigned_to": obj.get("assigned_to"),
            "comment": obj.get("comment")
        })
        return _obj


