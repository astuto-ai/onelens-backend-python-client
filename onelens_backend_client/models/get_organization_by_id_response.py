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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.organization_state import OrganizationState
from typing import Optional, Set
from typing_extensions import Self

class GetOrganizationByIDResponse(BaseModel):
    """
    GetOrganizationByIDResponse
    """ # noqa: E501
    name: StrictStr = Field(description="Name of the organization")
    id: StrictStr = Field(description="ID of the organization")
    short_id: StrictInt = Field(description="Unique identifier for the organization")
    status: Optional[OrganizationState]
    total_tenants: Optional[StrictInt]
    country: Optional[StrictStr]
    industry: Optional[List[StrictStr]]
    monthly_cloud_spend: Optional[StrictInt]
    cloud_service_providers: Optional[List[StrictStr]]
    website: Optional[StrictStr]
    changelogs: Optional[List[Dict[str, Any]]]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    created_by: Optional[StrictStr]
    updated_by: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["name", "id", "short_id", "status", "total_tenants", "country", "industry", "monthly_cloud_spend", "cloud_service_providers", "website", "changelogs", "created_at", "updated_at", "created_by", "updated_by"]

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
        """Create an instance of GetOrganizationByIDResponse from a JSON string"""
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
        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if total_tenants (nullable) is None
        # and model_fields_set contains the field
        if self.total_tenants is None and "total_tenants" in self.model_fields_set:
            _dict['total_tenants'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if industry (nullable) is None
        # and model_fields_set contains the field
        if self.industry is None and "industry" in self.model_fields_set:
            _dict['industry'] = None

        # set to None if monthly_cloud_spend (nullable) is None
        # and model_fields_set contains the field
        if self.monthly_cloud_spend is None and "monthly_cloud_spend" in self.model_fields_set:
            _dict['monthly_cloud_spend'] = None

        # set to None if cloud_service_providers (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_service_providers is None and "cloud_service_providers" in self.model_fields_set:
            _dict['cloud_service_providers'] = None

        # set to None if website (nullable) is None
        # and model_fields_set contains the field
        if self.website is None and "website" in self.model_fields_set:
            _dict['website'] = None

        # set to None if changelogs (nullable) is None
        # and model_fields_set contains the field
        if self.changelogs is None and "changelogs" in self.model_fields_set:
            _dict['changelogs'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['created_by'] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict['updated_by'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetOrganizationByIDResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "id": obj.get("id"),
            "short_id": obj.get("short_id"),
            "status": obj.get("status"),
            "total_tenants": obj.get("total_tenants"),
            "country": obj.get("country"),
            "industry": obj.get("industry"),
            "monthly_cloud_spend": obj.get("monthly_cloud_spend"),
            "cloud_service_providers": obj.get("cloud_service_providers"),
            "website": obj.get("website"),
            "changelogs": obj.get("changelogs"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "created_by": obj.get("created_by"),
            "updated_by": obj.get("updated_by")
        })
        return _obj


