"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .input import Input, InputTypedDict
from cribl_control_plane.types import BaseModel
from cribl_control_plane.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateInputByIDRequestTypedDict(TypedDict):
    id: str
    r"""Unique ID to PATCH"""
    input: InputTypedDict
    r"""Source object to be updated"""


class UpdateInputByIDRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unique ID to PATCH"""

    input: Annotated[
        Input, FieldMetadata(request=RequestMetadata(media_type="application/json"))
    ]
    r"""Source object to be updated"""


class UpdateInputByIDResponseTypedDict(TypedDict):
    r"""a list of Source objects"""

    count: NotRequired[int]
    r"""number of items present in the items array"""
    items: NotRequired[List[InputTypedDict]]


class UpdateInputByIDResponse(BaseModel):
    r"""a list of Source objects"""

    count: Optional[int] = None
    r"""number of items present in the items array"""

    items: Optional[List[Input]] = None
