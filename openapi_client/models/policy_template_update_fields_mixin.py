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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.description import Description
from openapi_client.models.policy_template_update_fields_mixin_details import PolicyTemplateUpdateFieldsMixinDetails
from openapi_client.models.policy_template_update_fields_mixin_execution_type import PolicyTemplateUpdateFieldsMixinExecutionType
from openapi_client.models.services import Services
from openapi_client.models.title import Title
from typing import Optional, Set
from typing_extensions import Self

class PolicyTemplateUpdateFieldsMixin(BaseModel):
    """
    PolicyTemplateUpdateFieldsMixin
    """ # noqa: E501
    title: Optional[Title] = None
    description: Optional[Description] = None
    services: Optional[Services] = None
    execution_type: Optional[PolicyTemplateUpdateFieldsMixinExecutionType] = None
    details: Optional[PolicyTemplateUpdateFieldsMixinDetails] = None
    __properties: ClassVar[List[str]] = ["title", "description", "services", "execution_type", "details"]

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
        """Create an instance of PolicyTemplateUpdateFieldsMixin from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of title
        if self.title:
            _dict['title'] = self.title.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of services
        if self.services:
            _dict['services'] = self.services.to_dict()
        # override the default output from pydantic by calling `to_dict()` of execution_type
        if self.execution_type:
            _dict['execution_type'] = self.execution_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict['details'] = self.details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PolicyTemplateUpdateFieldsMixin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": Title.from_dict(obj["title"]) if obj.get("title") is not None else None,
            "description": Description.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "services": Services.from_dict(obj["services"]) if obj.get("services") is not None else None,
            "execution_type": PolicyTemplateUpdateFieldsMixinExecutionType.from_dict(obj["execution_type"]) if obj.get("execution_type") is not None else None,
            "details": PolicyTemplateUpdateFieldsMixinDetails.from_dict(obj["details"]) if obj.get("details") is not None else None
        })
        return _obj


