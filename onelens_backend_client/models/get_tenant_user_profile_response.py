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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.base_user_persona import BaseUserPersona
from onelens_backend_client.models.city import City
from onelens_backend_client.models.country import Country
from onelens_backend_client.models.created_at import CreatedAt
from onelens_backend_client.models.display_date_format import DisplayDateFormat
from onelens_backend_client.models.display_language import DisplayLanguage
from onelens_backend_client.models.display_time_format import DisplayTimeFormat
from onelens_backend_client.models.email import Email
from onelens_backend_client.models.first_name import FirstName
from onelens_backend_client.models.job_title import JobTitle
from onelens_backend_client.models.last_login import LastLogin
from onelens_backend_client.models.last_name import LastName
from onelens_backend_client.models.manager import Manager
from onelens_backend_client.models.middle_name import MiddleName
from onelens_backend_client.models.mobile_country_code import MobileCountryCode
from onelens_backend_client.models.mobile_number import MobileNumber
from onelens_backend_client.models.preferred_currency import PreferredCurrency
from onelens_backend_client.models.profile_pic_url import ProfilePicUrl
from onelens_backend_client.models.sources import Sources
from onelens_backend_client.models.state import State
from onelens_backend_client.models.timezone import Timezone
from onelens_backend_client.models.user_role import UserRole
from onelens_backend_client.models.user_status import UserStatus
from typing import Set
from typing_extensions import Self


