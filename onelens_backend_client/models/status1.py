# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from pydantic import (
    BaseModel,
    ValidationError,
    field_validator,
)
from typing import Optional
from onelens_backend_client.models.anomaly_ticket_status import AnomalyTicketStatus
from onelens_backend_client.models.policy_ticket_status import PolicyTicketStatus
from typing import Union, Any, Set, TYPE_CHECKING, Dict
from typing_extensions import Self

STATUS1_ANY_OF_SCHEMAS = ["AnomalyTicketStatus", "PolicyTicketStatus"]


class Status1(BaseModel):
    """
    Status of the ticket
    """

    # data type: PolicyTicketStatus
    anyof_schema_1_validator: Optional[PolicyTicketStatus] = None
    # data type: AnomalyTicketStatus
    anyof_schema_2_validator: Optional[AnomalyTicketStatus] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[AnomalyTicketStatus, PolicyTicketStatus]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = {"AnomalyTicketStatus", "PolicyTicketStatus"}

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`"
                )
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used."
                )
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator("actual_instance")
    def actual_instance_must_validate_anyof(cls, v):
        if v is None:
            return v

        instance = Status1.model_construct()
        error_messages = []
        # validate data type: PolicyTicketStatus
        if not isinstance(v, PolicyTicketStatus):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `PolicyTicketStatus`"
            )
        else:
            return v

        # validate data type: AnomalyTicketStatus
        if not isinstance(v, AnomalyTicketStatus):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `AnomalyTicketStatus`"
            )
        else:
            return v

        if error_messages:
            # no match
            raise ValueError(
                "No match found when setting the actual_instance in Status1 with anyOf schemas: AnomalyTicketStatus, PolicyTicketStatus. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        if json_str is None:
            return instance

        error_messages = []
        # anyof_schema_1_validator: Optional[PolicyTicketStatus] = None
        try:
            instance.actual_instance = PolicyTicketStatus.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[AnomalyTicketStatus] = None
        try:
            instance.actual_instance = AnomalyTicketStatus.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into Status1 with anyOf schemas: AnomalyTicketStatus, PolicyTicketStatus. Details: "
                + ", ".join(error_messages)
            )
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(
            self.actual_instance.to_json
        ):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(
        self,
    ) -> Optional[Union[Dict[str, Any], AnomalyTicketStatus, PolicyTicketStatus]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(
            self.actual_instance.to_dict
        ):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
