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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.details2 import Details2
from onelens_backend_client.models.status1 import Status1
from onelens_backend_client.models.ticket_assignment import TicketAssignment
from typing import Optional, Set
from typing_extensions import Self

class UpdateTenantTicketRequest(BaseModel):
    """
    UpdateTenantTicketRequest
    """ # noqa: E501
    status: Optional[Status1] = None
    assignment: Optional[TicketAssignment] = None
    details: Optional[Details2] = None
    resource_attributes: Optional[Dict[str, Any]] = None
    ticket_id: StrictStr = Field(description="The unique identifier of the ticket")
    tenant_id: StrictStr = Field(description="The unique identifier of the tenant")
    __properties: ClassVar[List[str]] = ["status", "assignment", "details", "resource_attributes", "ticket_id", "tenant_id"]

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
        """Create an instance of UpdateTenantTicketRequest from a JSON string"""
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
        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if assignment (nullable) is None
        # and model_fields_set contains the field
        if self.assignment is None and "assignment" in self.model_fields_set:
            _dict['assignment'] = None

        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        # set to None if resource_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.resource_attributes is None and "resource_attributes" in self.model_fields_set:
            _dict['resource_attributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateTenantTicketRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": Status1.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "assignment": obj.get("assignment"),
            "details": Details2.from_dict(obj["details"]) if obj.get("details") is not None else None,
            "resource_attributes": obj.get("resource_attributes"),
            "ticket_id": obj.get("ticket_id"),
            "tenant_id": obj.get("tenant_id")
        })
        return _obj


