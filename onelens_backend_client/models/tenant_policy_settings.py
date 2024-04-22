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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.tenant_policy_exclusions import TenantPolicyExclusions
from onelens_backend_client.models.tenant_policy_state import TenantPolicyState
from typing import Optional, Set
from typing_extensions import Self

class TenantPolicySettings(BaseModel):
    """
    TenantPolicySettings
    """ # noqa: E501
    id: StrictStr = Field(description="The unique identifier of the tenant policy setting.")
    policy_id: StrictStr = Field(description="The id of the tenant policy.")
    config_overrides: Optional[Dict[str, Any]] = None
    state: TenantPolicyState = Field(description="The state of the policy template.")
    version: StrictInt = Field(description="The version of the tenant policy.")
    exclusions: TenantPolicyExclusions = Field(description="The exclusions for the tenant policy.")
    __properties: ClassVar[List[str]] = ["id", "policy_id", "config_overrides", "state", "version", "exclusions"]

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
        """Create an instance of TenantPolicySettings from a JSON string"""
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
        # set to None if config_overrides (nullable) is None
        # and model_fields_set contains the field
        if self.config_overrides is None and "config_overrides" in self.model_fields_set:
            _dict['config_overrides'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantPolicySettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "policy_id": obj.get("policy_id"),
            "config_overrides": obj.get("config_overrides"),
            "state": obj.get("state"),
            "version": obj.get("version"),
            "exclusions": TenantPolicyExclusions.from_dict(obj["exclusions"]) if obj.get("exclusions") is not None else None
        })
        return _obj


