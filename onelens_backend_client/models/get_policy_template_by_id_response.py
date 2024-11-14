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
from onelens_backend_client.models.action_type_filters_services_inner import (
    ActionTypeFiltersServicesInner,
)
from onelens_backend_client.models.policy_category import PolicyCategory
from onelens_backend_client.models.policy_execution_type import PolicyExecutionType
from onelens_backend_client.models.policy_template_details_output import (
    PolicyTemplateDetailsOutput,
)
from onelens_backend_client.models.policy_template_recommendation_details_output import (
    PolicyTemplateRecommendationDetailsOutput,
)
from onelens_backend_client.models.policy_template_state import PolicyTemplateState
from onelens_backend_client.models.provider import Provider
from typing import Set
from typing_extensions import Self


class GetPolicyTemplateByIDResponse(BaseModel):
    """
    GetPolicyTemplateByIDResponse
    """  # noqa: E501

    parent_ptp_id: StrictStr = Field(
        description="The id of the parent policy template pack."
    )
    title: StrictStr = Field(description="The title of the policy template.")
    alias: StrictStr = Field(description="The alias of the policy template.")
    description: Optional[StrictStr] = Field(
        default=None, description="The description of the policy template."
    )
    services: List[ActionTypeFiltersServicesInner] = Field(
        description="The list of services associated the policy template."
    )
    execution_type: PolicyExecutionType = Field(
        description="The execution type of the policy template."
    )
    details: PolicyTemplateDetailsOutput = Field(
        description="The details of the policy template."
    )
    description2: Optional[StrictStr] = Field(
        default=None, description="The description2 of the policy template."
    )
    resource_type: StrictStr = Field(
        description="The resource type of the policy template."
    )
    recommendation_details: PolicyTemplateRecommendationDetailsOutput = Field(
        description="The recommendation details for the policy template."
    )
    activated_at: Optional[datetime] = None
    category: PolicyCategory = Field(description="The category of the policy template.")
    provider: Provider = Field(description="The cloud provider of the policy template.")
    id: StrictStr = Field(description="The unique identifier of the policy template.")
    state: PolicyTemplateState = Field(description="The state of the policy template.")
    requirements: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "parent_ptp_id",
        "title",
        "alias",
        "description",
        "services",
        "execution_type",
        "details",
        "description2",
        "resource_type",
        "recommendation_details",
        "activated_at",
        "category",
        "provider",
        "id",
        "state",
        "requirements",
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
        """Create an instance of GetPolicyTemplateByIDResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in services (list)
        _items = []
        if self.services:
            for _item in self.services:
                if _item:
                    _items.append(_item.to_dict())
            _dict["services"] = _items
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict["details"] = self.details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recommendation_details
        if self.recommendation_details:
            _dict["recommendation_details"] = self.recommendation_details.to_dict()
        # set to None if activated_at (nullable) is None
        # and model_fields_set contains the field
        if self.activated_at is None and "activated_at" in self.model_fields_set:
            _dict["activated_at"] = None

        # set to None if requirements (nullable) is None
        # and model_fields_set contains the field
        if self.requirements is None and "requirements" in self.model_fields_set:
            _dict["requirements"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetPolicyTemplateByIDResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "parent_ptp_id": obj.get("parent_ptp_id"),
                "title": obj.get("title"),
                "alias": obj.get("alias"),
                "description": obj.get("description"),
                "services": [
                    ActionTypeFiltersServicesInner.from_dict(_item)
                    for _item in obj["services"]
                ]
                if obj.get("services") is not None
                else None,
                "execution_type": obj.get("execution_type"),
                "details": PolicyTemplateDetailsOutput.from_dict(obj["details"])
                if obj.get("details") is not None
                else None,
                "description2": obj.get("description2"),
                "resource_type": obj.get("resource_type"),
                "recommendation_details": PolicyTemplateRecommendationDetailsOutput.from_dict(
                    obj["recommendation_details"]
                )
                if obj.get("recommendation_details") is not None
                else None,
                "activated_at": obj.get("activated_at"),
                "category": obj.get("category"),
                "provider": obj.get("provider"),
                "id": obj.get("id"),
                "state": obj.get("state"),
                "requirements": obj.get("requirements"),
            }
        )
        return _obj
