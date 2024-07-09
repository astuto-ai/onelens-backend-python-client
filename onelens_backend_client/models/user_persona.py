# coding: utf-8

"""
    onelens-backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UserPersona(str, Enum):
    """
    UserPersona
    """

    """
    allowed enum values
    """
    DEVOPS = 'DevOps'
    FINOPS = 'FinOps'
    CXO = 'CXO'
    PRODUCT_MANAGER = 'Product Manager'
    ENGINEER = 'Engineer'
    FINANCE = 'Finance'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserPersona from a JSON string"""
        return cls(json.loads(json_str))

