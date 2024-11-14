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
from enum import Enum
from typing_extensions import Self


class AgentType(str, Enum):
    """
    Enum representing the type of agent.
    """

    """
    allowed enum values
    """
    TEST_WORKFLOW = "TEST_WORKFLOW"
    HIERARCHY_WORKFLOW = "HIERARCHY_WORKFLOW"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentType from a JSON string"""
        return cls(json.loads(json_str))
