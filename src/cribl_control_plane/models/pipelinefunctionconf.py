"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from cribl_control_plane.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FunctionSpecificConfigsTypedDict(TypedDict):
    pass


class FunctionSpecificConfigs(BaseModel):
    pass


class PipelineFunctionConfTypedDict(TypedDict):
    id: str
    r"""Function ID"""
    conf: FunctionSpecificConfigsTypedDict
    filter_: NotRequired[str]
    r"""Filter that selects data to be fed through this Function"""
    description: NotRequired[str]
    r"""Simple description of this step"""
    disabled: NotRequired[bool]
    r"""If true, data will not be pushed through this function"""
    final: NotRequired[bool]
    r"""If enabled, stops the results of this Function from being passed to the downstream Functions"""
    group_id: NotRequired[str]
    r"""Group ID"""


class PipelineFunctionConf(BaseModel):
    id: str
    r"""Function ID"""

    conf: FunctionSpecificConfigs

    filter_: Annotated[Optional[str], pydantic.Field(alias="filter")] = "true"
    r"""Filter that selects data to be fed through this Function"""

    description: Optional[str] = None
    r"""Simple description of this step"""

    disabled: Optional[bool] = None
    r"""If true, data will not be pushed through this function"""

    final: Optional[bool] = None
    r"""If enabled, stops the results of this Function from being passed to the downstream Functions"""

    group_id: Annotated[Optional[str], pydantic.Field(alias="groupId")] = None
    r"""Group ID"""
