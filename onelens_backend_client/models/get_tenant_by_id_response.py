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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from onelens_backend_client.models.tenant_state import TenantState
from typing import Optional, Set
from typing_extensions import Self

class GetTenantByIDResponse(BaseModel):
    """
    GetTenantByIDResponse
    """ # noqa: E501
    name: Annotated[str, Field(strict=True, max_length=200)] = Field(description="Name of the tenant")
    domains: List[StrictStr] = Field(description="List of domains associated with the tenant")
    timezone: StrictStr = Field(description="Timezone of the tenant")
    id: StrictStr = Field(description="Unique identifier for the tenant")
    tenant_state: TenantState = Field(description="State of the tenant")
    database_connection_string: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["name", "domains", "timezone", "id", "tenant_state", "database_connection_string"]

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
        """Create an instance of GetTenantByIDResponse from a JSON string"""
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
        # set to None if database_connection_string (nullable) is None
        # and model_fields_set contains the field
        if self.database_connection_string is None and "database_connection_string" in self.model_fields_set:
            _dict['database_connection_string'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTenantByIDResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "domains": obj.get("domains"),
            "timezone": obj.get("timezone"),
            "id": obj.get("id"),
            "tenant_state": obj.get("tenant_state"),
            "database_connection_string": obj.get("database_connection_string")
        })
        return _obj


