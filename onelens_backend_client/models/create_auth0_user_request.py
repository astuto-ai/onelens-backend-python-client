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
from onelens_backend_client.models.auth0_create_user_app_metadata import Auth0CreateUserAppMetadata
from typing import Optional, Set
from typing_extensions import Self

class CreateAuth0UserRequest(BaseModel):
    """
    CreateAuth0UserRequest
    """ # noqa: E501
    email: StrictStr = Field(description="The email of the user in Auth0.")
    password: StrictStr = Field(description="The password of the user in Auth0.")
    email_verified: Optional[StrictBool] = None
    app_metadata: Auth0CreateUserAppMetadata = Field(description="The app_metadata of the user in Auth0.")
    connection: Optional[StrictStr] = Field(default=None, description="The connection of the user in Auth0.")
    given_name: Optional[StrictStr] = None
    family_name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["email", "password", "email_verified", "app_metadata", "connection", "given_name", "family_name"]

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
        """Create an instance of CreateAuth0UserRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of app_metadata
        if self.app_metadata:
            _dict['app_metadata'] = self.app_metadata.to_dict()
        # set to None if email_verified (nullable) is None
        # and model_fields_set contains the field
        if self.email_verified is None and "email_verified" in self.model_fields_set:
            _dict['email_verified'] = None

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
        """Create an instance of CreateAuth0UserRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "password": obj.get("password"),
            "email_verified": obj.get("email_verified"),
            "app_metadata": Auth0CreateUserAppMetadata.from_dict(obj["app_metadata"]) if obj.get("app_metadata") is not None else None,
            "connection": obj.get("connection"),
            "given_name": obj.get("given_name"),
            "family_name": obj.get("family_name")
        })
        return _obj


