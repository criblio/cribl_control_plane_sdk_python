"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .output import Output, OutputTypedDict
from cribl_control_plane.types import BaseModel
from cribl_control_plane.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateOutputByIDRequestTypedDict(TypedDict):
    id: str
    r"""Unique ID to PATCH"""
    output: OutputTypedDict
    r"""Destination object to be updated"""


class UpdateOutputByIDRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unique ID to PATCH"""

    output: Annotated[
        Output, FieldMetadata(request=RequestMetadata(media_type="application/json"))
    ]
    r"""Destination object to be updated"""


class UpdateOutputByIDResponseTypedDict(TypedDict):
    r"""a list of Destination objects"""

    count: NotRequired[int]
    r"""number of items present in the items array"""
    items: NotRequired[List[OutputTypedDict]]


class UpdateOutputByIDResponse(BaseModel):
    r"""a list of Destination objects"""

    count: Optional[int] = None
    r"""number of items present in the items array"""

    items: Optional[List[Output]] = None
