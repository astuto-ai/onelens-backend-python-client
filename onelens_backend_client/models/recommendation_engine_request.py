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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from onelens_backend_client.models.recommendation_params import RecommendationParams
from typing import Optional, Set
from typing_extensions import Self

class RecommendationEngineRequest(BaseModel):
    """
    RecommendationEngineRequest
    """ # noqa: E501
    recommendation_unit_id: StrictStr = Field(description="Recommendation Unit ID")
    resource_id: StrictStr = Field(description="Resource ID")
    params: RecommendationParams = Field(description="Recommendation Params")
    policy_config: Dict[str, Any] = Field(description="Policy Config")
    tenant_id: StrictStr = Field(description="Tenant ID")
    __properties: ClassVar[List[str]] = ["recommendation_unit_id", "resource_id", "params", "policy_config", "tenant_id"]

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
        """Create an instance of RecommendationEngineRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of params
        if self.params:
            _dict['params'] = self.params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecommendationEngineRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "recommendation_unit_id": obj.get("recommendation_unit_id"),
            "resource_id": obj.get("resource_id"),
            "params": RecommendationParams.from_dict(obj["params"]) if obj.get("params") is not None else None,
            "policy_config": obj.get("policy_config"),
            "tenant_id": obj.get("tenant_id")
        })
        return _obj


