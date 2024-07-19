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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.effort import Effort
from onelens_backend_client.models.recommendation_query_details import RecommendationQueryDetails
from typing import Optional, Set
from typing_extensions import Self

class RecommendationUnitWithActionType(BaseModel):
    """
    RecommendationUnitWithActionType
    """ # noqa: E501
    id: StrictStr = Field(description="Recommendation Config ID")
    service: StrictStr = Field(description="Service AWS etc.")
    action_type_id: Optional[StrictInt] = None
    priority: StrictInt = Field(description="Priority")
    title: StrictStr = Field(description="Title")
    subtitle: Optional[StrictStr] = None
    description: StrictStr = Field(description="Description")
    effort: Effort = Field(description="Effort")
    query_details: Optional[RecommendationQueryDetails]
    action_type_service: Optional[StrictStr] = None
    action_type_title: Optional[StrictStr] = None
    action_type_subtitle: Optional[StrictStr] = None
    action_type_description: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "service", "action_type_id", "priority", "title", "subtitle", "description", "effort", "query_details", "action_type_service", "action_type_title", "action_type_subtitle", "action_type_description"]

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
        """Create an instance of RecommendationUnitWithActionType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of query_details
        if self.query_details:
            _dict['query_details'] = self.query_details.to_dict()
        # set to None if action_type_id (nullable) is None
        # and model_fields_set contains the field
        if self.action_type_id is None and "action_type_id" in self.model_fields_set:
            _dict['action_type_id'] = None

        # set to None if subtitle (nullable) is None
        # and model_fields_set contains the field
        if self.subtitle is None and "subtitle" in self.model_fields_set:
            _dict['subtitle'] = None

        # set to None if query_details (nullable) is None
        # and model_fields_set contains the field
        if self.query_details is None and "query_details" in self.model_fields_set:
            _dict['query_details'] = None

        # set to None if action_type_service (nullable) is None
        # and model_fields_set contains the field
        if self.action_type_service is None and "action_type_service" in self.model_fields_set:
            _dict['action_type_service'] = None

        # set to None if action_type_title (nullable) is None
        # and model_fields_set contains the field
        if self.action_type_title is None and "action_type_title" in self.model_fields_set:
            _dict['action_type_title'] = None

        # set to None if action_type_subtitle (nullable) is None
        # and model_fields_set contains the field
        if self.action_type_subtitle is None and "action_type_subtitle" in self.model_fields_set:
            _dict['action_type_subtitle'] = None

        # set to None if action_type_description (nullable) is None
        # and model_fields_set contains the field
        if self.action_type_description is None and "action_type_description" in self.model_fields_set:
            _dict['action_type_description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecommendationUnitWithActionType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "service": obj.get("service"),
            "action_type_id": obj.get("action_type_id"),
            "priority": obj.get("priority"),
            "title": obj.get("title"),
            "subtitle": obj.get("subtitle"),
            "description": obj.get("description"),
            "effort": obj.get("effort"),
            "query_details": RecommendationQueryDetails.from_dict(obj["query_details"]) if obj.get("query_details") is not None else None,
            "action_type_service": obj.get("action_type_service"),
            "action_type_title": obj.get("action_type_title"),
            "action_type_subtitle": obj.get("action_type_subtitle"),
            "action_type_description": obj.get("action_type_description")
        })
        return _obj


