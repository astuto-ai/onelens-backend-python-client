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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from onelens_backend_client.models.tenant_state import TenantState
from typing import Optional, Set
from typing_extensions import Self

class GetTenantByIDResponse(BaseModel):
    """
    GetTenantByIDResponse
    """ # noqa: E501
    name: Annotated[str, Field(strict=True, max_length=200)] = Field(description="Name of the tenant")
    domains: List[StrictStr] = Field(description="List of domains associated with the tenant")
    org_id: Optional[StrictStr]
    timezone: StrictStr = Field(description="Timezone of the tenant")
    id: StrictStr = Field(description="Unique identifier for the tenant")
    short_id: StrictStr = Field(description="Unique identifier for the tenant")
    region: StrictStr = Field(description="Region of the tenant")
    tenant_state: TenantState = Field(description="State of the tenant")
    database_connection_string: Optional[StrictStr]
    s3_bucket_name: Optional[StrictStr]
    type: Optional[List[StrictStr]]
    status_reason: Optional[StrictStr]
    expiry_date: Optional[datetime]
    plan: Optional[StrictStr]
    plan_config: Optional[Dict[str, Any]]
    billing_owner: Optional[StrictStr]
    billing_type: Optional[StrictStr]
    milestones: Optional[List[Dict[str, Any]]]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    created_by: Optional[StrictStr]
    updated_by: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["name", "domains", "org_id", "timezone", "id", "short_id", "region", "tenant_state", "database_connection_string", "s3_bucket_name", "type", "status_reason", "expiry_date", "plan", "plan_config", "billing_owner", "billing_type", "milestones", "created_at", "updated_at", "created_by", "updated_by"]

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
        """Create an instance of GetTenantByIDResponse from a JSON string"""
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
        # set to None if org_id (nullable) is None
        # and model_fields_set contains the field
        if self.org_id is None and "org_id" in self.model_fields_set:
            _dict['org_id'] = None

        # set to None if database_connection_string (nullable) is None
        # and model_fields_set contains the field
        if self.database_connection_string is None and "database_connection_string" in self.model_fields_set:
            _dict['database_connection_string'] = None

        # set to None if s3_bucket_name (nullable) is None
        # and model_fields_set contains the field
        if self.s3_bucket_name is None and "s3_bucket_name" in self.model_fields_set:
            _dict['s3_bucket_name'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if status_reason (nullable) is None
        # and model_fields_set contains the field
        if self.status_reason is None and "status_reason" in self.model_fields_set:
            _dict['status_reason'] = None

        # set to None if expiry_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_date is None and "expiry_date" in self.model_fields_set:
            _dict['expiry_date'] = None

        # set to None if plan (nullable) is None
        # and model_fields_set contains the field
        if self.plan is None and "plan" in self.model_fields_set:
            _dict['plan'] = None

        # set to None if plan_config (nullable) is None
        # and model_fields_set contains the field
        if self.plan_config is None and "plan_config" in self.model_fields_set:
            _dict['plan_config'] = None

        # set to None if billing_owner (nullable) is None
        # and model_fields_set contains the field
        if self.billing_owner is None and "billing_owner" in self.model_fields_set:
            _dict['billing_owner'] = None

        # set to None if billing_type (nullable) is None
        # and model_fields_set contains the field
        if self.billing_type is None and "billing_type" in self.model_fields_set:
            _dict['billing_type'] = None

        # set to None if milestones (nullable) is None
        # and model_fields_set contains the field
        if self.milestones is None and "milestones" in self.model_fields_set:
            _dict['milestones'] = None

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
        """Create an instance of GetTenantByIDResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "domains": obj.get("domains"),
            "org_id": obj.get("org_id"),
            "timezone": obj.get("timezone"),
            "id": obj.get("id"),
            "short_id": obj.get("short_id"),
            "region": obj.get("region"),
            "tenant_state": obj.get("tenant_state"),
            "database_connection_string": obj.get("database_connection_string"),
            "s3_bucket_name": obj.get("s3_bucket_name"),
            "type": obj.get("type"),
            "status_reason": obj.get("status_reason"),
            "expiry_date": obj.get("expiry_date"),
            "plan": obj.get("plan"),
            "plan_config": obj.get("plan_config"),
            "billing_owner": obj.get("billing_owner"),
            "billing_type": obj.get("billing_type"),
            "milestones": obj.get("milestones"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "created_by": obj.get("created_by"),
            "updated_by": obj.get("updated_by")
        })
        return _obj


