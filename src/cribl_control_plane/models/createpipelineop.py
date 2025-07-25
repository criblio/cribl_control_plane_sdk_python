"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pipeline import Pipeline, PipelineTypedDict
from cribl_control_plane.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class CreatePipelineResponseTypedDict(TypedDict):
    r"""a list of Pipeline objects"""

    count: NotRequired[int]
    r"""number of items present in the items array"""
    items: NotRequired[List[PipelineTypedDict]]


class CreatePipelineResponse(BaseModel):
    r"""a list of Pipeline objects"""

    count: Optional[int] = None
    r"""number of items present in the items array"""

    items: Optional[List[Pipeline]] = None
