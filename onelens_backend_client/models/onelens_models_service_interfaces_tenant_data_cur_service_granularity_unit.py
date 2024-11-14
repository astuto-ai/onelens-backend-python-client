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


class OnelensModelsServiceInterfacesTenantDataCurServiceGranularityUnit(str, Enum):
    """
    OnelensModelsServiceInterfacesTenantDataCurServiceGranularityUnit
    """

    """
    allowed enum values
    """
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OnelensModelsServiceInterfacesTenantDataCurServiceGranularityUnit from a JSON string"""
        return cls(json.loads(json_str))
