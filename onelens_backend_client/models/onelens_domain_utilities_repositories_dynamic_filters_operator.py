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


class OnelensDomainUtilitiesRepositoriesDynamicFiltersOperator(str, Enum):
    """
    OnelensDomainUtilitiesRepositoriesDynamicFiltersOperator
    """

    """
    allowed enum values
    """
    BETWEEN = "between"
    CONTAINS = "contains"
    ENDS_WITH = "ends_with"
    EQUALS = "equals"
    GREATER_THAN = "greater_than"
    GREATER_THAN_EQUAL = "greater_than_equal"
    IN = "in"
    LESS_THAN = "less_than"
    LESS_THAN_EQUAL = "less_than_equal"
    NOT_EQUALS = "not_equals"
    NOT_IN = "not_in"
    STARTS_WITH = "starts_with"
    IS = "is"
    IS_NOT = "is_not"
    IS_EMPTY = "is_empty"
    IS_NOT_EMPTY = "is_not_empty"
    IS_DATERANGE_TEMPLATE = "is_daterange_template"
    IS_NULL = "is_null"
    IS_NOT_NULL = "is_not_null"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OnelensDomainUtilitiesRepositoriesDynamicFiltersOperator from a JSON string"""
        return cls(json.loads(json_str))
