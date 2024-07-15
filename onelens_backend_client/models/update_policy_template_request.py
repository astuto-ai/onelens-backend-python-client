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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.create_policy_template_request_services_inner import CreatePolicyTemplateRequestServicesInner
from onelens_backend_client.models.policy_execution_type import PolicyExecutionType
from onelens_backend_client.models.policy_template_details_input import PolicyTemplateDetailsInput
from onelens_backend_client.models.policy_template_recommendation_details_input import PolicyTemplateRecommendationDetailsInput
from typing import Optional, Set
from typing_extensions import Self

class UpdatePolicyTemplateRequest(BaseModel):
    """
    UpdatePolicyTemplateRequest
    """ # noqa: E501
    force_update: Optional[StrictBool] = Field(default=False, description="Force update (TRUE/FALSE), default: FALSE")
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    services: Optional[List[CreatePolicyTemplateRequestServicesInner]] = None
    execution_type: Optional[PolicyExecutionType] = None
    details: Optional[PolicyTemplateDetailsInput] = None
    description2: Optional[StrictStr] = None
    resource_type: Optional[StrictStr] = None
    recommendation_details: Optional[PolicyTemplateRecommendationDetailsInput] = None
    id: StrictStr = Field(description="The unique identifier of the policy template.")
    __properties: ClassVar[List[str]] = ["force_update", "title", "description", "services", "execution_type", "details", "description2", "resource_type", "recommendation_details", "id"]

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
        """Create an instance of UpdatePolicyTemplateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recommendation_details
        if self.recommendation_details:
            _dict['recommendation_details'] = self.recommendation_details.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if services (nullable) is None
        # and model_fields_set contains the field
        if self.services is None and "services" in self.model_fields_set:
            _dict['services'] = None

        # set to None if execution_type (nullable) is None
        # and model_fields_set contains the field
        if self.execution_type is None and "execution_type" in self.model_fields_set:
            _dict['execution_type'] = None

        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        # set to None if description2 (nullable) is None
        # and model_fields_set contains the field
        if self.description2 is None and "description2" in self.model_fields_set:
            _dict['description2'] = None

        # set to None if resource_type (nullable) is None
        # and model_fields_set contains the field
        if self.resource_type is None and "resource_type" in self.model_fields_set:
            _dict['resource_type'] = None

        # set to None if recommendation_details (nullable) is None
        # and model_fields_set contains the field
        if self.recommendation_details is None and "recommendation_details" in self.model_fields_set:
            _dict['recommendation_details'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdatePolicyTemplateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "force_update": obj.get("force_update") if obj.get("force_update") is not None else False,
            "title": obj.get("title"),
            "description": obj.get("description"),
            "services": [CreatePolicyTemplateRequestServicesInner.from_dict(_item) for _item in obj["services"]] if obj.get("services") is not None else None,
            "execution_type": obj.get("execution_type"),
            "details": PolicyTemplateDetailsInput.from_dict(obj["details"]) if obj.get("details") is not None else None,
            "description2": obj.get("description2"),
            "resource_type": obj.get("resource_type"),
            "recommendation_details": PolicyTemplateRecommendationDetailsInput.from_dict(obj["recommendation_details"]) if obj.get("recommendation_details") is not None else None,
            "id": obj.get("id")
        })
        return _obj


