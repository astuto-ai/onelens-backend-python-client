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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Auth0UserAllFields(BaseModel):
    """
    Auth0UserAllFields
    """ # noqa: E501
    email: Optional[StrictStr] = None
    email_verified: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    identities: Optional[List[Any]] = None
    name: Optional[StrictStr] = None
    nickname: Optional[StrictStr] = None
    picture: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    user_id: StrictStr = Field(description="The user_id of the user in Auth0.")
    user_metadata: Optional[Dict[str, Any]] = None
    app_metadata: Optional[Dict[str, Any]] = Field(default=None, description="The app_metadata of the user in Auth0.")
    last_ip: Optional[StrictStr] = None
    last_login: Optional[datetime] = None
    logins_count: Optional[StrictInt] = None
    given_name: Optional[StrictStr] = None
    family_name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["email", "email_verified", "created_at", "identities", "name", "nickname", "picture", "updated_at", "user_id", "user_metadata", "app_metadata", "last_ip", "last_login", "logins_count", "given_name", "family_name"]

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
        """Create an instance of Auth0UserAllFields from a JSON string"""
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
        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if email_verified (nullable) is None
        # and model_fields_set contains the field
        if self.email_verified is None and "email_verified" in self.model_fields_set:
            _dict['email_verified'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if identities (nullable) is None
        # and model_fields_set contains the field
        if self.identities is None and "identities" in self.model_fields_set:
            _dict['identities'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if nickname (nullable) is None
        # and model_fields_set contains the field
        if self.nickname is None and "nickname" in self.model_fields_set:
            _dict['nickname'] = None

        # set to None if picture (nullable) is None
        # and model_fields_set contains the field
        if self.picture is None and "picture" in self.model_fields_set:
            _dict['picture'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if user_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.user_metadata is None and "user_metadata" in self.model_fields_set:
            _dict['user_metadata'] = None

        # set to None if last_ip (nullable) is None
        # and model_fields_set contains the field
        if self.last_ip is None and "last_ip" in self.model_fields_set:
            _dict['last_ip'] = None

        # set to None if last_login (nullable) is None
        # and model_fields_set contains the field
        if self.last_login is None and "last_login" in self.model_fields_set:
            _dict['last_login'] = None

        # set to None if logins_count (nullable) is None
        # and model_fields_set contains the field
        if self.logins_count is None and "logins_count" in self.model_fields_set:
            _dict['logins_count'] = None

        # set to None if given_name (nullable) is None
        # and model_fields_set contains the field
        if self.given_name is None and "given_name" in self.model_fields_set:
            _dict['given_name'] = None

        # set to None if family_name (nullable) is None
        # and model_fields_set contains the field
        if self.family_name is None and "family_name" in self.model_fields_set:
            _dict['family_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Auth0UserAllFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "email_verified": obj.get("email_verified"),
            "created_at": obj.get("created_at"),
            "identities": obj.get("identities"),
            "name": obj.get("name"),
            "nickname": obj.get("nickname"),
            "picture": obj.get("picture"),
            "updated_at": obj.get("updated_at"),
            "user_id": obj.get("user_id"),
            "user_metadata": obj.get("user_metadata"),
            "app_metadata": obj.get("app_metadata"),
            "last_ip": obj.get("last_ip"),
            "last_login": obj.get("last_login"),
            "logins_count": obj.get("logins_count"),
            "given_name": obj.get("given_name"),
            "family_name": obj.get("family_name")
        })
        return _obj


