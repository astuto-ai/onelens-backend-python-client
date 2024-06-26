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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from onelens_backend_client.models.get_single_policy_ticket_by_entity_id_response import GetSinglePolicyTicketByEntityIdResponse
from onelens_backend_client.models.pagination_fields import PaginationFields
from typing import Optional, Set
from typing_extensions import Self

class GetPolicyTicketsByEntityIdResponse(BaseModel):
    """
    GetPolicyTicketsByEntityIdResponse
    """ # noqa: E501
    pagination: PaginationFields = Field(description="Pagination fields.")
    entity_tickets: List[GetSinglePolicyTicketByEntityIdResponse] = Field(description="List of tickets")
    __properties: ClassVar[List[str]] = ["pagination", "entity_tickets"]

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
        """Create an instance of GetPolicyTicketsByEntityIdResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entity_tickets (list)
        _items = []
        if self.entity_tickets:
            for _item in self.entity_tickets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entity_tickets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetPolicyTicketsByEntityIdResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pagination": PaginationFields.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None,
            "entity_tickets": [GetSinglePolicyTicketByEntityIdResponse.from_dict(_item) for _item in obj["entity_tickets"]] if obj.get("entity_tickets") is not None else None
        })
        return _obj