class GetTenantUserProfileResponse(BaseModel):
    """
    GetTenantUserProfileResponse
    """  # noqa: E501

    profile_pic_url: Optional[ProfilePicUrl] = None
    last_login: Optional[LastLogin] = None
    status: Optional[UserStatus] = Field(
        default=None, description="Status of the user like ACTIVE, BLOCKED etc."
    )
    first_name: FirstName
    middle_name: Optional[MiddleName] = None
    last_name: LastName
    email: Optional[Email] = None
    mobile_country_code: Optional[MobileCountryCode] = None
    mobile_number: Optional[MobileNumber] = None
    persona: Optional[BaseUserPersona] = None
    role: Optional[UserRole] = Field(
        default=None, description="Role of the user in the tenant"
    )
    job_title: Optional[JobTitle] = None
    manager: Optional[Manager] = None
    city: Optional[City] = None
    state: Optional[State] = None
    country: Optional[Country] = None
    display_language: Optional[DisplayLanguage] = None
    preferred_currency: Optional[PreferredCurrency] = None
    timezone: Optional[Timezone] = None
    display_date_format: Optional[DisplayDateFormat] = None
    display_time_format: Optional[DisplayTimeFormat] = None
    sources: Optional[Sources] = None
    created_at: Optional[CreatedAt] = None
    node_ids: List[Any] = Field(
        description="Hierarchy node ids(cost centers) the user has access to."
    )
    ol_user_id: Optional[Any] = Field(
        description="Unique onelens identifier for the user"
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "profile_pic_url",
        "last_login",
        "status",
        "first_name",
        "middle_name",
        "last_name",
        "email",
        "mobile_country_code",
        "mobile_number",
        "persona",
        "role",
        "job_title",
        "manager",
        "city",
        "state",
        "country",
        "display_language",
        "preferred_currency",
        "timezone",
        "display_date_format",
        "display_time_format",
        "sources",
        "created_at",
        "node_ids",
        "ol_user_id",
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
        """Create an instance of GetTenantUserProfileResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set(
            [
                "additional_properties",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of profile_pic_url
        if self.profile_pic_url:
            _dict["profile_pic_url"] = self.profile_pic_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_login
        if self.last_login:
            _dict["last_login"] = self.last_login.to_dict()
        # override the default output from pydantic by calling `to_dict()` of first_name
        if self.first_name:
            _dict["first_name"] = self.first_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of middle_name
        if self.middle_name:
            _dict["middle_name"] = self.middle_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_name
        if self.last_name:
            _dict["last_name"] = self.last_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of email
        if self.email:
            _dict["email"] = self.email.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mobile_country_code
        if self.mobile_country_code:
            _dict["mobile_country_code"] = self.mobile_country_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mobile_number
        if self.mobile_number:
            _dict["mobile_number"] = self.mobile_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of persona
        if self.persona:
            _dict["persona"] = self.persona.to_dict()
        # override the default output from pydantic by calling `to_dict()` of job_title
        if self.job_title:
            _dict["job_title"] = self.job_title.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manager
        if self.manager:
            _dict["manager"] = self.manager.to_dict()
        # override the default output from pydantic by calling `to_dict()` of city
        if self.city:
            _dict["city"] = self.city.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict["state"] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict["country"] = self.country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of display_language
        if self.display_language:
            _dict["display_language"] = self.display_language.to_dict()
        # override the default output from pydantic by calling `to_dict()` of preferred_currency
        if self.preferred_currency:
            _dict["preferred_currency"] = self.preferred_currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timezone
        if self.timezone:
            _dict["timezone"] = self.timezone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of display_date_format
        if self.display_date_format:
            _dict["display_date_format"] = self.display_date_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of display_time_format
        if self.display_time_format:
            _dict["display_time_format"] = self.display_time_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sources
        if self.sources:
            _dict["sources"] = self.sources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict["created_at"] = self.created_at.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if ol_user_id (nullable) is None
        # and model_fields_set contains the field
        if self.ol_user_id is None and "ol_user_id" in self.model_fields_set:
            _dict["ol_user_id"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTenantUserProfileResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "profile_pic_url": ProfilePicUrl.from_dict(obj["profile_pic_url"])
                if obj.get("profile_pic_url") is not None
                else None,
                "last_login": LastLogin.from_dict(obj["last_login"])
                if obj.get("last_login") is not None
                else None,
                "status": obj.get("status"),
                "first_name": FirstName.from_dict(obj["first_name"])
                if obj.get("first_name") is not None
                else None,
                "middle_name": MiddleName.from_dict(obj["middle_name"])
                if obj.get("middle_name") is not None
                else None,
                "last_name": LastName.from_dict(obj["last_name"])
                if obj.get("last_name") is not None
                else None,
                "email": Email.from_dict(obj["email"])
                if obj.get("email") is not None
                else None,
                "mobile_country_code": MobileCountryCode.from_dict(
                    obj["mobile_country_code"]
                )
                if obj.get("mobile_country_code") is not None
                else None,
                "mobile_number": MobileNumber.from_dict(obj["mobile_number"])
                if obj.get("mobile_number") is not None
                else None,
                "persona": BaseUserPersona.from_dict(obj["persona"])
                if obj.get("persona") is not None
                else None,
                "role": obj.get("role"),
                "job_title": JobTitle.from_dict(obj["job_title"])
                if obj.get("job_title") is not None
                else None,
                "manager": Manager.from_dict(obj["manager"])
                if obj.get("manager") is not None
                else None,
                "city": City.from_dict(obj["city"])
                if obj.get("city") is not None
                else None,
                "state": State.from_dict(obj["state"])
                if obj.get("state") is not None
                else None,
                "country": Country.from_dict(obj["country"])
                if obj.get("country") is not None
                else None,
                "display_language": DisplayLanguage.from_dict(obj["display_language"])
                if obj.get("display_language") is not None
                else None,
                "preferred_currency": PreferredCurrency.from_dict(
                    obj["preferred_currency"]
                )
                if obj.get("preferred_currency") is not None
                else None,
                "timezone": Timezone.from_dict(obj["timezone"])
                if obj.get("timezone") is not None
                else None,
                "display_date_format": DisplayDateFormat.from_dict(
                    obj["display_date_format"]
                )
                if obj.get("display_date_format") is not None
                else None,
                "display_time_format": DisplayTimeFormat.from_dict(
                    obj["display_time_format"]
                )
                if obj.get("display_time_format") is not None
                else None,
                "sources": Sources.from_dict(obj["sources"])
                if obj.get("sources") is not None
                else None,
                "created_at": CreatedAt.from_dict(obj["created_at"])
                if obj.get("created_at") is not None
                else None,
                "node_ids": obj.get("node_ids"),
                "ol_user_id": obj.get("ol_user_id"),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
