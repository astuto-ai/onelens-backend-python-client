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
from typing import Any, ClassVar, Dict, List
from onelens_backend_client.models.tenant_policy_exclusions import TenantPolicyExclusions
from typing import Optional, Set
from typing_extensions import Self

class AddTenantPolicyExclusionsRequest(BaseModel):
    """
    AddTenantPolicyExclusionsRequest
    """ # noqa: E501
    exclusions: TenantPolicyExclusions = Field(description="The exclusions to add.")
    tenant_id: StrictStr = Field(description="The id of the tenant.")
    policy_id: StrictStr = Field(description="The id of the tenant policy.")
    __properties: ClassVar[List[str]] = ["exclusions", "tenant_id", "policy_id"]

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
        """Create an instance of AddTenantPolicyExclusionsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of exclusions
        if self.exclusions:
            _dict['exclusions'] = self.exclusions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddTenantPolicyExclusionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "exclusions": TenantPolicyExclusions.from_dict(obj["exclusions"]) if obj.get("exclusions") is not None else None,
            "tenant_id": obj.get("tenant_id"),
            "policy_id": obj.get("policy_id")
        })
        return _obj


