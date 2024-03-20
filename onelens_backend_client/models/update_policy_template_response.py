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
from onelens_backend_client.models.create_policy_template_request_services_inner import CreatePolicyTemplateRequestServicesInner
from onelens_backend_client.models.policy_category import PolicyCategory
from onelens_backend_client.models.policy_execution_type import PolicyExecutionType
from onelens_backend_client.models.policy_template_details import PolicyTemplateDetails
from onelens_backend_client.models.policy_template_state import PolicyTemplateState
from onelens_backend_client.models.provider import Provider
from typing import Optional, Set
from typing_extensions import Self

class UpdatePolicyTemplateResponse(BaseModel):
    """
    UpdatePolicyTemplateResponse
    """ # noqa: E501
    parent_ptp_id: StrictStr = Field(description="The id of the parent policy template pack.")
    title: StrictStr = Field(description="The title of the policy template.")
    alias: StrictStr = Field(description="The alias of the policy template.")
    description: Optional[StrictStr] = Field(default=None, description="The description of the policy template.")
    services: List[CreatePolicyTemplateRequestServicesInner] = Field(description="The list of services associated the policy template.")
    execution_type: PolicyExecutionType = Field(description="The execution type of the policy template.")
    details: PolicyTemplateDetails = Field(description="The details of the policy template.")
    id: StrictStr = Field(description="The unique identifier of the policy template.")
    state: PolicyTemplateState = Field(description="The state of the policy template.")
    category: PolicyCategory = Field(description="The category of the policy template.")
    provider: Provider = Field(description="The cloud provider of the policy template.")
    __properties: ClassVar[List[str]] = ["parent_ptp_id", "title", "alias", "description", "services", "execution_type", "details", "id", "state", "category", "provider"]

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
        """Create an instance of UpdatePolicyTemplateResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in services (list)
        _items = []
        if self.services:
            for _item in self.services:
                if _item:
                    _items.append(_item.to_dict())
            _dict['services'] = _items
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict['details'] = self.details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdatePolicyTemplateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parent_ptp_id": obj.get("parent_ptp_id"),
            "title": obj.get("title"),
            "alias": obj.get("alias"),
            "description": obj.get("description"),
            "services": [CreatePolicyTemplateRequestServicesInner.from_dict(_item) for _item in obj["services"]] if obj.get("services") is not None else None,
            "execution_type": obj.get("execution_type"),
            "details": PolicyTemplateDetails.from_dict(obj["details"]) if obj.get("details") is not None else None,
            "id": obj.get("id"),
            "state": obj.get("state"),
            "category": obj.get("category"),
            "provider": obj.get("provider")
        })
        return _obj


