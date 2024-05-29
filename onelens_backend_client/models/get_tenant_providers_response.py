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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from onelens_backend_client.models.tenant_provider import TenantProvider
from typing import Optional, Set
from typing_extensions import Self

class GetTenantProvidersResponse(BaseModel):
    """
    GetTenantProvidersResponse
    """ # noqa: E501
    tenant_provider_filter_data: Optional[List[TenantProvider]]
    attributes_data: Optional[Dict[str, Any]]
    __properties: ClassVar[List[str]] = ["tenant_provider_filter_data", "attributes_data"]

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
        """Create an instance of GetTenantProvidersResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tenant_provider_filter_data (list)
        _items = []
        if self.tenant_provider_filter_data:
            for _item in self.tenant_provider_filter_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tenant_provider_filter_data'] = _items
        # set to None if tenant_provider_filter_data (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_provider_filter_data is None and "tenant_provider_filter_data" in self.model_fields_set:
            _dict['tenant_provider_filter_data'] = None

        # set to None if attributes_data (nullable) is None
        # and model_fields_set contains the field
        if self.attributes_data is None and "attributes_data" in self.model_fields_set:
            _dict['attributes_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTenantProvidersResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenant_provider_filter_data": [TenantProvider.from_dict(_item) for _item in obj["tenant_provider_filter_data"]] if obj.get("tenant_provider_filter_data") is not None else None,
            "attributes_data": obj.get("attributes_data")
        })
        return _obj


