"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pipelinefunctionconf import PipelineFunctionConf, PipelineFunctionConfTypedDict
from cribl_control_plane.types import BaseModel
import pydantic
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PipelineGroupsTypedDict(TypedDict):
    name: str
    description: NotRequired[str]
    r"""Short description of this group"""
    disabled: NotRequired[bool]
    r"""Whether this group is disabled"""


class PipelineGroups(BaseModel):
    name: str

    description: Optional[str] = None
    r"""Short description of this group"""

    disabled: Optional[bool] = None
    r"""Whether this group is disabled"""


class ConfTypedDict(TypedDict):
    async_func_timeout: NotRequired[int]
    r"""Time (in ms) to wait for an async function to complete processing of a data item"""
    output: NotRequired[str]
    r"""The output destination for events processed by this Pipeline"""
    description: NotRequired[str]
    streamtags: NotRequired[List[str]]
    r"""Tags for filtering and grouping in @{product}"""
    functions: NotRequired[List[PipelineFunctionConfTypedDict]]
    r"""List of Functions to pass data through"""
    groups: NotRequired[Dict[str, PipelineGroupsTypedDict]]


class Conf(BaseModel):
    async_func_timeout: Annotated[
        Optional[int], pydantic.Field(alias="asyncFuncTimeout")
    ] = None
    r"""Time (in ms) to wait for an async function to complete processing of a data item"""

    output: Optional[str] = "default"
    r"""The output destination for events processed by this Pipeline"""

    description: Optional[str] = None

    streamtags: Optional[List[str]] = None
    r"""Tags for filtering and grouping in @{product}"""

    functions: Optional[List[PipelineFunctionConf]] = None
    r"""List of Functions to pass data through"""

    groups: Optional[Dict[str, PipelineGroups]] = None


class PipelineTypedDict(TypedDict):
    id: str
    conf: ConfTypedDict


class Pipeline(BaseModel):
    id: str

    conf: Conf
